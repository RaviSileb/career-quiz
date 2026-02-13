from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json

db = SQLAlchemy()

QUESTION_TYPES = {
    'single_choice': 'Výběr jedné odpovědi',
    'multiple_choice': 'Více správných odpovědí',
    'true_false': 'Pravda / Nepravda',
    'likert': 'Škálování (Likert)',
    'short_answer': 'Krátká odpověď',
    'matching': 'Přiřazování',
    'ordering': 'Seřazování',
}


class AdminUser(UserMixin, db.Model):
    __tablename__ = 'admin_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class QuizSetting(db.Model):
    """Nastavení kvízu (key-value)."""
    __tablename__ = 'quiz_setting'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)
    value = db.Column(db.String(200), nullable=False)

    @staticmethod
    def get(key, default=None):
        s = QuizSetting.query.filter_by(key=key).first()
        return s.value if s else default

    @staticmethod
    def get_int(key, default=0):
        val = QuizSetting.get(key)
        try:
            return int(val)
        except (TypeError, ValueError):
            return default

    @staticmethod
    def set_val(key, value):
        s = QuizSetting.query.filter_by(key=key).first()
        if s:
            s.value = str(value)
        else:
            s = QuizSetting(key=key, value=str(value))
            db.session.add(s)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(10))
    color = db.Column(db.String(7), default='#3498db')
    positions = db.relationship('Position', backref='category',
                                cascade='all, delete-orphan', order_by='Position.name')


class Position(db.Model):
    """Pracovní pozice v rámci kariérní kategorie."""
    __tablename__ = 'position'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    icon = db.Column(db.String(10), default='👤')
    active = db.Column(db.Boolean, default=True)


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(20), default='single_choice')
    part = db.Column(db.Integer, default=1)  # 1 = kariérní směr, 2 = pracovní pozice
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    order_num = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)
    extra_data = db.Column(db.Text)
    answers = db.relationship('Answer', backref='question',
                              cascade='all, delete-orphan', order_by='Answer.order_num')
    category = db.relationship('Category')

    @property
    def extra_data_parsed(self):
        if self.extra_data:
            try:
                return json.loads(self.extra_data)
            except (json.JSONDecodeError, TypeError):
                return {}
        return {}

    @extra_data_parsed.setter
    def extra_data_parsed(self, value):
        self.extra_data = json.dumps(value, ensure_ascii=False) if value else None

    @property
    def type_label(self):
        return QUESTION_TYPES.get(self.question_type, self.question_type)


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    order_num = db.Column(db.Integer, default=0)
    scores = db.relationship('AnswerScore', backref='answer', cascade='all, delete-orphan')
    position_scores = db.relationship('AnswerPositionScore', backref='answer',
                                      cascade='all, delete-orphan')


class AnswerScore(db.Model):
    """Bodování odpovědi pro kariérní kategorie (Part 1)."""
    __tablename__ = 'answer_score'
    id = db.Column(db.Integer, primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    score = db.Column(db.Integer, default=1)
    category = db.relationship('Category')


class AnswerPositionScore(db.Model):
    """Bodování odpovědi pro pracovní pozice (Part 2)."""
    __tablename__ = 'answer_position_score'
    id = db.Column(db.Integer, primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)
    score = db.Column(db.Integer, default=1)
    position = db.relationship('Position')


class QuizResult(db.Model):
    __tablename__ = 'quiz_result'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    # Part 1
    top_category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    scores_json = db.Column(db.Text)
    answered_count = db.Column(db.Integer, default=0)
    total_count = db.Column(db.Integer, default=0)
    # Part 2
    top3_categories_json = db.Column(db.Text)
    position_scores_json = db.Column(db.Text)
    part2_answered = db.Column(db.Integer, default=0)
    part2_total = db.Column(db.Integer, default=0)
    top_category = db.relationship('Category')
