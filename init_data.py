"""
135 kariérních otázek různých typů pro 11 kategorií.

Typy: single_choice, multiple_choice, true_false, likert,
      short_answer, matching, ordering

Kategorie (zkratky):
  ZEM - Zemědělství a lesnictví
  STA - Stavebnictví a architektura
  STR - Strojírenství a elektrotechnika
  DOP - Doprava a logistika
  IT  - Informační technologie
  ZDR - Zdravotnictví a medicína
  OBC - Obchod a služby
  SKO - Školství a vzdělávání
  PRA - Právo a veřejná správa
  MAN - Management a podnikání
  UME - Umění a kultura
"""


def get_categories():
    return [
        {'code': 'ZEM', 'name': 'Zemědělství a lesnictví',
         'description': 'Agronom, lesník, zahradník, veterinář, ekolog, vinař, zemědělský technik',
         'icon': '🌾', 'color': '#27ae60'},
        {'code': 'STA', 'name': 'Stavebnictví a architektura',
         'description': 'Architekt, stavbyvedoucí, projektant, geodet, urbanista, interiérový designér',
         'icon': '🏗️', 'color': '#e67e22'},
        {'code': 'STR', 'name': 'Strojírenství a elektrotechnika',
         'description': 'Strojní inženýr, elektrotechnik, mechatronik, svářeč, konstruktér, automatizační technik',
         'icon': '⚙️', 'color': '#7f8c8d'},
        {'code': 'DOP', 'name': 'Doprava a logistika',
         'description': 'Pilot, řidič, dispečer, logistik, námořník, strojvedoucí, celník',
         'icon': '🚗', 'color': '#2980b9'},
        {'code': 'IT', 'name': 'Informační technologie',
         'description': 'Programátor, správce sítě, analytik, UX designér, datový inženýr, kybernetik',
         'icon': '💻', 'color': '#8e44ad'},
        {'code': 'ZDR', 'name': 'Zdravotnictví a medicína',
         'description': 'Lékař, zdravotní sestra, farmaceut, fyzioterapeut, záchranář, zubař',
         'icon': '🏥', 'color': '#e74c3c'},
        {'code': 'OBC', 'name': 'Obchod a služby',
         'description': 'Obchodní zástupce, marketingový specialista, barista, kuchař, průvodce, recepční',
         'icon': '🛒', 'color': '#f39c12'},
        {'code': 'SKO', 'name': 'Školství a vzdělávání',
         'description': 'Učitel, profesor, lektor, vychovatel, speciální pedagog, metodik',
         'icon': '📚', 'color': '#3498db'},
        {'code': 'PRA', 'name': 'Právo a veřejná správa',
         'description': 'Advokát, soudce, notář, úředník, diplomat, policista, hasič',
         'icon': '⚖️', 'color': '#34495e'},
        {'code': 'MAN', 'name': 'Management a podnikání',
         'description': 'Manažer, podnikatel, finanční analytik, účetní, ekonom, HR specialista',
         'icon': '📊', 'color': '#1abc9c'},
        {'code': 'UME', 'name': 'Umění a kultura',
         'description': 'Malíř, herec, hudebník, grafik, fotograf, spisovatel, režisér',
         'icon': '🎨', 'color': '#e91e63'},
    ]


# ═══════════════════════ HELPER FUNKCE ═══════════════════════

def _sc(text, answers):
    """Single choice otázka."""
    return {'text': text, 'type': 'single_choice', 'answers': answers}


def _mc(text, answers):
    """Multiple choice otázka."""
    return {'text': text, 'type': 'multiple_choice', 'answers': answers}


def _tf(text, true_scores, false_scores):
    """True/False otázka."""
    return {
        'text': text, 'type': 'true_false',
        'answers': [
            {'text': 'Ano, souhlasím', 'scores': true_scores},
            {'text': 'Ne, nesouhlasím', 'scores': false_scores},
        ]
    }


def _likert(text, main, sec=None):
    """Likert škála 1-5 s hlavní a volitelnou vedlejší kategorií."""
    labels = ['Vůbec ne', 'Spíše ne', 'Neutrálně', 'Spíše ano', 'Rozhodně ano']
    answers = []
    for i, label in enumerate(labels):
        sc = {main: i}
        if sec and i >= 3:
            sc[sec] = i - 2
        answers.append({'text': label, 'scores': sc})
    return {
        'text': text, 'type': 'likert',
        'answers': answers,
        'extra_data': {'labels': labels}
    }


def _short(text, keyword_groups, default_scores=None):
    """Short answer s keyword mapováním."""
    return {
        'text': text, 'type': 'short_answer',
        'extra_data': {
            'keyword_groups': keyword_groups,
            'default_scores': default_scores or {}
        }
    }


def _match(text, pairs):
    """Matching otázka."""
    return {
        'text': text, 'type': 'matching',
        'extra_data': {'pairs': pairs}
    }


def _order(text, items, correct_order, scores):
    """Ordering otázka."""
    return {
        'text': text, 'type': 'ordering',
        'extra_data': {
            'items': items,
            'correct_order': correct_order,
            'scores': scores
        }
    }


# ════════════════════════ 150 OTÁZEK ════════════════════════

