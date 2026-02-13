"""
app.py – Kariérní kvíz v0.2.0

Dvoudílný kvíz:
  Part 1 – Kariérní směr (7 typů otázek, boduje kategorie)
  Part 2 – Pracovní pozice (single_choice, boduje pozice v top-3 kategoriích)
"""

import os
import json
import random
from datetime import datetime
from functools import wraps

from flask import (
    Flask, render_template, request, redirect, url_for,
    flash, session, jsonify,
)
from flask_login import (
    LoginManager, login_user, logout_user, login_required, current_user,
)

from models import (
    db, QUESTION_TYPES, AdminUser, Category, Position,
    Question, Answer, AnswerScore, AnswerPositionScore,
    QuizSetting, QuizResult,
)

# ══════════════════════════════════════════
#  App factory
# ══════════════════════════════════════════

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-2024')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///career_quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'
login_manager.login_message = 'Přihlaste se pro přístup do administrace.'
login_manager.login_message_category = 'warning'


@login_manager.user_loader
def load_user(user_id):
    return AdminUser.query.get(int(user_id))


# ══════════════════════════════════════════
#  Scoring engine
# ══════════════════════════════════════════

def score_question_part1(question, form_data):
    """Bodování Part-1 otázky → dict {category_id: score}."""
    scores = {}
    qkey = f'question_{question.id}'
    qtype = question.question_type

    if qtype in ('single_choice', 'true_false', 'likert'):
        val = form_data.get(qkey)
        if val:
            answer = Answer.query.get(int(val))
            if answer and answer.question_id == question.id:
                for s in answer.scores:
                    scores[s.category_id] = scores.get(s.category_id, 0) + s.score

    elif qtype == 'multiple_choice':
        vals = form_data.getlist(qkey)
        for v in vals:
            answer = Answer.query.get(int(v))
            if answer and answer.question_id == question.id:
                for s in answer.scores:
                    scores[s.category_id] = scores.get(s.category_id, 0) + s.score

    elif qtype == 'short_answer':
        user_text = (form_data.get(qkey) or '').strip().lower()
        if user_text:
            for answer in question.answers:
                if answer.text.lower() in user_text or user_text in answer.text.lower():
                    for s in answer.scores:
                        scores[s.category_id] = scores.get(s.category_id, 0) + s.score

    elif qtype == 'matching':
        ed = question.extra_data_parsed
        pairs = ed.get('pairs', [])
        for i, pair in enumerate(pairs):
            user_val = form_data.get(f'{qkey}_match_{i}', '')
            if user_val == pair.get('right', ''):
                # Correct match → score from corresponding answer
                if i < len(question.answers):
                    for s in question.answers[i].scores:
                        scores[s.category_id] = scores.get(s.category_id, 0) + s.score

    elif qtype == 'ordering':
        order_str = form_data.get(f'{qkey}_order', '')
        if order_str:
            user_order = order_str.split(',')
            ed = question.extra_data_parsed
            correct = ed.get('correct_order', [])
            # Score based on position accuracy
            for i, idx_str in enumerate(user_order):
                try:
                    orig_idx = int(idx_str)
                    if orig_idx == i and i < len(question.answers):
                        for s in question.answers[i].scores:
                            scores[s.category_id] = scores.get(s.category_id, 0) + s.score
                except (ValueError, IndexError):
                    pass

    return scores


def score_question_part2(question, form_data):
    """Bodování Part-2 otázky → dict {position_id: score}."""
    scores = {}
    qkey = f'question_{question.id}'
    val = form_data.get(qkey)
    if val:
        answer = Answer.query.get(int(val))
        if answer and answer.question_id == question.id:
            for ps in answer.position_scores:
                scores[ps.position_id] = scores.get(ps.position_id, 0) + ps.score
    return scores


# ══════════════════════════════════════════
#  Public routes
# ══════════════════════════════════════════

@app.route('/')
def index():
    categories = Category.query.all()
    p1_count = Question.query.filter_by(part=1, active=True).count()
    p2_count = Question.query.filter_by(part=2, active=True).count()
    positions_count = Position.query.filter_by(active=True).count()

    # type counts for Part 1
    type_counts = {}
    for code, label in QUESTION_TYPES.items():
        c = Question.query.filter_by(part=1, active=True, question_type=code).count()
        if c > 0:
            type_counts[label] = c

    part1_setting = QuizSetting.get_int('part1_count', 40)
    part2_setting = QuizSetting.get_int('part2_count', 40)

    return render_template('index.html',
                           categories=categories,
                           p1_count=p1_count,
                           p2_count=p2_count,
                           positions_count=positions_count,
                           type_counts=type_counts,
                           part1_setting=part1_setting,
                           part2_setting=part2_setting)


