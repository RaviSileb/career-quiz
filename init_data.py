"""
init_data.py – Inicializační data pro kariérní kvíz.

Obsahuje:
  • 11 kariérních kategorií
  • 88 pracovních pozic (8 × 11 kategorií) dle NSP.cz
  • 135 kariérních otázek (Part 1 – kariérní směr)

Typy otázek (7):
  1. single_choice   – 30 otázek
  2. multiple_choice  – 18 otázek
  3. true_false       – 20 otázek
  4. likert           – 30 otázek
  5. short_answer     – 15 otázek
  6. matching         – 12 otázek
  7. ordering         – 10 otázek
"""

# ──────────────────────────────────────────────
#  Helper funkce pro tvorbu otázek
# ──────────────────────────────────────────────

def _sc(text, answers):
    """Single-choice otázka (výběr jedné odpovědi).

    answers: list of (text, {category_code: score, ...})
    """
    return {
        'text': text,
        'type': 'single_choice',
        'part': 1,
        'answers': [{'text': a[0], 'scores': a[1]} for a in answers],
    }


def _mc(text, answers):
    """Multiple-choice otázka (více správných odpovědí).

    answers: list of (text, {category_code: score, ...})
    """
    return {
        'text': text,
        'type': 'multiple_choice',
        'part': 1,
        'answers': [{'text': a[0], 'scores': a[1]} for a in answers],
    }


def _tf(text, true_scores, false_scores):
    """True/False otázka (Pravda / Nepravda)."""
    return {
        'text': text,
        'type': 'true_false',
        'part': 1,
        'answers': [
            {'text': 'Pravda', 'scores': true_scores},
            {'text': 'Nepravda', 'scores': false_scores},
        ],
    }


def _likert(text, scores_map):
    """Likert škála (1–5).

    scores_map: {1: {...}, 2: {...}, 3: {...}, 4: {...}, 5: {...}}
    """
    return {
        'text': text,
        'type': 'likert',
        'part': 1,
        'answers': [
            {'text': str(i), 'scores': scores_map.get(i, {})} for i in range(1, 6)
        ],
    }


def _short(text, keywords):
    """Short-answer otázka (krátká odpověď s keyword matching).

    keywords: list of (keyword, {category_code: score, ...})
    """
    return {
        'text': text,
        'type': 'short_answer',
        'part': 1,
        'answers': [{'text': kw[0], 'scores': kw[1]} for kw in keywords],
        'extra_data': {'keywords': [kw[0] for kw in keywords]},
    }


def _match(text, pairs):
    """Matching otázka (přiřazování).

    pairs: list of (left, right, {category_code: score, ...})
    """
    return {
        'text': text,
        'type': 'matching',
        'part': 1,
        'answers': [{'text': f"{p[0]} → {p[1]}", 'scores': p[2]} for p in pairs],
        'extra_data': {'pairs': [{'left': p[0], 'right': p[1]} for p in pairs]},
    }


def _order(text, items):
    """Ordering otázka (seřazování).

    items: list of (text, {category_code: score, ...})
    """
    return {
        'text': text,
        'type': 'ordering',
        'part': 1,
        'answers': [{'text': item[0], 'scores': item[1]} for item in items],
        'extra_data': {'correct_order': [item[0] for item in items]},
    }


# ──────────────────────────────────────────────
#  Kategorie
# ──────────────────────────────────────────────

def get_categories():
    """Vrátí 11 kariérních kategorií."""
    return [
        {
            'code': 'ZEM',
            'name': 'Zemědělství a lesnictví',
            'description': 'Práce v oblasti zemědělské výroby, lesního hospodářství, '
                           'zahradnictví, chovu zvířat a ochrany životního prostředí.',
            'icon': '🌾',
            'color': '#27ae60',
        },
        {
            'code': 'STA',
            'name': 'Stavebnictví a architektura',
            'description': 'Projektování, výstavba a údržba budov, infrastruktury '
                           'a interiérový design.',
            'icon': '🏗️',
            'color': '#e67e22',
        },
        {
            'code': 'STR',
            'name': 'Strojírenství a elektrotechnika',
            'description': 'Konstrukce, výroba a údržba strojů, elektrických zařízení '
                           'a automatizačních systémů.',
            'icon': '⚙️',
            'color': '#7f8c8d',
        },
        {
            'code': 'DOP',
            'name': 'Doprava a logistika',
            'description': 'Organizace přepravy osob a zboží, řízení dodavatelských '
                           'řetězců a skladové hospodářství.',
            'icon': '🚗',
            'color': '#2980b9',
        },
        {
            'code': 'IT',
            'name': 'Informační technologie',
            'description': 'Vývoj softwaru, správa sítí, analýza dat, kybernetická '
                           'bezpečnost a webový design.',
            'icon': '💻',
            'color': '#8e44ad',
        },
        {
            'code': 'ZDR',
            'name': 'Zdravotnictví a medicína',
            'description': 'Léčba, prevence a výzkum v oblasti lidského zdraví, '
                           'farmacie a rehabilitace.',
            'icon': '🏥',
            'color': '#e74c3c',
        },
        {
            'code': 'OBC',
            'name': 'Obchod a služby',
            'description': 'Prodej, marketing, pohostinství, cestovní ruch '
                           'a zákaznický servis.',
            'icon': '🛒',
            'color': '#f39c12',
        },
        {
            'code': 'SKO',
            'name': 'Školství a vzdělávání',
            'description': 'Výuka, lektorství, vědecký výzkum, koučink a práce '
                           's dětmi a mládeží.',
            'icon': '📚',
            'color': '#3498db',
        },
        {
            'code': 'PRA',
            'name': 'Právo a veřejná správa',
            'description': 'Legislativa, soudnictví, bezpečnostní složky '
                           'a státní administrativa.',
            'icon': '⚖️',
            'color': '#34495e',
        },
        {
            'code': 'MAN',
            'name': 'Management a podnikání',
            'description': 'Řízení firem, finanční plánování, lidské zdroje, '
                           'controlling a podnikatelské strategie.',
            'icon': '📊',
            'color': '#1abc9c',
        },
        {
            'code': 'UME',
            'name': 'Umění a kultura',
            'description': 'Herectví, hudba, grafický design, fotografie, '
                           'literatura a filmová tvorba.',
            'icon': '🎨',
            'color': '#e91e63',
        },
    ]


# ──────────────────────────────────────────────
#  Pracovní pozice (88 = 8 × 11)
# ──────────────────────────────────────────────

