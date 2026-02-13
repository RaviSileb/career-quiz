import os
import json
import random
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, AdminUser, Category, Question, Answer, AnswerScore, QuizResult, QUESTION_TYPES

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'super-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'
login_manager.login_message = 'Pro přístup do administrace se musíte přihlásit.'


@login_manager.user_loader
def load_user(user_id):
    return AdminUser.query.get(int(user_id))


# ═══════════════════ POMOCNÉ FUNKCE ═══════════════════

def score_question(question, form_data, cat_scores):
    """Vyhodnotí jednu otázku a přičte body do cat_scores. Vrátí True pokud odpovězena."""
    qtype = question.question_type
    qid = question.id

    if qtype in ('single_choice', 'true_false', 'likert'):
        answer_id = form_data.get(f'question_{qid}')
        if answer_id:
            answer = Answer.query.get(int(answer_id))
            if answer and answer.question_id == question.id:
                for asc in answer.scores:
                    cat_scores[asc.category_id] = cat_scores.get(asc.category_id, 0) + asc.score
                return True

    elif qtype == 'multiple_choice':
        answer_ids = form_data.getlist(f'question_{qid}')
        if answer_ids:
            for aid in answer_ids:
                answer = Answer.query.get(int(aid))
                if answer and answer.question_id == question.id:
                    for asc in answer.scores:
                        cat_scores[asc.category_id] = cat_scores.get(asc.category_id, 0) + asc.score
            return True

    elif qtype == 'short_answer':
        user_text = form_data.get(f'question_{qid}', '').strip().lower()
        if user_text and question.extra_data:
            data = question.extra_data_parsed
            matched = False
            for kg in data.get('keyword_groups', []):
                if any(kw.lower() in user_text for kw in kg.get('keywords', [])):
                    for cid_s, sv in kg.get('scores', {}).items():
                        cat_scores[int(cid_s)] = cat_scores.get(int(cid_s), 0) + sv
                    matched = True
                    break
            if not matched:
                for cid_s, sv in data.get('default_scores', {}).items():
                    cat_scores[int(cid_s)] = cat_scores.get(int(cid_s), 0) + sv
            return True

    elif qtype == 'matching':
        if question.extra_data:
            data = question.extra_data_parsed
            pairs = data.get('pairs', [])
            answered_any = False
            for i, pair in enumerate(pairs):
                selected = form_data.get(f'question_{qid}_match_{i}', '')
                if selected:
                    answered_any = True
                    if selected == pair['right']:
                        for cid_s, sv in pair.get('scores', {}).items():
                            cat_scores[int(cid_s)] = cat_scores.get(int(cid_s), 0) + sv
            return answered_any

    elif qtype == 'ordering':
        user_order_str = form_data.get(f'question_{qid}_order', '')
        if user_order_str and question.extra_data:
            data = question.extra_data_parsed
            correct = data.get('correct_order', [])
            try:
                user_order = [int(x) for x in user_order_str.split(',')]
                correct_count = sum(1 for u, c in zip(user_order, correct) if u == c)
                for cid_s, sv in data.get('scores', {}).items():
                    cat_scores[int(cid_s)] = cat_scores.get(int(cid_s), 0) + sv * correct_count
            except (ValueError, TypeError):
                pass
            return True

    return False


# ═══════════════════ VEŘEJNÉ ROUTY ═══════════════════

@app.route('/')
def index():
    categories = Category.query.order_by(Category.name).all()
    total_questions = Question.query.filter_by(active=True).count()

    # Počet otázek dle typu
    type_counts = {}
    for code, label in QUESTION_TYPES.items():
        count = Question.query.filter_by(active=True, question_type=code).count()
        if count > 0:
            type_counts[label] = count

    return render_template('index.html', categories=categories,
                           total_questions=total_questions, type_counts=type_counts)