@app.route('/quiz')
def quiz():
    """Part 1 – kariérní směr."""
    part1_count = QuizSetting.get_int('part1_count', 40)
    all_q = Question.query.filter_by(part=1, active=True).all()

    if len(all_q) <= part1_count:
        questions = all_q
    else:
        questions = random.sample(all_q, part1_count)

    random.shuffle(questions)

    # Prepare extra quiz_data for matching / ordering
    quiz_data = {}
    for q in questions:
        if q.question_type == 'matching':
            ed = q.extra_data_parsed
            pairs = ed.get('pairs', [])
            rights = [p['right'] for p in pairs]
            shuffled_rights = rights[:]
            random.shuffle(shuffled_rights)
            quiz_data[q.id] = {'pairs': pairs, 'shuffled_rights': shuffled_rights}
        elif q.question_type == 'ordering':
            ed = q.extra_data_parsed
            items = list(enumerate(ed.get('correct_order', [])))
            shuffled = items[:]
            random.shuffle(shuffled)
            quiz_data[q.id] = {'shuffled_items': shuffled}
        elif q.question_type == 'likert':
            ed = q.extra_data_parsed
            labels = ed.get('labels', ['Vůbec ne', 'Spíše ne', 'Neutrálně', 'Spíše ano', 'Rozhodně ano'])
            quiz_data[q.id] = {'labels': labels}

    # Store question IDs in session for validation
    session['part1_qids'] = [q.id for q in questions]

    return render_template('quiz.html',
                           questions=questions,
                           total=len(questions),
                           quiz_data=quiz_data,
                           part=1)


@app.route('/quiz/submit', methods=['POST'])
def submit_part1():
    """Process Part 1 answers, compute category scores, redirect to interstitial."""
    qids = session.get('part1_qids', [])
    if not qids:
        flash('Kvíz vypršel. Začněte prosím znovu.', 'warning')
        return redirect(url_for('quiz'))

    category_scores = {}  # category_id → total score
    answered = 0

    for qid in qids:
        question = Question.query.get(qid)
        if not question:
            continue
        sc = score_question_part1(question, request.form)
        if sc:
            answered += 1
            for cid, pts in sc.items():
                category_scores[cid] = category_scores.get(cid, 0) + pts

    # Determine top 3 categories
    sorted_cats = sorted(category_scores.items(), key=lambda x: x[1], reverse=True)
    top3 = sorted_cats[:3]

    # Build results for display
    all_cats = Category.query.all()
    max_score = max(category_scores.values()) if category_scores else 1

    results = []
    for cat in all_cats:
        sc = category_scores.get(cat.id, 0)
        pct = round(sc / max_score * 100) if max_score else 0
        results.append({'category': cat, 'score': sc, 'percentage': pct})
    results.sort(key=lambda x: x['score'], reverse=True)

    top_results = results[:3]

    # Store in session for Part 2
    session['part1_scores'] = {str(k): v for k, v in category_scores.items()}
    session['part1_answered'] = answered
    session['part1_total'] = len(qids)
    session['top3_cat_ids'] = [cid for cid, _ in top3]

    return render_template('part1_results.html',
                           results=results,
                           top_results=top_results,
                           answered=answered,
                           total=len(qids))


@app.route('/quiz/part2')
def quiz_part2():
    """Part 2 – position-specific questions from top 3 categories."""
    top3_ids = session.get('top3_cat_ids')
    if not top3_ids:
        flash('Nejdříve dokončete první část kvízu.', 'warning')
        return redirect(url_for('quiz'))

    part2_count = QuizSetting.get_int('part2_count', 40)

    # Gather questions from top 3 categories proportionally
    # Distribute evenly: ceil(part2_count / 3) per category, then trim
    per_cat = (part2_count + 2) // 3
    selected = []

    for cid in top3_ids:
        pool = Question.query.filter_by(part=2, category_id=cid, active=True).all()
        if len(pool) <= per_cat:
            selected.extend(pool)
        else:
            selected.extend(random.sample(pool, per_cat))

    # Trim to exact count
    if len(selected) > part2_count:
        selected = selected[:part2_count]

    random.shuffle(selected)
    session['part2_qids'] = [q.id for q in selected]

    # Get top3 categories for display
    top3_cats = [Category.query.get(cid) for cid in top3_ids]

    return render_template('quiz_part2.html',
                           questions=selected,
                           total=len(selected),
                           top3_cats=top3_cats,
                           part=2)


