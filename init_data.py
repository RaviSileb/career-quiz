"""
Inicializacni data – 11 kariernich kategorii a 150 otazek.
Kratke nazvy kategorii pouzivane v scores slovnicich:
  ZEM  = Zemedelstvi, lesnictvi a rybarstvi
  STA  = Stavebnictvi a architektura
  STR  = Strojirenstvi, vyroba a energetika
  DOP  = Doprava, logistika a spoje
  IT   = Informacni technologie a telekomunikace
  ZDR  = Zdravotnictvi a socialni pece
  OBC  = Obchod, cestovni ruch a gastronomie
  SKO  = Skolstvi, vychova a veda
  PRA  = Pravo, bezpecnost a verejna sprava
  MAN  = Management, administrativa a finance
  UME  = Umeni, kultura a remesla
"""

# Zkratky pro citelnost
ZEM = "Zemědělství, lesnictví a rybářství"
STA = "Stavebnictví a architektura"
STR = "Strojírenství, výroba a energetika"
DOP = "Doprava, logistika a spoje"
IT  = "IT a telekomunikace"
ZDR = "Zdravotnictví a sociální péče"
OBC = "Obchod, cestovní ruch a gastronomie"
SKO = "Školství, výchova a věda"
PRA = "Právo, bezpečnost a veřejná správa"
MAN = "Management, administrativa a finance"
UME = "Umění, kultura a řemesla"


def get_categories():
    return [
        {"name": ZEM, "description": "Práce s přírodními zdroji, rostlinami a zvířaty – pěstitel plodin, chovatel, lesník, rybář.", "icon": "🌾", "color": "#27ae60"},
        {"name": STA, "description": "Budování infrastruktury a domů – zedník, instalatér, architekt, stavbyvedoucí.", "icon": "🏗️", "color": "#e67e22"},
        {"name": STR, "description": "Průmyslová výroba a energie – CNC obráběč, svářeč, energetik, konstruktér.", "icon": "⚙️", "color": "#7f8c8d"},
        {"name": DOP, "description": "Pohyb osob, zboží a informací – řidič, strojvedoucí, pilot, logistik.", "icon": "🚛", "color": "#2980b9"},
        {"name": IT,  "description": "Digitální technologie – vývojář softwaru, správce sítí, datový specialista, AI.", "icon": "💻", "color": "#8e44ad"},
        {"name": ZDR, "description": "Fyzické a duševní zdraví – lékař, sestra, záchranář, farmaceut, sociální pracovník.", "icon": "🏥", "color": "#e74c3c"},
        {"name": OBC, "description": "Prodej a pohostinství – kuchař, číšník, průvodce, obchodní zástupce, realitní makléř.", "icon": "🛒", "color": "#f39c12"},
        {"name": SKO, "description": "Vzdělávání a výzkum – učitel, lektor, trenér, vědec, archeolog.", "icon": "📚", "color": "#16a085"},
        {"name": PRA, "description": "Stát, spravedlnost a ochrana – právník, policista, hasič, voják, úředník.", "icon": "⚖️", "color": "#2c3e50"},
        {"name": MAN, "description": "Řízení firem a ekonomika – manažer, účetní, daňový poradce, auditor.", "icon": "📊", "color": "#d35400"},
        {"name": UME, "description": "Kreativní a umělecké profese – designér, herec, hudebník, zlatník, restaurátor.", "icon": "🎨", "color": "#9b59b6"},
    ]