@app.route('/quiz')
def quiz():
    questions = Question.query.filter_by(active=True).all()
    random.shuffle(questions)

    # Připravit data pro matching a ordering
    quiz_data = {}
    for q in questions:
        if q.question_type == 'matching' and q.extra_data:
            data = q.extra_data_parsed
            pairs = data.get('pairs', [])
            rights = [p['right'] for p in pairs]
            random.shuffle(rights)
            quiz_data[q.id] = {'shuffled_rights': rights, 'pairs': pairs}

        elif q.question_type == 'ordering' and q.extra_data:
            data = q.extra_data_parsed
            items = data.get('items', [])
            indexed = list(enumerate(items))
            random.shuffle(indexed)
            quiz_data[q.id] = {'shuffled_items': indexed}

        elif q.question_type == 'likert' and q.extra_data:
            data = q.extra_data_parsed
            quiz_data[q.id] = {'labels': data.get('labels', [
                'Vůbec ne', 'Spíše ne', 'Neutrálně', 'Spíše ano', 'Rozhodně ano'
            ])}

    return render_template('quiz.html', questions=questions,
                           total=len(questions), quiz_data=quiz_data)


@app.route('/submit', methods=['POST'])
def submit():
    categories = Category.query.all()
    cat_scores = {cat.id: 0 for cat in categories}
    answered = 0
    total = 0

    questions = Question.query.filter_by(active=True).all()
    total = len(questions)

    for q in questions:
        if score_question(q, request.form, cat_scores):
            answered += 1

    # Výsledky seřazené podle skóre
    total_score = sum(cat_scores.values())
    results = []
    for cat in categories:
        sc = cat_scores.get(cat.id, 0)
        pct = round((sc / total_score) * 100, 1) if total_score > 0 else 0
        results.append({'category': cat, 'score': sc, 'percentage': pct})
    results.sort(key=lambda x: x['score'], reverse=True)

    # Uložení výsledku
    if results:
        top = results[0]
        quiz_result = QuizResult(
            top_category_id=top['category'].id,
            scores_json=json.dumps({str(cat.id): cat_scores[cat.id] for cat in categories}),
            answered_count=answered,
            total_count=total
        )
        db.session.add(quiz_result)
        db.session.commit()

    return render_template('result.html', results=results, answered=answered,
                           total=total, top_results=results[:3])


# ═══════════════════ ADMIN ROUTY ═══════════════════

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        user = AdminUser.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Úspěšně přihlášen/a.', 'success')
            return redirect(url_for('admin_dashboard'))
        flash('Neplatné přihlašovací údaje.', 'danger')
    return render_template('admin/login.html')


@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    flash('Odhlášen/a.', 'info')
    return redirect(url_for('index'))


@app.route('/admin')
@login_required
def admin_dashboard():
    stats = {
        'categories': Category.query.count(),
        'questions': Question.query.count(),
        'active_questions': Question.query.filter_by(active=True).count(),
        'results': QuizResult.query.count(),
    }

    # Počet otázek dle typu
    type_stats = {}
    for code, label in QUESTION_TYPES.items():
        count = Question.query.filter_by(question_type=code).count()
        if count > 0:
            type_stats[label] = count

    recent_results = QuizResult.query.order_by(QuizResult.timestamp.desc()).limit(10).all()
    return render_template('admin/dashboard.html', stats=stats,
                           type_stats=type_stats, recent_results=recent_results)


# --- Kategorie ---
@app.route('/admin/categories')
@login_required
def admin_categories():
    categories = Category.query.order_by(Category.name).all()
    return render_template('admin/categories.html', categories=categories)