@app.route('/quiz/part2/submit', methods=['POST'])
def submit_part2():
    """Process Part 2 answers, compute position scores, save final result."""
    qids = session.get('part2_qids', [])
    top3_ids = session.get('top3_cat_ids', [])
    if not qids or not top3_ids:
        flash('Kvíz vypršel. Začněte prosím znovu.', 'warning')
        return redirect(url_for('quiz'))

    position_scores = {}  # position_id → total score
    answered = 0

    for qid in qids:
        question = Question.query.get(qid)
        if not question:
            continue
        sc = score_question_part2(question, request.form)
        if sc:
            answered += 1
            for pid, pts in sc.items():
                position_scores[pid] = position_scores.get(pid, 0) + pts

    # Restore Part 1 data
    part1_scores = session.get('part1_scores', {})
    part1_answered = session.get('part1_answered', 0)
    part1_total = session.get('part1_total', 0)

    # Top category from Part 1
    top_cat_id = None
    if part1_scores:
        top_cat_id = int(max(part1_scores, key=part1_scores.get))

    # Save to DB
    result = QuizResult(
        top_category_id=top_cat_id,
        scores_json=json.dumps(part1_scores),
        answered_count=part1_answered,
        total_count=part1_total,
        top3_categories_json=json.dumps(top3_ids),
        position_scores_json=json.dumps({str(k): v for k, v in position_scores.items()}),
        part2_answered=answered,
        part2_total=len(qids),
    )
    db.session.add(result)
    db.session.commit()

    # Clear session
    for key in ['part1_qids', 'part1_scores', 'part1_answered', 'part1_total',
                'top3_cat_ids', 'part2_qids']:
        session.pop(key, None)

    return redirect(url_for('result', result_id=result.id))


@app.route('/result/<int:result_id>')
def result(result_id):
    """Show combined Part 1 + Part 2 results."""
    res = QuizResult.query.get_or_404(result_id)

    # Part 1 category results
    cat_scores = json.loads(res.scores_json or '{}')
    all_cats = Category.query.all()
    max_cat_score = max((int(v) for v in cat_scores.values()), default=1) or 1

    category_results = []
    for cat in all_cats:
        sc = int(cat_scores.get(str(cat.id), 0))
        pct = round(sc / max_cat_score * 100)
        category_results.append({'category': cat, 'score': sc, 'percentage': pct})
    category_results.sort(key=lambda x: x['score'], reverse=True)
    top_cat_results = category_results[:3]

    # Part 2 position results
    pos_scores = json.loads(res.position_scores_json or '{}')
    top3_ids = json.loads(res.top3_categories_json or '[]')

    position_results_by_cat = {}
    for cid in top3_ids:
        cat = Category.query.get(cid)
        if not cat:
            continue
        cat_positions = Position.query.filter_by(category_id=cid, active=True).all()
        pos_list = []
        for pos in cat_positions:
            sc = int(pos_scores.get(str(pos.id), 0))
            pos_list.append({'position': pos, 'score': sc})
        pos_list.sort(key=lambda x: x['score'], reverse=True)
        # Calculate percentage relative to max in this category
        max_pos = max((p['score'] for p in pos_list), default=1) or 1
        for p in pos_list:
            p['percentage'] = round(p['score'] / max_pos * 100)
        position_results_by_cat[cat] = pos_list

    # Top positions overall
    all_pos_results = []
    for cat, pos_list in position_results_by_cat.items():
        for p in pos_list:
            all_pos_results.append({**p, 'category': cat})
    all_pos_results.sort(key=lambda x: x['score'], reverse=True)
    top_positions = all_pos_results[:5]

    return render_template('result.html',
                           res=res,
                           category_results=category_results,
                           top_cat_results=top_cat_results,
                           position_results_by_cat=position_results_by_cat,
                           top_positions=top_positions)