def get_questions():
    return [
        # ======================= BLOK 1: ZAJMY A VOLNY CAS (1-20) =======================
        {
            "text": "Co tě nejvíce baví ve volném čase?",
            "answers": [
                {"text": "Práce na zahradě, péče o zvířata", "scores": {ZEM: 3}},
                {"text": "Kutilství, opravování a stavění věcí", "scores": {STA: 2, STR: 1}},
                {"text": "Programování, hraní her na počítači", "scores": {IT: 3}},
                {"text": "Kreslení, malování nebo hraní na hudební nástroj", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Jaký typ knih nebo článků čteš nejraději?",
            "answers": [
                {"text": "O přírodě, zvířatech a ekologii", "scores": {ZEM: 3}},
                {"text": "Technické manuály, návody na opravy", "scores": {STR: 2, STA: 1}},
                {"text": "Detektivky, kriminálky, vojenské příběhy", "scores": {PRA: 3}},
                {"text": "Biografie podnikatelů a knihy o financích", "scores": {MAN: 3}},
            ]
        },
        {
            "text": "Jaký typ filmů nebo seriálů preferuješ?",
            "answers": [
                {"text": "Lékařské nebo zdravotnické seriály", "scores": {ZDR: 3}},
                {"text": "Kriminálky a soudní dramata", "scores": {PRA: 3}},
                {"text": "Dokumenty o cestování a gastronomii", "scores": {OBC: 3}},
                {"text": "Sci-fi o technologiích a budoucnosti", "scores": {IT: 2, STR: 1}},
            ]
        },
        {
            "text": "Kdybys mohl/a navštívit jakýkoli kurz zdarma, co by to bylo?",
            "answers": [
                {"text": "Kurz svářečských technik nebo CNC obrábění", "scores": {STR: 3}},
                {"text": "Kurz vaření nebo barmanství", "scores": {OBC: 3}},
                {"text": "Kurz grafického designu nebo fotografie", "scores": {UME: 3}},
                {"text": "Kurz první pomoci nebo zdravovědy", "scores": {ZDR: 3}},
            ]
        },
        {
            "text": "Co tě na internetu nejvíce fascinuje?",
            "answers": [
                {"text": "Jak fungují webové stránky a aplikace", "scores": {IT: 3}},
                {"text": "Online obchodování a marketing", "scores": {OBC: 2, MAN: 1}},
                {"text": "Vzdělávací videa a vědecké kanály", "scores": {SKO: 3}},
                {"text": "Umělecké a kreativní komunity", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Jaký typ společenské hry tě nejvíce baví?",
            "answers": [
                {"text": "Strategické hry (šachy, Settlers)", "scores": {MAN: 2, IT: 1}},
                {"text": "Kreativní hry (Dixit, Pictionary)", "scores": {UME: 3}},
                {"text": "Vědomostní kvízy a trivia", "scores": {SKO: 3}},
                {"text": "Kooperativní hry, kde se pomáhá druhým", "scores": {ZDR: 2, SKO: 1}},
            ]
        },
        {
            "text": "Co bys dělal/a, kdybys měl/a celý den absolutního volna?",
            "answers": [
                {"text": "Trávil/a čas venku – les, rybaření, zahrada", "scores": {ZEM: 3}},
                {"text": "Stavěl/a a opravoval/a věci doma", "scores": {STA: 3}},
                {"text": "Tvořil/a umění, hudbu nebo řemeslné výrobky", "scores": {UME: 3}},
                {"text": "Organizoval/a výlet nebo společnou akci", "scores": {OBC: 2, MAN: 1}},
            ]
        },
        {
            "text": "Jaký typ dobrovolnické práce tě přitahuje?",
            "answers": [
                {"text": "Učení dětí nebo doučování", "scores": {SKO: 3}},
                {"text": "Pomoc v nemocnici nebo domově seniorů", "scores": {ZDR: 3}},
                {"text": "Úklid přírody a sázení stromů", "scores": {ZEM: 3}},
                {"text": "Organizování charitativních sbírek", "scores": {MAN: 2, OBC: 1}},
            ]
        },
        {
            "text": "Jakou výstavu bys nejraději navštívil/a?",
            "answers": [
                {"text": "Technologický veletrh nebo hackathon", "scores": {IT: 3}},
                {"text": "Stavební a architektonický veletrh", "scores": {STA: 3}},
                {"text": "Galerii moderního umění a designu", "scores": {UME: 3}},
                {"text": "Autosalon nebo železniční muzeum", "scores": {DOP: 2, STR: 1}},
            ]
        },
        {
            "text": "Jaký typ soutěže by tě nejvíce lákal?",
            "answers": [
                {"text": "Programátorský hackathon", "scores": {IT: 3}},
                {"text": "Podnikatelský pitch (Shark Tank / Den D)", "scores": {MAN: 3}},
                {"text": "Soutěž mladých záchranářů nebo hasičů", "scores": {PRA: 2, ZDR: 1}},
                {"text": "Kuchařská soutěž (MasterChef)", "scores": {OBC: 3}},
            ]
        },
        {
            "text": "Jaký typ podcastu posloucháš nejraději?",
            "answers": [
                {"text": "O nových technologiích a startupu", "scores": {IT: 2, MAN: 1}},
                {"text": "True crime a forenzní případy", "scores": {PRA: 3}},
                {"text": "O zdraví, medicíně, psychologii", "scores": {ZDR: 3}},
                {"text": "O historii, vědě a objevech", "scores": {SKO: 3}},
            ]
        },
        {
            "text": "Kdybys měl/a blog, o čem by byl?",
            "answers": [
                {"text": "Recepty, cestování, recenze restaurací", "scores": {OBC: 3}},
                {"text": "DIY stavby, rekonstrukce, kutilství", "scores": {STA: 3}},
                {"text": "Osobní finance, investování", "scores": {MAN: 3}},
                {"text": "Příroda, zahradničení, farmářský život", "scores": {ZEM: 3}},
            ]
        },
        {
            "text": "Jaký sport nebo pohybovou aktivitu máš nejraději?",
            "answers": [
                {"text": "Turistiku, rybaření, práci venku", "scores": {ZEM: 2, DOP: 1}},
                {"text": "Týmové sporty (fotbal, hokej)", "scores": {PRA: 1, SKO: 1, DOP: 1}},
                {"text": "Tanec, gymnastiku, umělecké sporty", "scores": {UME: 3}},
                {"text": "Motokros, rally, karting", "scores": {DOP: 2, STR: 1}},
            ]
        },
        {
            "text": "Co bys rád/a vytvořil/a?",
            "answers": [
                {"text": "Mobilní aplikaci nebo webovou stránku", "scores": {IT: 3}},
                {"text": "Dům nebo nábytek vlastníma rukama", "scores": {STA: 2, STR: 1}},
                {"text": "Umělecké dílo – obraz, sochu, šperk", "scores": {UME: 3}},
                {"text": "Vzdělávací program nebo kurz", "scores": {SKO: 3}},
            ]
        },
        {
            "text": "Který kroužek by tě v mládí nejvíce bavil?",
            "answers": [
                {"text": "Modelářský nebo robotický kroužek", "scores": {STR: 2, IT: 1}},
                {"text": "Rybářský nebo myslivecký spolek", "scores": {ZEM: 3}},
                {"text": "Dramatický nebo výtvarný kroužek", "scores": {UME: 3}},
                {"text": "Mladí zdravotníci nebo první pomoc", "scores": {ZDR: 3}},
            ]
        },
        {
            "text": "Jaký typ YouTube kanálu sleduješ nejraději?",
            "answers": [
                {"text": "Opravy aut, strojů, jak na to", "scores": {STR: 2, DOP: 1}},
                {"text": "Záběry z kabin pilotů, strojvedoucích", "scores": {DOP: 3}},
                {"text": "Cooking show a food vlogy", "scores": {OBC: 3}},
                {"text": "Právní rozbory, policejní záběry", "scores": {PRA: 3}},
            ]
        },
        {
            "text": "Jaká prázdninová brigáda by tě bavila?",
            "answers": [
                {"text": "Farma – sklizeň, péče o zvířata", "scores": {ZEM: 3}},
                {"text": "Stavba – pomocné práce, zednické práce", "scores": {STA: 3}},
                {"text": "Hotel – recepce, obsluha, kuchyně", "scores": {OBC: 3}},
                {"text": "Kancelář – administrativa, účetnictví", "scores": {MAN: 3}},
            ]
        },
        {
            "text": "Co tě fascinuje při cestování?",
            "answers": [
                {"text": "Příroda, krajina, národní parky", "scores": {ZEM: 3}},
                {"text": "Architektura měst, mosty, stavby", "scores": {STA: 3}},
                {"text": "Místní jídla a kulturní tradice", "scores": {OBC: 2, UME: 1}},
                {"text": "Dopravní systémy – metro, vlaky, letiště", "scores": {DOP: 3}},
            ]
        },
        {
            "text": "Jak reaguješ, když se ti něco doma rozbije?",
            "answers": [
                {"text": "Opravím to sám/sama – manuálně", "scores": {STA: 2, STR: 1}},
                {"text": "Vyhledám návod na internetu a vyřeším to", "scores": {IT: 2}},
                {"text": "Zavolám odborníka, nemám na to nervy", "scores": {MAN: 1, OBC: 1}},
                {"text": "Zkusím kreativní improvizaci", "scores": {UME: 2, STR: 1}},
            ]
        },
        {
            "text": "Jaké prostředí tě nejvíce uklidňuje?",
            "answers": [
                {"text": "Les, louka, pole, rybník", "scores": {ZEM: 3}},
                {"text": "Dílna plná nástrojů a materiálu", "scores": {STR: 2, STA: 1}},
                {"text": "Útulná kavárna nebo knihovna", "scores": {SKO: 2, OBC: 1}},
                {"text": "Ateliér nebo hudební zkušebna", "scores": {UME: 3}},
            ]
        },

        # ======================= BLOK 2: PRACOVNI PREFERENCE (21-45) =======================
        {
            "text": "V jakém prostředí bys chtěl/a pracovat?",
            "answers": [
                {"text": "Venku v přírodě – pole, les, voda", "scores": {ZEM: 3}},
                {"text": "Na stavbě nebo v dílně", "scores": {STA: 2, STR: 1}},
                {"text": "V moderní kanceláři s počítači", "scores": {IT: 2, MAN: 1}},
                {"text": "V nemocnici, ordinaci nebo laboratoři", "scores": {ZDR: 3}},
            ]
        },
        {
            "text": "Jak velký pracovní tým je pro tebe ideální?",
            "answers": [
                {"text": "Pracuji nejlépe sám/sama", "scores": {IT: 2, UME: 1}},
                {"text": "Malý tým 3–5 lidí", "scores": {STR: 1, STA: 1, ZEM: 1}},
                {"text": "Střední tým 10–20 lidí", "scores": {MAN: 2, DOP: 1}},
                {"text": "Velký kolektiv, hodně interakce s lidmi", "scores": {ZDR: 1, OBC: 1, SKO: 1}},
            ]
        },
        {
            "text": "Co je pro tebe v práci nejdůležitější?",
            "answers": [
                {"text": "Tvořit rukama něco konkrétního", "scores": {STA: 2, STR: 1, UME: 1}},
                {"text": "Pomáhat lidem a mít pozitivní dopad", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Finanční ohodnocení a kariérní růst", "scores": {MAN: 3}},
                {"text": "Intelektuální výzvy a řešení problémů", "scores": {IT: 2, SKO: 1}},
            ]
        },
        {
            "text": "Jaký typ pracovních úkolů tě nejvíce baví?",
            "answers": [
                {"text": "Přesná manuální práce s nástroji/stroji", "scores": {STR: 2, STA: 1}},
                {"text": "Komunikace s klienty a vyjednávání", "scores": {OBC: 2, MAN: 1}},
                {"text": "Analýza dat a řešení logických problémů", "scores": {IT: 2, MAN: 1}},
                {"text": "Péče o lidi, zvířata nebo přírodu", "scores": {ZDR: 2, ZEM: 1}},
            ]
        },
        {
            "text": "Jak by vypadal tvůj ideální pracovní den?",
            "answers": [
                {"text": "Ráno nasednout za volant a na cestu", "scores": {DOP: 3}},
                {"text": "Učit nebo předávat znalosti", "scores": {SKO: 3}},
                {"text": "Řešit právní nebo bezpečnostní záležitosti", "scores": {PRA: 3}},
                {"text": "Vařit pro hosty a sledovat jejich radost", "scores": {OBC: 3}},
            ]
        },
        {
            "text": "Co tě na práci motivuje nejvíce?",
            "answers": [
                {"text": "Vidět hmatatelný výsledek práce", "scores": {STA: 2, STR: 1, ZEM: 1}},
                {"text": "Radost z tvořivosti a estetiky", "scores": {UME: 3}},
                {"text": "Vědomí, že chráním bezpečnost lidí", "scores": {PRA: 3}},
                {"text": "Radost z objevování nového poznání", "scores": {SKO: 3}},
            ]
        },
        {
            "text": "Kde bys chtěl/a geograficky pracovat?",
            "answers": [
                {"text": "Na venkově, v přírodě", "scores": {ZEM: 3}},
                {"text": "Odkudkoli – práce na dálku", "scores": {IT: 3}},
                {"text": "V terénu, na cestách, různá místa", "scores": {DOP: 2, OBC: 1}},
                {"text": "V nemocnici, škole nebo na úřadě", "scores": {ZDR: 1, SKO: 1, PRA: 1}},
            ]
        },
        {
            "text": "Jaký typ pracovního oblečení ti vyhovuje?",
            "answers": [
                {"text": "Pracovní montérky, rukavice, helma", "scores": {STA: 2, STR: 2}},
                {"text": "Zdravotnický plášť nebo uniforma", "scores": {ZDR: 2, PRA: 1}},
                {"text": "Pohodlné oblečení, třeba i teplákové", "scores": {IT: 2, UME: 1}},
                {"text": "Formální oblek nebo kostým", "scores": {MAN: 2, PRA: 1}},
            ]
        },
        {
            "text": "Jak se stavíš k práci ve směnách a o víkendech?",
            "answers": [
                {"text": "Nevadí – záchrana životů nečeká", "scores": {ZDR: 2, PRA: 1}},
                {"text": "Nevadí – pracuji, když je potřeba (sklizeň, sezóna)", "scores": {ZEM: 2, OBC: 1}},
                {"text": "Preferuji pravidelnou pracovní dobu", "scores": {MAN: 2, SKO: 1}},
                {"text": "Je mi to jedno, důležitá je svoboda", "scores": {IT: 2, UME: 1}},
            ]
        },
        {
            "text": "Jak reaguješ na rutinní, opakující se práci?",
            "answers": [
                {"text": "Nevadí mi, dává mi to klid a jistotu", "scores": {STR: 2, DOP: 1}},
                {"text": "Snažím se ji automatizovat nebo zefektivnit", "scores": {IT: 3}},
                {"text": "Nesnáším ji, potřebuji kreativitu", "scores": {UME: 3}},
                {"text": "Toleruji ji, pokud pomáhám lidem", "scores": {ZDR: 2, SKO: 1}},
            ]
        },
        {
            "text": "Jaký typ projektu by tě nejvíce bavil?",
            "answers": [
                {"text": "Stavba domu nebo rekonstrukce", "scores": {STA: 3}},
                {"text": "Organizace logistiky velkého eventu", "scores": {DOP: 2, MAN: 1}},
                {"text": "Vědecký výzkumný projekt", "scores": {SKO: 3}},
                {"text": "Natočení krátkého filmu nebo klipu", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Preferuješ práci s lidmi, nebo samostatnou práci?",
            "answers": [
                {"text": "Rozhodně s lidmi – učit, léčit, radit", "scores": {SKO: 2, ZDR: 1}},
                {"text": "Spíše samostatně u počítače nebo u stroje", "scores": {IT: 2, STR: 1}},
                {"text": "V tandemu – řidič + navigátor, chirurg + sestra", "scores": {DOP: 2, ZDR: 1}},
                {"text": "Záleží na projektu", "scores": {MAN: 1, OBC: 1}},
            ]
        },
        {
            "text": "Jak vnímáš práci pod časovým tlakem?",
            "answers": [
                {"text": "Motivuje mě – záchranáři, hasiči to znají", "scores": {ZDR: 2, PRA: 1}},
                {"text": "Zvládám – deadliny jsou běžná věc", "scores": {MAN: 2, IT: 1}},
                {"text": "Preferuji klidné tempo a kvalitu", "scores": {UME: 2, ZEM: 1}},
                {"text": "Jsem na to zvyklý/á – doprava nečeká", "scores": {DOP: 3}},
            ]
        },
        {
            "text": "Co je důležitější – stabilita, nebo dobrodružství?",
            "answers": [
                {"text": "Stabilita – státní služba, úřad", "scores": {PRA: 2, SKO: 1}},
                {"text": "Dobrodružství – terénní práce, cestování", "scores": {DOP: 2, ZEM: 1}},
                {"text": "Mix – stabilní základ, prostor pro inovace", "scores": {IT: 2, STR: 1}},
                {"text": "Úplná svoboda – podnikání", "scores": {MAN: 2, OBC: 1}},
            ]
        },
        {
            "text": "Jaký typ odpovědnosti tě přitahuje?",
            "answers": [
                {"text": "Odpovědnost za životy a zdraví lidí", "scores": {ZDR: 3}},
                {"text": "Odpovědnost za bezpečnost a pořádek", "scores": {PRA: 3}},
                {"text": "Odpovědnost za kvalitu a funkčnost výrobku", "scores": {STR: 2, STA: 1}},
                {"text": "Odpovědnost za finanční výsledky", "scores": {MAN: 3}},
            ]
        },
        {
            "text": "Jaká práce ti připadá nejsmysluplnější?",
            "answers": [
                {"text": "Pěstovat potraviny a starat se o přírodu", "scores": {ZEM: 3}},
                {"text": "Stavět domy, kde budou bydlet rodiny", "scores": {STA: 3}},
                {"text": "Léčit nemocné a zachraňovat životy", "scores": {ZDR: 3}},
                {"text": "Vzdělávat budoucí generace", "scores": {SKO: 3}},
            ]
        },
        {
            "text": "Jaký pracovní nástroj by byl tvůj nejlepší přítel?",
            "answers": [
                {"text": "Motorová pila nebo traktor", "scores": {ZEM: 3}},
                {"text": "Svářečka nebo soustruh", "scores": {STR: 3}},
                {"text": "Notebook s editorem kódu", "scores": {IT: 3}},
                {"text": "Stetoskop nebo laboratorní mikroskop", "scores": {ZDR: 2, SKO: 1}},
            ]
        },
        {
            "text": "Jak se stavíš k fyzicky náročné práci?",
            "answers": [
                {"text": "Mám rád/a fyzickou práci – stavba, zahrada", "scores": {STA: 2, ZEM: 2}},
                {"text": "Preferuji sedavou práci u počítače", "scores": {IT: 2, MAN: 1}},
                {"text": "Nemám problém, pokud to má smysl – záchranář", "scores": {PRA: 2, ZDR: 1}},
                {"text": "Mix – práce v terénu i v kanceláři", "scores": {DOP: 2, SKO: 1}},
            ]
        },
        {
            "text": "Pracoval/a bys rád/a s jídlem a nápoji?",
            "answers": [
                {"text": "Ano, příprava jídel mě baví", "scores": {OBC: 3}},
                {"text": "Spíše pěstování surovin – farma, vinice", "scores": {ZEM: 3}},
                {"text": "Ne, ale rád/a organizuji akce s občerstvením", "scores": {MAN: 2, OBC: 1}},
                {"text": "Jídlo mě moc nezajímá profesně", "scores": {IT: 1, STR: 1}},
            ]
        },
        {
            "text": "Co je pro tebe v práci nejhorší?",
            "answers": [
                {"text": "Sedět celý den zavřený/á uvnitř", "scores": {ZEM: 2, DOP: 1}},
                {"text": "Žádná kreativita, jen opakování", "scores": {UME: 3}},
                {"text": "Nespravedlnost a bezbrannost", "scores": {PRA: 3}},
                {"text": "Nemožnost vidět výsledky své práce", "scores": {STA: 2, STR: 1}},
            ]
        },
        {
            "text": "Jak vnímáš práci s technikou a stroji?",
            "answers": [
                {"text": "Miluji to – výrobní linky, CNC, roboty", "scores": {STR: 3}},
                {"text": "Baví mě řídit – auto, vlak, letadlo", "scores": {DOP: 3}},
                {"text": "Používám techniku jako nástroj (PC, mobil)", "scores": {IT: 2, MAN: 1}},
                {"text": "Preferuji práci rukama bez velkých strojů", "scores": {UME: 2, ZEM: 1}},
            ]
        },
        {
            "text": "Líbila by se ti práce v uniformě?",
            "answers": [
                {"text": "Ano – policista, hasič, voják", "scores": {PRA: 3}},
                {"text": "Ano – zdravotník, záchranář", "scores": {ZDR: 3}},
                {"text": "Spíše ne, chci se oblékat podle sebe", "scores": {UME: 2, IT: 1}},
                {"text": "Nevadí mi pracovní oděv na stavbě či v továrně", "scores": {STA: 2, STR: 1}},
            ]
        },
        {
            "text": "Bavilo by tě řídit velké vozidlo nebo stroj?",
            "answers": [
                {"text": "Ano – kamion, autobus, nákladní vlak", "scores": {DOP: 3}},
                {"text": "Ano – bagr, kombajn, harvestor", "scores": {STA: 1, ZEM: 2}},
                {"text": "Spíše bych řídil/a tým lidí", "scores": {MAN: 3}},
                {"text": "Ne, preferuji kreativní nebo intelektuální práci", "scores": {UME: 2, IT: 1}},
            ]
        },
        {
            "text": "Jak se stavíš k cestování za prací?",
            "answers": [
                {"text": "Rád/a – řidič, pilot, průvodce", "scores": {DOP: 2, OBC: 1}},
                {"text": "Občas ano – obchodní cestovatel", "scores": {OBC: 2, MAN: 1}},
                {"text": "Preferuji stálé pracoviště", "scores": {STR: 1, SKO: 1, PRA: 1}},
                {"text": "Z domova – remote práce", "scores": {IT: 3}},
            ]
        },

        # ======================= BLOK 3: DOVEDNOSTI A SCHOPNOSTI (46-70) =======================
        {
            "text": "V jakém školním předmětu vynikáš?",
            "answers": [
                {"text": "Matematika a informatika", "scores": {IT: 2, MAN: 1}},
                {"text": "Biologie a chemie", "scores": {ZDR: 2, ZEM: 1}},
                {"text": "Dějepis a občanská nauka", "scores": {PRA: 2, SKO: 1}},
                {"text": "Výtvarná výchova a pracovní činnosti", "scores": {UME: 2, STA: 1}},
            ]
        },
        {
            "text": "Jaká je tvá nejvýraznější dovednost?",
            "answers": [
                {"text": "Logické a analytické myšlení", "scores": {IT: 2, SKO: 1}},
                {"text": "Šikovné ruce a manuální zručnost", "scores": {STR: 2, STA: 1}},
                {"text": "Empatie a porozumění lidem", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Kreativita a představivost", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Jak přistupuješ k řešení složitých problémů?",
            "answers": [
                {"text": "Analyzuji data a hledám vzorce", "scores": {IT: 2, SKO: 1}},
                {"text": "Rozděluji problém na menší části – systematicky", "scores": {STR: 2, STA: 1}},
                {"text": "Hledám kreativní a neotřelá řešení", "scores": {UME: 2, OBC: 1}},
                {"text": "Konzultuji s ostatními a hledám konsenzus", "scores": {MAN: 2, PRA: 1}},
            ]
        },
        {
            "text": "Jak jsi na tom s technologiemi?",
            "answers": [
                {"text": "Jsem expert/ka – kód, sítě, databáze", "scores": {IT: 3}},
                {"text": "Ovládám řízení strojů a technických zařízení", "scores": {STR: 2, DOP: 1}},
                {"text": "Používám techniku jako nástroj, ale není to moje vášeň", "scores": {MAN: 2, SKO: 1}},
                {"text": "Preferuji práci bez technologií", "scores": {ZEM: 2, UME: 1}},
            ]
        },
        {
            "text": "Jak zvládáš matematiku a logické úlohy?",
            "answers": [
                {"text": "Výborně – je to moje silná stránka", "scores": {IT: 2, STR: 1}},
                {"text": "Baví mě aplikovaná matematika – rozpočty, kalkulace", "scores": {MAN: 2, STA: 1}},
                {"text": "Zvládám, ale nejsem nadšenec", "scores": {PRA: 1, DOP: 1}},
                {"text": "Mám raději jazyky a komunikaci", "scores": {OBC: 2, SKO: 1}},
            ]
        },
        {
            "text": "Jak hodnotíš své komunikační dovednosti?",
            "answers": [
                {"text": "Jsem skvělý/á řečník/řečnice", "scores": {SKO: 2, PRA: 1}},
                {"text": "Umím dobře naslouchat", "scores": {ZDR: 2, PRA: 1}},
                {"text": "Lépe se vyjadřuji písemně nebo v kódu", "scores": {IT: 2}},
                {"text": "Komunikuji nejlépe vizuálně – obrázky, design", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Jak zvládáš veřejné vystupování?",
            "answers": [
                {"text": "Miluji to – pedagog, lektor, trenér", "scores": {SKO: 3}},
                {"text": "Zvládám, když jsem připravený/á – právník, manažer", "scores": {PRA: 2, MAN: 1}},
                {"text": "Preferuji práci v zákulisí", "scores": {IT: 2, STR: 1}},
                {"text": "Komunikuji lépe v malých skupinkách", "scores": {ZDR: 2, OBC: 1}},
            ]
        },
        {
            "text": "Máš rád/a práci s detaily a přesností?",
            "answers": [
                {"text": "Ano – přesnost je klíčová (chirurgie, laborka)", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Ano – přesnost v číslech (účetnictví, finance)", "scores": {MAN: 3}},
                {"text": "Ano – přesnost ve výrobě (CNC, svařování)", "scores": {STR: 3}},
                {"text": "Ne, raději vidím celkový obraz", "scores": {OBC: 1, UME: 1, DOP: 1}},
            ]
        },
        {
            "text": "Jak jsi na tom s cizími jazyky?",
            "answers": [
                {"text": "Hovořím plynně – chci pracovat mezinárodně", "scores": {OBC: 2, MAN: 1}},
                {"text": "Angličtina pro IT nebo vědu mi stačí", "scores": {IT: 2, SKO: 1}},
                {"text": "Jazyky mě moc nebaví", "scores": {STR: 1, STA: 1, ZEM: 1}},
                {"text": "Rád/a se učím jazyky kvůli cestování a lidem", "scores": {OBC: 2, SKO: 1}},
            ]
        },
        {
            "text": "Máš zkušenosti s vedením lidí?",
            "answers": [
                {"text": "Ano, rád/a vedu týmy a projekty", "scores": {MAN: 3}},
                {"text": "Vedu jen v krizových situacích – záchranář, hasič", "scores": {PRA: 2, ZDR: 1}},
                {"text": "Raději se nechám vést, pracuji samostatně", "scores": {IT: 1, STR: 1, UME: 1}},
                {"text": "Vedu tím, že učím a inspiruji", "scores": {SKO: 3}},
            ]
        },
        {
            "text": "Jak pracuješ s daty a čísly?",
            "answers": [
                {"text": "Baví mě analyzovat data a hledat trendy", "scores": {IT: 2, MAN: 1}},
                {"text": "Pracuji s rozpočty a kalkulacemi", "scores": {MAN: 2, STA: 1}},
                {"text": "Data používám pro vědecký výzkum", "scores": {SKO: 3}},
                {"text": "Preferuji práci s lidmi než s čísly", "scores": {ZDR: 2, OBC: 1}},
            ]
        },
        {
            "text": "Jak jsi na tom s prostorovou představivostí?",
            "answers": [
                {"text": "Výborně – navrhuji budovy, konstrukce", "scores": {STA: 3}},
                {"text": "Dobře – 3D modelování, CAD, design", "scores": {STR: 2, UME: 1}},
                {"text": "Průměrně – stačí mi plánování tras a logistiky", "scores": {DOP: 2}},
                {"text": "Není moje silná stránka", "scores": {SKO: 1, PRA: 1}},
            ]
        },
        {
            "text": "Umíš dobře organizovat čas a priority?",
            "answers": [
                {"text": "Ano – projektové řízení je můj obor", "scores": {MAN: 3}},
                {"text": "Ano – v dopravě je čas klíčový", "scores": {DOP: 3}},
                {"text": "Snažím se, ale kreativita nesnáší řízení", "scores": {UME: 2}},
                {"text": "Organizuji hlavně práci jiných – učitel, vedoucí", "scores": {SKO: 2, MAN: 1}},
            ]
        },
        {
            "text": "Jak zvládáš stresové situace?",
            "answers": [
                {"text": "Pod stresem jsem nejefektivnější – záchranář", "scores": {ZDR: 2, PRA: 1}},
                {"text": "Stress si nepřipouštím, pracuji v klidu – farma, les", "scores": {ZEM: 3}},
                {"text": "Promyslím strategii – manažerský přístup", "scores": {MAN: 2, IT: 1}},
                {"text": "Vyjadřuji stres tvorbou – umění, musik", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Jak se učíš nové věci nejlépe?",
            "answers": [
                {"text": "Praktickým zkoušením – dílna, laboratoř", "scores": {STR: 2, ZDR: 1}},
                {"text": "Studiem teorie – knihy, dokumenty", "scores": {SKO: 2, PRA: 1}},
                {"text": "Sledováním tutoriálů online", "scores": {IT: 2, UME: 1}},
                {"text": "Diskuzí s ostatními a výměnou zkušeností", "scores": {OBC: 2, MAN: 1}},
            ]
        },
        {
            "text": "Jak jsi na tom s přesností a pečlivostí?",
            "answers": [
                {"text": "Jsem perfekcionista – každý detail musí sedět", "scores": {STR: 2, ZDR: 1}},
                {"text": "Pečlivost v dokumentech a právních textech", "scores": {PRA: 2, MAN: 1}},
                {"text": "Pečlivost v estetice – symetrie, barvy, kompozice", "scores": {UME: 3}},
                {"text": "Důležitý je výsledek, ne proces", "scores": {OBC: 1, DOP: 1, MAN: 1}},
            ]
        },
        {
            "text": "Jak zvládáš práci s živými organismy?",
            "answers": [
                {"text": "Skvěle – zvířata a rostliny jsou moje vášeň", "scores": {ZEM: 3}},
                {"text": "Dobře – pacienti jsou živé bytosti", "scores": {ZDR: 3}},
                {"text": "Preferuji práci s neživými materiály a stroji", "scores": {STR: 2, STA: 1}},
                {"text": "Pracuji raději s daty a informacemi", "scores": {IT: 2, MAN: 1}},
            ]
        },
        {
            "text": "Máš zkušenosti s řízením vozidel?",
            "answers": [
                {"text": "Ano, řízení je moje vášeň – chci profesní ŘP", "scores": {DOP: 3}},
                {"text": "Ano, ale jen jako dopravu do práce", "scores": {MAN: 1, OBC: 1}},
                {"text": "Řídím traktory nebo zemědělské stroje", "scores": {ZEM: 3}},
                {"text": "Neřídím, ale rád/a si nechám svézt", "scores": {IT: 1, UME: 1}},
            ]
        },
        {
            "text": "Umíš pracovat s elektřinou a elektronikou?",
            "answers": [
                {"text": "Ano – elektrikář, elektronik, energetik", "scores": {STR: 3}},
                {"text": "Ano – programuji hardware, IoT, roboty", "scores": {IT: 3}},
                {"text": "Základy zvládám, ale není to můj obor", "scores": {STA: 1, DOP: 1}},
                {"text": "Raději se držím od elektřiny dál", "scores": {ZEM: 1, UME: 1, OBC: 1}},
            ]
        },

        # ======================= BLOK 4: HODNOTY A MOTIVACE (71-95) =======================
        {
            "text": "Co je pro tebe v životě nejdůležitější?",
            "answers": [
                {"text": "Poznání a neustálé učení se", "scores": {SKO: 3}},
                {"text": "Bezpečnost rodiny a komunity", "scores": {PRA: 2, ZDR: 1}},
                {"text": "Finanční nezávislost a úspěch", "scores": {MAN: 3}},
                {"text": "Svoboda a sebevyjádření", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Jaký přínos chceš mít pro společnost?",
            "answers": [
                {"text": "Zásobovat lidi jídlem a starat se o krajinu", "scores": {ZEM: 3}},
                {"text": "Stavět a udržovat infrastrukturu", "scores": {STA: 3}},
                {"text": "Chránit práva a bezpečnost občanů", "scores": {PRA: 3}},
                {"text": "Inovovat a rozvíjet technologie", "scores": {IT: 2, STR: 1}},
            ]
        },
        {
            "text": "Co tě nejvíce trápí na současném světě?",
            "answers": [
                {"text": "Ničení přírody a klimatická změna", "scores": {ZEM: 3}},
                {"text": "Nemoci a nedostatek zdravotní péče", "scores": {ZDR: 3}},
                {"text": "Nespravedlnost, kriminalita, korupce", "scores": {PRA: 3}},
                {"text": "Nedostatek kvalitního vzdělání", "scores": {SKO: 3}},
            ]
        },
        {
            "text": "Jaký typ úspěchu je pro tebe nejcennější?",
            "answers": [
                {"text": "Vytvoření něčeho hmatatelného – budova, stroj, produkt", "scores": {STA: 2, STR: 2}},
                {"text": "Vyléčení pacienta nebo záchrana života", "scores": {ZDR: 3}},
                {"text": "Úspěšný podnikatelský projekt", "scores": {MAN: 2, OBC: 1}},
                {"text": "Ocenění za umělecké dílo", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Jak vnímáš autoritu a pravidla?",
            "answers": [
                {"text": "Jsou základem – zákon je zákon", "scores": {PRA: 3}},
                {"text": "Respektuji je, ale hledám prostor pro inovace", "scores": {IT: 2, STR: 1}},
                {"text": "Omezují kreativitu – tvůrce potřebuje svobodu", "scores": {UME: 3}},
                {"text": "Dodržuji bezpečnostní předpisy – ochrana zdraví", "scores": {ZDR: 2, STA: 1}},
            ]
        },
        {
            "text": "Jaký je tvůj postoj k riziku?",
            "answers": [
                {"text": "Podstupuji ho denně – hasič, policista, záchranář", "scores": {PRA: 2, ZDR: 1}},
                {"text": "Kalkuluji rizika – podnikatel, investor", "scores": {MAN: 3}},
                {"text": "Preferuji jistotu – úředník, učitel", "scores": {PRA: 1, SKO: 2}},
                {"text": "Riskuji v tvorbě – experimentuji s uměním", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Co tě nejvíce inspiruje?",
            "answers": [
                {"text": "Příroda, krajina a zvířata", "scores": {ZEM: 3}},
                {"text": "Technologické inovace a vynálezy", "scores": {IT: 2, STR: 1}},
                {"text": "Příběhy lidí, kteří pomáhají druhým", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Umělecká díla, hudba, filmy", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Jaký odkaz chceš po sobě zanechat?",
            "answers": [
                {"text": "Zdravou krajinu a prosperující farmu", "scores": {ZEM: 3}},
                {"text": "Stavby, které přetrvají generace", "scores": {STA: 3}},
                {"text": "Technologický pokrok", "scores": {IT: 2, STR: 1}},
                {"text": "Umělecké dílo nebo vzdělané žáky", "scores": {UME: 2, SKO: 1}},
            ]
        },
        {
            "text": "Jak se stavíš k penězům a financím?",
            "answers": [
                {"text": "Finance jsou můj obor – účetnictví, audit", "scores": {MAN: 3}},
                {"text": "Potřebuji je, ale nejsou priorita – pomáhat lidem", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Investuji a podnikám", "scores": {MAN: 2, OBC: 1}},
                {"text": "Peníze mě nezajímají tolik jako tvorba", "scores": {UME: 2, ZEM: 1}},
            ]
        },
        {
            "text": "Jaký typ spravedlnosti je ti blízký?",
            "answers": [
                {"text": "Trestní – pachatel musí být potrestán", "scores": {PRA: 3}},
                {"text": "Sociální – každý zaslouží rovné šance", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Tržní – kdo pracuje, ten má", "scores": {MAN: 2, OBC: 1}},
                {"text": "Ekologická – příroda potřebuje ochranu", "scores": {ZEM: 3}},
            ]
        },
        {
            "text": "Jak vnímáš technologický pokrok?",
            "answers": [
                {"text": "Fascinuje mě – AI, roboty, automatizace", "scores": {IT: 3}},
                {"text": "Užitečný v medicíně a výrobě", "scores": {ZDR: 1, STR: 2}},
                {"text": "Měl by respektovat přírodu", "scores": {ZEM: 2, STA: 1}},
                {"text": "Hrozba pro tradiční řemesla a umění", "scores": {UME: 2, OBC: 1}},
            ]
        },
        {
            "text": "Co si ceníš na lidech nejvíce?",
            "answers": [
                {"text": "Odvahu a rozhodnost", "scores": {PRA: 2, DOP: 1}},
                {"text": "Laskavost a empatii", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Pracovitost a spolehlivost", "scores": {STA: 1, STR: 1, ZEM: 1}},
                {"text": "Kreativitu a originalitu", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Jak se díváš na ekologii a ochranu přírody?",
            "answers": [
                {"text": "Je to moje životní mise – lesník, ekolog", "scores": {ZEM: 3}},
                {"text": "Důležitá – udržitelné stavebnictví a energetika", "scores": {STA: 1, STR: 2}},
                {"text": "Řešení leží v technologiích – zelené IT, IoT", "scores": {IT: 3}},
                {"text": "Musíme vzdělávat lidi o ekologii", "scores": {SKO: 3}},
            ]
        },
        {
            "text": "Jak vnímáš práci ve veřejné správě?",
            "answers": [
                {"text": "Chci sloužit státu – policie, armáda, úřad", "scores": {PRA: 3}},
                {"text": "Zajímá mě jen jako regulátor byznysu", "scores": {MAN: 2}},
                {"text": "V školství – státní školy a výzkum", "scores": {SKO: 3}},
                {"text": "Ve zdravotnictví – státní nemocnice", "scores": {ZDR: 3}},
            ]
        },
        {
            "text": "Jak vnímáš práci s lidmi v obtížných situacích?",
            "answers": [
                {"text": "Zvládám to – sociální pracovník, terapeut", "scores": {ZDR: 3}},
                {"text": "Zvládám to – policista, záchranář", "scores": {PRA: 3}},
                {"text": "Raději pracuji s materiálem nebo technikou", "scores": {STR: 2, STA: 1}},
                {"text": "Pomáhám jinak – vaření, ubytování, obchod", "scores": {OBC: 3}},
            ]
        },
        {
            "text": "Jaký vztah máš k tradičním řemeslům?",
            "answers": [
                {"text": "Fascinují mě – chci je zachovat (kovář, zlatník)", "scores": {UME: 3}},
                {"text": "Respektuji je, ale preferuji moderní výrobu", "scores": {STR: 2}},
                {"text": "Některá řemesla ve stavebnictví mě baví", "scores": {STA: 3}},
                {"text": "Řemesla nahradí technologie", "scores": {IT: 2, MAN: 1}},
            ]
        },
        {
            "text": "Jak vnímáš obchod a prodej?",
            "answers": [
                {"text": "Baví mě jednat s lidmi a prodávat", "scores": {OBC: 3}},
                {"text": "Zajímá mě strategický marketing a management", "scores": {MAN: 3}},
                {"text": "Prodávám to, co sám/sama vytvořím", "scores": {UME: 2, ZEM: 1}},
                {"text": "Obchod mě nezajímá – chci tvořit nebo pomáhat", "scores": {ZDR: 1, STR: 1, SKO: 1}},
            ]
        },
        {
            "text": "Jak vnímáš potřebu celoživotního vzdělávání?",
            "answers": [
                {"text": "Nutnost – v IT se vše mění každý rok", "scores": {IT: 3}},
                {"text": "Nutnost – medicína a právo se neustále vyvíjejí", "scores": {ZDR: 2, PRA: 1}},
                {"text": "Vzdělávám se sám/sama v řemesle praxí", "scores": {STA: 2, STR: 1}},
                {"text": "Vzdělávání je moje práce – učitel, vědec", "scores": {SKO: 3}},
            ]
        },
        {
            "text": "Jak vnímáš mezinárodní spolupráci?",
            "answers": [
                {"text": "Důležitá – globální obchod a cestovní ruch", "scores": {OBC: 2, MAN: 1}},
                {"text": "Důležitá – mezinárodní výzkum a věda", "scores": {SKO: 3}},
                {"text": "Důležitá – mezinárodní doprava a logistika", "scores": {DOP: 3}},
                {"text": "Důležitá – globální umělecká scéna", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Co je pro tebe důležitější – jistota, nebo vášeň?",
            "answers": [
                {"text": "Jistota – stabilní zaměstnání a plat", "scores": {PRA: 2, MAN: 1}},
                {"text": "Vášeň – dělat to, co miluji", "scores": {UME: 2, ZEM: 1}},
                {"text": "Rovnováha – dobrý plat a smysluplná práce", "scores": {IT: 2, ZDR: 1}},
                {"text": "Jistota zázemí + vášeň v práci s lidmi", "scores": {SKO: 2, OBC: 1}},
            ]
        },

        # ======================= BLOK 5: OSOBNOSTNI RYSY (96-120) =======================
        {
            "text": "Jak bys popsal/a svou osobnost jedním slovem?",
            "answers": [
                {"text": "Analytický/á", "scores": {IT: 2, MAN: 1}},
                {"text": "Empatický/á", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Praktický/á", "scores": {STA: 2, STR: 1}},
                {"text": "Kreativní", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Jsi spíše introvert, nebo extrovert?",
            "answers": [
                {"text": "Introvert – pracuji sám/sama u počítače/stroje", "scores": {IT: 2, STR: 1}},
                {"text": "Spíše introvert – příroda a klid", "scores": {ZEM: 2, UME: 1}},
                {"text": "Spíše extrovert – rád/a mezi lidmi", "scores": {OBC: 2, SKO: 1}},
                {"text": "Extrovert – lidi mi dodávají energii", "scores": {ZDR: 1, PRA: 1, MAN: 1}},
            ]
        },
        {
            "text": "Jak řešíš konflikty?",
            "answers": [
                {"text": "Argumentuji fakty a logikou", "scores": {PRA: 2, IT: 1}},
                {"text": "Snažím se pochopit druhou stranu", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Hledám kompromis a oboustranně výhodné řešení", "scores": {MAN: 2, OBC: 1}},
                {"text": "Radši se vyrovnám fyzickou činností", "scores": {STA: 1, STR: 1, ZEM: 1}},
            ]
        },
        {
            "text": "Jak se rozhoduješ?",
            "answers": [
                {"text": "Na základě dat a analýzy", "scores": {IT: 2, MAN: 1}},
                {"text": "Na základě zkušeností a praxe", "scores": {STR: 2, STA: 1}},
                {"text": "Na základě citu a empatie", "scores": {ZDR: 2, UME: 1}},
                {"text": "Zvažuji pravidla a precedenty", "scores": {PRA: 3}},
            ]
        },
        {
            "text": "Jak reaguješ na konstruktivní kritiku?",
            "answers": [
                {"text": "Vítám ji – pomáhá mi profesně růst", "scores": {SKO: 2, MAN: 1}},
                {"text": "Hodnotím ji racionálně a opravím chybu", "scores": {IT: 2, STR: 1}},
                {"text": "Potřebuji čas na zpracování – jsem citlivý/á", "scores": {UME: 2, ZDR: 1}},
                {"text": "Motivuje mě to k větší snaze", "scores": {DOP: 1, OBC: 1, STA: 1}},
            ]
        },
        {
            "text": "Jaký jsi vedoucí nebo lídr?",
            "answers": [
                {"text": "Vizionář – inspiruji ostatní strategií", "scores": {MAN: 3}},
                {"text": "Expert – vedu příkladem a znalostmi", "scores": {IT: 2, SKO: 1}},
                {"text": "Organizátor – plánuji a koordinuji", "scores": {DOP: 2, STA: 1}},
                {"text": "Ochránce – starám se o tým a bezpečnost", "scores": {PRA: 2, ZDR: 1}},
            ]
        },
        {
            "text": "Co děláš, když se ti něco nepovede?",
            "answers": [
                {"text": "Analyzuji chybu a učím se z ní", "scores": {IT: 2, SKO: 1}},
                {"text": "Zkouším to znovu jinými nástroji a technikami", "scores": {STR: 2, STA: 1}},
                {"text": "Přijmu to s klidem – v přírodě se něco vždy nepovede", "scores": {ZEM: 3}},
                {"text": "Požádám o pomoc a radu", "scores": {ZDR: 1, OBC: 1, MAN: 1}},
            ]
        },
        {
            "text": "Jak se stavíš k soutěživosti?",
            "answers": [
                {"text": "Jsem velmi soutěživý/á – chci vyhrát", "scores": {MAN: 2, OBC: 1}},
                {"text": "Soutěžím sám/sama se sebou – zlepšuji se", "scores": {UME: 2, IT: 1}},
                {"text": "Preferuji spolupráci", "scores": {SKO: 2, ZDR: 1}},
                {"text": "Soutěžím fair play – pravidla jsou pravidla", "scores": {PRA: 2, DOP: 1}},
            ]
        },
        {
            "text": "Jak vnímáš hierarchii v práci?",
            "answers": [
                {"text": "Důležitá – armáda, policie, hasiči ji potřebují", "scores": {PRA: 3}},
                {"text": "Potřebná – na stavbě musí být stavbyvedoucí", "scores": {STA: 2, STR: 1}},
                {"text": "Preferuji ploché struktury – startup, IT tým", "scores": {IT: 2, MAN: 1}},
                {"text": "Nezajímá mě – pracuji sám/sama", "scores": {UME: 2, ZEM: 1}},
            ]
        },
        {
            "text": "Jak zvládáš noční směny?",
            "answers": [
                {"text": "Zvládám – je to součást záchranářské práce", "scores": {ZDR: 2, PRA: 1}},
                {"text": "Zvládám – v dopravě se jezdí nonstop", "scores": {DOP: 3}},
                {"text": "Raději pracuji přes den", "scores": {MAN: 1, SKO: 1, STA: 1}},
                {"text": "Tvořím nejlépe v noci – umělec, programátor", "scores": {UME: 2, IT: 1}},
            ]
        },
        {
            "text": "Jak se stavíš k zodpovědnosti za druhé lidi?",
            "answers": [
                {"text": "Přijímám ji – vedu tým, firmu", "scores": {MAN: 3}},
                {"text": "Přijímám ji – životy pacientů závisí na mně", "scores": {ZDR: 3}},
                {"text": "Přijímám ji – bezpečnost cestujících je moje povinnost", "scores": {DOP: 3}},
                {"text": "Raději odpovídám za sebe a svou práci", "scores": {UME: 2, IT: 1}},
            ]
        },
        {
            "text": "Jak vnímáš tradice a zvyky?",
            "answers": [
                {"text": "Respektuji a udržuji – tradiční řemesla, folklór", "scores": {UME: 2, ZEM: 1}},
                {"text": "Respektuji, ale modernizuji – stavební postupy", "scores": {STA: 2, STR: 1}},
                {"text": "Využívám to v obchodu – regionální produkty", "scores": {OBC: 3}},
                {"text": "Inovace jsou důležitější než tradice", "scores": {IT: 2, MAN: 1}},
            ]
        },
        {
            "text": "Jak reaguješ na nečekané události?",
            "answers": [
                {"text": "Rychle a rozhodně – trénink v bezpečnosti", "scores": {PRA: 2, ZDR: 1}},
                {"text": "Analyticky – hledám příčinu a řešení", "scores": {IT: 2, STR: 1}},
                {"text": "Flexibilně – v dopravě se plány mění stále", "scores": {DOP: 3}},
                {"text": "Kreativně – improvizuji", "scores": {UME: 2, OBC: 1}},
            ]
        },
        {
            "text": "Jaký typ fyzické kondice je ti blízký?",
            "answers": [
                {"text": "Síla a vytrvalost – stavba, hasičský sport", "scores": {STA: 2, PRA: 1}},
                {"text": "Obratnost a koordinace – řemeslo, chirurgie", "scores": {UME: 1, ZDR: 2}},
                {"text": "Dlouhé sezení mi nevadí – kancelář, kabina", "scores": {MAN: 1, DOP: 1, IT: 1}},
                {"text": "Pohyb venku – farma, les, turistika", "scores": {ZEM: 3}},
            ]
        },
        {
            "text": "Jak zvládáš monotónní a opakující se úkoly?",
            "answers": [
                {"text": "Nevadí mi – výrobní linka, CNC", "scores": {STR: 3}},
                {"text": "Nevadí mi – řízení na dlouhých trasách", "scores": {DOP: 3}},
                {"text": "Vadí mi – potřebuji rozmanitost", "scores": {UME: 2, SKO: 1}},
                {"text": "Automatizuji je – naprogramuji to", "scores": {IT: 3}},
            ]
        },
        {
            "text": "Jak vnímáš administrativu a papírování?",
            "answers": [
                {"text": "Baví mě to – smlouvy, dokumenty, fakturace", "scores": {MAN: 3}},
                {"text": "Zvládám – úřednická práce je potřebná", "scores": {PRA: 2}},
                {"text": "Nesnáším to – chci být v terénu", "scores": {ZEM: 2, DOP: 1}},
                {"text": "Digitalizuji to – papír je zbytečný", "scores": {IT: 2, OBC: 1}},
            ]
        },
        {
            "text": "Jak vnímáš práci o svátcích a prázdninách?",
            "answers": [
                {"text": "Nutnost – lékaři, záchranáři, policisté pracují vždy", "scores": {ZDR: 2, PRA: 1}},
                {"text": "Sezóna – v gastronomii a turismu je to hlavní čas", "scores": {OBC: 3}},
                {"text": "V zemědělství se pracuje, když příroda velí", "scores": {ZEM: 3}},
                {"text": "Volno je pro mě důležité", "scores": {MAN: 1, IT: 1, SKO: 1}},
            ]
        },
        {
            "text": "Máš rád/a práci pod širým nebem?",
            "answers": [
                {"text": "Ano – pole, les, zahrada, rybník", "scores": {ZEM: 3}},
                {"text": "Ano – stavba, střecha, venkovní montáže", "scores": {STA: 3}},
                {"text": "Částečně – terénní výzkum, exkurze", "scores": {SKO: 2, DOP: 1}},
                {"text": "Ne – preferuji interiér", "scores": {IT: 2, MAN: 1}},
            ]
        },

        # ======================= BLOK 6: ZIVOTNI SCENARE (121-150) =======================
        {
            "text": "Ztroskotáš na pustém ostrově. Co uděláš jako první?",
            "answers": [
                {"text": "Prozkoumám terén, najdu vodu a jídlo", "scores": {ZEM: 3}},
                {"text": "Postavím přístřešek a signální zařízení", "scores": {STA: 2, STR: 1}},
                {"text": "Ošetřím zraněné a zajistím zdravotní péči", "scores": {ZDR: 3}},
                {"text": "Organizuji skupinu a rozdělím úkoly", "scores": {MAN: 2, PRA: 1}},
            ]
        },
        {
            "text": "Dostaneš milion korun. Co s ním uděláš?",
            "answers": [
                {"text": "Koupím farmu nebo lesní pozemek", "scores": {ZEM: 3}},
                {"text": "Investuji do startupu nebo vlastního podnikání", "scores": {MAN: 2, OBC: 1}},
                {"text": "Financuji vědecký výzkum nebo stipendia", "scores": {SKO: 3}},
                {"text": "Podpořím umělecké projekty nebo si zařídím dílnu", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Máš superschopnost. Jakou si vybereš?",
            "answers": [
                {"text": "Superinteligenci – řeším jakýkoli problém", "scores": {IT: 2, SKO: 1}},
                {"text": "Schopnost léčit nemoci dotykem", "scores": {ZDR: 3}},
                {"text": "Superrychlost – stíhám vše a jsem všude", "scores": {DOP: 2, PRA: 1}},
                {"text": "Schopnost tvořit z ničeho hmotu", "scores": {STA: 2, UME: 1}},
            ]
        },
        {
            "text": "Jsi ředitel/ka školy. Co jako první změníš?",
            "answers": [
                {"text": "Zavedení praxe v řemeslech a technických oborech", "scores": {STR: 2, STA: 1}},
                {"text": "Více IT a programování od 1. třídy", "scores": {IT: 3}},
                {"text": "Zaměření na kreativitu a umění", "scores": {UME: 3}},
                {"text": "Program duševního zdraví a wellbeingu", "scores": {ZDR: 2, SKO: 1}},
            ]
        },
        {
            "text": "Zakládáš firmu. V jakém oboru?",
            "answers": [
                {"text": "Stavební firma nebo výrobní podnik", "scores": {STA: 2, STR: 1}},
                {"text": "IT startup nebo SaaS řešení", "scores": {IT: 3}},
                {"text": "Restaurace, kavárna nebo hotel", "scores": {OBC: 3}},
                {"text": "Ekologická farma nebo včelařství", "scores": {ZEM: 3}},
            ]
        },
        {
            "text": "Vynalezneš něco revolučního. Co to bude?",
            "answers": [
                {"text": "Umělou inteligenci pro diagnostiku nemocí", "scores": {IT: 2, ZDR: 1}},
                {"text": "Lék na dosud neléčitelnou nemoc", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Ekologický materiál pro stavebnictví", "scores": {STA: 2, ZEM: 1}},
                {"text": "Nový způsob výuky, který změní vzdělávání", "scores": {SKO: 3}},
            ]
        },
        {
            "text": "Jsi prezident/ka. Jaký zákon jako první prosadíš?",
            "answers": [
                {"text": "Přísnou ochranu životního prostředí a krajiny", "scores": {ZEM: 3}},
                {"text": "Reformu bezpečnostních složek a justice", "scores": {PRA: 3}},
                {"text": "Univerzální přístup ke zdravotní péči", "scores": {ZDR: 3}},
                {"text": "Reformu vzdělávacího systému", "scores": {SKO: 3}},
            ]
        },
        {
            "text": "Organizuješ akci pro celé město. Jakou?",
            "answers": [
                {"text": "Farmářský trh nebo den otevřených farem", "scores": {ZEM: 2, OBC: 1}},
                {"text": "Kulturní festival s hudbou a uměním", "scores": {UME: 3}},
                {"text": "Sportovní nebo charitativní akci", "scores": {ZDR: 1, PRA: 1, SKO: 1}},
                {"text": "Tech konferenci nebo hackathon", "scores": {IT: 3}},
            ]
        },
        {
            "text": "Můžeš strávit den s jakoukoli osobností. Koho si vybereš?",
            "answers": [
                {"text": "Inženýra Elona Muska nebo vynálezce", "scores": {IT: 2, STR: 1}},
                {"text": "Lékaře Alberta Schweitzera", "scores": {ZDR: 3}},
                {"text": "Umělce Leonarda da Vinciho", "scores": {UME: 3}},
                {"text": "Pedagoga Jana Amose Komenského", "scores": {SKO: 3}},
            ]
        },
        {
            "text": "Jaký typ domu bys si postavil/a?",
            "answers": [
                {"text": "Farmu se stodolou a poli kolem", "scores": {ZEM: 3}},
                {"text": "Pasivní dům nebo dřevostavbu – sám/sama", "scores": {STA: 3}},
                {"text": "Smart home s plnou automatizací", "scores": {IT: 2, STR: 1}},
                {"text": "Architektonicky unikátní stavbu", "scores": {UME: 2, STA: 1}},
            ]
        },
        {
            "text": "Jsi vedoucí týmu a nastane krize. Jak zareaguješ?",
            "answers": [
                {"text": "Analýza situace, plán, exekuce", "scores": {MAN: 3}},
                {"text": "Nejdřív zajistím bezpečnost všech", "scores": {PRA: 2, ZDR: 1}},
                {"text": "Hledám technické řešení problému", "scores": {STR: 2, IT: 1}},
                {"text": "Postarám se o morálku a komunikuji s týmem", "scores": {SKO: 2, OBC: 1}},
            ]
        },
        {
            "text": "Najdeš záhadný předmět. Co s ním uděláš?",
            "answers": [
                {"text": "Vědecky ho prozkoumám a analyzuji", "scores": {SKO: 3}},
                {"text": "Nakreslím ho nebo o něm napíšu příběh", "scores": {UME: 3}},
                {"text": "Zjistím, zda není nebezpečný – ohlásím nález", "scores": {PRA: 3}},
                {"text": "Rozeberu ho a zjistím, jak funguje", "scores": {STR: 2, IT: 1}},
            ]
        },
        {
            "text": "Píšeš knihu. Jaký bude žánr?",
            "answers": [
                {"text": "Sci-fi nebo technologický thriller", "scores": {IT: 2, STR: 1}},
                {"text": "Právnický thriller nebo detektivka", "scores": {PRA: 3}},
                {"text": "Kuchařka nebo průvodce cestování", "scores": {OBC: 3}},
                {"text": "Historický román nebo populárně-naučná kniha", "scores": {SKO: 3}},
            ]
        },
        {
            "text": "Rozhoduješ o budoucnosti svého města. Co uděláš?",
            "answers": [
                {"text": "Rozšířím zelené plochy, komunitní zahrady", "scores": {ZEM: 3}},
                {"text": "Vybuduji moderní dopravní infrastrukturu", "scores": {DOP: 2, STA: 1}},
                {"text": "Postavím novou nemocnici a sociální centrum", "scores": {ZDR: 3}},
                {"text": "Vytvořím kulturní čtvrť s galeriemi a dílnami", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Kde se vidíš za 10 let?",
            "answers": [
                {"text": "Na vlastní farmě nebo v lesnickém revíru", "scores": {ZEM: 3}},
                {"text": "Vedu stavební firmu nebo inženýrský tým", "scores": {STA: 2, STR: 1}},
                {"text": "Vedu IT firmu nebo vývojářský tým", "scores": {IT: 2, MAN: 1}},
                {"text": "Pracuji jako lékař/ka, učitel/ka, nebo umělec/umělkyně", "scores": {ZDR: 1, SKO: 1, UME: 1}},
            ]
        },
        {
            "text": "Jak vnímáš práci s potravinami a gastronomii?",
            "answers": [
                {"text": "Vaření je moje vášeň – šéfkuchař, cukrář", "scores": {OBC: 3}},
                {"text": "Zajímá mě pěstování potravin", "scores": {ZEM: 3}},
                {"text": "Zajímá mě nutriční poradenství a zdraví", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Gastronomie mě profesně nezajímá", "scores": {IT: 1, STR: 1}},
            ]
        },
        {
            "text": "Jaký je tvůj vztah k letectví a kosmickému průmyslu?",
            "answers": [
                {"text": "Fascinuje mě – pilot, letecký mechanik", "scores": {DOP: 3}},
                {"text": "Zajímá mě kosmický výzkum a technologie", "scores": {SKO: 2, STR: 1}},
                {"text": "Zajímá mě IT stránka – navigace, autopilot", "scores": {IT: 3}},
                {"text": "Nemám k tomu zvláštní vztah", "scores": {ZEM: 1, OBC: 1}},
            ]
        },
        {
            "text": "Jak vnímáš energetiku a obnovitelné zdroje?",
            "answers": [
                {"text": "Chci pracovat v energetice – solární, větrná, jádro", "scores": {STR: 3}},
                {"text": "Zajímá mě energetická efektivita budov", "scores": {STA: 3}},
                {"text": "Zajímají mě smart grids a IoT v energetice", "scores": {IT: 3}},
                {"text": "Důležitá pro přírodu – ekologický přístup", "scores": {ZEM: 2, SKO: 1}},
            ]
        },
        {
            "text": "Jak by vypadal tvůj vysněný den v práci?",
            "answers": [
                {"text": "Ráno na poli, odpoledne v lese se zvířaty", "scores": {ZEM: 3}},
                {"text": "Řízení projektu, schůzky, prezentace", "scores": {MAN: 3}},
                {"text": "Celý den operuji / léčím pacienty", "scores": {ZDR: 3}},
                {"text": "Tvořím ve svém ateliéru nebo studiu", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Jaký typ cestovního ruchu tě láká jako profese?",
            "answers": [
                {"text": "Průvodce cestovního ruchu – ukazovat krásy světa", "scores": {OBC: 3}},
                {"text": "Hotelový management – organizace a služby", "scores": {OBC: 2, MAN: 1}},
                {"text": "Cestovní fotograf nebo dokumentarista", "scores": {UME: 3}},
                {"text": "Cestovní ruch mě profesně nezajímá", "scores": {IT: 1, STR: 1}},
            ]
        },
        {
            "text": "Jaký máš vztah k železnici a kolejové dopravě?",
            "answers": [
                {"text": "Chci řídit vlak – strojvedoucí", "scores": {DOP: 3}},
                {"text": "Zajímá mě technika kolejových vozidel", "scores": {STR: 2, DOP: 1}},
                {"text": "Zajímá mě logistika a plánování jízdních řádů", "scores": {DOP: 2, MAN: 1}},
                {"text": "Nemám k tomu zvláštní vztah", "scores": {UME: 1, ZDR: 1}},
            ]
        },
        {
            "text": "Jak vnímáš práci v laboratoři?",
            "answers": [
                {"text": "Fascinuje mě – výzkum, experimenty, analýzy", "scores": {SKO: 2, ZDR: 1}},
                {"text": "Zajímá mě – testování materiálů a kvality", "scores": {STR: 2}},
                {"text": "Nezajímá mě – chci být v terénu nebo mezi lidmi", "scores": {ZEM: 1, OBC: 1, DOP: 1}},
                {"text": "Preferuji digitální laboratoř – simulace, AI", "scores": {IT: 3}},
            ]
        },
        {
            "text": "Jakou roli bys měl/a ve filmu?",
            "answers": [
                {"text": "Režisér nebo kameraman – tvořím zákulisí", "scores": {UME: 3}},
                {"text": "Akční hrdina – policista, hasič, voják", "scores": {PRA: 3}},
                {"text": "Lékař, který zachraňuje životy", "scores": {ZDR: 3}},
                {"text": "Geniální hacker nebo vynálezce", "scores": {IT: 2, STR: 1}},
            ]
        },
        {
            "text": "Kdyby jsi mohl/a jednu věc na světě zlepšit, co by to bylo?",
            "answers": [
                {"text": "Kvalitu potravin a zemědělství", "scores": {ZEM: 3}},
                {"text": "Dopravní infrastrukturu a logistiku", "scores": {DOP: 2, STA: 1}},
                {"text": "Přístup ke kvalitnímu vzdělání pro všechny", "scores": {SKO: 3}},
                {"text": "Bezpečnost a spravedlnost ve společnosti", "scores": {PRA: 3}},
            ]
        },
        {
            "text": "Jaký typ práce s kovem nebo dřevem tě láká?",
            "answers": [
                {"text": "Svařování, obrábění, zámečnictví", "scores": {STR: 3}},
                {"text": "Tesařství, stavba dřevěných konstrukcí", "scores": {STA: 3}},
                {"text": "Umělecké kovářství, zlatnictví, houslařství", "scores": {UME: 3}},
                {"text": "Práce s materiálem mě nezajímá", "scores": {IT: 1, MAN: 1}},
            ]
        },
        {
            "text": "Jak vnímáš budoucnost robotiky a automatizace?",
            "answers": [
                {"text": "Chci ji programovat a vyvíjet", "scores": {IT: 3}},
                {"text": "Chci roboty nasazovat ve výrobě", "scores": {STR: 3}},
                {"text": "Zajímá mě robotika v medicíně", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Obávám se dopadu na zaměstnanost", "scores": {MAN: 1, PRA: 1, SKO: 1}},
            ]
        },
        {
            "text": "Jaký typ zákaznického servisu je ti blízký?",
            "answers": [
                {"text": "Přímý kontakt – číšník, recepční, průvodce", "scores": {OBC: 3}},
                {"text": "Technická podpora – IT helpdesk", "scores": {IT: 2}},
                {"text": "Poradenství – sociální pracovník, finanční poradce", "scores": {ZDR: 1, MAN: 2}},
                {"text": "Raději pracuji bez kontaktu se zákazníky", "scores": {STR: 1, ZEM: 1, STA: 1}},
            ]
        },
        {
            "text": "Jak se díváš na budoucnost svého oboru?",
            "answers": [
                {"text": "Zemědělství a potravinářství budou vždy potřeba", "scores": {ZEM: 3}},
                {"text": "Stavět a opravovat se bude vždycky", "scores": {STA: 2, STR: 1}},
                {"text": "IT a digitalizace porostou exponenciálně", "scores": {IT: 3}},
                {"text": "Lidé budou vždy potřebovat lékaře a učitele", "scores": {ZDR: 2, SKO: 1}},
            ]
        },

        # ======================= BLOK 7: DOPLNKOVE OTAZKY (130-150) =======================
        {
            "text": "Jak vnímáš práci s nebezpečnými materiály (chemikálie, výbušniny)?",
            "answers": [
                {"text": "Nevadí mi – pracuji s bezpečnostními protokoly", "scores": {STR: 2, PRA: 1}},
                {"text": "Zvládám – chemikálie v laboratoři nebo lékárně", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Raději pracuji s bezpečnými materiály", "scores": {UME: 1, OBC: 1, MAN: 1}},
                {"text": "Nevadí mi – hnojiva a postřiky na farmě", "scores": {ZEM: 3}},
            ]
        },
        {
            "text": "Jak se stavíš k práci ve výškách?",
            "answers": [
                {"text": "Nevadí mi – lešení, střechy, jeřáby", "scores": {STA: 3}},
                {"text": "Nevadí mi – stožáry, věže, antény", "scores": {STR: 2, IT: 1}},
                {"text": "Preferuji práci na zemi", "scores": {ZEM: 2, OBC: 1}},
                {"text": "Výšky mi nevadí – záchranářský vrtulník, horolezectví", "scores": {PRA: 2, ZDR: 1}},
            ]
        },
        {
            "text": "Jak vnímáš práci na směny (ranní, odpolední, noční)?",
            "answers": [
                {"text": "Jsem na to zvyklý/á – nemocnice, záchranná služba", "scores": {ZDR: 3}},
                {"text": "Zvládám – výrobní hala, nepřetržitý provoz", "scores": {STR: 3}},
                {"text": "Preferuji fixní pracovní dobu", "scores": {MAN: 2, SKO: 1}},
                {"text": "Řídím se přírodou – ráno vstávám, večer odpočívám", "scores": {ZEM: 3}},
            ]
        },
        {
            "text": "Jaký typ projektu bys chtěl/a vést?",
            "answers": [
                {"text": "Výstavbu nové budovy nebo mostu", "scores": {STA: 3}},
                {"text": "Vývoj softwarového produktu", "scores": {IT: 3}},
                {"text": "Organizaci mezinárodní konference", "scores": {OBC: 2, MAN: 1}},
                {"text": "Výzkumný grant na univerzitě", "scores": {SKO: 3}},
            ]
        },
        {
            "text": "Jak vnímáš práci s vodou (přehrady, vodovody, rybníky)?",
            "answers": [
                {"text": "Zajímá mě rybářství a akvakultura", "scores": {ZEM: 3}},
                {"text": "Zajímá mě vodní stavitelství – přehrady, kanalizace", "scores": {STA: 3}},
                {"text": "Zajímá mě lodní doprava a přístavy", "scores": {DOP: 3}},
                {"text": "Voda mě profesně nezajímá", "scores": {IT: 1, UME: 1}},
            ]
        },
        {
            "text": "Jak bys řešil/a konflikt mezi dvěma kolegy?",
            "answers": [
                {"text": "Mediací – vyslechnu obě strany a najdu řešení", "scores": {MAN: 2, PRA: 1}},
                {"text": "Empaticky – postarám se o emoce obou stran", "scores": {ZDR: 2, SKO: 1}},
                {"text": "Pravidly – odkážu na předpisy a směrnice", "scores": {PRA: 3}},
                {"text": "Kreativně – navrhnu kompromis mimo zaběhané postupy", "scores": {UME: 2, OBC: 1}},
            ]
        },
        {
            "text": "Jaký typ psaní tě baví nejvíce?",
            "answers": [
                {"text": "Technické dokumentace a manuály", "scores": {IT: 2, STR: 1}},
                {"text": "Právní texty, smlouvy, zákony", "scores": {PRA: 3}},
                {"text": "Kreativní psaní – příběhy, scénáře, poezie", "scores": {UME: 3}},
                {"text": "Obchodní plány a marketingové texty", "scores": {MAN: 2, OBC: 1}},
            ]
        },
        {
            "text": "Jak vnímáš práci s mapami, GPS a navigací?",
            "answers": [
                {"text": "Denní chleba – navigace, trasování, logistika", "scores": {DOP: 3}},
                {"text": "Používám při geodézii a stavebním plánování", "scores": {STA: 2, STR: 1}},
                {"text": "GIS a mapové aplikace mě z IT stránky zajímají", "scores": {IT: 3}},
                {"text": "Využívám při terénním výzkumu a zemědělství", "scores": {ZEM: 2, SKO: 1}},
            ]
        },
        {
            "text": "Jaký typ školení bys rád/a absolvoval/a?",
            "answers": [
                {"text": "Řidičský průkaz skupiny C, D nebo průkaz strojvedoucího", "scores": {DOP: 3}},
                {"text": "Certifikaci v kybernetické bezpečnosti", "scores": {IT: 3}},
                {"text": "Kurz krizového managementu", "scores": {MAN: 2, PRA: 1}},
                {"text": "Specializaci v ošetřovatelství nebo fyzioterapii", "scores": {ZDR: 3}},
            ]
        },
        {
            "text": "Jak vnímáš práci s textilem a módou?",
            "answers": [
                {"text": "Baví mě – módní návrhář, krejčí, textilní designér", "scores": {UME: 3}},
                {"text": "Zajímá mě textilní výroba a technologie", "scores": {STR: 2}},
                {"text": "Zajímá mě prodej a marketing v módě", "scores": {OBC: 2, MAN: 1}},
                {"text": "Textil a móda mě profesně nezajímají", "scores": {IT: 1, ZEM: 1}},
            ]
        },
        {
            "text": "Kdybys zakládal/a neziskovou organizaci, čemu by se věnovala?",
            "answers": [
                {"text": "Ochraně životního prostředí a biodiverzity", "scores": {ZEM: 3}},
                {"text": "Vzdělávání znevýhodněných dětí", "scores": {SKO: 3}},
                {"text": "Poskytování zdravotní péče v rozvojových zemích", "scores": {ZDR: 3}},
                {"text": "Podpoře začínajících umělců a řemeslníků", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Jaký vztah máš ke zvukové technice a akustice?",
            "answers": [
                {"text": "Fascinuje mě – zvukař, producent, DJ", "scores": {UME: 3}},
                {"text": "Zajímá mě technická stránka – akustický inženýr", "scores": {STR: 2, IT: 1}},
                {"text": "Používám ji při výuce nebo přednáškách", "scores": {SKO: 2}},
                {"text": "Nemám k tomu zvláštní vztah", "scores": {STA: 1, DOP: 1}},
            ]
        },
        {
            "text": "Jak vnímáš práci v potravinářském průmyslu?",
            "answers": [
                {"text": "Baví mě – pekař, řezník, pivovarník, vinař", "scores": {OBC: 2, ZEM: 1}},
                {"text": "Zajímá mě kvalita a hygiena potravin", "scores": {ZDR: 2}},
                {"text": "Zajímá mě automatizace potravinářské výroby", "scores": {STR: 2, IT: 1}},
                {"text": "Potravinářský průmysl mě nezajímá", "scores": {PRA: 1, MAN: 1}},
            ]
        },
        {
            "text": "Jak se stavíš k práci s dokumenty a archivy?",
            "answers": [
                {"text": "Baví mě – archivář, knihovník, dokumentarista", "scores": {SKO: 2, PRA: 1}},
                {"text": "Zajímá mě digitalizace a správa dat", "scores": {IT: 3}},
                {"text": "Pracuji s dokumenty v administrativě", "scores": {MAN: 2}},
                {"text": "Preferuji práci v terénu, ne u papírů", "scores": {ZEM: 1, DOP: 1, STA: 1}},
            ]
        },
        {
            "text": "Jaký typ inovace tě nejvíce přitahuje?",
            "answers": [
                {"text": "Chytré zemědělství – drony, senzory, precizní farming", "scores": {ZEM: 2, IT: 1}},
                {"text": "3D tisk a nové výrobní technologie", "scores": {STR: 2, STA: 1}},
                {"text": "Telemedicína a digitální zdravotnictví", "scores": {ZDR: 2, IT: 1}},
                {"text": "Autonomní vozidla a drony v dopravě", "scores": {DOP: 2, IT: 1}},
            ]
        },
        {
            "text": "Jak vnímáš sport a tělesnou výchovu jako profesi?",
            "answers": [
                {"text": "Chci být trenér nebo sportovní instruktor", "scores": {SKO: 2, ZDR: 1}},
                {"text": "Zajímá mě sportovní management a organizace", "scores": {MAN: 2, OBC: 1}},
                {"text": "Zajímá mě sportovní medicína a rehabilitace", "scores": {ZDR: 3}},
                {"text": "Sport jako profese mě nezajímá", "scores": {IT: 1, STR: 1}},
            ]
        },
        {
            "text": "Jaký typ komunikace preferuješ v práci?",
            "answers": [
                {"text": "Osobní jednání a schůzky", "scores": {OBC: 2, MAN: 1}},
                {"text": "E-maily, chat a digitální nástroje", "scores": {IT: 2, MAN: 1}},
                {"text": "Telefonní hovory a rádiová komunikace", "scores": {DOP: 2, PRA: 1}},
                {"text": "Vizuální komunikace – obrázky, nákresy, modely", "scores": {UME: 2, STA: 1}},
            ]
        },
        {
            "text": "Jak bys využil/a umělou inteligenci ve své práci?",
            "answers": [
                {"text": "K automatizaci výroby a optimalizaci procesů", "scores": {STR: 2, IT: 1}},
                {"text": "K diagnostice nemocí a vývoji léků", "scores": {ZDR: 2, SKO: 1}},
                {"text": "K analýze dat, predikci trendů a financí", "scores": {MAN: 2, IT: 1}},
                {"text": "K tvorbě umění, hudby nebo designu", "scores": {UME: 3}},
            ]
        },
        {
            "text": "Co bys dělal/a jako poslední den ve své kariéře?",
            "answers": [
                {"text": "Procházel/a bych se po své farmě nebo lese", "scores": {ZEM: 3}},
                {"text": "Obdivoval/a bych stavby, které jsem pomáhal/a vytvořit", "scores": {STA: 3}},
                {"text": "Vzpomínal/a na žáky a pacienty, kterým jsem pomohl/a", "scores": {SKO: 2, ZDR: 1}},
                {"text": "Připravoval/a bych předání firmy další generaci", "scores": {MAN: 3}},
            ]
        },
        {
            "text": "Jaký je tvůj ideální pracovní výsledek na konci dne?",
            "answers": [
                {"text": "Hotový výrobek, opravený stroj, postavená zeď", "scores": {STR: 2, STA: 1}},
                {"text": "Spokojený zákazník nebo host", "scores": {OBC: 3}},
                {"text": "Bezpečně dovezení cestující do cíle", "scores": {DOP: 3}},
                {"text": "Odeslání kódu nebo vyřešení technického problému", "scores": {IT: 3}},
            ]
        },
        {
            "text": "Jak vnímáš práci s dětmi a mládeží?",
            "answers": [
                {"text": "Je to moje poslání – učitel, vychovatel, trenér", "scores": {SKO: 3}},
                {"text": "Baví mě to – vedoucí skautů, instruktor", "scores": {SKO: 2, PRA: 1}},
                {"text": "Zajímá mě dětská medicína – pediatr, logoped", "scores": {ZDR: 3}},
                {"text": "Preferuji práci s dospělými", "scores": {MAN: 1, STR: 1, DOP: 1}},
            ]
        },
    ]
