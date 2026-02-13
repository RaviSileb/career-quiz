import os
import json
import random
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from models import db, AdminUser, Category, Question, Answer, AnswerScore, QuizResult

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


# ==================== VEREJNE ROUTY ====================

@app.route('/')
def index():
    categories = Category.query.order_by(Category.name).all()
    total_questions = Question.query.filter_by(active=True).count()
    return render_template('index.html', categories=categories, total_questions=total_questions)


@app.route('/quiz')
def quiz():
    questions = Question.query.filter_by(active=True).all()
    random.shuffle(questions)
    return render_template('quiz.html', questions=questions, total=len(questions))


@app.route('/submit', methods=['POST'])
def submit():
    categories = Category.query.all()
    scores = {cat.id: 0 for cat in categories}
    max_possible = {cat.id: 0 for cat in categories}
    answered = 0

    questions = Question.query.filter_by(active=True).all()
    question_ids = [str(q.id) for q in questions]

    for q_id in question_ids:
        answer_id = request.form.get(f'question_{q_id}')
        if answer_id:
            answered += 1
            answer = Answer.query.get(int(answer_id))
            if answer:
                for ascore in answer.scores:
                    scores[ascore.category_id] = scores.get(ascore.category_id, 0) + ascore.score

    # Vypocet max moznych bodu na kategorii (z tech otazek, co uzivatel dostal)
    submitted_q_ids = []
    for q_id in question_ids:
        if request.form.get(f'question_{q_id}'):
            submitted_q_ids.append(int(q_id))

    for q_id in submitted_q_ids:
        question = Question.query.get(q_id)
        if question:
            for answer in question.answers:
                for ascore in answer.scores:
                    if ascore.score > max_possible.get(ascore.category_id, 0):
                        pass  # Pouze pro zobrazení procent
                    max_possible[ascore.category_id] = max_possible.get(ascore.category_id, 0) + max(
                        [s.score for s in answer.scores if s.category_id == ascore.category_id], default=0
                    )

    # Serazeni kategorii podle skore
    results = []
    total_score = sum(scores.values())
    for cat in categories:
        cat_score = scores.get(cat.id, 0)
        if total_score > 0:
            percentage = round((cat_score / total_score) * 100, 1) if total_score > 0 else 0
        else:
            percentage = 0
        results.append({
            'category': cat,
            'score': cat_score,
            'percentage': percentage,
        })

    results.sort(key=lambda x: x['score'], reverse=True)

    # Ulozeni vysledku
    if results:
        top = results[0]
        quiz_result = QuizResult(
            top_category_id=top['category'].id,
            scores_json=json.dumps({str(cat.id): scores[cat.id] for cat in categories})
        )
        db.session.add(quiz_result)
        db.session.commit()

    return render_template('result.html', results=results, answered=answered,
                           top_results=results[:3])


# ==================== ADMIN ROUTY ====================

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
    recent_results = QuizResult.query.order_by(QuizResult.timestamp.desc()).limit(10).all()
    return render_template('admin/dashboard.html', stats=stats, recent_results=recent_results)


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


# --- Otazky ---
@app.route('/admin/questions')
@login_required
def admin_questions():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    category_id = request.args.get('category', 0, type=int)

    query = Question.query
    if search:
        query = query.filter(Question.text.ilike(f'%{search}%'))
    if category_id:
        query = query.join(Answer).join(AnswerScore).filter(AnswerScore.category_id == category_id).distinct()

    questions = query.order_by(Question.id).paginate(page=page, per_page=20, error_out=False)
    categories = Category.query.order_by(Category.name).all()
    return render_template('admin/questions.html', questions=questions, categories=categories,
                           search=search, category_id=category_id)


@app.route('/admin/questions/new', methods=['GET', 'POST'])
@login_required
def admin_question_new():
    categories = Category.query.order_by(Category.name).all()
    if request.method == 'POST':
        question = Question(
            text=request.form['text'],
            active=bool(request.form.get('is_active'))
        )
        db.session.add(question)
        db.session.flush()

        # Zpracovani odpovedi
        answer_idx = 0
        while True:
            answer_text = request.form.get(f'answer_{answer_idx}_text')
            if answer_text is None:
                break
            if answer_text.strip():
                answer = Answer(text=answer_text.strip(), question_id=question.id)
                db.session.add(answer)
                db.session.flush()

                # Zpracovani score pro kazdou kategorii
                for cat in categories:
                    score_val = request.form.get(f'answer_{answer_idx}_score_{cat.id}', '0')
                    try:
                        score_val = int(score_val)
                    except ValueError:
                        score_val = 0
                    if score_val != 0:
                        ascore = AnswerScore(answer_id=answer.id, category_id=cat.id, score=score_val)
                        db.session.add(ascore)
            answer_idx += 1

        db.session.commit()
        flash('Otázka vytvořena.', 'success')
        return redirect(url_for('admin_questions'))
    return render_template('admin/question_form.html', question=None, categories=categories)


@app.route('/admin/questions/<int:q_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_question_edit(q_id):
    question = Question.query.get_or_404(q_id)
    categories = Category.query.order_by(Category.name).all()

    if request.method == 'POST':
        question.text = request.form['text']
        question.active = bool(request.form.get('is_active'))

        # Smazat stare odpovedi
        for answer in question.answers:
            AnswerScore.query.filter_by(answer_id=answer.id).delete()
        Answer.query.filter_by(question_id=question.id).delete()

        # Nové odpovedi
        answer_idx = 0
        while True:
            answer_text = request.form.get(f'answer_{answer_idx}_text')
            if answer_text is None:
                break
            if answer_text.strip():
                answer = Answer(text=answer_text.strip(), question_id=question.id)
                db.session.add(answer)
                db.session.flush()

                for cat in categories:
                    score_val = request.form.get(f'answer_{answer_idx}_score_{cat.id}', '0')
                    try:
                        score_val = int(score_val)
                    except ValueError:
                        score_val = 0
                    if score_val != 0:
                        ascore = AnswerScore(answer_id=answer.id, category_id=cat.id, score=score_val)
                        db.session.add(ascore)
            answer_idx += 1

        db.session.commit()
        flash('Otázka upravena.', 'success')
        return redirect(url_for('admin_questions'))

    # Priprava dat odpovedi pro formular
    answers_data = []
    for answer in question.answers:
        scores_dict = {s.category_id: s.score for s in answer.scores}
        answers_data.append({'text': answer.text, 'scores': scores_dict})

    return render_template('admin/question_form.html', question=question,
                           categories=categories, answers_data=answers_data)


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