# ══════════════════════════════════════════
#  Admin routes
# ══════════════════════════════════════════

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    if request.method == 'POST':
        user = AdminUser.query.filter_by(username=request.form.get('username')).first()
        if user and user.check_password(request.form.get('password')):
            login_user(user)
            flash('Přihlášení úspěšné.', 'success')
            return redirect(url_for('admin_dashboard'))
        flash('Neplatné přihlašovací údaje.', 'danger')
    return render_template('admin/login.html')


@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    flash('Odhlášení úspěšné.', 'info')
    return redirect(url_for('index'))


@app.route('/admin')
@login_required
def admin_dashboard():
    stats = {
        'categories': Category.query.count(),
        'positions': Position.query.count(),
        'questions': Question.query.count(),
        'active_questions': Question.query.filter_by(active=True).count(),
        'p1_questions': Question.query.filter_by(part=1, active=True).count(),
        'p2_questions': Question.query.filter_by(part=2, active=True).count(),
        'results': QuizResult.query.count(),
    }

    type_stats = {}
    for code, label in QUESTION_TYPES.items():
        c = Question.query.filter_by(question_type=code).count()
        if c > 0:
            type_stats[label] = c

    recent_results = QuizResult.query.order_by(QuizResult.timestamp.desc()).limit(10).all()
    settings = {
        'part1_count': QuizSetting.get_int('part1_count', 40),
        'part2_count': QuizSetting.get_int('part2_count', 40),
    }

    return render_template('admin/dashboard.html',
                           stats=stats,
                           type_stats=type_stats,
                           recent_results=recent_results,
                           settings=settings)


# ── Settings ──

@app.route('/admin/settings', methods=['GET', 'POST'])
@login_required
def admin_settings():
    if request.method == 'POST':
        p1 = request.form.get('part1_count', '40')
        p2 = request.form.get('part2_count', '40')
        try:
            p1_int = max(1, min(int(p1), 200))
            p2_int = max(1, min(int(p2), 200))
        except ValueError:
            flash('Neplatné hodnoty.', 'danger')
            return redirect(url_for('admin_settings'))

        QuizSetting.set_val('part1_count', p1_int)
        QuizSetting.set_val('part2_count', p2_int)
        db.session.commit()
        flash('Nastavení uloženo.', 'success')
        return redirect(url_for('admin_settings'))

    p1_total = Question.query.filter_by(part=1, active=True).count()
    p2_total = Question.query.filter_by(part=2, active=True).count()

    # Per-category Part 2 counts
    cat_p2 = {}
    for cat in Category.query.all():
        cnt = Question.query.filter_by(part=2, category_id=cat.id, active=True).count()
        cat_p2[cat] = cnt

    return render_template('admin/settings.html',
                           part1_count=QuizSetting.get_int('part1_count', 40),
                           part2_count=QuizSetting.get_int('part2_count', 40),
                           p1_total=p1_total,
                           p2_total=p2_total,
                           cat_p2=cat_p2)


# ── Categories ──

@app.route('/admin/categories')
@login_required
def admin_categories():
    categories = Category.query.all()
    return render_template('admin/categories.html', categories=categories)


@app.route('/admin/category/new', methods=['GET', 'POST'])
@login_required
def admin_category_new():
    if request.method == 'POST':
        cat = Category(
            code=request.form.get('code', '').upper()[:10],
            name=request.form['name'],
            description=request.form.get('description', ''),
            icon=request.form.get('icon', '📁'),
            color=request.form.get('color', '#3498db'),
        )
        db.session.add(cat)
        db.session.commit()
        flash(f'Kategorie "{cat.name}" vytvořena.', 'success')
        return redirect(url_for('admin_categories'))
    return render_template('admin/category_form.html', category=None)


