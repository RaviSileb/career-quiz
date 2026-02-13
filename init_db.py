"""
init_db.py – Inicializace databáze pro dvoudílný kariérní kvíz.

Vytvoří tabulky, naplní:
  • admin účet (admin / admin123)
  • 11 kategorií
  • 88 pozic
  • 135 Part-1 otázek (kariérní směr) s AnswerScore
  • 880 Part-2 otázek (pracovní pozice) s AnswerPositionScore
  • výchozí nastavení (part1_count=40, part2_count=40)
"""

import os
import sys
import json

from app import app
from models import (
    db, AdminUser, Category, Position, Question, Answer,
    AnswerScore, AnswerPositionScore, QuizSetting, QuizResult,
)
from init_data import get_categories, get_positions, get_questions
from init_data_part2 import get_part2_questions


def init_database():
    with app.app_context():
        db.create_all()

        # ── Už inicializováno? ──
        if AdminUser.query.first():
            print('Databáze již existuje – přeskakuji.')
            return

        print('=== Inicializace databáze ===')

        # ── Admin ──
        admin = AdminUser(username='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.flush()
        print('✓ Admin účet vytvořen')

        # ── Výchozí nastavení ──
        for key, val in [('part1_count', '40'), ('part2_count', '40')]:
            db.session.add(QuizSetting(key=key, value=val))
        db.session.flush()
        print('✓ Výchozí nastavení kvízu')

        # ── Kategorie ──
        cat_map = {}  # code → Category obj
        for cd in get_categories():
            cat = Category(
                code=cd['code'],
                name=cd['name'],
                description=cd['description'],
                icon=cd['icon'],
                color=cd['color'],
            )
            db.session.add(cat)
            db.session.flush()
            cat_map[cd['code']] = cat
        print(f'✓ {len(cat_map)} kategorií')

        # ── Pozice ──
        pos_map = {}  # position_name → Position obj
        for pd in get_positions():
            pos = Position(
                name=pd['name'],
                description=pd['description'],
                category_id=cat_map[pd['category']].id,
                icon=pd.get('icon', '👤'),
            )
            db.session.add(pos)
            db.session.flush()
            pos_map[pd['name']] = pos
        print(f'✓ {len(pos_map)} pozic')

        # ── Part 1 otázky ──
        p1_count = 0
        for qd in get_questions():
            q = Question(
                text=qd['text'],
                question_type=qd['type'],
                part=1,
                order_num=p1_count,
                active=True,
            )
            # extra_data (matching, ordering, short_answer)
            if 'extra_data' in qd:
                ed = qd['extra_data']
                # Convert category codes to IDs in extra_data scores
                if 'scores' in ed:
                    new_scores = {}
                    for code, sc in ed['scores'].items():
                        if code in cat_map:
                            new_scores[str(cat_map[code].id)] = sc
                        else:
                            new_scores[code] = sc
                    ed['scores'] = new_scores
                q.extra_data = json.dumps(ed, ensure_ascii=False)

            db.session.add(q)
            db.session.flush()

            # Odpovědi
            for i, ad in enumerate(qd.get('answers', [])):
                ans = Answer(
                    question_id=q.id,
                    text=ad['text'],
                    order_num=i,
                )
                db.session.add(ans)
                db.session.flush()

                # AnswerScore (category scoring)
                for code, sc in ad.get('scores', {}).items():
                    if sc and code in cat_map:
                        db.session.add(AnswerScore(
                            answer_id=ans.id,
                            category_id=cat_map[code].id,
                            score=sc,
                        ))

            p1_count += 1

        db.session.flush()
        print(f'✓ {p1_count} Part-1 otázek')

        # ── Part 2 otázky ──
        p2_count = 0
        for qd in get_part2_questions():
            cat_code = qd.get('category')
            cat_id = cat_map[cat_code].id if cat_code in cat_map else None

            q = Question(
                text=qd['text'],
                question_type=qd['type'],
                part=2,
                category_id=cat_id,
                order_num=p2_count,
                active=True,
            )
            db.session.add(q)
            db.session.flush()

            for i, ad in enumerate(qd.get('answers', [])):
                ans = Answer(
                    question_id=q.id,
                    text=ad['text'],
                    order_num=i,
                )
                db.session.add(ans)
                db.session.flush()

                # AnswerPositionScore (position scoring)
                for pos_name, sc in ad.get('position_scores', {}).items():
                    if sc and pos_name in pos_map:
                        db.session.add(AnswerPositionScore(
                            answer_id=ans.id,
                            position_id=pos_map[pos_name].id,
                            score=sc,
                        ))

            p2_count += 1

            # Periodic flush every 100 questions
            if p2_count % 100 == 0:
                db.session.flush()

        db.session.commit()
        print(f'✓ {p2_count} Part-2 otázek')
        print(f'=== Celkem: {p1_count + p2_count} otázek ===')
        print('Inicializace dokončena.')


if __name__ == '__main__':
    init_database()
