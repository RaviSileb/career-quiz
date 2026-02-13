import json
from app import app
from models import db, AdminUser, Category, Question, Answer, AnswerScore
from init_data import get_categories, get_questions


def convert_scores(scores_dict, cat_map):
    """Převede slovník {kód_kategorie: skóre} na {id_kategorie: skóre}."""
    result = {}
    for code, sv in scores_dict.items():
        if code in cat_map:
            result[cat_map[code]] = sv
    return result


def init_database():
    with app.app_context():
        db.create_all()

        # Admin
        if not AdminUser.query.first():
            admin = AdminUser(username='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("[OK] Admin vytvořen (admin / admin123)")

        # Kategorie
        if not Category.query.first():
            cat_map = {}  # code -> id
            for cd in get_categories():
                cat = Category(
                    name=cd['name'],
                    description=cd['description'],
                    icon=cd['icon'],
                    color=cd['color']
                )
                db.session.add(cat)
                db.session.flush()
                cat_map[cd['code']] = cat.id
            db.session.commit()
            print(f"[OK] {len(cat_map)} kategorií vytvořeno")

            # Otázky
            if not Question.query.first():
                qdata = get_questions()
                for i, qd in enumerate(qdata):
                    qtype = qd.get('type', 'single_choice')

                    # Zpracování extra_data – převedeme kódy kategorií na ID
                    raw_extra = qd.get('extra_data')
                    extra_json = None
                    if raw_extra:
                        extra = json.loads(json.dumps(raw_extra))

                        # Matching – převést scores v párech
                        if qtype == 'matching' and 'pairs' in extra:
                            for pair in extra['pairs']:
                                if 'scores' in pair:
                                    pair['scores'] = {
                                        str(k): v for k, v in
                                        convert_scores(pair['scores'], cat_map).items()
                                    }

                        # Ordering – převést scores
                        if qtype == 'ordering' and 'scores' in extra:
                            extra['scores'] = {
                                str(k): v for k, v in
                                convert_scores(extra['scores'], cat_map).items()
                            }

                        # Short answer – převést scores v keyword groups
                        if qtype == 'short_answer' and 'keyword_groups' in extra:
                            for kg in extra['keyword_groups']:
                                if 'scores' in kg:
                                    kg['scores'] = {
                                        str(k): v for k, v in
                                        convert_scores(kg['scores'], cat_map).items()
                                    }
                            if 'default_scores' in extra:
                                extra['default_scores'] = {
                                    str(k): v for k, v in
                                    convert_scores(extra['default_scores'], cat_map).items()
                                }

                        # Fill blank – převést scores
                        if qtype == 'fill_blank':
                            if 'correct_scores' in extra:
                                extra['correct_scores'] = {
                                    str(k): v for k, v in
                                    convert_scores(extra['correct_scores'], cat_map).items()
                                }
                            if 'wrong_scores' in extra:
                                extra['wrong_scores'] = {
                                    str(k): v for k, v in
                                    convert_scores(extra['wrong_scores'], cat_map).items()
                                }

                        extra_json = json.dumps(extra, ensure_ascii=False)

                    q = Question(
                        text=qd['text'],
                        question_type=qtype,
                        order_num=i + 1,
                        active=True,
                        extra_data=extra_json
                    )
                    db.session.add(q)
                    db.session.flush()

                    # Odpovědi (pro answer-based typy)
                    for j, ad in enumerate(qd.get('answers', [])):
                        a = Answer(question_id=q.id, text=ad['text'], order_num=j)
                        db.session.add(a)
                        db.session.flush()

                        for code, sv in ad.get('scores', {}).items():
                            if code in cat_map:
                                db.session.add(AnswerScore(
                                    answer_id=a.id,
                                    category_id=cat_map[code],
                                    score=sv
                                ))

                db.session.commit()
                print(f"[OK] {len(qdata)} otázek vytvořeno")

                # Statistika typů
                from collections import Counter
                type_counts = Counter(qd.get('type', 'single_choice') for qd in qdata)
                for t, c in sorted(type_counts.items()):
                    print(f"     {t}: {c}")
        else:
            print("[OK] Data již existují")


if __name__ == '__main__':
    init_database()