def get_positions():
    """Vrátí 88 pracovních pozic (8 na každou kategorii) dle NSP.cz."""
    return [
        # ── ZEM ──────────────────────────────
        {'name': 'Agronom', 'category': 'ZEM',
         'description': 'Řídí rostlinnou výrobu, plánuje osevní postupy a dohlíží na užití hnojiv a pesticidů.',
         'icon': '🌱'},
        {'name': 'Veterinární lékař', 'category': 'ZEM',
         'description': 'Diagnostikuje a léčí onemocnění zvířat, provádí preventivní péči a vakcinace.',
         'icon': '🐄'},
        {'name': 'Lesní inženýr', 'category': 'ZEM',
         'description': 'Plánuje a řídí hospodaření v lesích, zajišťuje obnovu a ochranu lesních porostů.',
         'icon': '🌲'},
        {'name': 'Zahradník', 'category': 'ZEM',
         'description': 'Pěstuje a ošetřuje okrasné i užitkové rostliny, navrhuje zahradní úpravy.',
         'icon': '🌻'},
        {'name': 'Zemědělský technik', 'category': 'ZEM',
         'description': 'Obsluhuje a udržuje zemědělskou techniku, zajišťuje mechanizaci polních prací.',
         'icon': '🚜'},
        {'name': 'Chovatel zvířat', 'category': 'ZEM',
         'description': 'Stará se o hospodářská nebo domácí zvířata, zajišťuje krmení, ustájení a welfare.',
         'icon': '🐑'},
        {'name': 'Myslivec', 'category': 'ZEM',
         'description': 'Pečuje o zvěř, řídí myslivecké hospodaření a chrání přírodní ekosystémy.',
         'icon': '🦌'},
        {'name': 'Ekolog', 'category': 'ZEM',
         'description': 'Hodnotí dopady lidské činnosti na životní prostředí a navrhuje opatření na jeho ochranu.',
         'icon': '🌍'},

        # ── STA ──────────────────────────────
        {'name': 'Architekt', 'category': 'STA',
         'description': 'Navrhuje budovy a urbanistické celky s ohledem na estetiku, funkčnost a udržitelnost.',
         'icon': '🏛️'},
        {'name': 'Stavbyvedoucí', 'category': 'STA',
         'description': 'Organizuje a řídí stavební práce, dohlíží na dodržování harmonogramu a kvality.',
         'icon': '👷'},
        {'name': 'Projektant', 'category': 'STA',
         'description': 'Zpracovává projektovou dokumentaci staveb včetně statických a technických výpočtů.',
         'icon': '📐'},
        {'name': 'Geodet', 'category': 'STA',
         'description': 'Provádí měření a mapování terénu pro potřeby výstavby a katastru nemovitostí.',
         'icon': '📏'},
        {'name': 'Rozpočtář staveb', 'category': 'STA',
         'description': 'Kalkuluje náklady na stavební práce a materiály, sestavuje rozpočty staveb.',
         'icon': '🧮'},
        {'name': 'Interiérový designér', 'category': 'STA',
         'description': 'Navrhuje funkční a estetické interiéry bytových i komerčních prostor.',
         'icon': '🪑'},
        {'name': 'Zedník', 'category': 'STA',
         'description': 'Provádí zdění, omítání a další stavební práce při stavbě a rekonstrukcích budov.',
         'icon': '🧱'},
        {'name': 'Instalatér', 'category': 'STA',
         'description': 'Montuje a opravuje rozvody vody, plynu a topení v budovách.',
         'icon': '🔧'},

        # ── STR ──────────────────────────────
        {'name': 'Strojní konstruktér', 'category': 'STR',
         'description': 'Navrhuje strojní díly a sestavy pomocí CAD systémů, provádí pevnostní výpočty.',
         'icon': '🔩'},
        {'name': 'Strojní technolog', 'category': 'STR',
         'description': 'Stanovuje technologické postupy výroby, optimalizuje výrobní procesy.',
         'icon': '🏭'},
        {'name': 'Elektrotechnik', 'category': 'STR',
         'description': 'Navrhuje, instaluje a udržuje elektrická zařízení a rozvody.',
         'icon': '⚡'},
        {'name': 'Autotronik', 'category': 'STR',
         'description': 'Diagnostikuje a opravuje elektronické systémy v motorových vozidlech.',
         'icon': '🔌'},
        {'name': 'Programátor CNC', 'category': 'STR',
         'description': 'Sestavuje programy pro číslicově řízené obráběcí stroje.',
         'icon': '🖥️'},
        {'name': 'Svářeč', 'category': 'STR',
         'description': 'Spojuje kovové díly svařováním různými metodami (MIG, TIG, oblouk).',
         'icon': '🔥'},
        {'name': 'Obráběč kovů', 'category': 'STR',
         'description': 'Vyrábí kovové součásti soustružením, frézováním a broušením na obráběcích strojích.',
         'icon': '🔨'},
        {'name': 'Mechatronik', 'category': 'STR',
         'description': 'Projektuje a udržuje mechatronické systémy propojující mechaniku, elektroniku a IT.',
         'icon': '🤖'},

        # ── DOP ──────────────────────────────
        {'name': 'Logistik', 'category': 'DOP',
         'description': 'Plánuje a optimalizuje přepravu a skladování zboží v dodavatelském řetězci.',
         'icon': '📦'},
        {'name': 'Pilot', 'category': 'DOP',
         'description': 'Řídí letadlo, zodpovídá za bezpečnost letu a cestujících.',
         'icon': '✈️'},
        {'name': 'Řidič', 'category': 'DOP',
         'description': 'Přepravuje osoby nebo náklad silničními vozidly v souladu s předpisy.',
         'icon': '🚛'},
        {'name': 'Dispečer', 'category': 'DOP',
         'description': 'Koordinuje provoz dopravních prostředků a řeší operativní situace.',
         'icon': '📡'},
        {'name': 'Strojvedoucí', 'category': 'DOP',
         'description': 'Řídí vlakovou soupravu, dbá na bezpečnost železničního provozu.',
         'icon': '🚂'},
        {'name': 'Kapitán plavidla', 'category': 'DOP',
         'description': 'Velí posádce lodi, odpovídá za navigaci a bezpečnost plavby.',
         'icon': '⚓'},
        {'name': 'Skladník', 'category': 'DOP',
         'description': 'Přijímá, eviduje a vydává zboží ze skladu, obsluhuje manipulační techniku.',
         'icon': '🏗️'},
        {'name': 'Celník', 'category': 'DOP',
         'description': 'Kontroluje přepravu zboží přes hranice, ověřuje celní dokumenty a vybírá cla.',
         'icon': '🛃'},

        # ── IT ───────────────────────────────
        {'name': 'Programátor', 'category': 'IT',
         'description': 'Vyvíjí softwarové aplikace, píše a testuje zdrojový kód v různých jazycích.',
         'icon': '👨‍💻'},
        {'name': 'Analytik IT', 'category': 'IT',
         'description': 'Analyzuje požadavky na informační systémy a navrhuje jejich řešení.',
         'icon': '📊'},
        {'name': 'Správce sítí', 'category': 'IT',
         'description': 'Spravuje a zabezpečuje počítačové sítě, servery a síťovou infrastrukturu.',
         'icon': '🌐'},
        {'name': 'Webdesigner', 'category': 'IT',
         'description': 'Navrhuje vizuální stránku webových stránek a zajišťuje uživatelský komfort.',
         'icon': '🎨'},
        {'name': 'Tester', 'category': 'IT',
         'description': 'Testuje software, hledá chyby a ověřuje splnění funkčních požadavků.',
         'icon': '🔍'},
        {'name': 'Datový inženýr', 'category': 'IT',
         'description': 'Navrhuje datové pipeline, spravuje databáze a zajišťuje kvalitu dat.',
         'icon': '🗄️'},
        {'name': 'Kybernetik', 'category': 'IT',
         'description': 'Chrání informační systémy před kybernetickými hrozbami a navrhuje bezpečnostní opatření.',
         'icon': '🛡️'},
        {'name': 'Herní vývojář', 'category': 'IT',
         'description': 'Programuje počítačové a mobilní hry, implementuje herní mechaniky a logiku.',
         'icon': '🎮'},

        # ── ZDR ──────────────────────────────
        {'name': 'Lékař', 'category': 'ZDR',
         'description': 'Diagnostikuje a léčí onemocnění, provádí vyšetření a předepisuje léčbu.',
         'icon': '👨‍⚕️'},
        {'name': 'Farmaceut', 'category': 'ZDR',
         'description': 'Připravuje a vydává léčiva, poradí pacientům ohledně užívání léků.',
         'icon': '💊'},
        {'name': 'Zubař', 'category': 'ZDR',
         'description': 'Vyšetřuje a ošetřuje zuby a ústní dutinu, provádí stomatologické zákroky.',
         'icon': '🦷'},
        {'name': 'Zdravotní sestra', 'category': 'ZDR',
         'description': 'Poskytuje ošetřovatelskou péči pacientům, asistuje lékařům při vyšetřeních.',
         'icon': '👩‍⚕️'},
        {'name': 'Fyzioterapeut', 'category': 'ZDR',
         'description': 'Rehabilituje pacienty pomocí pohybových cvičení a fyzikálních procedur.',
         'icon': '💪'},
        {'name': 'Záchranář', 'category': 'ZDR',
         'description': 'Poskytuje přednemocniční neodkladnou péči a transportuje pacienty do nemocnice.',
         'icon': '🚑'},
        {'name': 'Nutriční terapeut', 'category': 'ZDR',
         'description': 'Sestavuje výživové plány, poradí v oblasti dietologie a prevence obezity.',
         'icon': '🥗'},
        {'name': 'Biomedicínský inženýr', 'category': 'ZDR',
         'description': 'Vyvíjí a udržuje zdravotnickou techniku – přístroje, implantáty a diagnostické systémy.',
         'icon': '🔬'},

        # ── OBC ──────────────────────────────
        {'name': 'Obchodní zástupce', 'category': 'OBC',
         'description': 'Vyhledává zákazníky, prezentuje produkty a uzavírá obchodní smlouvy.',
         'icon': '🤝'},
        {'name': 'Marketingový specialista', 'category': 'OBC',
         'description': 'Plánuje a realizuje marketingové kampaně, analyzuje trh a konkurenci.',
         'icon': '📢'},
        {'name': 'Nákupčí', 'category': 'OBC',
         'description': 'Zajišťuje nákup materiálů a zboží za optimálních cenových a kvalitativních podmínek.',
         'icon': '🛍️'},
        {'name': 'Kuchař', 'category': 'OBC',
         'description': 'Připravuje pokrmy dle receptur, tvoří jídelní lístky a dohlíží na hygienu.',
         'icon': '👨‍🍳'},
        {'name': 'Průvodce', 'category': 'OBC',
         'description': 'Provází turisty po pamětihodnostech, sděluje historické a kulturní informace.',
         'icon': '🗺️'},
        {'name': 'Recepční', 'category': 'OBC',
         'description': 'Zajišťuje příjem hostů v hotelu nebo firmě, poskytuje informace a organizuje služby.',
         'icon': '🏨'},
        {'name': 'Realitní makléř', 'category': 'OBC',
         'description': 'Zprostředkovává prodej a pronájem nemovitostí, jedná s klienty.',
         'icon': '🏠'},
        {'name': 'Barman', 'category': 'OBC',
         'description': 'Připravuje a servíruje nápoje, obsluhuje hosty u baru.',
         'icon': '🍸'},

        # ── SKO ──────────────────────────────
        {'name': 'Učitel', 'category': 'SKO',
         'description': 'Vzdělává žáky na základních a středních školách, připravuje výukové materiály.',
         'icon': '👨‍🏫'},
        {'name': 'Lektor', 'category': 'SKO',
         'description': 'Vede odborné kurzy a školení pro dospělé, přizpůsobuje výuku cílové skupině.',
         'icon': '🎓'},
        {'name': 'Vědecký pracovník', 'category': 'SKO',
         'description': 'Provádí výzkum v dané vědní disciplíně, publikuje vědecké práce.',
         'icon': '🔬'},
        {'name': 'Kouč', 'category': 'SKO',
         'description': 'Rozvíjí potenciál klientů prostřednictvím koučovacích technik a rozhovorů.',
         'icon': '💡'},
        {'name': 'Trenér', 'category': 'SKO',
         'description': 'Vede sportovní tréninky, připravuje závodníky na soutěže.',
         'icon': '🏋️'},
        {'name': 'Vychovatel', 'category': 'SKO',
         'description': 'Pečuje o děti ve školní družině nebo internátě, organizuje volnočasové aktivity.',
         'icon': '🧒'},
        {'name': 'Speciální pedagog', 'category': 'SKO',
         'description': 'Vzdělává a rozvíjí žáky se speciálními vzdělávacími potřebami.',
         'icon': '♿'},
        {'name': 'Knihovník', 'category': 'SKO',
         'description': 'Spravuje knihovní fond, pomáhá čtenářům s vyhledáváním informací.',
         'icon': '📖'},

        # ── PRA ──────────────────────────────
        {'name': 'Advokát', 'category': 'PRA',
         'description': 'Zastupuje klienty před soudy, poskytuje právní poradenství a sepisuje právní dokumenty.',
         'icon': '⚖️'},
        {'name': 'Soudce', 'category': 'PRA',
         'description': 'Rozhoduje spory a trestní věci v soudním řízení dle platného práva.',
         'icon': '🏛️'},
        {'name': 'Notář', 'category': 'PRA',
         'description': 'Ověřuje listiny, sepisuje notářské zápisy a provádí dědická řízení.',
         'icon': '📜'},
        {'name': 'Státní zástupce', 'category': 'PRA',
         'description': 'Zastupuje veřejný zájem v trestním řízení, podává obžaloby.',
         'icon': '🔱'},
        {'name': 'Exekutor', 'category': 'PRA',
         'description': 'Vymáhá pohledávky na základě soudních rozhodnutí a exekučních titulů.',
         'icon': '📋'},
        {'name': 'Policista', 'category': 'PRA',
         'description': 'Chrání veřejný pořádek, vyšetřuje trestné činy a zajišťuje bezpečnost občanů.',
         'icon': '👮'},
        {'name': 'Hasič', 'category': 'PRA',
         'description': 'Zasahuje při požárech a mimořádných událostech, provádí záchranné práce.',
         'icon': '🧑‍🚒'},
        {'name': 'Úředník', 'category': 'PRA',
         'description': 'Vykonává státní správu, zpracovává podání, vydává rozhodnutí a povolení.',
         'icon': '🏢'},

        # ── MAN ──────────────────────────────
        {'name': 'Generální ředitel', 'category': 'MAN',
         'description': 'Řídí celou společnost, určuje strategické směřování a zodpovídá za výsledky.',
         'icon': '👔'},
        {'name': 'Projektový manažer', 'category': 'MAN',
         'description': 'Plánuje, koordinuje a řídí projekty od zadání po dokončení.',
         'icon': '📋'},
        {'name': 'Finanční analytik', 'category': 'MAN',
         'description': 'Analyzuje finanční data, hodnotí investice a připravuje finanční modely.',
         'icon': '💹'},
        {'name': 'Účetní', 'category': 'MAN',
         'description': 'Vede účetnictví, zpracovává daňová přiznání a finanční výkazy.',
         'icon': '🧾'},
        {'name': 'HR specialista', 'category': 'MAN',
         'description': 'Zajišťuje nábor zaměstnanců, péči o pracovníky a rozvoj lidských zdrojů.',
         'icon': '👥'},
        {'name': 'Manažer kvality', 'category': 'MAN',
         'description': 'Zavádí a kontroluje systémy řízení kvality dle ISO norem.',
         'icon': '✅'},
        {'name': 'Podnikatel', 'category': 'MAN',
         'description': 'Zakládá a provozuje vlastní podnik, řídí obchodní aktivity a rozvoj firmy.',
         'icon': '🚀'},
        {'name': 'Controller', 'category': 'MAN',
         'description': 'Sleduje hospodaření firmy, sestavuje rozpočty a reporty pro vedení.',
         'icon': '📈'},

        # ── UME ──────────────────────────────
        {'name': 'Herec', 'category': 'UME',
         'description': 'Ztvárňuje postavy v divadle, filmu a televizi, interpretuje dramatické texty.',
         'icon': '🎭'},
        {'name': 'Režisér', 'category': 'UME',
         'description': 'Vede tvůrčí tým při natáčení filmu nebo inscenaci divadelního představení.',
         'icon': '🎬'},
        {'name': 'Hudebník', 'category': 'UME',
         'description': 'Hraje na hudební nástroje, vystupuje na koncertech a nahrává hudbu.',
         'icon': '🎵'},
        {'name': 'Grafik', 'category': 'UME',
         'description': 'Vytváří vizuální návrhy – loga, plakáty, obaly a digitální grafiku.',
         'icon': '🖌️'},
        {'name': 'Fotograf', 'category': 'UME',
         'description': 'Zachycuje obrazy pomocí fotografické techniky pro umělecké i komerční účely.',
         'icon': '📷'},
        {'name': 'Spisovatel', 'category': 'UME',
         'description': 'Píše literární díla – romány, povídky, básně a novinářské texty.',
         'icon': '✍️'},
        {'name': 'Kameraman', 'category': 'UME',
         'description': 'Natáčí filmové a televizní záběry, pracuje s kamerou a osvětlením.',
         'icon': '🎥'},
        {'name': 'Ilustrátor', 'category': 'UME',
         'description': 'Kreslí ilustrace pro knihy, časopisy, reklamy a digitální média.',
         'icon': '🖼️'},
    ]


