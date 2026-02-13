from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()


class AdminUser(UserMixin, db.Model):
    __tablename__ = 'admin_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(10))
    color = db.Column(db.String(7), default='#3498db')


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    order_num = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)
    answers = db.relationship('Answer', backref='question', cascade='all, delete-orphan', order_by='Answer.order_num')


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    order_num = db.Column(db.Integer, default=0)
    scores = db.relationship('AnswerScore', backref='answer', cascade='all, delete-orphan')


class AnswerScore(db.Model):
    __tablename__ = 'answer_score'
    id = db.Column(db.Integer, primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    score = db.Column(db.Integer, default=1)
    category = db.relationship('Category')


class QuizResult(db.Model):
    __tablename__ = 'quiz_result'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    top_category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    scores_json = db.Column(db.Text)
    top_category = db.relationship('Category')
