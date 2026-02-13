# Release Notes

## v0.1.0 – Multi-Type Quiz Engine (2025-02-13)

### 🆕 Nové funkce

#### 8 typů otázek
- **Výběr jedné odpovědi (Single Choice)** – klasický výběr z možností (radio)
- **Více správných odpovědí (Multiple Choice)** – zaškrtávací políčka
- **Pravda / Nepravda (True/False)** – velká tlačítka Ano/Ne
- **Škálování (Likert Scale)** – stupnice 1–5 s popisky
- **Krátká odpověď (Short Answer)** – textový vstup s keyword matching
- **Doplňování (Fill in the Blank)** – vyplnění chybějícího slova
- **Přiřazování (Matching)** – propojení párů pomocí dropdown menu
- **Seřazování (Ordering)** – drag & drop řazení s tlačítky nahoru/dolů

#### 150 kariérních otázek
- 30× výběr jedné odpovědi
- 18× více správných odpovědí
- 20× pravda/nepravda
- 30× likert škála
- 15× krátká odpověď
- 15× doplňování
- 12× přiřazování
- 10× seřazování

#### Vylepšené admin rozhraní
- Filtr otázek podle typu
- Dynamický formulář – mění se podle zvoleného typu otázky
- Editor matching párů s category scoring
- Editor klíčových slov pro short answer
- Editor seřazování s definicí správného pořadí
- Přehled otázek podle typu na dashboardu

#### UI/UX vylepšení
- SortableJS pro drag & drop řazení (CDN)
- Barevné badge pro každý typ otázky
- Responzivní design pro mobile
- Progress bar sledující zodpovězené otázky všech typů
- Animované Likert a True/False tlačítka

### 📦 Technické změny
- `models.py`: `Question.question_type`, `Question.extra_data` (JSON), `QuizResult.answered_count`/`total_count`
- `app.py`: `score_question()` – univerzální scoring engine pro všech 8 typů
- `init_data.py`: Helper funkce `_sc`, `_mc`, `_tf`, `_likert`, `_short`, `_fill`, `_match`, `_order`
- `init_db.py`: Automatická konverze category kódů na ID v extra_data

### ⬆️ Upgrade z v0.0.1
- Kompletní přepis – nekompatibilní databáze
- Smazat starý kontejner: `docker rm -f career-quiz`
- Build: `docker build --network=host -t career-quiz:0.1.0 .`
- Run: `docker run -d --name career-quiz -p 8080:5000 career-quiz:0.1.0`

---

## v0.0.1 – Initial Release (2025-02-12)
- 150 otázek, 11 kategoriíonly single choice
- Flask + SQLite + Docker
- Admin rozhraní (CRUD)
