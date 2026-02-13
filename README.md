# 🎯 Career Quiz v0.2.0

Dvoudílný interaktivní kariérní kvíz s **1015 otázkami**, který pomáhá uživatelům najít ideální kariérní směr i konkrétní pracovní pozici. Pozice vycházejí z databáze [NSP.cz](https://nsp.cz).

## ✨ Funkce

- **Dvoudílný kvíz:**
  - **Část 1 – Kariérní směr:** 135 otázek (7 typů), určí top 3 kariérní kategorie
  - **Část 2 – Konkrétní pozice:** 880 otázek zaměřených na 88 pracovních pozic dle NSP.cz
- **7 typů otázek** – výběr jedné/více odpovědí, pravda/nepravda, Likert škála, krátká odpověď, přiřazování, seřazování
- **88 pracovních pozic** (8 na kategorii) s popisy dle NSP.cz
- **Konfigurovatelný počet otázek** – admin nastaví kolik otázek se zobrazí v každé části (výchozí: 40 + 40)
- **Mezivýsledky** po 1. části s grafickým zobrazením top 3 kategorií
- **Finální výsledky** s doporučenými pozicemi a podrobnostmi podle kategorií
- **Admin rozhraní** pro správu otázek, kategorií a nastavení kvízu
- **Responzivní design** – Bootstrap 5 + SortableJS pro drag & drop

## 🔄 Jak kvíz funguje

1. **Část 1** – Žák odpoví na 40 otázek různých typů → systém vyhodnotí 3 nejsilnější kariérní kategorie
2. **Mezivýsledky** – Zobrazí se přehled kategorií s procentuálním skóre
3. **Část 2** – 40 otázek z top 3 kategorií cílí na konkrétní pracovní pozice
4. **Výsledky** – Top pozice s popisem + kompletní přehled kategorií a pozic

## 📊 Profesní kategorie a pozice

| Ikona | Kategorie | Pozice |
|-------|-----------|--------|
| 🌾 | Zemědělství a lesnictví | Agronom, Veterinář, Lesní inženýr, Zahradník, Zem. technik, Chovatel, Myslivec, Ekolog |
| 🏗️ | Stavebnictví a architektura | Architekt, Stavbyvedoucí, Projektant, Geodet, Rozpočtář, Interiér. designér, Zedník, Instalatér |
| ⚙️ | Strojírenství a elektrotechnika | Strojní konstruktér, Technolog, Elektrotechnik, Autotronik, CNC programátor, Svářeč, Obráběč, Mechatronik |
| 🚗 | Doprava a logistika | Logistik, Pilot, Řidič, Dispečer, Strojvedoucí, Kapitán plavidla, Skladník, Celník |
| 💻 | Informační technologie | Programátor, Analytik IT, Správce sítí, Webdesigner, Tester, Datový inženýr, Kybernetik, Herní vývojář |
| 🏥 | Zdravotnictví a medicína | Lékař, Farmaceut, Zubař, Zdravotní sestra, Fyzioterapeut, Záchranář, Nutriční terapeut, Biomed. inženýr |
| 🛒 | Obchod a služby | Obch. zástupce, Marketing. specialista, Nákupčí, Kuchař, Průvodce, Recepční, Realitní makléř, Barman |
| 📚 | Školství a vzdělávání | Učitel, Lektor, Vědecký pracovník, Kouč, Trenér, Vychovatel, Speciální pedagog, Knihovník |
| ⚖️ | Právo a veřejná správa | Advokát, Soudce, Notář, Státní zástupce, Exekutor, Policista, Hasič, Úředník |
| 📊 | Management a podnikání | Gen. ředitel, Projektový manažer, Finanční analytik, Účetní, HR specialista, Manažer kvality, Podnikatel, Controller |
| 🎨 | Umění a kultura | Herec, Režisér, Hudebník, Grafik, Fotograf, Spisovatel, Kameraman, Ilustrátor |

## 🛠️ Technologie

- **Backend:** Flask 3.0, Flask-SQLAlchemy, Flask-Login, Gunicorn
- **Databáze:** SQLite
- **Frontend:** Bootstrap 5.3, Bootstrap Icons, SortableJS
- **Kontejnerizace:** Docker
- **Registry:** GitHub Container Registry (ghcr.io)

## 🚀 Spuštění

### Z GHCR (nejjednodušší)

```bash
docker login ghcr.io -u RaviSileb
docker pull ghcr.io/ravisileb/career-quiz:v0.2.0
docker run -d --name career-quiz -p 8080:5000 ghcr.io/ravisileb/career-quiz:v0.2.0
```

### Lokální build

```bash
docker build -t career-quiz .
docker run -d --name career-quiz -p 8080:5000 career-quiz
```

Aplikace poběží na **http://localhost:8080**

### Bez Dockeru

```bash
pip install -r requirements.txt
python init_db.py
python app.py
```

## 🔐 Admin rozhraní

Přístup na `/admin/login` s výchozími přihlašovacími údaji:

- **Uživatel:** `admin`
- **Heslo:** `admin123`

Admin umožňuje:
- Správu kategorií a otázek (CRUD, filtrování podle části/typu/kategorie)
- Nastavení počtu otázek pro Část 1 a Část 2
- Přehled výsledků kvízů

> ⚠️ V produkci změňte heslo a `SECRET_KEY` v Dockerfile.

## 📁 Struktura projektu

```
career_quiz/
├── app.py                 # Flask aplikace, routing, scoring engine (Part 1 + 2)
├── models.py              # SQLAlchemy modely (Question, Category, Position, ...)
├── init_data.py           # 135 Part-1 otázek, 11 kategorií, 88 pozic
├── init_data_part2.py     # 880 Part-2 otázek (80 × 11 kategorií)
├── init_db.py             # Inicializace databáze
├── requirements.txt       # Python závislosti
├── Dockerfile             # Docker konfigurace
├── static/
│   └── style.css          # Vlastní styly
└── templates/
    ├── base.html           # Základní layout
    ├── index.html          # Úvodní stránka s popisem kvízu
    ├── quiz.html           # Část 1 – kariérní směr
    ├── quiz_part2.html     # Část 2 – konkrétní pozice
    ├── part1_results.html  # Mezivýsledky po 1. části
    ├── result.html         # Finální výsledky
    └── admin/
        ├── dashboard.html  # Admin přehled
        ├── settings.html   # Nastavení počtu otázek
        ├── questions.html  # Správa otázek
        ├── categories.html # Správa kategorií
        └── ...
```

## 📝 Licence

Soukromý projekt.
