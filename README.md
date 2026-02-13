# 🎯 Career Quiz

Interaktivní kariérní kvíz, který pomocí 135 otázek různých typů pomáhá uživatelům zjistit, které profesní oblasti jim nejvíce vyhovují.

## ✨ Funkce

- **7 typů otázek** – výběr jedné/více odpovědí, pravda/nepravda, Likert škála, krátká odpověď, přiřazování, seřazování
- **135 kariérních otázek** pokrývajících 11 profesních kategorií
- **Automatické vyhodnocení** s grafem výsledků a top 3 doporučenými oblastmi
- **Admin rozhraní** pro správu otázek a kategorií (CRUD)
- **Responzivní design** – Bootstrap 5 + SortableJS pro drag & drop

## 📊 Profesní kategorie

| Ikona | Kategorie |
|-------|-----------|
| 🌾 | Zemědělství a lesnictví |
| 🏗️ | Stavebnictví a architektura |
| ⚙️ | Strojírenství a elektrotechnika |
| 🚗 | Doprava a logistika |
| 💻 | Informační technologie |
| 🏥 | Zdravotnictví a medicína |
| 🛒 | Obchod a služby |
| 📚 | Školství a vzdělávání |
| ⚖️ | Právo a veřejná správa |
| 📊 | Management a podnikání |
| 🎨 | Umění a kultura |

## 🛠️ Technologie

- **Backend:** Flask 3.0, Flask-SQLAlchemy, Flask-Login, Gunicorn
- **Databáze:** SQLite
- **Frontend:** Bootstrap 5.3, Bootstrap Icons, SortableJS
- **Kontejnerizace:** Docker

## 🚀 Spuštění

### Docker (doporučeno)

```bash
docker build -t career-quiz .
docker run -d --name career-quiz -p 8080:5000 career-quiz
```

Aplikace poběží na **http://localhost:8080**

### Lokálně

```bash
pip install -r requirements.txt
python init_db.py
python app.py
```

## 🔐 Admin rozhraní

Přístup na `/admin/login` s výchozími přihlašovacími údaji:

- **Uživatel:** `admin`
- **Heslo:** `admin123`

> ⚠️ V produkci změňte heslo a `SECRET_KEY` v Dockerfile.

## 📁 Struktura projektu

```
career_quiz/
├── app.py                 # Flask aplikace + routing + scoring engine
├── models.py              # SQLAlchemy modely (Question, Category, ...)
├── init_data.py           # 135 otázek a 11 kategorií
├── init_db.py             # Inicializace databáze
├── requirements.txt       # Python závislosti
├── Dockerfile             # Docker konfigurace
├── static/
│   └── style.css          # Vlastní styly
└── templates/
    ├── base.html           # Základní layout
    ├── index.html          # Úvodní stránka
    ├── quiz.html           # Kvíz
    ├── result.html         # Výsledky
    └── admin/              # Admin šablony
```

## 📝 Licence

Soukromý projekt.