def get_questions():
    return [

        # ══════════════ SINGLE CHOICE (1–30) ══════════════

        # 1
        _sc('Jaká činnost vás láká nejvíce?', [
            {'text': 'Pěstování plodin a péče o přírodu', 'scores': {'ZEM': 4}},
            {'text': 'Navrhování a stavba budov', 'scores': {'STA': 4}},
            {'text': 'Opravování a konstruování strojů', 'scores': {'STR': 4}},
            {'text': 'Programování a vývoj aplikací', 'scores': {'IT': 4}},
        ]),
        # 2
        _sc('Jak byste nejraději trávili pracovní den?', [
            {'text': 'Venku v přírodě, fyzická práce', 'scores': {'ZEM': 3, 'STA': 1}},
            {'text': 'V kanceláři u počítače', 'scores': {'IT': 3, 'MAN': 1}},
            {'text': 'V nemocnici či ordinaci s pacienty', 'scores': {'ZDR': 4}},
            {'text': 'Ve třídě se studenty', 'scores': {'SKO': 4}},
        ]),
        # 3
        _sc('Co je pro vás v práci nejdůležitější?', [
            {'text': 'Pomáhat ostatním lidem', 'scores': {'ZDR': 2, 'SKO': 2}},
            {'text': 'Tvořit nové originální věci', 'scores': {'UME': 3, 'IT': 1}},
            {'text': 'Organizovat a řídit tým', 'scores': {'MAN': 4}},
            {'text': 'Dodržovat pravidla a zákon', 'scores': {'PRA': 3, 'DOP': 1}},
        ]),
        # 4
        _sc('Jaký typ problémů řešíte nejraději?', [
            {'text': 'Technické a mechanické', 'scores': {'STR': 3, 'DOP': 1}},
            {'text': 'Logické a analytické', 'scores': {'IT': 3, 'MAN': 1}},
            {'text': 'Mezilidské a komunikační', 'scores': {'SKO': 2, 'OBC': 2}},
            {'text': 'Kreativní a designové', 'scores': {'UME': 3, 'STA': 1}},
        ]),
        # 5
        _sc('S jakými materiály byste chtěli pracovat?', [
            {'text': 'Dřevo, kov, beton', 'scores': {'STA': 3, 'STR': 2}},
            {'text': 'Potraviny a přírodní produkty', 'scores': {'ZEM': 3, 'OBC': 1}},
            {'text': 'Data, čísla a informace', 'scores': {'IT': 2, 'MAN': 2}},
            {'text': 'Barvy, textil, design', 'scores': {'UME': 4}},
        ]),
        # 6
        _sc('Které prostředí vám vyhovuje nejvíce?', [
            {'text': 'Pole, les, farma', 'scores': {'ZEM': 4}},
            {'text': 'Stavba, dílna, továrna', 'scores': {'STA': 2, 'STR': 2}},
            {'text': 'Soud, úřad, kancelář', 'scores': {'PRA': 3, 'MAN': 1}},
            {'text': 'Ateliér, jeviště, studio', 'scores': {'UME': 4}},
        ]),
        # 7
        _sc('Jakou roli v týmu preferujete?', [
            {'text': 'Vůdce – rozhoduji a deleguju', 'scores': {'MAN': 4}},
            {'text': 'Expert – řeším odborné problémy', 'scores': {'IT': 2, 'STR': 2}},
            {'text': 'Komunikátor – jednám s lidmi', 'scores': {'OBC': 3, 'SKO': 1}},
            {'text': 'Tvůrce – vytvářím nové nápady', 'scores': {'UME': 3, 'STA': 1}},
        ]),
        # 8
        _sc('Co byste si vybrali jako koníček?', [
            {'text': 'Zahrádkaření a chov zvířat', 'scores': {'ZEM': 4}},
            {'text': 'Modelářství a kutilství', 'scores': {'STR': 3, 'STA': 1}},
            {'text': 'Malování, hudba nebo divadlo', 'scores': {'UME': 4}},
            {'text': 'Cestování a poznávání nových míst', 'scores': {'DOP': 3, 'OBC': 1}},
        ]),
        # 9
        _sc('Jaký předmět ve škole vás baví/bavil nejvíce?', [
            {'text': 'Matematika a fyzika', 'scores': {'STR': 2, 'IT': 2}},
            {'text': 'Biologie a chemie', 'scores': {'ZDR': 3, 'ZEM': 1}},
            {'text': 'Dějepis a občanská nauka', 'scores': {'PRA': 2, 'SKO': 2}},
            {'text': 'Výtvarná a hudební výchova', 'scores': {'UME': 4}},
        ]),
        # 10
        _sc('Kde se vidíte za 10 let?', [
            {'text': 'Vedu vlastní firmu', 'scores': {'MAN': 4}},
            {'text': 'Jsem uznávaný odborník ve svém oboru', 'scores': {'IT': 2, 'ZDR': 2}},
            {'text': 'Pomáhám komunitě a společnosti', 'scores': {'SKO': 2, 'PRA': 2}},
            {'text': 'Tvořím umělecká díla', 'scores': {'UME': 4}},
        ]),
        # 11
        _sc('Jaký typ cestování preferujete?', [
            {'text': 'Na nákladním autě – dlouhé trasy', 'scores': {'DOP': 4}},
            {'text': 'Na konference a obchodní jednání', 'scores': {'MAN': 3, 'OBC': 1}},
            {'text': 'Do nemocnic a zdravotnických zařízení', 'scores': {'ZDR': 4}},
            {'text': 'Na stavby a terénní průzkumy', 'scores': {'STA': 3, 'ZEM': 1}},
        ]),
        # 12
        _sc('Jak reagujete na stres?', [
            {'text': 'Analyzuji problém a hledám systematické řešení', 'scores': {'IT': 3, 'STR': 1}},
            {'text': 'Komunikuji s kolegy a hledáme řešení společně', 'scores': {'MAN': 2, 'SKO': 2}},
            {'text': 'Zachovám klid – jsem zvyklý/á na tlak', 'scores': {'ZDR': 3, 'PRA': 1}},
            {'text': 'Ventiluji kreativně – sportem či uměním', 'scores': {'UME': 3, 'ZEM': 1}},
        ]),
        # 13
        _sc('Který z těchto nástrojů vás přitahuje?', [
            {'text': 'Stetoskop', 'scores': {'ZDR': 4}},
            {'text': 'Soustruh', 'scores': {'STR': 4}},
            {'text': 'Notebook s IDE', 'scores': {'IT': 4}},
            {'text': 'Fotoaparát', 'scores': {'UME': 4}},
        ]),
        # 14
        _sc('Jaký typ knih/článků čtete nejraději?', [
            {'text': 'Naučné o technologiích', 'scores': {'IT': 3, 'STR': 1}},
            {'text': 'Romány a prózu', 'scores': {'UME': 3, 'SKO': 1}},
            {'text': 'Ekonomické a podnikatelské', 'scores': {'MAN': 3, 'OBC': 1}},
            {'text': 'Přírodovědné a ekologické', 'scores': {'ZEM': 3, 'ZDR': 1}},
        ]),
        # 15
        _sc('Co vás na dovolené baví nejvíce?', [
            {'text': 'Návštěva museí a galerií', 'scores': {'UME': 3, 'SKO': 1}},
            {'text': 'Poznávání místní kuchyně a obchodů', 'scores': {'OBC': 4}},
            {'text': 'Turistika v přírodě', 'scores': {'ZEM': 3, 'DOP': 1}},
            {'text': 'Plánování tras a logistiky výletu', 'scores': {'DOP': 3, 'MAN': 1}},
        ]),
        # 16
        _sc('Jakou dovednost byste se chtěli naučit?', [
            {'text': 'První pomoc a ošetřování', 'scores': {'ZDR': 4}},
            {'text': 'Řízení projektů', 'scores': {'MAN': 4}},
            {'text': 'Svařování a obrábění', 'scores': {'STR': 4}},
            {'text': 'Rétorika a právní minimum', 'scores': {'PRA': 3, 'SKO': 1}},
        ]),
        # 17
        _sc('Jaký typ filmu/seriálu preferujete?', [
            {'text': 'Sci-fi o technologiích budoucnosti', 'scores': {'IT': 3, 'STR': 1}},
            {'text': 'Soudní drama a kriminálky', 'scores': {'PRA': 4}},
            {'text': 'Dokumenty o přírodě', 'scores': {'ZEM': 3, 'ZDR': 1}},
            {'text': 'Životopisné filmy o umělcích', 'scores': {'UME': 4}},
        ]),
        # 18
        _sc('Při skupinovém projektu preferujete:', [
            {'text': 'Výzkum a sběr dat', 'scores': {'IT': 2, 'ZDR': 2}},
            {'text': 'Prezentaci výsledků', 'scores': {'OBC': 2, 'SKO': 2}},
            {'text': 'Plánování a koordinaci', 'scores': {'MAN': 3, 'DOP': 1}},
            {'text': 'Grafické zpracování a design', 'scores': {'UME': 3, 'STA': 1}},
        ]),
        # 19
        _sc('Jakou aplikaci používáte na telefonu nejčastěji?', [
            {'text': 'Mapy a navigaci', 'scores': {'DOP': 4}},
            {'text': 'Sociální sítě a komunikaci', 'scores': {'OBC': 2, 'UME': 2}},
            {'text': 'Kalkulačku a tabulky', 'scores': {'MAN': 3, 'STR': 1}},
            {'text': 'Naučné a vzdělávací aplikace', 'scores': {'SKO': 3, 'IT': 1}},
        ]),
        # 20
        _sc('Co byste udělali s prázdným pozemkem?', [
            {'text': 'Založil/a bych zahradu nebo sad', 'scores': {'ZEM': 4}},
            {'text': 'Navrhl/a bych a postavil/a dům', 'scores': {'STA': 4}},
            {'text': 'Otevřel/a bych obchod nebo kavárnu', 'scores': {'OBC': 3, 'MAN': 1}},
            {'text': 'Vytvořil/a bych veřejný park s uměním', 'scores': {'UME': 3, 'PRA': 1}},
        ]),
        # 21
        _sc('Jak nejraději komunikujete?', [
            {'text': 'Písemně – e-maily, reporty', 'scores': {'PRA': 2, 'IT': 2}},
            {'text': 'Osobně – tváří v tvář', 'scores': {'ZDR': 2, 'SKO': 2}},
            {'text': 'Přes prezentace a schůzky', 'scores': {'MAN': 3, 'OBC': 1}},
            {'text': 'Vizuálně – nákresy, schémata', 'scores': {'STA': 2, 'UME': 2}},
        ]),
        # 22
        _sc('Jaký typ práce vás uspokojuje nejvíce?', [
            {'text': 'Fyzická práce s viditelnými výsledky', 'scores': {'STA': 2, 'ZEM': 2}},
            {'text': 'Analytická práce s daty', 'scores': {'IT': 3, 'MAN': 1}},
            {'text': 'Péče o druhé a poradenství', 'scores': {'ZDR': 2, 'SKO': 2}},
            {'text': 'Přeprava a logistika', 'scores': {'DOP': 4}},
        ]),
        # 23
        _sc('Kdybyste mohli vynalézat, co by to bylo?', [
            {'text': 'Nový lék nebo vakcínu', 'scores': {'ZDR': 4}},
            {'text': 'Ekologický motor', 'scores': {'STR': 3, 'DOP': 1}},
            {'text': 'Revoluční aplikaci', 'scores': {'IT': 4}},
            {'text': 'Nový hudební nástroj', 'scores': {'UME': 4}},
        ]),
        # 24
        _sc('Která osobnost vás inspiruje nejvíce?', [
            {'text': 'Elon Musk – podnikatel a vizionář', 'scores': {'MAN': 3, 'IT': 1}},
            {'text': 'Marie Curie – vědkyně', 'scores': {'ZDR': 2, 'STR': 2}},
            {'text': 'Leonardo da Vinci – umělec a vynálezce', 'scores': {'UME': 3, 'STA': 1}},
            {'text': 'Jan Amos Komenský – pedagog', 'scores': {'SKO': 4}},
        ]),
        # 25
        _sc('Co děláte, když máte volný víkend?', [
            {'text': 'Pracuji na zahradě nebo farmě', 'scores': {'ZEM': 4}},
            {'text': 'Opravuji věci doma', 'scores': {'STR': 3, 'STA': 1}},
            {'text': 'Učím se nový programovací jazyk', 'scores': {'IT': 4}},
            {'text': 'Navštěvuji výstavu nebo koncert', 'scores': {'UME': 4}},
        ]),
        # 26
        _sc('Jak byste nejraději pomohli komunitě?', [
            {'text': 'Dobrovolnictví v nemocnici', 'scores': {'ZDR': 4}},
            {'text': 'Doučování dětí', 'scores': {'SKO': 4}},
            {'text': 'Právní poradna pro potřebné', 'scores': {'PRA': 4}},
            {'text': 'Organizace charitativního bazaru', 'scores': {'OBC': 3, 'MAN': 1}},
        ]),
        # 27
        _sc('Jaký předmět byste učili, kdybyste byli učitel/ka?', [
            {'text': 'Informatiku', 'scores': {'IT': 3, 'SKO': 1}},
            {'text': 'Biologii', 'scores': {'ZDR': 2, 'ZEM': 1, 'SKO': 1}},
            {'text': 'Dějepis nebo zeměpis', 'scores': {'SKO': 2, 'PRA': 2}},
            {'text': 'Výtvarnou výchovu', 'scores': {'UME': 3, 'SKO': 1}},
        ]),
        # 28
        _sc('Jaký pracovní benefit oceníte nejvíce?', [
            {'text': 'Služební auto', 'scores': {'DOP': 3, 'OBC': 1}},
            {'text': 'Vzdělávací kurzy a certifikace', 'scores': {'SKO': 2, 'IT': 2}},
            {'text': 'Flexibilní pracovní dobu', 'scores': {'UME': 2, 'MAN': 2}},
            {'text': 'Zdravotní pojištění navíc', 'scores': {'ZDR': 3, 'PRA': 1}},
        ]),
        # 29
        _sc('Co vás motivuje k práci?', [
            {'text': 'Finanční odměna a podnikatelský úspěch', 'scores': {'MAN': 3, 'OBC': 1}},
            {'text': 'Vědomí, že pomáhám lidem', 'scores': {'ZDR': 2, 'SKO': 2}},
            {'text': 'Intelektuální výzvy', 'scores': {'IT': 2, 'PRA': 2}},
            {'text': 'Tvůrčí svoboda a sebevyjádření', 'scores': {'UME': 4}},
        ]),
        # 30
        _sc('Jaký typ dovedností považujete za svou silnou stránku?', [
            {'text': 'Technické a manuální', 'scores': {'STR': 2, 'STA': 2}},
            {'text': 'Komunikační a sociální', 'scores': {'OBC': 2, 'SKO': 2}},
            {'text': 'Analytické a logické', 'scores': {'IT': 2, 'MAN': 2}},
            {'text': 'Logistické a organizační', 'scores': {'DOP': 2, 'MAN': 2}},
        ]),

        # ══════════════ MULTIPLE CHOICE (31–48) ══════════════

        # 31
        _mc('Které z těchto činností vás zajímají? (vyberte všechny)', [
            {'text': 'Práce s laboratorními přístroji', 'scores': {'ZDR': 2, 'STR': 1}},
            {'text': 'Psaní kódu a skriptů', 'scores': {'IT': 3}},
            {'text': 'Vedení obchodních jednání', 'scores': {'OBC': 2, 'MAN': 1}},
            {'text': 'Malování a kreslení', 'scores': {'UME': 3}},
            {'text': 'Řízení vozidel a strojů', 'scores': {'DOP': 2, 'STR': 1}},
        ]),
        # 32
        _mc('Které předměty vás ve škole bavily? (vyberte všechny)', [
            {'text': 'Matematika', 'scores': {'IT': 1, 'STR': 1, 'MAN': 1}},
            {'text': 'Český jazyk a literatura', 'scores': {'SKO': 2, 'UME': 1}},
            {'text': 'Přírodopis/Biologie', 'scores': {'ZDR': 2, 'ZEM': 1}},
            {'text': 'Zeměpis', 'scores': {'DOP': 2, 'ZEM': 1}},
            {'text': 'Občanská výchova', 'scores': {'PRA': 2, 'SKO': 1}},
        ]),
        # 33
        _mc('Které vlastnosti vás nejlépe vystihují? (vyberte všechny)', [
            {'text': 'Trpělivost a empatie', 'scores': {'ZDR': 2, 'SKO': 2}},
            {'text': 'Přesnost a pečlivost', 'scores': {'STR': 2, 'PRA': 1}},
            {'text': 'Kreativita a originalita', 'scores': {'UME': 3}},
            {'text': 'Podnikavost a odvaha', 'scores': {'MAN': 3}},
            {'text': 'Fyzická zdatnost', 'scores': {'ZEM': 2, 'STA': 1, 'DOP': 1}},
        ]),
        # 34
        _mc('Které technologie vás fascinují? (vyberte všechny)', [
            {'text': 'Umělá inteligence a strojové učení', 'scores': {'IT': 3}},
            {'text': '3D tisk a CNC stroje', 'scores': {'STR': 3}},
            {'text': 'Elektromobily a autonomní řízení', 'scores': {'DOP': 2, 'STR': 1}},
            {'text': 'Lékařské zobrazovací systémy (CT, MRI)', 'scores': {'ZDR': 3}},
            {'text': 'Drony a satelitní technologie', 'scores': {'ZEM': 1, 'DOP': 1, 'IT': 1}},
        ]),
        # 35
        _mc('Které aktivity by vás bavily na brigádě? (vyberte všechny)', [
            {'text': 'Sběr ovoce a práce na farmě', 'scores': {'ZEM': 3}},
            {'text': 'Prodej v obchodě', 'scores': {'OBC': 3}},
            {'text': 'Pomoc na stavbě', 'scores': {'STA': 3}},
            {'text': 'Kancelářská administrativa', 'scores': {'MAN': 1, 'PRA': 2}},
            {'text': 'Práce v kuchyni restaurace', 'scores': {'OBC': 2, 'UME': 1}},
        ]),
        # 36
        _mc('Které z těchto hodnot jsou pro vás klíčové? (vyberte všechny)', [
            {'text': 'Spravedlnost a dodržování zákonů', 'scores': {'PRA': 3}},
            {'text': 'Inovace a pokrok', 'scores': {'IT': 2, 'STR': 1}},
            {'text': 'Ochrana přírody a udržitelnost', 'scores': {'ZEM': 3}},
            {'text': 'Vzdělání a předávání znalostí', 'scores': {'SKO': 3}},
        ]),
        # 37
        _mc('Ve kterých situacích se cítíte nejlépe? (vyberte všechny)', [
            {'text': 'Při jednání s klienty', 'scores': {'OBC': 2, 'MAN': 1}},
            {'text': 'Při sestavování rozpočtu', 'scores': {'MAN': 3}},
            {'text': 'Při práci rukama (řezání, montáž)', 'scores': {'STA': 2, 'STR': 2}},
            {'text': 'Při péči o nemocné', 'scores': {'ZDR': 3}},
        ]),
        # 38
        _mc('Jaké typy problémů vás přitahují? (vyberte všechny)', [
            {'text': 'Jak optimalizovat dopravu ve městě', 'scores': {'DOP': 3}},
            {'text': 'Jak navrhnout energetikou úsporný dům', 'scores': {'STA': 2, 'STR': 1}},
            {'text': 'Jak zvýšit úrodu bez chemie', 'scores': {'ZEM': 3}},
            {'text': 'Jak naučit žáky kriticky myslet', 'scores': {'SKO': 3}},
        ]),
        # 39
        _mc('Které z těchto kroužků/aktivit by vás bavily? (vyberte všechny)', [
            {'text': 'Programátorský kroužek', 'scores': {'IT': 3}},
            {'text': 'Dramatický kroužek', 'scores': {'UME': 3}},
            {'text': 'Zdravotnický kroužek', 'scores': {'ZDR': 3}},
            {'text': 'Modelářský kroužek', 'scores': {'STR': 3}},
            {'text': 'Debatní klub', 'scores': {'PRA': 2, 'SKO': 1}},
        ]),
        # 40
        _mc('Které pracovní podmínky preferujete? (vyberte všechny)', [
            {'text': 'Práce na směny', 'scores': {'ZDR': 1, 'DOP': 2}},
            {'text': 'Remote / práce z domova', 'scores': {'IT': 3}},
            {'text': 'Cestování za prací', 'scores': {'OBC': 2, 'DOP': 1}},
            {'text': 'Práce venku za každého počasí', 'scores': {'ZEM': 2, 'STA': 2}},
        ]),
        # 41
        _mc('Co byste rádi zlepšili ve společnosti? (vyberte všechny)', [
            {'text': 'Kvalitu zdravotní péče', 'scores': {'ZDR': 3}},
            {'text': 'Dopravní infrastrukturu', 'scores': {'DOP': 2, 'STA': 1}},
            {'text': 'Vzdělávací systém', 'scores': {'SKO': 3}},
            {'text': 'Přístup k umění a kultuře', 'scores': {'UME': 3}},
        ]),
        # 42
        _mc('Jaké informační zdroje sledujete? (vyberte všechny)', [
            {'text': 'Technologické blogy a novinky', 'scores': {'IT': 3}},
            {'text': 'Právní a legislativní změny', 'scores': {'PRA': 3}},
            {'text': 'Ekonomické zprávy', 'scores': {'MAN': 2, 'OBC': 1}},
            {'text': 'Články o zemědělství a ekologii', 'scores': {'ZEM': 3}},
        ]),
        # 43
        _mc('Kde byste chtěli pracovat v zahraničí? (vyberte všechny)', [
            {'text': 'Silicon Valley – technologické firmy', 'scores': {'IT': 3}},
            {'text': 'Švýcarsko – farmaceutický průmysl', 'scores': {'ZDR': 2, 'STR': 1}},
            {'text': 'Dubaj – stavebnictví a architektura', 'scores': {'STA': 3}},
            {'text': 'Paříž – módní průmysl a umění', 'scores': {'UME': 3}},
        ]),
        # 44
        _mc('Které dovednosti byste se chtěli naučit? (vyberte všechny)', [
            {'text': 'Programování v Pythonu', 'scores': {'IT': 3}},
            {'text': 'Účetnictví a finance', 'scores': {'MAN': 3}},
            {'text': 'Ošetřovatelství a první pomoc', 'scores': {'ZDR': 3}},
            {'text': 'Řízení kamionů nebo autobusů', 'scores': {'DOP': 3}},
            {'text': 'Fotografování a střih videa', 'scores': {'UME': 3}},
        ]),
        # 45
        _mc('Které nástroje byste rádi ovládali? (vyberte všechny)', [
            {'text': 'Tabulkový procesor a databáze', 'scores': {'MAN': 2, 'IT': 1}},
            {'text': 'Grafické programy (Photoshop, Figma)', 'scores': {'UME': 2, 'IT': 1}},
            {'text': 'Tesařské a zednické nářadí', 'scores': {'STA': 3}},
            {'text': 'Mikroskop a pipety', 'scores': {'ZDR': 2, 'ZEM': 1}},
        ]),
        # 46
        _mc('Jaké televizní pořady/kanály sledujete? (vyberte všechny)', [
            {'text': 'National Geographic / příroda', 'scores': {'ZEM': 2, 'ZDR': 1}},
            {'text': 'Discovery / technika a stavby', 'scores': {'STR': 2, 'STA': 1}},
            {'text': 'Zpravodajství a politika', 'scores': {'PRA': 2, 'MAN': 1}},
            {'text': 'Kulturní magazíny a umělecké pořady', 'scores': {'UME': 3}},
        ]),
        # 47
        _mc('Které z těchto certifikátů/zkoušek by vás zajímaly? (vyberte všechny)', [
            {'text': 'Řidičský průkaz skupiny C / D', 'scores': {'DOP': 3}},
            {'text': 'Svářečský certifikát', 'scores': {'STR': 3}},
            {'text': 'PRINCE2 / PMP (projektové řízení)', 'scores': {'MAN': 3}},
            {'text': 'Jazykové certifikáty (FCE, DELF)', 'scores': {'SKO': 2, 'OBC': 1}},
        ]),
        # 48
        _mc('Jaké webové stránky navštěvujete nejčastěji? (vyberte všechny)', [
            {'text': 'Stack Overflow, GitHub', 'scores': {'IT': 3}},
            {'text': 'LinkedIn, Business Insider', 'scores': {'MAN': 2, 'OBC': 1}},
            {'text': 'PubMed, medicínské portály', 'scores': {'ZDR': 3}},
            {'text': 'Behance, DeviantArt', 'scores': {'UME': 3}},
        ]),

        # ══════════════ TRUE/FALSE (49–68) ══════════════

        # 49
        _tf('Rád/a pracuji venku za každého počasí.',
            {'ZEM': 3, 'STA': 2}, {'IT': 2, 'MAN': 1}),
        # 50
        _tf('Baví mě vysvětlovat složité věci jednoduchým způsobem.',
            {'SKO': 3, 'OBC': 1}, {'STR': 1, 'IT': 1}),
        # 51
        _tf('Jsem přesný/á a dodržuji termíny za každou cenu.',
            {'PRA': 2, 'MAN': 2}, {'UME': 2, 'ZEM': 1}),
        # 52
        _tf('Krev a zranění mi nedělají problém.',
            {'ZDR': 4}, {'UME': 1, 'IT': 1}),
        # 53
        _tf('Rád/a řídím auto nebo jiné dopravní prostředky.',
            {'DOP': 4}, {'IT': 1, 'UME': 1}),
        # 54
        _tf('Zajímá mě, jak fungují zákony a právní systém.',
            {'PRA': 4}, {'STR': 1, 'ZEM': 1}),
        # 55
        _tf('Dokážu pracovat dlouho v soustředění na jednu věc.',
            {'IT': 2, 'STR': 2}, {'OBC': 2, 'DOP': 1}),
        # 56
        _tf('Baví mě obchodovat a přesvědčovat lidi.',
            {'OBC': 3, 'MAN': 1}, {'IT': 1, 'ZEM': 1}),
        # 57
        _tf('Mám rád/a zvířata a přírodu více než městský ruch.',
            {'ZEM': 4}, {'IT': 1, 'MAN': 1}),
        # 58
        _tf('Umím dobře kreslit, malovat nebo navrhovat.',
            {'UME': 3, 'STA': 1}, {'STR': 1, 'DOP': 1}),
        # 59
        _tf('Rád/a řeším matematické úlohy a hádanky.',
            {'IT': 2, 'STR': 2}, {'UME': 1, 'OBC': 1}),
        # 60
        _tf('Chtěl/a bych pracovat v nemocnici.',
            {'ZDR': 4}, {'ZEM': 1, 'STA': 1}),
        # 61
        _tf('Organizování akcí a událostí mě naplňuje.',
            {'MAN': 3, 'OBC': 1}, {'STR': 1, 'ZEM': 1}),
        # 62
        _tf('Baví mě stavět věci – i ze stavebnice LEGO.',
            {'STA': 3, 'STR': 1}, {'PRA': 1, 'SKO': 1}),
        # 63
        _tf('Rád/a čtu odbornou literaturu a studuji nové poznatky.',
            {'SKO': 3, 'ZDR': 1}, {'DOP': 1, 'OBC': 1}),
        # 64
        _tf('Chtěl/a bych mít vlastní podnik.',
            {'MAN': 4}, {'PRA': 1, 'SKO': 1}),
        # 65
        _tf('Práce se stroji a elektronikou mě přitahuje.',
            {'STR': 3, 'DOP': 1}, {'UME': 1, 'SKO': 1}),
        # 66
        _tf('Rád/a pomáhám spolužákům s učením.',
            {'SKO': 4}, {'STR': 1, 'DOP': 1}),
        # 67
        _tf('Zajímají mě mapy, trasy a navigace.',
            {'DOP': 3, 'ZEM': 1}, {'UME': 1, 'ZDR': 1}),
        # 68
        _tf('Chtěl/a bych pracovat v oblasti, kde se nosí uniforma.',
            {'PRA': 2, 'ZDR': 1, 'DOP': 1}, {'UME': 2, 'IT': 1}),

        # ══════════════ LIKERT 1–5 (69–98) ══════════════

        # 69
        _likert('Baví mě programování a práce s počítačem.', 'IT', 'STR'),
        # 70
        _likert('Rád/a pracuji s půdou, rostlinami a přírodou.', 'ZEM'),
        # 71
        _likert('Zajímám se o zdraví lidí a medicínu.', 'ZDR', 'SKO'),
        # 72
        _likert('Rád/a navrhuju a kreslím plány budov.', 'STA', 'UME'),
        # 73
        _likert('Baví mě opravovat a udržovat stroje.', 'STR', 'DOP'),
        # 74
        _likert('Rád/a řídím tým a rozhoduji.', 'MAN', 'OBC'),
        # 75
        _likert('Zajímám se o hudbu, divadlo nebo výtvarné umění.', 'UME'),
        # 76
        _likert('Rád/a vysvětluji a učím ostatní.', 'SKO', 'ZDR'),
        # 77
        _likert('Baví mě prodávat a jednat s klienty.', 'OBC', 'MAN'),
        # 78
        _likert('Zajímám se o dopravní prostředky a logistiku.', 'DOP', 'STR'),
        # 79
        _likert('Zákony a právo mě fascinují.', 'PRA'),
        # 80
        _likert('Rád/a analyzuji data a hledám vzorce.', 'IT', 'MAN'),
        # 81
        _likert('Představa práce na stavbě mě přitahuje.', 'STA', 'STR'),
        # 82
        _likert('Rád/a bych zachránil/a lidský život.', 'ZDR', 'PRA'),
        # 83
        _likert('Chtěl/a bych vést vlastní firmu.', 'MAN', 'OBC'),
        # 84
        _likert('Baví mě fotografie a grafický design.', 'UME', 'IT'),
        # 85
        _likert('Rád/a organizuji a plánuji cesty.', 'DOP', 'MAN'),
        # 86
        _likert('Zajímají mě chemické a biologické procesy.', 'ZDR', 'ZEM'),
        # 87
        _likert('Rád/a bych pracoval/a s dětmi nebo mladými lidmi.', 'SKO'),
        # 88
        _likert('Přitahuje mě práce s elektřinou a elektronikou.', 'STR', 'IT'),
        # 89
        _likert('Zajímám se o ochranu životního prostředí.', 'ZEM', 'PRA'),
        # 90
        _likert('Rád/a píšu příběhy, básně nebo scénáře.', 'UME', 'SKO'),
        # 91
        _likert('Baví mě jednat s úřady a řešit administrativu.', 'PRA', 'MAN'),
        # 92
        _likert('Představa práce v kuchyni restaurace mě láká.', 'OBC', 'UME'),
        # 93
        _likert('Rád/a bych navrhoval/a interiéry a prostory.', 'STA', 'UME'),
        # 94
        _likert('Fascinuje mě robotika a automatizace.', 'STR', 'IT'),
        # 95
        _likert('Chtěl/a bych pracovat v mezinárodním prostředí.', 'OBC', 'MAN'),
        # 96
        _likert('Zajímám se o výživu a zdravý životní styl.', 'ZDR', 'ZEM'),
        # 97
        _likert('Rád/a se učím cizí jazyky.', 'SKO', 'OBC'),
        # 98
        _likert('Představa, že budu řídit vlak nebo letadlo, mě nadchne.', 'DOP'),

        # ══════════════ SHORT ANSWER (99–113) ══════════════

        # 99
        _short('Napište jedno povolání, které vás nejvíce láká:', [
            {'keywords': ['programátor', 'developer', 'vývojář', 'informatik', 'koder'], 'scores': {'IT': 4}},
            {'keywords': ['lékař', 'doktor', 'chirurg', 'zdravotní'], 'scores': {'ZDR': 4}},
            {'keywords': ['učitel', 'pedagog', 'lektor', 'profesor'], 'scores': {'SKO': 4}},
            {'keywords': ['architekt', 'stavbyvedoucí', 'projektant'], 'scores': {'STA': 4}},
            {'keywords': ['policista', 'hasič', 'soudce', 'advokát', 'právník'], 'scores': {'PRA': 4}},
            {'keywords': ['manažer', 'podnikatel', 'ředitel', 'ekonom'], 'scores': {'MAN': 4}},
            {'keywords': ['malíř', 'herec', 'hudebník', 'fotograf', 'grafik', 'umělec'], 'scores': {'UME': 4}},
            {'keywords': ['řidič', 'pilot', 'strojvedoucí', 'dispečer', 'logistik'], 'scores': {'DOP': 4}},
            {'keywords': ['inženýr', 'mechanik', 'technik', 'konstruktér', 'svářeč'], 'scores': {'STR': 4}},
            {'keywords': ['farmář', 'zemědělec', 'lesník', 'zahradník', 'veterinář'], 'scores': {'ZEM': 4}},
            {'keywords': ['obchodník', 'prodavač', 'kuchař', 'barista', 'číšník'], 'scores': {'OBC': 4}},
        ]),
        # 100
        _short('Jakou činnost děláte nejraději? (jedno slovo nebo fráze)', [
            {'keywords': ['programování', 'kódování', 'vývoj'], 'scores': {'IT': 3}},
            {'keywords': ['vaření', 'pečení', 'gastronomie'], 'scores': {'OBC': 3}},
            {'keywords': ['kreslení', 'malování', 'focení', 'fotografování'], 'scores': {'UME': 3}},
            {'keywords': ['stavění', 'budování', 'montáž'], 'scores': {'STA': 3}},
            {'keywords': ['řízení', 'jízda', 'létání'], 'scores': {'DOP': 3}},
            {'keywords': ['učení', 'vyučování', 'vzdělávání'], 'scores': {'SKO': 3}},
            {'keywords': ['léčení', 'ošetřování', 'péče'], 'scores': {'ZDR': 3}},
            {'keywords': ['zahradničení', 'pěstování', 'chov'], 'scores': {'ZEM': 3}},
            {'keywords': ['organizování', 'plánování', 'vedení'], 'scores': {'MAN': 3}},
            {'keywords': ['prodej', 'obchod', 'marketing'], 'scores': {'OBC': 3}},
        ]),
        # 101
        _short('Jaký nástroj je pro vás nejdůležitější?', [
            {'keywords': ['počítač', 'notebook', 'klávesnice', 'monitor'], 'scores': {'IT': 3}},
            {'keywords': ['stetoskop', 'skalpel', 'injekce', 'mikroskop'], 'scores': {'ZDR': 3}},
            {'keywords': ['kladivo', 'vrtačka', 'pila', 'šroubovák'], 'scores': {'STA': 2, 'STR': 1}},
            {'keywords': ['volant', 'řídítka', 'joystick'], 'scores': {'DOP': 3}},
            {'keywords': ['štětec', 'tužka', 'pero'], 'scores': {'UME': 3}},
            {'keywords': ['hrábě', 'rýč', 'lopata', 'sekera'], 'scores': {'ZEM': 3}},
            {'keywords': ['kniha', 'učebnice', 'tabule'], 'scores': {'SKO': 3}},
        ]),
        # 102
        _short('Jakou hodnotu považujete v práci za nejdůležitější? (jedno slovo)', [
            {'keywords': ['spravedlnost', 'právo', 'zákon'], 'scores': {'PRA': 3}},
            {'keywords': ['pomoc', 'solidarita', 'péče'], 'scores': {'ZDR': 2, 'SKO': 1}},
            {'keywords': ['kreativita', 'tvořivost', 'umění'], 'scores': {'UME': 3}},
            {'keywords': ['peníze', 'plat', 'výdělek', 'zisk'], 'scores': {'MAN': 2, 'OBC': 1}},
            {'keywords': ['příroda', 'ekologie', 'životní prostředí'], 'scores': {'ZEM': 3}},
            {'keywords': ['inovace', 'technologie', 'pokrok'], 'scores': {'IT': 2, 'STR': 1}},
        ]),
        # 103
        _short('Kde byste nejraději pracovali? (místo)', [
            {'keywords': ['kancelář', 'office', 'firma'], 'scores': {'MAN': 2, 'IT': 1}},
            {'keywords': ['nemocnice', 'ordinace', 'klinika', 'lékárna'], 'scores': {'ZDR': 3}},
            {'keywords': ['škola', 'univerzita', 'třída'], 'scores': {'SKO': 3}},
            {'keywords': ['stavba', 'dílna', 'továrna', 'fabrika'], 'scores': {'STA': 2, 'STR': 1}},
            {'keywords': ['venku', 'příroda', 'les', 'farma', 'pole'], 'scores': {'ZEM': 3}},
            {'keywords': ['ateliér', 'studio', 'galerie', 'divadlo'], 'scores': {'UME': 3}},
            {'keywords': ['sklad', 'depo', 'letiště', 'nádraží'], 'scores': {'DOP': 3}},
            {'keywords': ['soud', 'úřad', 'radnice'], 'scores': {'PRA': 3}},
            {'keywords': ['obchod', 'prodejna', 'restaurace', 'hotel'], 'scores': {'OBC': 3}},
        ]),
        # 104
        _short('Napište jednu svou silnou stránku:', [
            {'keywords': ['komunikace', 'mluvení', 'řečnění', 'vyjednávání'], 'scores': {'OBC': 2, 'SKO': 1}},
            {'keywords': ['analytické', 'logika', 'analýza', 'myšlení'], 'scores': {'IT': 2, 'MAN': 1}},
            {'keywords': ['manuální', 'zručnost', 'šikovnost', 'ruční'], 'scores': {'STR': 2, 'STA': 1}},
            {'keywords': ['empatie', 'naslouchání', 'citlivost'], 'scores': {'ZDR': 2, 'SKO': 1}},
            {'keywords': ['kreativita', 'tvořivost', 'fantazie', 'představivost'], 'scores': {'UME': 3}},
            {'keywords': ['organizace', 'plánování', 'systematičnost'], 'scores': {'MAN': 2, 'DOP': 1}},
        ]),
        # 105
        _short('Jaký obor byste chtěli studovat na VŠ?', [
            {'keywords': ['medicína', 'lékařství', 'farmacie', 'ošetřovatelství'], 'scores': {'ZDR': 4}},
            {'keywords': ['informatika', 'počítače', 'kybernetika', 'software'], 'scores': {'IT': 4}},
            {'keywords': ['práva', 'právo', 'právnická'], 'scores': {'PRA': 4}},
            {'keywords': ['ekonomie', 'finance', 'management', 'obchod'], 'scores': {'MAN': 3, 'OBC': 1}},
            {'keywords': ['pedagogika', 'učitelství', 'andragogika'], 'scores': {'SKO': 4}},
            {'keywords': ['architektura', 'stavitelství', 'stavební'], 'scores': {'STA': 4}},
            {'keywords': ['strojírenství', 'elektrotechnika', 'mechatronika'], 'scores': {'STR': 4}},
            {'keywords': ['umění', 'design', 'grafika', 'muzikologie', 'dramaturgie'], 'scores': {'UME': 4}},
            {'keywords': ['zemědělství', 'agronomie', 'lesnictví', 'ekologie'], 'scores': {'ZEM': 4}},
            {'keywords': ['doprava', 'logistika', 'dopravní'], 'scores': {'DOP': 4}},
        ]),
        # 106
        _short('Jaký vynález lidstva považujete za nejdůležitější?', [
            {'keywords': ['internet', 'počítač', 'telefon', 'web'], 'scores': {'IT': 3}},
            {'keywords': ['antibiotika', 'penicilin', 'vakcína', 'lék'], 'scores': {'ZDR': 3}},
            {'keywords': ['kolo', 'auto', 'letadlo', 'vlak', 'parní stroj'], 'scores': {'DOP': 2, 'STR': 1}},
            {'keywords': ['knihtisk', 'písmo', 'kniha'], 'scores': {'SKO': 3}},
            {'keywords': ['elektřina', 'elektřinu', 'žárovka'], 'scores': {'STR': 3}},
            {'keywords': ['zemědělství', 'pluh', 'setba'], 'scores': {'ZEM': 3}},
        ]),
        # 107
        _short('Jaký druh hudby posloucháte nejčastěji? (žánr)', [
            {'keywords': ['klasická', 'opera', 'orchestrální', 'symfonická'], 'scores': {'UME': 3, 'SKO': 1}},
            {'keywords': ['rock', 'metal', 'punk', 'alternativní'], 'scores': {'UME': 2, 'STR': 1}},
            {'keywords': ['pop', 'dance', 'mainstream'], 'scores': {'OBC': 2, 'UME': 1}},
            {'keywords': ['elektronická', 'techno', 'house', 'edm'], 'scores': {'IT': 2, 'UME': 1}},
            {'keywords': ['folk', 'country', 'lidová'], 'scores': {'ZEM': 2, 'UME': 1}},
            {'keywords': ['jazz', 'blues', 'soul'], 'scores': {'UME': 3}},
        ]),
        # 108
        _short('Jak byste charakterizovali svého ideálního nadřízeného? (jedno slovo)', [
            {'keywords': ['férový', 'spravedlivý', 'čestný'], 'scores': {'PRA': 2, 'MAN': 1}},
            {'keywords': ['inspirativní', 'kreativní', 'vizionář'], 'scores': {'UME': 2, 'MAN': 1}},
            {'keywords': ['odborník', 'profesionální', 'zkušený'], 'scores': {'STR': 1, 'IT': 1, 'ZDR': 1}},
            {'keywords': ['empatický', 'lidský', 'chápavý', 'milý'], 'scores': {'SKO': 2, 'ZDR': 1}},
            {'keywords': ['rozhodný', 'silný', 'vůdce'], 'scores': {'MAN': 3}},
        ]),
        # 109
        _short('Jaký je váš oblíbený sport nebo pohybová aktivita?', [
            {'keywords': ['fotbal', 'hokej', 'basketbal', 'volejbal', 'tenis', 'rugby'], 'scores': {'DOP': 1, 'MAN': 1}},
            {'keywords': ['turistika', 'běh', 'cyklistika', 'kolo'], 'scores': {'ZEM': 2, 'DOP': 1}},
            {'keywords': ['posilování', 'fitness', 'crossfit'], 'scores': {'STA': 1, 'STR': 1}},
            {'keywords': ['tanec', 'balet', 'gymnasiky', 'gymnastika'], 'scores': {'UME': 3}},
            {'keywords': ['plavání', 'jóga', 'pilates'], 'scores': {'ZDR': 2}},
            {'keywords': ['šachy', 'esport', 'videohry'], 'scores': {'IT': 2, 'MAN': 1}},
        ]),
        # 110
        _short('Co je podle vás největší výzva 21. století?', [
            {'keywords': ['klimatická', 'globální', 'oteplování', 'ekologie', 'příroda'], 'scores': {'ZEM': 3}},
            {'keywords': ['ai', 'umělá inteligence', 'technologie', 'kybernetika'], 'scores': {'IT': 3}},
            {'keywords': ['chudoba', 'nerovnost', 'spravedlnost'], 'scores': {'PRA': 2, 'OBC': 1}},
            {'keywords': ['zdraví', 'pandemie', 'nemoci', 'covid'], 'scores': {'ZDR': 3}},
            {'keywords': ['vzdělání', 'gramotnost', 'vzdělávání'], 'scores': {'SKO': 3}},
        ]),
        # 111
        _short('Jakou superschopnost byste chtěli mít?', [
            {'keywords': ['léčení', 'uzdravování', 'regenerace'], 'scores': {'ZDR': 3}},
            {'keywords': ['létání', 'teleportace', 'rychlost'], 'scores': {'DOP': 3}},
            {'keywords': ['neviditelnost', 'telepatie', 'čtení myšlenek'], 'scores': {'PRA': 2, 'SKO': 1}},
            {'keywords': ['síla', 'super síla', 'nezranitelnost'], 'scores': {'STA': 2, 'STR': 1}},
            {'keywords': ['genialita', 'inteligence', 'vše vědět'], 'scores': {'IT': 2, 'SKO': 1}},
            {'keywords': ['tvoření', 'vytváření', 'magie'], 'scores': {'UME': 3}},
        ]),
        # 112
        _short('Jakého historického období se nejvíc obdivujete?', [
            {'keywords': ['antika', 'řím', 'řecko', 'starověk'], 'scores': {'PRA': 2, 'STA': 1}},
            {'keywords': ['renesance', 'baroko', 'středověk'], 'scores': {'UME': 2, 'STA': 1}},
            {'keywords': ['průmyslová', 'revoluce', '19. století'], 'scores': {'STR': 2, 'DOP': 1}},
            {'keywords': ['budoucnost', 'moderní', '21. století', 'digitální'], 'scores': {'IT': 3}},
        ]),
        # 113
        _short('Jaký druh jídla preferujete?', [
            {'keywords': ['domácí', 'tradiční', 'české', 'babičky'], 'scores': {'ZEM': 2, 'OBC': 1}},
            {'keywords': ['sushi', 'asijské', 'exotické', 'thajské', 'indické'], 'scores': {'OBC': 2, 'DOP': 1}},
            {'keywords': ['italské', 'pasta', 'pizza', 'francouzské'], 'scores': {'OBC': 2, 'UME': 1}},
            {'keywords': ['zdravé', 'bio', 'vegan', 'raw', 'organické'], 'scores': {'ZDR': 2, 'ZEM': 1}},
            {'keywords': ['fast food', 'burger', 'kebab'], 'scores': {'OBC': 2}},
        ]),

        # ══════════════ MATCHING (114–125) ══════════════

        # 129
        _match('Přiřaďte nástroje k profesím:', [
            {'left': 'Stetoskop', 'right': 'Lékař', 'scores': {'ZDR': 2}},
            {'left': 'Kladivo', 'right': 'Stavař', 'scores': {'STA': 2}},
            {'left': 'Notebook', 'right': 'Programátor', 'scores': {'IT': 2}},
            {'left': 'Štětec', 'right': 'Malíř', 'scores': {'UME': 2}},
        ]),
        # 130
        _match('Přiřaďte předměty ke studijním oborům:', [
            {'left': 'Anatomie', 'right': 'Medicína', 'scores': {'ZDR': 2}},
            {'left': 'Algoritmy', 'right': 'Informatika', 'scores': {'IT': 2}},
            {'left': 'Statika', 'right': 'Stavebnictví', 'scores': {'STA': 2}},
            {'left': 'Pedologie', 'right': 'Zemědělství', 'scores': {'ZEM': 2}},
        ]),
        # 131
        _match('Přiřaďte prostředí k povoláním:', [
            {'left': 'Operační sál', 'right': 'Chirurg', 'scores': {'ZDR': 2}},
            {'left': 'Soudní síň', 'right': 'Soudce', 'scores': {'PRA': 2}},
            {'left': 'Pole', 'right': 'Agronom', 'scores': {'ZEM': 2}},
            {'left': 'Ateliér', 'right': 'Designér', 'scores': {'UME': 2}},
            {'left': 'Kancelář', 'right': 'Manažer', 'scores': {'MAN': 2}},
        ]),
        # 132
        _match('Přiřaďte zkratky k technologiím:', [
            {'left': 'HTML', 'right': 'Webové stránky', 'scores': {'IT': 2}},
            {'left': 'CNC', 'right': 'Obráběcí stroje', 'scores': {'STR': 2}},
            {'left': 'GPS', 'right': 'Navigace', 'scores': {'DOP': 2}},
            {'left': 'BIM', 'right': 'Modelování budov', 'scores': {'STA': 2}},
        ]),
        # 133
        _match('Přiřaďte vlastnosti k profesím:', [
            {'left': 'Empatie', 'right': 'Terapeut', 'scores': {'ZDR': 2}},
            {'left': 'Kreativita', 'right': 'Grafik', 'scores': {'UME': 2}},
            {'left': 'Přesnost', 'right': 'Účetní', 'scores': {'MAN': 2}},
            {'left': 'Odvaha', 'right': 'Hasič', 'scores': {'PRA': 2}},
        ]),
        # 134
        _match('Přiřaďte materiály k oborům:', [
            {'left': 'Beton', 'right': 'Stavebnictví', 'scores': {'STA': 2}},
            {'left': 'Ocel', 'right': 'Strojírenství', 'scores': {'STR': 2}},
            {'left': 'Léčiva', 'right': 'Farmacie', 'scores': {'ZDR': 2}},
            {'left': 'Obilí', 'right': 'Zemědělství', 'scores': {'ZEM': 2}},
        ]),
        # 135
        _match('Přiřaďte softwarové nástroje k profesím:', [
            {'left': 'AutoCAD', 'right': 'Projektant', 'scores': {'STA': 2}},
            {'left': 'VS Code', 'right': 'Programátor', 'scores': {'IT': 2}},
            {'left': 'SAP', 'right': 'Ekonom', 'scores': {'MAN': 2}},
            {'left': 'Photoshop', 'right': 'Grafik', 'scores': {'UME': 2}},
        ]),
        # 136
        _match('Přiřaďte dopravní prostředky k profesím:', [
            {'left': 'Kamion', 'right': 'Řidič', 'scores': {'DOP': 2}},
            {'left': 'Sanitka', 'right': 'Záchranář', 'scores': {'ZDR': 2}},
            {'left': 'Traktor', 'right': 'Farmář', 'scores': {'ZEM': 2}},
            {'left': 'Autobus MHD', 'right': 'Řidič MHD', 'scores': {'DOP': 2}},
        ]),
        # 137
        _match('Přiřaďte vzdělávací tituly k oborům:', [
            {'left': 'MUDr.', 'right': 'Medicína', 'scores': {'ZDR': 2}},
            {'left': 'Ing.', 'right': 'Technika', 'scores': {'STR': 1, 'IT': 1}},
            {'left': 'JUDr.', 'right': 'Právo', 'scores': {'PRA': 2}},
            {'left': 'MgA.', 'right': 'Umění', 'scores': {'UME': 2}},
        ]),
        # 138
        _match('Přiřaďte firmy/instituce k oborům:', [
            {'left': 'Škoda Auto', 'right': 'Strojírenství', 'scores': {'STR': 2}},
            {'left': 'FN Motol', 'right': 'Zdravotnictví', 'scores': {'ZDR': 2}},
            {'left': 'Seznam.cz', 'right': 'IT', 'scores': {'IT': 2}},
            {'left': 'Národní divadlo', 'right': 'Umění', 'scores': {'UME': 2}},
        ]),
        # 139
        _match('Přiřaďte dokumenty k profesím:', [
            {'left': 'Receptura', 'right': 'Lékárník', 'scores': {'ZDR': 2}},
            {'left': 'Projektová dokumentace', 'right': 'Architekt', 'scores': {'STA': 2}},
            {'left': 'Obchodní smlouva', 'right': 'Obchodník', 'scores': {'OBC': 2}},
            {'left': 'Školní vzdělávací plán', 'right': 'Ředitel školy', 'scores': {'SKO': 2}},
        ]),
        # 140
        _match('Přiřaďte certifikáty k oborům:', [
            {'left': 'ISO 9001', 'right': 'Management kvality', 'scores': {'MAN': 2}},
            {'left': 'ECDL', 'right': 'IT dovednosti', 'scores': {'IT': 2}},
            {'left': 'HACCP', 'right': 'Potravinářství', 'scores': {'OBC': 2}},
            {'left': 'Profesní průkaz', 'right': 'Doprava', 'scores': {'DOP': 2}},
        ]),

        # ══════════════ ORDERING (126–135) ══════════════

        # 141
        _order('Seřaďte kroky vývoje softwaru od začátku:',
               ['Analýza požadavků', 'Návrh architektury', 'Implementace kódu', 'Testování', 'Nasazení'],
               [0, 1, 2, 3, 4], {'IT': 1}),
        # 142
        _order('Seřaďte fáze stavby domu:',
               ['Základy', 'Hrubá stavba', 'Střecha', 'Instalace', 'Kolaudace'],
               [0, 1, 2, 3, 4], {'STA': 1}),
        # 143
        _order('Seřaďte kroky první pomoci (ABCDE):',
               ['Airway – průchodnost dýchacích cest', 'Breathing – dýchání',
                'Circulation – krevní oběh', 'Disability – neurologický stav',
                'Exposure – celkový vyšetření'],
               [0, 1, 2, 3, 4], {'ZDR': 1}),
        # 144
        _order('Seřaďte kroky soudního řízení:',
               ['Podání žaloby', 'Přípravné jednání', 'Hlavní líčení', 'Rozsudek', 'Odvolání'],
               [0, 1, 2, 3, 4], {'PRA': 1}),
        # 145
        _order('Seřaďte stupně vzdělání od nejnižšího:',
               ['Základní škola', 'Střední škola', 'Bakalářské studium',
                'Magisterské studium', 'Doktorské studium'],
               [0, 1, 2, 3, 4], {'SKO': 1}),
        # 146
        _order('Seřaďte fáze zemědělského cyklu:',
               ['Příprava půdy', 'Setí', 'Hnojení a ošetřování', 'Sklizeň', 'Uskladnění'],
               [0, 1, 2, 3, 4], {'ZEM': 1}),
        # 147
        _order('Seřaďte kroky logistického procesu:',
               ['Objednávka', 'Balení', 'Nakládka', 'Přeprava', 'Doručení'],
               [0, 1, 2, 3, 4], {'DOP': 1}),
        # 148
        _order('Seřaďte kroky prodeje produktu:',
               ['Průzkum trhu', 'Vývoj produktu', 'Marketing', 'Prodej', 'Zákaznický servis'],
               [0, 1, 2, 3, 4], {'OBC': 1, 'MAN': 1}),
        # 149
        _order('Seřaďte kroky výroby strojní součástky:',
               ['Technický výkres', 'Volba materiálu', 'Obrábění', 'Kontrola kvality', 'Montáž'],
               [0, 1, 2, 3, 4], {'STR': 1}),
        # 150
        _order('Seřaďte kroky tvorby uměleckého díla:',
               ['Inspirace a nápad', 'Skicování', 'Tvorba díla', 'Finální úpravy', 'Výstava/prezentace'],
               [0, 1, 2, 3, 4], {'UME': 1}),
    ]