@app.route('/admin/categories/new', methods=['GET', 'POST'])
@login_required
def admin_category_new():
    if request.method == 'POST':
        cat = Category(
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


@app.route('/admin/categories/<int:cat_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_category_edit(cat_id):
    cat = Category.query.get_or_404(cat_id)
    if request.method == 'POST':
        cat.name = request.form['name']
        cat.description = request.form.get('description', '')
        cat.icon = request.form.get('icon', '📁')
        cat.color = request.form.get('color', '#3498db')
        db.session.commit()
        flash(f'Kategorie "{cat.name}" upravena.', 'success')
        return redirect(url_for('admin_categories'))
    return render_template('admin/category_form.html', category=cat)


@app.route('/admin/categories/<int:cat_id>/delete', methods=['POST'])
@login_required
def admin_category_delete(cat_id):
    cat = Category.query.get_or_404(cat_id)
    db.session.delete(cat)
    db.session.commit()
    flash(f'Kategorie "{cat.name}" smazána.', 'warning')
    return redirect(url_for('admin_categories'))


# --- Otázky ---
@app.route('/admin/questions')
@login_required
def admin_questions():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    category_id = request.args.get('category', 0, type=int)
    qtype = request.args.get('type', '')

    query = Question.query
    if search:
        query = query.filter(Question.text.ilike(f'%{search}%'))
    if qtype:
        query = query.filter(Question.question_type == qtype)
    if category_id:
        query = query.join(Answer).join(AnswerScore).filter(
            AnswerScore.category_id == category_id).distinct()

    questions = query.order_by(Question.id).paginate(page=page, per_page=20, error_out=False)
    categories = Category.query.order_by(Category.name).all()
    return render_template('admin/questions.html', questions=questions, categories=categories,
                           search=search, category_id=category_id, qtype=qtype,
                           question_types=QUESTION_TYPES)


@app.route('/admin/questions/new', methods=['GET', 'POST'])
@login_required
def admin_question_new():
    categories = Category.query.order_by(Category.name).all()
    if request.method == 'POST':
        qtype = request.form.get('question_type', 'single_choice')
        question = Question(
            text=request.form['text'],
            question_type=qtype,
            active=bool(request.form.get('is_active'))
        )

        # Extra data pro speciální typy
        extra = _parse_extra_data(request.form, qtype)
        if extra:
            question.extra_data = json.dumps(extra, ensure_ascii=False)

        db.session.add(question)
        db.session.flush()

        # Zpracování odpovědí (pro answer-based typy)
        if qtype in ('single_choice', 'multiple_choice', 'true_false', 'likert'):
            _save_answers(request.form, question, categories)

        db.session.commit()
        flash('Otázka vytvořena.', 'success')
        return redirect(url_for('admin_questions'))
    return render_template('admin/question_form.html', question=None,
                           categories=categories, question_types=QUESTION_TYPES)


@app.route('/admin/questions/<int:q_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_question_edit(q_id):
    question = Question.query.get_or_404(q_id)
    categories = Category.query.order_by(Category.name).all()

    if request.method == 'POST':
        question.text = request.form['text']
        question.question_type = request.form.get('question_type', question.question_type)
        question.active = bool(request.form.get('is_active'))

        # Extra data
        extra = _parse_extra_data(request.form, question.question_type)
        question.extra_data = json.dumps(extra, ensure_ascii=False) if extra else None

        # Smazat staré odpovědi
        for answer in question.answers:
            AnswerScore.query.filter_by(answer_id=answer.id).delete()
        Answer.query.filter_by(question_id=question.id).delete()

        # Nové odpovědi
        if question.question_type in ('single_choice', 'multiple_choice', 'true_false', 'likert'):
            _save_answers(request.form, question, categories)

        db.session.commit()
        flash('Otázka upravena.', 'success')
        return redirect(url_for('admin_questions'))

    # Příprava dat pro formulář
    answers_data = []
    for answer in question.answers:
        scores_dict = {s.category_id: s.score for s in answer.scores}
        answers_data.append({'text': answer.text, 'scores': scores_dict})

    return render_template('admin/question_form.html', question=question,
                           categories=categories, answers_data=answers_data,
                           question_types=QUESTION_TYPES)


def _parse_extra_data(form, qtype):
    """Zpracuje extra data z formuláře podle typu otázky."""
    extra = {}

    if qtype == 'likert':
        labels = form.get('likert_labels', '')
        if labels:
            extra['labels'] = [l.strip() for l in labels.split(',')]
        else:
            extra['labels'] = ['Vůbec ne', 'Spíše ne', 'Neutrálně', 'Spíše ano', 'Rozhodně ano']

    elif qtype == 'matching':
        pairs = []
        idx = 0
        while True:
            left = form.get(f'match_{idx}_left')
            right = form.get(f'match_{idx}_right')
            if left is None:
                break
            if left.strip() and right.strip():
                pair = {'left': left.strip(), 'right': right.strip(), 'scores': {}}
                # Přečíst skóre pro tento pár
                for key in form:
                    if key.startswith(f'match_{idx}_score_'):
                        cat_id = key.replace(f'match_{idx}_score_', '')
                        try:
                            sv = int(form[key])
                            if sv > 0:
                                pair['scores'][cat_id] = sv
                        except ValueError:
                            pass
                pairs.append(pair)
            idx += 1
        extra['pairs'] = pairs

    elif qtype == 'ordering':
        items_str = form.get('order_items', '')
        scores_str = form.get('order_scores', '')
        if items_str:
            items = [i.strip() for i in items_str.split('\n') if i.strip()]
            extra['items'] = items
            extra['correct_order'] = list(range(len(items)))
            extra['scores'] = {}
            if scores_str:
                try:
                    for part in scores_str.split(','):
                        cid, sv = part.strip().split(':')
                        extra['scores'][cid.strip()] = int(sv.strip())
                except (ValueError, IndexError):
                    pass

    elif qtype == 'short_answer':
        keyword_groups = []
        idx = 0
        while True:
            keywords = form.get(f'keyword_{idx}_words')
            if keywords is None:
                break
            if keywords.strip():
                kg = {
                    'keywords': [k.strip() for k in keywords.split(',') if k.strip()],
                    'scores': {}
                }
                for key in form:
                    if key.startswith(f'keyword_{idx}_score_'):
                        cat_id = key.replace(f'keyword_{idx}_score_', '')
                        try:
                            sv = int(form[key])
                            if sv > 0:
                                kg['scores'][cat_id] = sv
                        except ValueError:
                            pass
                keyword_groups.append(kg)
            idx += 1
        extra['keyword_groups'] = keyword_groups
        extra['default_scores'] = {}

    return extra if extra else None


def _save_answers(form, question, categories):
    """Uloží odpovědi a jejich skóre z formuláře."""
    answer_idx = 0
    while True:
        answer_text = form.get(f'answer_{answer_idx}_text')
        if answer_text is None:
            break
        if answer_text.strip():
            answer = Answer(text=answer_text.strip(), question_id=question.id, order_num=answer_idx)
            db.session.add(answer)
            db.session.flush()

            for cat in categories:
                score_val = form.get(f'answer_{answer_idx}_score_{cat.id}', '0')
                try:
                    score_val = int(score_val)
                except ValueError:
                    score_val = 0
                if score_val != 0:
                    ascore = AnswerScore(answer_id=answer.id, category_id=cat.id, score=score_val)
                    db.session.add(ascore)
        answer_idx += 1


@app.route('/admin/questions/<int:q_id>/delete', methods=['POST'])
@login_required
def admin_question_delete(q_id):
    question = Question.query.get_or_404(q_id)
    db.session.delete(question)
    db.session.commit()
    flash('Otázka smazána.', 'warning')
    return redirect(url_for('admin_questions'))


@app.route('/admin/questions/<int:q_id>/toggle', methods=['POST'])
@login_required
def admin_question_toggle(q_id):
    question = Question.query.get_or_404(q_id)
    question.active = not question.active
    db.session.commit()
    status = "aktivována" if question.active else "deaktivována"
    flash(f'Otázka {status}.', 'info')
    return redirect(url_for('admin_questions'))


# --- Heslo ---
@app.route('/admin/password', methods=['GET', 'POST'])
@login_required
def admin_password():
    if request.method == 'POST':
        old_pw = request.form.get('old_password', '')
        new_pw = request.form.get('new_password', '')
        confirm = request.form.get('confirm_password', '')

        if not current_user.check_password(old_pw):
            flash('Staré heslo je nesprávné.', 'danger')
        elif new_pw != confirm:
            flash('Nová hesla se neshodují.', 'danger')
        elif len(new_pw) < 6:
            flash('Heslo musí mít alespoň 6 znaků.', 'danger')
        else:
            current_user.set_password(new_pw)
            db.session.commit()
            flash('Heslo úspěšně změněno.', 'success')
            return redirect(url_for('admin_dashboard'))
    return render_template('admin/password.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