# ──────────────────────────────────────────────
#  135 kariérních otázek – Part 1
# ──────────────────────────────────────────────

def get_questions():
    """Vrátí 135 kariérních otázek (Part 1 – kariérní směr).

    Rozložení typů:
      30× single_choice, 18× multiple_choice, 20× true_false,
      30× likert, 15× short_answer, 12× matching, 10× ordering.
    """
    questions = []

    # ══════════════════════════════════════════
    #  SINGLE CHOICE (30 otázek) – q1..q30
    # ══════════════════════════════════════════

    # q1
    questions.append(_sc(
        'Jaký typ pracovního prostředí vás nejvíce přitahuje?',
        [
            ('Práce venku v přírodě – na poli, v lese nebo na farmě', {'ZEM': 3}),
            ('Kancelář s počítačem a moderními technologiemi', {'IT': 3}),
            ('Nemocnice, laboratoř nebo zdravotnické zařízení', {'ZDR': 3}),
            ('Ateliér, divadlo nebo kreativní studio', {'UME': 3}),
        ],
    ))

    # q2
    questions.append(_sc(
        'Který školní předmět vás nejvíce bavil?',
        [
            ('Matematika a fyzika', {'STR': 2, 'IT': 1}),
            ('Biologie a chemie', {'ZDR': 2, 'ZEM': 1}),
            ('Dějepis a společenské vědy', {'PRA': 2, 'SKO': 1}),
            ('Výtvarná nebo hudební výchova', {'UME': 3}),
        ],
    ))

    # q3
    questions.append(_sc(
        'Jak byste nejraději trávili svůj pracovní den?',
        [
            ('Řízením týmu a plánováním strategie', {'MAN': 3}),
            ('Prací s lidmi – učením nebo poradenstvím', {'SKO': 3}),
            ('Navrhováním budov nebo interiérů', {'STA': 3}),
            ('Řízením vozidla nebo koordinací přepravy', {'DOP': 3}),
        ],
    ))

    # q4
    questions.append(_sc(
        'Co je pro vás v práci nejdůležitější?',
        [
            ('Vysoký plat a kariérní růst', {'MAN': 2, 'IT': 1}),
            ('Pomáhání lidem a společnosti', {'ZDR': 2, 'SKO': 1}),
            ('Tvůrčí svoboda a sebevyjádření', {'UME': 3}),
            ('Stabilita a jistota zaměstnání', {'PRA': 2, 'STA': 1}),
        ],
    ))

    # q5
    questions.append(_sc(
        'Který z těchto projektů byste nejraději realizovali?',
        [
            ('Vyvinout mobilní aplikaci', {'IT': 3}),
            ('Postavit rodinný dům', {'STA': 3}),
            ('Zorganizovat obchodní konferenci', {'OBC': 2, 'MAN': 1}),
            ('Natočit dokumentární film', {'UME': 3}),
        ],
    ))

    # q6
    questions.append(_sc(
        'Jakou knihu byste si nejraději přečetli?',
        [
            ('Učebnici programování nebo IT příručku', {'IT': 3}),
            ('Právnický nebo historický text', {'PRA': 2, 'SKO': 1}),
            ('Příručku o zahradničení nebo ekologii', {'ZEM': 3}),
            ('Román nebo sbírku básní', {'UME': 2, 'SKO': 1}),
        ],
    ))

    # q7
    questions.append(_sc(
        'Kde byste nejraději pracovali?',
        [
            ('Ve výrobní hale u strojů', {'STR': 3}),
            ('V obchodě nebo restauraci s lidmi', {'OBC': 3}),
            ('Na stavbě nebo v projekční kanceláři', {'STA': 3}),
            ('V logistickém centru nebo na letišti', {'DOP': 3}),
        ],
    ))

    # q8
    questions.append(_sc(
        'Jakým způsobem nejraději řešíte problémy?',
        [
            ('Logicky a analyticky – hledám data a fakta', {'IT': 2, 'MAN': 1}),
            ('Kreativně – hledám neotřelá řešení', {'UME': 2, 'STA': 1}),
            ('Prakticky – opravím to vlastníma rukama', {'STR': 2, 'ZEM': 1}),
            ('Komunikací – promluvím si s lidmi', {'SKO': 2, 'OBC': 1}),
        ],
    ))

    # q9
    questions.append(_sc(
        'Který z těchto cílů je vám nejbližší?',
        [
            ('Ochránit přírodu a životní prostředí', {'ZEM': 3}),
            ('Zajistit spravedlnost ve společnosti', {'PRA': 3}),
            ('Vyléčit vážnou nemoc', {'ZDR': 3}),
            ('Vybudovat úspěšnou firmu', {'MAN': 3}),
        ],
    ))

    # q10
    questions.append(_sc(
        'Jaký typ kolegů byste chtěli mít?',
        [
            ('Inženýry a techniky', {'STR': 2, 'IT': 1}),
            ('Lékaře a zdravotníky', {'ZDR': 3}),
            ('Obchodníky a manažery', {'OBC': 2, 'MAN': 1}),
            ('Umělce a kreativce', {'UME': 3}),
        ],
    ))

    # q11
    questions.append(_sc(
        'Jak reagujete na stresové situace?',
        [
            ('Zachovám klid a postupuji systematicky', {'PRA': 2, 'DOP': 1}),
            ('Hledám kreativní únikovou cestu', {'UME': 2, 'OBC': 1}),
            ('Vyhodnotím situaci a povedu tým k řešení', {'MAN': 3}),
            ('Okamžitě jednám – rychlý zásah je klíčový', {'ZDR': 2, 'PRA': 1}),
        ],
    ))

    # q12
    questions.append(_sc(
        'Jakou dovednost byste se nejraději naučili?',
        [
            ('Programování a analýzu dat', {'IT': 3}),
            ('Řízení letadla nebo lodi', {'DOP': 3}),
            ('Svařování nebo obrábění kovů', {'STR': 3}),
            ('Vaření na profesionální úrovni', {'OBC': 3}),
        ],
    ))

    # q13
    questions.append(_sc(
        'Jaký typ vzdělávání vás zajímá nejvíce?',
        [
            ('Technické – strojírenství, elektrotechnika', {'STR': 3}),
            ('Přírodovědné – biologie, ekologie', {'ZEM': 2, 'ZDR': 1}),
            ('Humanitní – právo, politologie, historie', {'PRA': 2, 'SKO': 1}),
            ('Ekonomické – finance, marketing, management', {'MAN': 2, 'OBC': 1}),
        ],
    ))

    # q14
    questions.append(_sc(
        'Co vás na práci motivuje nejvíce?',
        [
            ('Viditelný výsledek – postavená budova, hotový výrobek', {'STA': 2, 'STR': 1}),
            ('Uznání a potlesk publika', {'UME': 3}),
            ('Vděčnost lidí, kterým pomáhám', {'ZDR': 2, 'SKO': 1}),
            ('Finanční odměna a bonusy', {'MAN': 2, 'OBC': 1}),
        ],
    ))

    # q15
    questions.append(_sc(
        'Jak byste nejraději komunikovali v práci?',
        [
            ('Přes e-mail, chat a videohovory', {'IT': 2, 'MAN': 1}),
            ('Osobně tváří v tvář', {'SKO': 2, 'ZDR': 1}),
            ('Prostřednictvím výkresů a návrhů', {'STA': 2, 'STR': 1}),
            ('Přes obchodní jednání a prezentace', {'OBC': 2, 'MAN': 1}),
        ],
    ))

    # q16
    questions.append(_sc(
        'Jakou roli zaujímáte ve skupinové práci?',
        [
            ('Vedoucí – organizuji a rozhoduji', {'MAN': 3}),
            ('Analytik – zkoumám data a navrhuji řešení', {'IT': 2, 'MAN': 1}),
            ('Tvůrce – přicházím s nápady', {'UME': 2, 'STA': 1}),
            ('Realizátor – dělám praktickou práci', {'STR': 2, 'ZEM': 1}),
        ],
    ))

    # q17
    questions.append(_sc(
        'Které riziko byste nejspíše podstoupili?',
        [
            ('Založit vlastní startup', {'MAN': 3}),
            ('Pracovat ve výškách na stavbě', {'STA': 2, 'STR': 1}),
            ('Zachraňovat lidi v ohrožení života', {'ZDR': 2, 'PRA': 1}),
            ('Cestovat do nebezpečných oblastí jako reportér', {'UME': 2, 'OBC': 1}),
        ],
    ))

    # q18
    questions.append(_sc(
        'Jaký druh technologie vás nejvíce fascinuje?',
        [
            ('Umělá inteligence a strojové učení', {'IT': 3}),
            ('Medicínské přístroje a robotická chirurgie', {'ZDR': 2, 'STR': 1}),
            ('Elektromobily a autonomní řízení', {'DOP': 2, 'STR': 1}),
            ('3D tisk a moderní stavební technologie', {'STA': 2, 'STR': 1}),
        ],
    ))

    # q19
    questions.append(_sc(
        'Jak důležitá je pro vás práce v týmu?',
        [
            ('Velmi – nejraději pracuji ve velkém týmu', {'MAN': 2, 'OBC': 1}),
            ('Preferuji menší tým 3–5 lidí', {'STA': 1, 'ZDR': 1, 'SKO': 1}),
            ('Raději pracuji sám nebo ve dvojici', {'IT': 2, 'UME': 1}),
            ('Záleží na situaci – jsem flexibilní', {'DOP': 1, 'PRA': 1, 'STR': 1}),
        ],
    ))

    # q20
    questions.append(_sc(
        'Jaký pracovní rytmus vám vyhovuje?',
        [
            ('Pravidelný – denní rutina a řád', {'PRA': 2, 'MAN': 1}),
            ('Směnný provoz – střídání denních a nočních', {'ZDR': 2, 'DOP': 1}),
            ('Sezónní – intenzivní práce v sezóně, klid mimo ni', {'ZEM': 3}),
            ('Nepravidelný – každý den je jiný', {'UME': 2, 'OBC': 1}),
        ],
    ))

    # q21
    questions.append(_sc(
        'Kterou z těchto činností byste dělali nejraději celý den?',
        [
            ('Psát kód a vyvíjet software', {'IT': 3}),
            ('Učit skupinu studentů nové dovednosti', {'SKO': 3}),
            ('Pěstovat rostliny a starat se o zahradu', {'ZEM': 3}),
            ('Obchodovat a vyjednávat s klienty', {'OBC': 3}),
        ],
    ))

    # q22
    questions.append(_sc(
        'Jaký typ problémů řešíte nejraději?',
        [
            ('Technické – jak opravit stroj nebo navrhnout mechanismus', {'STR': 3}),
            ('Právní – jak interpretovat zákon a obhájit klienta', {'PRA': 3}),
            ('Zdravotní – jak diagnostikovat a vyléčit pacienta', {'ZDR': 3}),
            ('Logistické – jak dostat zboží z bodu A do bodu B', {'DOP': 3}),
        ],
    ))

    # q23
    questions.append(_sc(
        'Jaký druh odpovědnosti přijímáte nejsnáze?',
        [
            ('Za zdraví a životy lidí', {'ZDR': 2, 'PRA': 1}),
            ('Za finanční výsledky firmy', {'MAN': 3}),
            ('Za kvalitu stavby nebo výrobku', {'STA': 2, 'STR': 1}),
            ('Za vzdělání a rozvoj druhých', {'SKO': 3}),
        ],
    ))

    # q24
    questions.append(_sc(
        'Co byste udělali s volným milionem korun?',
        [
            ('Investoval/a do vlastního podnikání', {'MAN': 3}),
            ('Financoval/a ekologický projekt', {'ZEM': 2, 'PRA': 1}),
            ('Koupil/a vybavení pro kreativní studio', {'UME': 3}),
            ('Financoval/a zdravotnický výzkum', {'ZDR': 2, 'SKO': 1}),
        ],
    ))

    # q25
    questions.append(_sc(
        'Jaký pracovní nástroj je vám nejbližší?',
        [
            ('Počítač a software', {'IT': 3}),
            ('Stetoskop a lékařské přístroje', {'ZDR': 3}),
            ('Soustruh, fréza nebo svářečka', {'STR': 3}),
            ('Pero, štětec nebo fotoaparát', {'UME': 3}),
        ],
    ))

    # q26
    questions.append(_sc(
        'Kam byste jeli na pracovní stáž?',
        [
            ('Do Silicon Valley – technologické firmy', {'IT': 3}),
            ('Do Švýcarska – farmaceutický výzkum', {'ZDR': 2, 'ZEM': 1}),
            ('Do Dubaje – megaprojekty ve stavebnictví', {'STA': 3}),
            ('Do Hollywoodu – filmová studia', {'UME': 3}),
        ],
    ))

    # q27
    questions.append(_sc(
        'Jaký typ cestování v rámci práce preferujete?',
        [
            ('Pravidelné služební cesty za klienty', {'OBC': 2, 'MAN': 1}),
            ('Řízení nákladního vozu po Evropě', {'DOP': 3}),
            ('Terénní výzkum v přírodě', {'ZEM': 2, 'SKO': 1}),
            ('Necestovat – preferuji jednu lokalitu', {'PRA': 1, 'STR': 1, 'IT': 1}),
        ],
    ))

    # q28
    questions.append(_sc(
        'Jaký je váš ideální pracovní oděv?',
        [
            ('Montérky nebo pracovní kombinéza', {'STR': 2, 'STA': 1}),
            ('Oblek nebo formální oblečení', {'PRA': 2, 'MAN': 1}),
            ('Zdravotnický plášť', {'ZDR': 3}),
            ('Volné oblečení – džíny a tričko', {'IT': 2, 'UME': 1}),
        ],
    ))

    # q29
    questions.append(_sc(
        'Který z těchto výroků vás nejlépe vystihuje?',
        [
            ('Mám rád/a čísla, grafy a analytické úkoly', {'MAN': 2, 'IT': 1}),
            ('Mám rád/a práci rukama a viditelný výsledek', {'STA': 2, 'STR': 1}),
            ('Mám rád/a kontakt s lidmi a pomáhání', {'ZDR': 1, 'SKO': 1, 'OBC': 1}),
            ('Mám rád/a tvůrčí proces a umělecký výraz', {'UME': 3}),
        ],
    ))

    # q30
    questions.append(_sc(
        'Co vás na škole bavilo nejvíce?',
        [
            ('Laboratorní cvičení a pokusy', {'ZDR': 2, 'STR': 1}),
            ('Školní výlety a exkurze do přírody', {'ZEM': 2, 'DOP': 1}),
            ('Skupinové projekty a prezentace', {'MAN': 2, 'OBC': 1}),
            ('Výtvarné a dramatické kroužky', {'UME': 3}),
        ],
    ))

    # ══════════════════════════════════════════
    #  MULTIPLE CHOICE (18 otázek) – q31..q48
    # ══════════════════════════════════════════

    # q31
    questions.append(_mc(
        'Které z těchto činností vás baví? (vyberte všechny)',
        [
            ('Programování a tvorba webů', {'IT': 3}),
            ('Kreslení, malování nebo fotografování', {'UME': 3}),
            ('Opravování strojů a elektroniky', {'STR': 3}),
            ('Zahradničení a práce s přírodou', {'ZEM': 3}),
            ('Organizování akcí a jednání s lidmi', {'OBC': 2, 'MAN': 1}),
        ],
    ))

    # q32
    questions.append(_mc(
        'Jaké TV pořady nebo videa sledujete nejraději?',
        [
            ('Dokumenty o přírodě a zvířatech', {'ZEM': 3}),
            ('Technologické novinky a recenze', {'IT': 2, 'STR': 1}),
            ('Kriminální seriály a soudní drama', {'PRA': 3}),
            ('Kuchařské show a cestopisy', {'OBC': 3}),
            ('Vzdělávací a populárně-vědecké pořady', {'SKO': 3}),
        ],
    ))

    # q33
    questions.append(_mc(
        'Které vlastnosti vás nejlépe vystihují?',
        [
            ('Pečlivost a smysl pro detail', {'STR': 2, 'PRA': 1}),
            ('Empatie a soucit', {'ZDR': 2, 'SKO': 1}),
            ('Kreativita a originalita', {'UME': 3}),
            ('Odvaha a rozhodnost', {'PRA': 2, 'MAN': 1}),
            ('Trpělivost a vytrvalost', {'ZEM': 2, 'SKO': 1}),
        ],
    ))

    # q34
    questions.append(_mc(
        'Které předměty ve škole jste měli nejraději?',
        [
            ('Informatika', {'IT': 3}),
            ('Tělesná výchova', {'ZDR': 1, 'SKO': 1, 'PRA': 1}),
            ('Chemie', {'ZDR': 2, 'ZEM': 1}),
            ('Zeměpis', {'DOP': 2, 'ZEM': 1}),
            ('Občanská výchova', {'PRA': 2, 'SKO': 1}),
        ],
    ))

    # q35
    questions.append(_mc(
        'Jaké volnočasové aktivity provozujete?',
        [
            ('Sporty a outdoorové aktivity', {'ZDR': 1, 'ZEM': 1, 'DOP': 1}),
            ('Hraní počítačových her', {'IT': 2, 'UME': 1}),
            ('Kutilství a domácí opravy', {'STA': 2, 'STR': 1}),
            ('Čtení a studium', {'SKO': 2, 'PRA': 1}),
            ('Vaření a pečení', {'OBC': 3}),
        ],
    ))

    # q36
    questions.append(_mc(
        'O jakých tématech rádi diskutujete?',
        [
            ('Politika a právo', {'PRA': 3}),
            ('Věda a výzkum', {'SKO': 2, 'ZDR': 1}),
            ('Business a investice', {'MAN': 3}),
            ('Ekologie a životní prostředí', {'ZEM': 3}),
            ('Umění, film a hudba', {'UME': 3}),
        ],
    ))

    # q37
    questions.append(_mc(
        'Které z těchto dovedností byste chtěli zlepšit?',
        [
            ('Komunikační a prezentační schopnosti', {'OBC': 2, 'SKO': 1}),
            ('Technické kreslení a CAD', {'STA': 2, 'STR': 1}),
            ('Cizí jazyky', {'DOP': 1, 'OBC': 1, 'SKO': 1}),
            ('Finanční gramotnost', {'MAN': 3}),
            ('Zdravověda a první pomoc', {'ZDR': 3}),
        ],
    ))

    # q38
    questions.append(_mc(
        'Jaké pracovní benefity jsou pro vás nejdůležitější?',
        [
            ('Služební auto nebo příspěvek na dopravu', {'DOP': 2, 'OBC': 1}),
            ('Vzdělávací kurzy a konference', {'SKO': 2, 'IT': 1}),
            ('Flexibilní pracovní doba a home office', {'IT': 2, 'MAN': 1}),
            ('Zdravotní a sportovní benefity', {'ZDR': 2, 'ZEM': 1}),
            ('Firemní akce a teambuildingy', {'OBC': 2, 'MAN': 1}),
        ],
    ))

    # q39
    questions.append(_mc(
        'Jaké nástroje nebo pomůcky rádi používáte?',
        [
            ('Notebook a programátorské nástroje', {'IT': 3}),
            ('Zachraňovací nůž, pila, sekyra', {'ZEM': 2, 'PRA': 1}),
            ('Měřicí přístroje a multimetr', {'STR': 3}),
            ('Kuchyňské náčiní a spotřebiče', {'OBC': 3}),
            ('Tužky, barvy a grafický tablet', {'UME': 3}),
        ],
    ))

    # q40
    questions.append(_mc(
        'Co vás přivádí do dobrého rozpoložení v práci?',
        [
            ('Vyřešení složitého technického problému', {'IT': 2, 'STR': 1}),
            ('Úspěšně dokončený obchod', {'OBC': 2, 'MAN': 1}),
            ('Uzdravení pacienta', {'ZDR': 3}),
            ('Předání znalostí studentům', {'SKO': 3}),
            ('Dokončení uměleckého díla', {'UME': 3}),
        ],
    ))

    # q41
    questions.append(_mc(
        'Jaký typ lidí obdivujete?',
        [
            ('Vynálezce a inovátory (Elon Musk, Nikola Tesla)', {'IT': 2, 'STR': 1}),
            ('Lékaře a humanitární pracovníky', {'ZDR': 3}),
            ('Umělce a hudebníky', {'UME': 3}),
            ('Soudce a bojovníky za spravedlnost', {'PRA': 3}),
            ('Podnikatele a vizionáře', {'MAN': 3}),
        ],
    ))

    # q42
    questions.append(_mc(
        'Které z těchto situací byste zvládli nejlépe?',
        [
            ('Řídit kamion na dálnici v noci', {'DOP': 3}),
            ('Vést poradu s 20 lidmi', {'MAN': 3}),
            ('Ošetřit zraněného člověka', {'ZDR': 3}),
            ('Opravit rozbitý motor', {'STR': 3}),
            ('Navrhnout reklamní kampaň', {'OBC': 2, 'UME': 1}),
        ],
    ))

    # q43
    questions.append(_mc(
        'Jakým způsobem se nejlépe učíte?',
        [
            ('Praktickými cvičeními a experimenty', {'STR': 2, 'ZDR': 1}),
            ('Čtením knih a článků', {'SKO': 2, 'PRA': 1}),
            ('Sledováním videí a tutoriálů', {'IT': 2, 'UME': 1}),
            ('Diskusí s ostatními', {'OBC': 2, 'SKO': 1}),
            ('Prací v terénu a pozorováním', {'ZEM': 2, 'DOP': 1}),
        ],
    ))

    # q44
    questions.append(_mc(
        'Které z těchto hodnot jsou pro vás nejdůležitější?',
        [
            ('Spravedlnost a dodržování pravidel', {'PRA': 3}),
            ('Inovace a pokrok', {'IT': 2, 'STR': 1}),
            ('Udržitelnost a ochrana přírody', {'ZEM': 3}),
            ('Solidarita a pomoc druhým', {'ZDR': 2, 'SKO': 1}),
            ('Svoboda a nezávislost', {'UME': 2, 'MAN': 1}),
        ],
    ))

    # q45
    questions.append(_mc(
        'Jaké typy projektů vás lákají?',
        [
            ('Stavba domu nebo rekonstrukce bytu', {'STA': 3}),
            ('Vývoj nové aplikace nebo webu', {'IT': 3}),
            ('Organizace festivalu nebo výstavy', {'UME': 2, 'OBC': 1}),
            ('Výzkumný projekt na univerzitě', {'SKO': 3}),
            ('Obchodní expanze firmy do zahraničí', {'MAN': 2, 'OBC': 1}),
        ],
    ))

    # q46
    questions.append(_mc(
        'Které problémy dnešní doby vás nejvíce trápí?',
        [
            ('Klimatická změna a znečištění', {'ZEM': 3}),
            ('Nerovnost a porušování lidských práv', {'PRA': 3}),
            ('Nedostatek lékařů a zdravotní péče', {'ZDR': 3}),
            ('Kybernetické hrozby a ochrana dat', {'IT': 3}),
            ('Kvalita vzdělávání', {'SKO': 3}),
        ],
    ))

    # q47
    questions.append(_mc(
        'Jaké aplikace nebo weby používáte nejčastěji?',
        [
            ('GitHub, Stack Overflow, VS Code', {'IT': 3}),
            ('AutoCAD, SketchUp nebo BIM nástroje', {'STA': 3}),
            ('Sociální sítě a e-shopy', {'OBC': 2, 'UME': 1}),
            ('Účetní a ERP systémy', {'MAN': 3}),
            ('Mapy, navigace a dopravní aplikace', {'DOP': 3}),
        ],
    ))

    # q48
    questions.append(_mc(
        'Jakou práci byste chtěli dělat o letních prázdninách?',
        [
            ('Brigáda na farmě nebo v lese', {'ZEM': 3}),
            ('Pomocný stavební dělník', {'STA': 2, 'STR': 1}),
            ('Číšník nebo prodavač', {'OBC': 3}),
            ('IT podpora nebo správce webu', {'IT': 3}),
            ('Animátor nebo vedoucí tábora', {'SKO': 2, 'UME': 1}),
        ],
    ))

    # ══════════════════════════════════════════
    #  TRUE / FALSE (20 otázek) – q49..q68
    # ══════════════════════════════════════════

    # q49
    questions.append(_tf(
        'Rád/a pracuji s počítačem a novými technologiemi.',
        {'IT': 3},
        {'ZEM': 1, 'STR': 1},
    ))

    # q50
    questions.append(_tf(
        'Nebojím se fyzicky náročné práce.',
        {'STA': 2, 'STR': 1, 'ZEM': 1},
        {'IT': 1, 'MAN': 1},
    ))

    # q51
    questions.append(_tf(
        'Umím dobře naslouchat druhým lidem a vcítit se do jejich situace.',
        {'ZDR': 2, 'SKO': 1},
        {'STR': 1, 'IT': 1},
    ))

    # q52
    questions.append(_tf(
        'Zajímám se o zákony a pravidla fungování společnosti.',
        {'PRA': 3},
        {'UME': 1, 'ZEM': 1},
    ))

    # q53
    questions.append(_tf(
        'Baví mě vymýšlet nové věci a tvořit něco originálního.',
        {'UME': 3},
        {'PRA': 1, 'DOP': 1},
    ))

    # q54
    questions.append(_tf(
        'Rád/a organizuji a plánuji činnosti pro sebe i ostatní.',
        {'MAN': 3},
        {'UME': 1, 'ZEM': 1},
    ))

    # q55
    questions.append(_tf(
        'Příroda a zvířata jsou mi blízké.',
        {'ZEM': 3},
        {'IT': 1, 'MAN': 1},
    ))

    # q56
    questions.append(_tf(
        'Dokážu zachovat klid i v krizových a nebezpečných situacích.',
        {'ZDR': 2, 'PRA': 1, 'DOP': 1},
        {'UME': 1},
    ))

    # q57
    questions.append(_tf(
        'Mám rád/a cestování a poznávání nových míst.',
        {'DOP': 2, 'OBC': 1},
        {'PRA': 1, 'STA': 1},
    ))

    # q58
    questions.append(_tf(
        'Jsem dobrý/á v matematice a logickém myšlení.',
        {'IT': 2, 'STR': 1, 'MAN': 1},
        {'UME': 1, 'OBC': 1},
    ))

    # q59
    questions.append(_tf(
        'Rád/a učím ostatní a vysvětluji jim nové věci.',
        {'SKO': 3},
        {'STR': 1, 'DOP': 1},
    ))

    # q60
    questions.append(_tf(
        'Zajímají mě finanční trhy a ekonomika.',
        {'MAN': 3},
        {'ZEM': 1, 'UME': 1},
    ))

    # q61
    questions.append(_tf(
        'Mám dobré vyjadřovací schopnosti – umím přesvědčit ostatní.',
        {'OBC': 2, 'PRA': 1},
        {'STR': 1, 'ZEM': 1},
    ))

    # q62
    questions.append(_tf(
        'Práce s nástroji a technickými zařízeními mi jde snadno.',
        {'STR': 3},
        {'SKO': 1, 'PRA': 1},
    ))

    # q63
    questions.append(_tf(
        'Jsem ochotný/á pracovat v noci, o víkendech nebo svátcích.',
        {'ZDR': 2, 'DOP': 1, 'PRA': 1},
        {'MAN': 1, 'SKO': 1},
    ))

    # q64
    questions.append(_tf(
        'Rád/a čtu odbornou literaturu a studuji nové poznatky.',
        {'SKO': 2, 'ZDR': 1},
        {'DOP': 1, 'OBC': 1},
    ))

    # q65
    questions.append(_tf(
        'Umím dobře kreslit, malovat nebo fotografovat.',
        {'UME': 3},
        {'STR': 1, 'DOP': 1},
    ))

    # q66
    questions.append(_tf(
        'Baví mě jednat s lidmi a prodávat produkty nebo služby.',
        {'OBC': 3},
        {'IT': 1, 'ZEM': 1},
    ))

    # q67
    questions.append(_tf(
        'Zajímá mě, jak fungují budovy – od základů po střechu.',
        {'STA': 3},
        {'UME': 1, 'SKO': 1},
    ))

    # q68
    questions.append(_tf(
        'Rád/a řídím – auto, motorku, loď nebo jiný dopravní prostředek.',
        {'DOP': 3},
        {'SKO': 1, 'UME': 1},
    ))

    # ══════════════════════════════════════════
    #  LIKERT (30 otázek) – q69..q98
    # ══════════════════════════════════════════

    # q69
    questions.append(_likert(
        'Jak moc vás zajímá práce s počítači a programování?',
        {1: {}, 2: {'IT': 1}, 3: {'IT': 2}, 4: {'IT': 3}, 5: {'IT': 4}},
    ))

    # q70
    questions.append(_likert(
        'Jak moc vás přitahuje práce v zdravotnictví?',
        {1: {}, 2: {'ZDR': 1}, 3: {'ZDR': 2}, 4: {'ZDR': 3}, 5: {'ZDR': 4}},
    ))

    # q71
    questions.append(_likert(
        'Jak moc vás baví práce s rostlinami a zvířaty?',
        {1: {}, 2: {'ZEM': 1}, 3: {'ZEM': 2}, 4: {'ZEM': 3}, 5: {'ZEM': 4}},
    ))

    # q72
    questions.append(_likert(
        'Jak silně toužíte po manažerské pozici?',
        {1: {}, 2: {'MAN': 1}, 3: {'MAN': 2}, 4: {'MAN': 3}, 5: {'MAN': 4}},
    ))

    # q73
    questions.append(_likert(
        'Jak moc vás zajímá stavebnictví a architektura?',
        {1: {}, 2: {'STA': 1}, 3: {'STA': 2}, 4: {'STA': 3}, 5: {'STA': 4}},
    ))

    # q74
    questions.append(_likert(
        'Jak moc vás přitahuje umělecká tvorba?',
        {1: {}, 2: {'UME': 1}, 3: {'UME': 2}, 4: {'UME': 3}, 5: {'UME': 4}},
    ))

    # q75
    questions.append(_likert(
        'Jak moc vás zajímá práce v oblasti práva a spravedlnosti?',
        {1: {}, 2: {'PRA': 1}, 3: {'PRA': 2}, 4: {'PRA': 3}, 5: {'PRA': 4}},
    ))

    # q76
    questions.append(_likert(
        'Jak moc vás baví obchodování a jednání s klienty?',
        {1: {}, 2: {'OBC': 1}, 3: {'OBC': 2}, 4: {'OBC': 3}, 5: {'OBC': 4}},
    ))

    # q77
    questions.append(_likert(
        'Jak moc vás zajímá strojírenství a práce s technikou?',
        {1: {}, 2: {'STR': 1}, 3: {'STR': 2}, 4: {'STR': 3}, 5: {'STR': 4}},
    ))

    # q78
    questions.append(_likert(
        'Jak moc vás přitahuje oblast dopravy a logistiky?',
        {1: {}, 2: {'DOP': 1}, 3: {'DOP': 2}, 4: {'DOP': 3}, 5: {'DOP': 4}},
    ))

    # q79
    questions.append(_likert(
        'Jak moc vás baví učení a předávání znalostí?',
        {1: {}, 2: {'SKO': 1}, 3: {'SKO': 2}, 4: {'SKO': 3}, 5: {'SKO': 4}},
    ))

    # q80
    questions.append(_likert(
        'Nakolik souhlasíte: „Chtěl/a bych pracovat venku v přírodě."',
        {1: {'IT': 1}, 2: {}, 3: {'ZEM': 1}, 4: {'ZEM': 2}, 5: {'ZEM': 3, 'DOP': 1}},
    ))

    # q81
    questions.append(_likert(
        'Nakolik souhlasíte: „Rád/a analyzuji data a hledám vzorce."',
        {1: {}, 2: {'MAN': 1}, 3: {'IT': 1, 'MAN': 1}, 4: {'IT': 2, 'MAN': 1}, 5: {'IT': 3, 'MAN': 2}},
    ))

    # q82
    questions.append(_likert(
        'Nakolik souhlasíte: „Chci pomáhat nemocným a zraněným."',
        {1: {}, 2: {'ZDR': 1}, 3: {'ZDR': 2}, 4: {'ZDR': 3}, 5: {'ZDR': 4}},
    ))

    # q83
    questions.append(_likert(
        'Nakolik souhlasíte: „Zajímá mě design a vizuální stránka věcí."',
        {1: {}, 2: {'UME': 1}, 3: {'UME': 1, 'STA': 1}, 4: {'UME': 2, 'STA': 1}, 5: {'UME': 3, 'STA': 1}},
    ))

    # q84
    questions.append(_likert(
        'Nakolik souhlasíte: „Rád/a řeším konflikty a vedu jednání."',
        {1: {}, 2: {'PRA': 1}, 3: {'PRA': 1, 'MAN': 1}, 4: {'PRA': 2, 'MAN': 1}, 5: {'PRA': 2, 'MAN': 2}},
    ))

    # q85
    questions.append(_likert(
        'Nakolik souhlasíte: „Dokážu dobře pracovat pod časovým tlakem."',
        {1: {}, 2: {'DOP': 1}, 3: {'ZDR': 1, 'DOP': 1}, 4: {'ZDR': 2, 'DOP': 1}, 5: {'ZDR': 2, 'DOP': 2, 'PRA': 1}},
    ))

    # q86
    questions.append(_likert(
        'Nakolik souhlasíte: „Zajímám se o ekonomiku a finanční řízení."',
        {1: {}, 2: {'MAN': 1}, 3: {'MAN': 2}, 4: {'MAN': 3}, 5: {'MAN': 4}},
    ))

    # q87
    questions.append(_likert(
        'Nakolik souhlasíte: „Baví mě experimentovat a zkoušet nové postupy."',
        {1: {}, 2: {'SKO': 1}, 3: {'IT': 1, 'STR': 1}, 4: {'IT': 2, 'STR': 1}, 5: {'IT': 2, 'STR': 2, 'SKO': 1}},
    ))

    # q88
    questions.append(_likert(
        'Nakolik souhlasíte: „Rád/a pracuji se dřevem, kovem nebo jinými materiály."',
        {1: {}, 2: {'STA': 1}, 3: {'STR': 1, 'STA': 1}, 4: {'STR': 2, 'STA': 1}, 5: {'STR': 3, 'STA': 2}},
    ))

    # q89
    questions.append(_likert(
        'Nakolik souhlasíte: „Chtěl/a bych vést vlastní firmu."',
        {1: {}, 2: {'MAN': 1}, 3: {'MAN': 2}, 4: {'MAN': 3, 'OBC': 1}, 5: {'MAN': 4, 'OBC': 1}},
    ))

    # q90
    questions.append(_likert(
        'Nakolik souhlasíte: „Bezpečnost a ochrana lidí je pro mě prioritou."',
        {1: {}, 2: {'PRA': 1}, 3: {'PRA': 2}, 4: {'PRA': 2, 'ZDR': 1}, 5: {'PRA': 3, 'ZDR': 2}},
    ))

    # q91
    questions.append(_likert(
        'Nakolik souhlasíte: „Rád/a cestuji a poznávám nová místa."',
        {1: {}, 2: {'DOP': 1}, 3: {'DOP': 2}, 4: {'DOP': 2, 'OBC': 1}, 5: {'DOP': 3, 'OBC': 2}},
    ))

    # q92
    questions.append(_likert(
        'Nakolik souhlasíte: „Rád/a vařím nebo peču pro ostatní."',
        {1: {}, 2: {'OBC': 1}, 3: {'OBC': 2}, 4: {'OBC': 3}, 5: {'OBC': 4}},
    ))

    # q93
    questions.append(_likert(
        'Nakolik souhlasíte: „Zajímá mě hudba, divadlo nebo film."',
        {1: {}, 2: {'UME': 1}, 3: {'UME': 2}, 4: {'UME': 3}, 5: {'UME': 4}},
    ))

    # q94
    questions.append(_likert(
        'Nakolik souhlasíte: „Rád/a čtu vědecké nebo odborné články."',
        {1: {}, 2: {'SKO': 1}, 3: {'SKO': 2}, 4: {'SKO': 2, 'ZDR': 1}, 5: {'SKO': 3, 'ZDR': 1}},
    ))

    # q95
    questions.append(_likert(
        'Nakolik souhlasíte: „Udržitelné zemědělství je důležité téma."',
        {1: {}, 2: {'ZEM': 1}, 3: {'ZEM': 2}, 4: {'ZEM': 3}, 5: {'ZEM': 4}},
    ))

    # q96
    questions.append(_likert(
        'Nakolik souhlasíte: „Rád/a navrhuji a konstruuji věci na papíře nebo v CADu."',
        {1: {}, 2: {'STA': 1}, 3: {'STA': 1, 'STR': 1}, 4: {'STA': 2, 'STR': 2}, 5: {'STA': 3, 'STR': 2}},
    ))

    # q97
    questions.append(_likert(
        'Nakolik souhlasíte: „Chtěl/a bych pracovat v mezinárodním prostředí."',
        {1: {}, 2: {'OBC': 1}, 3: {'MAN': 1, 'DOP': 1}, 4: {'MAN': 2, 'DOP': 1, 'OBC': 1}, 5: {'MAN': 2, 'DOP': 2, 'OBC': 1}},
    ))

    # q98
    questions.append(_likert(
        'Nakolik souhlasíte: „Chtěl/a bych pracovat s dětmi a mládeží."',
        {1: {}, 2: {'SKO': 1}, 3: {'SKO': 2}, 4: {'SKO': 3}, 5: {'SKO': 4}},
    ))

    # ══════════════════════════════════════════
    #  SHORT ANSWER (15 otázek) – q99..q113
    # ══════════════════════════════════════════

    # q99
    questions.append(_short(
        'Napište jedno povolání, které vás nejvíce zajímá.',
        [
            ('programátor', {'IT': 3}),
            ('vývojář', {'IT': 3}),
            ('lékař', {'ZDR': 3}),
            ('doktor', {'ZDR': 3}),
            ('architekt', {'STA': 3}),
            ('učitel', {'SKO': 3}),
            ('herec', {'UME': 3}),
            ('policista', {'PRA': 3}),
            ('podnikatel', {'MAN': 3}),
            ('kuchař', {'OBC': 3}),
            ('řidič', {'DOP': 3}),
            ('mechanik', {'STR': 3}),
            ('farmář', {'ZEM': 3}),
            ('zahradník', {'ZEM': 3}),
            ('manažer', {'MAN': 3}),
        ],
    ))

    # q100
    questions.append(_short(
        'Jaký je váš oblíbený předmět nebo obor? (jedno slovo)',
        [
            ('informatika', {'IT': 3}),
            ('matematika', {'IT': 2, 'STR': 1}),
            ('biologie', {'ZDR': 2, 'ZEM': 1}),
            ('chemie', {'ZDR': 2, 'ZEM': 1}),
            ('fyzika', {'STR': 3}),
            ('dějepis', {'PRA': 2, 'SKO': 1}),
            ('čeština', {'SKO': 2, 'UME': 1}),
            ('výtvarná', {'UME': 3}),
            ('hudební', {'UME': 3}),
            ('zeměpis', {'DOP': 2, 'ZEM': 1}),
            ('ekonomie', {'MAN': 3}),
            ('právo', {'PRA': 3}),
            ('sport', {'SKO': 1, 'ZDR': 1}),
        ],
    ))

    # q101
    questions.append(_short(
        'Kdybyste mohli změnit jednu věc na světě, co by to bylo?',
        [
            ('životní prostředí', {'ZEM': 3}),
            ('příroda', {'ZEM': 3}),
            ('ekologie', {'ZEM': 3}),
            ('zdraví', {'ZDR': 3}),
            ('nemoci', {'ZDR': 3}),
            ('vzdělání', {'SKO': 3}),
            ('chudoba', {'MAN': 2, 'OBC': 1}),
            ('nespravedlnost', {'PRA': 3}),
            ('korupce', {'PRA': 3}),
            ('technologie', {'IT': 3}),
            ('umění', {'UME': 3}),
        ],
    ))

    # q102
    questions.append(_short(
        'Jaký je váš koníček? (jedno slovo)',
        [
            ('programování', {'IT': 3}),
            ('zahradničení', {'ZEM': 3}),
            ('kreslení', {'UME': 3}),
            ('malování', {'UME': 3}),
            ('fotografie', {'UME': 3}),
            ('vaření', {'OBC': 3}),
            ('čtení', {'SKO': 2, 'PRA': 1}),
            ('sport', {'ZDR': 1, 'SKO': 1}),
            ('modelářství', {'STR': 2, 'STA': 1}),
            ('hudba', {'UME': 3}),
            ('cestování', {'DOP': 2, 'OBC': 1}),
            ('kutilství', {'STA': 2, 'STR': 1}),
            ('rybaření', {'ZEM': 3}),
            ('auta', {'DOP': 2, 'STR': 1}),
        ],
    ))

    # q103
    questions.append(_short(
        'Jakou superschopnost byste chtěli mít?',
        [
            ('léčení', {'ZDR': 3}),
            ('uzdravování', {'ZDR': 3}),
            ('neviditelnost', {'PRA': 2, 'IT': 1}),
            ('létání', {'DOP': 3}),
            ('teleportace', {'DOP': 3}),
            ('síla', {'STR': 2, 'STA': 1}),
            ('inteligence', {'IT': 2, 'SKO': 1}),
            ('telekineze', {'STR': 2}),
            ('kreativita', {'UME': 3}),
            ('ovládání času', {'MAN': 3}),
        ],
    ))

    # q104
    questions.append(_short(
        'Jaký typ firmy byste chtěli založit?',
        [
            ('technologická', {'IT': 3}),
            ('stavební', {'STA': 3}),
            ('restaurace', {'OBC': 3}),
            ('kavárna', {'OBC': 3}),
            ('farma', {'ZEM': 3}),
            ('škola', {'SKO': 3}),
            ('galerie', {'UME': 3}),
            ('advokátní', {'PRA': 3}),
            ('dopravní', {'DOP': 3}),
            ('poradenská', {'MAN': 3}),
            ('nemocnice', {'ZDR': 3}),
            ('dílna', {'STR': 3}),
        ],
    ))

    # q105
    questions.append(_short(
        'Jaké zvíře nejlépe vystihuje vaši povahu?',
        [
            ('lev', {'MAN': 3}),
            ('orel', {'DOP': 2, 'PRA': 1}),
            ('delfín', {'SKO': 2, 'ZDR': 1}),
            ('mravenec', {'STR': 2, 'STA': 1}),
            ('sova', {'SKO': 2, 'IT': 1}),
            ('liška', {'OBC': 3}),
            ('vlk', {'PRA': 2, 'ZEM': 1}),
            ('motýl', {'UME': 3}),
            ('včela', {'ZEM': 2, 'MAN': 1}),
            ('kočka', {'UME': 2, 'IT': 1}),
            ('pes', {'ZDR': 2, 'PRA': 1}),
        ],
    ))

    # q106
    questions.append(_short(
        'Který nástroj nebo přístroj byste chtěli ovládat na profesionální úrovni?',
        [
            ('počítač', {'IT': 3}),
            ('kamera', {'UME': 3}),
            ('mikroskop', {'ZDR': 2, 'SKO': 1}),
            ('soustruh', {'STR': 3}),
            ('traktor', {'ZEM': 3}),
            ('letadlo', {'DOP': 3}),
            ('jeřáb', {'STA': 3}),
            ('kytara', {'UME': 3}),
            ('skalpel', {'ZDR': 3}),
            ('kalkulačka', {'MAN': 2, 'IT': 1}),
        ],
    ))

    # q107
    questions.append(_short(
        'Kam byste se nejraději podívali na pracovní stáž? (město nebo země)',
        [
            ('japonsko', {'IT': 2, 'STR': 1}),
            ('tokio', {'IT': 2, 'STR': 1}),
            ('amerika', {'IT': 2, 'MAN': 1}),
            ('new york', {'MAN': 2, 'OBC': 1}),
            ('londýn', {'MAN': 2, 'PRA': 1}),
            ('paříž', {'UME': 3}),
            ('vídeň', {'UME': 2, 'SKO': 1}),
            ('berlín', {'STA': 2, 'UME': 1}),
            ('norsko', {'ZEM': 2, 'DOP': 1}),
            ('švýcarsko', {'ZDR': 2, 'MAN': 1}),
        ],
    ))

    # q108
    questions.append(_short(
        'Jakou hodnotu považujete v práci za nejdůležitější? (jedno slovo)',
        [
            ('spravedlnost', {'PRA': 3}),
            ('kreativita', {'UME': 3}),
            ('přesnost', {'STR': 2, 'IT': 1}),
            ('pečlivost', {'ZDR': 2, 'MAN': 1}),
            ('spolehlivost', {'DOP': 2, 'STA': 1}),
            ('trpělivost', {'SKO': 2, 'ZEM': 1}),
            ('odvaha', {'PRA': 2, 'ZDR': 1}),
            ('inovace', {'IT': 2, 'MAN': 1}),
            ('komunikace', {'OBC': 2, 'SKO': 1}),
            ('zodpovědnost', {'MAN': 2, 'ZDR': 1}),
        ],
    ))

    # q109
    questions.append(_short(
        'Co byste nejraději vynalezli?',
        [
            ('lék', {'ZDR': 3}),
            ('robot', {'STR': 2, 'IT': 1}),
            ('aplikace', {'IT': 3}),
            ('stroj', {'STR': 3}),
            ('materiál', {'STA': 2, 'STR': 1}),
            ('energii', {'STR': 2, 'ZEM': 1}),
            ('potravinu', {'ZEM': 2, 'OBC': 1}),
            ('hru', {'IT': 2, 'UME': 1}),
            ('umělé srdce', {'ZDR': 3}),
        ],
    ))

    # q110
    questions.append(_short(
        'Jaký typ problému řešíte nejraději? (jedno slovo)',
        [
            ('technický', {'STR': 2, 'IT': 1}),
            ('logický', {'IT': 3}),
            ('právní', {'PRA': 3}),
            ('zdravotní', {'ZDR': 3}),
            ('finanční', {'MAN': 3}),
            ('organizační', {'MAN': 2, 'DOP': 1}),
            ('kreativní', {'UME': 3}),
            ('lidský', {'SKO': 2, 'ZDR': 1}),
            ('přírodní', {'ZEM': 3}),
            ('stavební', {'STA': 3}),
        ],
    ))

    # q111
    questions.append(_short(
        'Jakou vlastnost obdivujete u svého vzoru?',
        [
            ('odvaha', {'PRA': 2, 'ZDR': 1}),
            ('inteligence', {'IT': 2, 'SKO': 1}),
            ('kreativita', {'UME': 3}),
            ('laskavost', {'ZDR': 2, 'SKO': 1}),
            ('cílevědomost', {'MAN': 3}),
            ('zručnost', {'STR': 2, 'STA': 1}),
            ('vytrvalost', {'ZEM': 2, 'DOP': 1}),
            ('charisma', {'OBC': 2, 'MAN': 1}),
            ('férovost', {'PRA': 3}),
        ],
    ))

    # q112
    questions.append(_short(
        'Kde se vidíte za 10 let? (stručně)',
        [
            ('vedení firmy', {'MAN': 3}),
            ('vlastní podnik', {'MAN': 3}),
            ('laboratoř', {'ZDR': 2, 'SKO': 1}),
            ('nemocnice', {'ZDR': 3}),
            ('škola', {'SKO': 3}),
            ('kancelář', {'PRA': 2, 'MAN': 1}),
            ('příroda', {'ZEM': 3}),
            ('ateliér', {'UME': 3}),
            ('zahraničí', {'DOP': 2, 'OBC': 1}),
            ('dílna', {'STR': 3}),
            ('stavba', {'STA': 3}),
        ],
    ))

    # q113
    questions.append(_short(
        'Jaký slogan by měla mít vaše vysněná firma?',
        [
            ('inovace', {'IT': 2, 'MAN': 1}),
            ('kvalita', {'STR': 2, 'MAN': 1}),
            ('zdraví', {'ZDR': 3}),
            ('příroda', {'ZEM': 3}),
            ('kreativita', {'UME': 3}),
            ('spolehlivost', {'DOP': 2, 'STA': 1}),
            ('vzdělání', {'SKO': 3}),
            ('spravedlnost', {'PRA': 3}),
            ('úspěch', {'MAN': 2, 'OBC': 1}),
            ('tradice', {'ZEM': 1, 'STA': 1, 'OBC': 1}),
        ],
    ))

    # ══════════════════════════════════════════
    #  MATCHING (12 otázek) – q114..q125
    # ══════════════════════════════════════════

    # q114
    questions.append(_match(
        'Přiřaďte nástroj k profesi:',
        [
            ('Stetoskop', 'Lékař', {'ZDR': 2}),
            ('Soustruh', 'Strojní obráběč', {'STR': 2}),
            ('Vodováha', 'Zedník', {'STA': 2}),
            ('Kompilátor', 'Programátor', {'IT': 2}),
        ],
    ))

    # q115
    questions.append(_match(
        'Přiřaďte pracovní prostředí k oboru:',
        [
            ('Pole a lesy', 'Zemědělství', {'ZEM': 2}),
            ('Soudní síň', 'Právo', {'PRA': 2}),
            ('Ateliér', 'Umění', {'UME': 2}),
            ('Sklad a terminál', 'Logistika', {'DOP': 2}),
        ],
    ))

    # q116
    questions.append(_match(
        'Přiřaďte školní předmět ke kariérní oblasti:',
        [
            ('Informatika', 'IT sektor', {'IT': 2}),
            ('Biologie', 'Zdravotnictví', {'ZDR': 2}),
            ('Ekonomie', 'Management', {'MAN': 2}),
            ('Výtvarná výchova', 'Umění', {'UME': 2}),
        ],
    ))

    # q117
    questions.append(_match(
        'Přiřaďte dovednost k profesi:',
        [
            ('Vyjednávání', 'Obchodní zástupce', {'OBC': 2}),
            ('Empatie', 'Učitel', {'SKO': 2}),
            ('Technické kreslení', 'Projektant', {'STA': 2}),
            ('Řízení vozidel', 'Řidič', {'DOP': 2}),
        ],
    ))

    # q118
    questions.append(_match(
        'Přiřaďte úkol k pracovní pozici:',
        [
            ('Osevní plán', 'Agronom', {'ZEM': 2}),
            ('Rozpočet stavby', 'Rozpočtář', {'STA': 2}),
            ('Audit účtů', 'Controller', {'MAN': 2}),
            ('Testování softwaru', 'Tester', {'IT': 2}),
        ],
    ))

    # q119
    questions.append(_match(
        'Přiřaďte vlastnost k oboru:',
        [
            ('Přesnost', 'Strojírenství', {'STR': 2}),
            ('Kreativita', 'Umění a kultura', {'UME': 2}),
            ('Empatie', 'Zdravotnictví', {'ZDR': 2}),
            ('Analytičnost', 'Informační technologie', {'IT': 2}),
        ],
    ))

    # q120
    questions.append(_match(
        'Přiřaďte produkt k odvětví:',
        [
            ('Operační systém', 'Informační technologie', {'IT': 2}),
            ('Rodinný dům', 'Stavebnictví', {'STA': 2}),
            ('Bioprodukty', 'Zemědělství', {'ZEM': 2}),
            ('Obchodní smlouva', 'Právo', {'PRA': 2}),
        ],
    ))

    # q121
    questions.append(_match(
        'Přiřaďte typ zákazníka k oboru:',
        [
            ('Pacient', 'Zdravotnictví', {'ZDR': 2}),
            ('Student', 'Školství', {'SKO': 2}),
            ('Turista', 'Obchod a služby', {'OBC': 2}),
            ('Investor', 'Management', {'MAN': 2}),
        ],
    ))

    # q122
    questions.append(_match(
        'Přiřaďte certifikaci k oboru:',
        [
            ('ISO 9001', 'Management kvality', {'MAN': 2}),
            ('Cisco CCNA', 'IT sítě', {'IT': 2}),
            ('Svářečský průkaz', 'Strojírenství', {'STR': 2}),
            ('Řidičák skupiny C', 'Doprava', {'DOP': 2}),
        ],
    ))

    # q123
    questions.append(_match(
        'Přiřaďte riziko k profesi:',
        [
            ('Pád z výšky', 'Stavbyvedoucí', {'STA': 2}),
            ('Infekce', 'Zdravotní sestra', {'ZDR': 2}),
            ('Kybernetický útok', 'Správce sítí', {'IT': 2}),
            ('Dopravní nehoda', 'Řidič', {'DOP': 2}),
        ],
    ))

    # q124
    questions.append(_match(
        'Přiřaďte symbol k oboru:',
        [
            ('⚖️', 'Právo', {'PRA': 2}),
            ('💻', 'IT', {'IT': 2}),
            ('🌾', 'Zemědělství', {'ZEM': 2}),
            ('🎨', 'Umění', {'UME': 2}),
        ],
    ))

    # q125
    questions.append(_match(
        'Přiřaďte cíl k profesi:',
        [
            ('Vyléčit pacienta', 'Lékař', {'ZDR': 2}),
            ('Dokončit stavbu', 'Stavbyvedoucí', {'STA': 2}),
            ('Zvýšit tržby', 'Obchodní zástupce', {'OBC': 2}),
            ('Naučit studenty', 'Učitel', {'SKO': 2}),
        ],
    ))

    # ══════════════════════════════════════════
    #  ORDERING (10 otázek) – q126..q135
    # ══════════════════════════════════════════

    # q126
    questions.append(_order(
        'Seřaďte tyto činnosti podle toho, jak vás přitahují (od nejvíce po nejméně):',
        [
            ('Navrhovat a programovat software', {'IT': 3}),
            ('Léčit a pomáhat nemocným', {'ZDR': 3}),
            ('Řídit tým a rozhodovat o strategii', {'MAN': 3}),
            ('Tvořit umělecká díla', {'UME': 3}),
        ],
    ))

    # q127
    questions.append(_order(
        'Seřaďte pracovní prostředí podle preference (od nejlepšího):',
        [
            ('Venku v přírodě', {'ZEM': 3}),
            ('V dílně nebo výrobní hale', {'STR': 3}),
            ('V kanceláři za počítačem', {'IT': 2, 'MAN': 1}),
            ('Na stavbě nebo u projekčního stolu', {'STA': 3}),
        ],
    ))

    # q128
    questions.append(_order(
        'Seřaďte typy úkolů podle oblíbenosti (od nejvíce):',
        [
            ('Jednání s klienty a obchodní schůzky', {'OBC': 3}),
            ('Výuka a přednášky', {'SKO': 3}),
            ('Analýza právních dokumentů', {'PRA': 3}),
            ('Plánování tras a přepravy', {'DOP': 3}),
        ],
    ))

    # q129
    questions.append(_order(
        'Seřaďte hodnoty podle důležitosti pro vaši kariéru:',
        [
            ('Vysoký plat', {'MAN': 2, 'IT': 1}),
            ('Pomoc druhým', {'ZDR': 2, 'SKO': 1}),
            ('Tvůrčí svoboda', {'UME': 3}),
            ('Jistota zaměstnání', {'PRA': 2, 'STA': 1}),
        ],
    ))

    # q130
    questions.append(_order(
        'Seřaďte dovednosti podle toho, které chcete rozvíjet nejvíce:',
        [
            ('Technické a řemeslné dovednosti', {'STR': 2, 'STA': 1}),
            ('Komunikace a prezentace', {'OBC': 2, 'SKO': 1}),
            ('Analytické myšlení a práce s daty', {'IT': 2, 'MAN': 1}),
            ('Kreativní a umělecké schopnosti', {'UME': 3}),
        ],
    ))

    # q131
    questions.append(_order(
        'Seřaďte pracovní aktivity podle preference:',
        [
            ('Práce s čísly a rozpočty', {'MAN': 3}),
            ('Práce s lidmi a komunikace', {'SKO': 2, 'OBC': 1}),
            ('Práce venku a fyzická aktivita', {'ZEM': 2, 'STA': 1}),
            ('Práce s technologiemi a stroji', {'STR': 2, 'IT': 1}),
        ],
    ))

    # q132
    questions.append(_order(
        'Seřaďte motivace podle důležitosti:',
        [
            ('Uznání a prestiž', {'PRA': 2, 'MAN': 1}),
            ('Smysluplnost – dělám něco užitečného', {'ZDR': 2, 'SKO': 1}),
            ('Dobrodružství a nové zážitky', {'DOP': 2, 'UME': 1}),
            ('Jistota a stabilní příjem', {'STA': 2, 'PRA': 1}),
        ],
    ))

    # q133
    questions.append(_order(
        'Seřaďte oblasti podle zájmu:',
        [
            ('Právo a spravedlnost', {'PRA': 3}),
            ('Zdraví a medicína', {'ZDR': 3}),
            ('Příroda a ekologie', {'ZEM': 3}),
            ('Technika a inženýrství', {'STR': 2, 'IT': 1}),
        ],
    ))

    # q134
    questions.append(_order(
        'Seřaďte typy odpovědnosti podle toho, co vám vyhovuje nejvíce:',
        [
            ('Za zdraví a bezpečnost lidí', {'ZDR': 2, 'PRA': 1}),
            ('Za finanční výsledky', {'MAN': 3}),
            ('Za kvalitu výrobku nebo stavby', {'STR': 2, 'STA': 1}),
            ('Za vzdělání a rozvoj ostatních', {'SKO': 3}),
        ],
    ))

    # q135
    questions.append(_order(
        'Seřaďte ideální pracovní den podle preference:',
        [
            ('Den na služební cestě za klientem', {'OBC': 2, 'DOP': 1}),
            ('Den plný schůzek a strategického plánování', {'MAN': 3}),
            ('Klidný den s knihami a výzkumem', {'SKO': 2, 'ZDR': 1}),
            ('Den v ateliéru s tvůrčí prací', {'UME': 3}),
        ],
    ))

    return questions