@app.route('/admin/category/<int:cat_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_category_edit(cat_id):
    cat = Category.query.get_or_404(cat_id)
    if request.method == 'POST':
        cat.code = request.form.get('code', cat.code).upper()[:10]
        cat.name = request.form['name']
        cat.description = request.form.get('description', '')
        cat.icon = request.form.get('icon', '📁')
        cat.color = request.form.get('color', '#3498db')
        db.session.commit()
        flash(f'Kategorie "{cat.name}" upravena.', 'success')
        return redirect(url_for('admin_categories'))
    return render_template('admin/category_form.html', category=cat)


@app.route('/admin/category/<int:cat_id>/delete', methods=['POST'])
@login_required
def admin_category_delete(cat_id):
    cat = Category.query.get_or_404(cat_id)
    db.session.delete(cat)
    db.session.commit()
    flash(f'Kategorie smazána.', 'success')
    return redirect(url_for('admin_categories'))


# ── Questions ──

@app.route('/admin/questions')
@login_required
def admin_questions():
    search = request.args.get('search', '')
    category_id = request.args.get('category', 0, type=int)
    qtype = request.args.get('type', '')
    part_filter = request.args.get('part', 0, type=int)

    query = Question.query

    if search:
        query = query.filter(Question.text.contains(search))
    if category_id:
        query = query.filter_by(category_id=category_id)
    if qtype:
        query = query.filter_by(question_type=qtype)
    if part_filter:
        query = query.filter_by(part=part_filter)

    questions = query.order_by(Question.part, Question.id).paginate(
        page=request.args.get('page', 1, type=int), per_page=25, error_out=False)

    return render_template('admin/questions.html',
                           questions=questions,
                           categories=Category.query.all(),
                           question_types=QUESTION_TYPES,
                           search=search,
                           category_id=category_id,
                           qtype=qtype,
                           part_filter=part_filter)


@app.route('/admin/question/new', methods=['GET', 'POST'])
@login_required
def admin_question_new():
    categories = Category.query.all()
    if request.method == 'POST':
        q = _save_question(None, request.form)
        flash(f'Otázka #{q.id} vytvořena.', 'success')
        return redirect(url_for('admin_questions'))

    return render_template('admin/question_form.html',
                           question=None,
                           question_types=QUESTION_TYPES,
                           categories=categories,
                           answers_data=None)


@app.route('/admin/question/<int:q_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_question_edit(q_id):
    question = Question.query.get_or_404(q_id)
    categories = Category.query.all()

    if request.method == 'POST':
        _save_question(question, request.form)
        flash(f'Otázka #{question.id} upravena.', 'success')
        return redirect(url_for('admin_questions'))

    # Prepare answers_data for template
    answers_data = []
    for a in question.answers:
        scores = {str(s.category_id): s.score for s in a.scores}
        answers_data.append({'text': a.text, 'scores': scores})

    return render_template('admin/question_form.html',
                           question=question,
                           question_types=QUESTION_TYPES,
                           categories=categories,
                           answers_data=answers_data)


@app.route('/admin/question/<int:q_id>/toggle', methods=['POST'])
@login_required
def admin_question_toggle(q_id):
    q = Question.query.get_or_404(q_id)
    q.active = not q.active
    db.session.commit()
    flash(f'Otázka #{q.id} {"aktivována" if q.active else "deaktivována"}.', 'success')
    return redirect(url_for('admin_questions'))


@app.route('/admin/question/<int:q_id>/delete', methods=['POST'])
@login_required
def admin_question_delete(q_id):
    q = Question.query.get_or_404(q_id)
    db.session.delete(q)
    db.session.commit()
    flash(f'Otázka #{q_id} smazána.', 'success')
    return redirect(url_for('admin_questions'))


def _save_question(question, form):
    """Create or update a question from form data."""
    qtype = form.get('question_type', 'single_choice')
    is_new = question is None

    if is_new:
        question = Question()
        db.session.add(question)

    question.text = form['text']
    question.question_type = qtype
    question.active = bool(form.get('is_active'))
    question.part = int(form.get('part', 1))

    cat_id = form.get('category_id')
    question.category_id = int(cat_id) if cat_id and cat_id != '0' else None

    # Clear old answers
    if not is_new:
        for a in question.answers:
            db.session.delete(a)
        db.session.flush()

    if qtype in ('single_choice', 'multiple_choice', 'true_false', 'likert'):
        idx = 0
        while f'answer_{idx}_text' in form:
            text = form[f'answer_{idx}_text']
            if text.strip():
                ans = Answer(question=question, text=text, order_num=idx)
                db.session.add(ans)
                db.session.flush()

                # Category scores
                for cat in Category.query.all():
                    sc = form.get(f'answer_{idx}_score_{cat.id}', '0')
                    try:
                        sc_int = int(sc)
                    except ValueError:
                        sc_int = 0
                    if sc_int > 0:
                        db.session.add(AnswerScore(
                            answer_id=ans.id, category_id=cat.id, score=sc_int))
            idx += 1

        if qtype == 'likert':
            labels = form.get('likert_labels', '')
            labels_list = [l.strip() for l in labels.split(',') if l.strip()]
            question.extra_data_parsed = {'labels': labels_list}

    elif qtype == 'matching':
        pairs = []
        idx = 0
        while f'match_{idx}_left' in form:
            left = form[f'match_{idx}_left']
            right = form[f'match_{idx}_right']
            if left.strip() and right.strip():
                ans = Answer(question=question, text=f'{left} → {right}', order_num=idx)
                db.session.add(ans)
                db.session.flush()

                pair_scores = {}
                for cat in Category.query.all():
                    sc = form.get(f'match_{idx}_score_{cat.id}', '0')
                    try:
                        sc_int = int(sc)
                    except ValueError:
                        sc_int = 0
                    if sc_int > 0:
                        db.session.add(AnswerScore(
                            answer_id=ans.id, category_id=cat.id, score=sc_int))
                        pair_scores[str(cat.id)] = sc_int

                pairs.append({'left': left, 'right': right, 'scores': pair_scores})
            idx += 1
        question.extra_data_parsed = {'pairs': pairs}

    elif qtype == 'ordering':
        items_text = form.get('order_items', '')
        items_list = [l.strip() for l in items_text.strip().split('\n') if l.strip()]
        scores_text = form.get('order_scores', '')
        order_scores = {}
        if scores_text:
            for part in scores_text.split(','):
                part = part.strip()
                if ':' in part:
                    k, v = part.split(':', 1)
                    order_scores[k.strip()] = int(v.strip())

        for i, item in enumerate(items_list):
            ans = Answer(question=question, text=item, order_num=i)
            db.session.add(ans)
            db.session.flush()
            for cat_id_str, sc in order_scores.items():
                try:
                    db.session.add(AnswerScore(
                        answer_id=ans.id, category_id=int(cat_id_str), score=sc))
                except ValueError:
                    pass

        question.extra_data_parsed = {
            'correct_order': items_list,
            'items': items_list,
            'scores': order_scores,
        }

    elif qtype == 'short_answer':
        keyword_groups = []
        idx = 0
        while f'keyword_{idx}_words' in form:
            words_text = form[f'keyword_{idx}_words']
            keywords = [w.strip() for w in words_text.split(',') if w.strip()]
            if keywords:
                kg_scores = {}
                for cat in Category.query.all():
                    sc = form.get(f'keyword_{idx}_score_{cat.id}', '0')
                    try:
                        sc_int = int(sc)
                    except ValueError:
                        sc_int = 0
                    if sc_int > 0:
                        kg_scores[str(cat.id)] = sc_int

                keyword_groups.append({'keywords': keywords, 'scores': kg_scores})

                for kw in keywords:
                    ans = Answer(question=question, text=kw, order_num=idx)
                    db.session.add(ans)
                    db.session.flush()
                    for cat_id_str, sc in kg_scores.items():
                        db.session.add(AnswerScore(
                            answer_id=ans.id, category_id=int(cat_id_str), score=sc))
            idx += 1

        all_kw = [kw for kg in keyword_groups for kw in kg['keywords']]
        question.extra_data_parsed = {
            'keywords': all_kw,
            'keyword_groups': keyword_groups,
        }

    db.session.commit()
    return question


# ── Password ──

@app.route('/admin/password', methods=['GET', 'POST'])
@login_required
def admin_password():
    if request.method == 'POST':
        old = request.form.get('old_password')
        new = request.form.get('new_password')
        confirm = request.form.get('confirm_password')

        if not current_user.check_password(old):
            flash('Staré heslo není správné.', 'danger')
        elif new != confirm:
            flash('Nová hesla se neshodují.', 'danger')
        elif len(new) < 6:
            flash('Heslo musí mít alespoň 6 znaků.', 'danger')
        else:
            current_user.set_password(new)
            db.session.commit()
            flash('Heslo bylo změněno.', 'success')
            return redirect(url_for('admin_dashboard'))

    return render_template('admin/password.html')


# ══════════════════════════════════════════
#  Run
# ══════════════════════════════════════════

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
