from app import app
from models import db, AdminUser, Category, Question, Answer, AnswerScore
from init_data import get_categories, get_questions


def init_database():
    with app.app_context():
        db.create_all()
        if not AdminUser.query.first():
            admin = AdminUser(username='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("[OK] Admin vytvoren (admin / admin123)")
        if not Category.query.first():
            cat_map = {}
            for cd in get_categories():
                cat = Category(name=cd['name'], description=cd['description'], icon=cd['icon'], color=cd['color'])
                db.session.add(cat)
                db.session.flush()
                cat_map[cd['name']] = cat.id
            db.session.commit()
            print(f"[OK] {len(cat_map)} kategorii")
            if not Question.query.first():
                qdata = get_questions()
                for i, qd in enumerate(qdata):
                    q = Question(text=qd['text'], order_num=i + 1, active=True)
                    db.session.add(q)
                    db.session.flush()
                    for j, ad in enumerate(qd['answers']):
                        a = Answer(question_id=q.id, text=ad['text'], order_num=j)
                        db.session.add(a)
                        db.session.flush()
                        for cname, sv in ad.get('scores', {}).items():
                            if cname in cat_map:
                                db.session.add(AnswerScore(answer_id=a.id, category_id=cat_map[cname], score=sv))
                db.session.commit()
                print(f"[OK] {len(qdata)} otazek")
        else:
            print("[OK] Data jiz existuji")


if __name__ == '__main__':
    init_database()
