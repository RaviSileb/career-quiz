"""
Kariérní kvíz – Část 2: podrobné oborové otázky.

Celkem 880 otázek (80 otázek × 11 kategorií).
Každá otázka je single-choice se 4 odpověďmi.
Každá odpověď přiděluje 2–4 body jedné až dvěma pozicím.

Kategorie (v pořadí):
  ZEM  Zemědělství a lesnictví        (1–80)
  STA  Stavebnictví a architektura    (81–160)
  ELE  Elektrotechnika a energetika   (161–240)
  STR  Strojírenství a výroba         (241–320)
  INF  Informatika a digitální tech.  (321–400)
  ZDR  Zdravotnictví a farmacie       (401–480)
  EKO  Ekonomika a podnikání          (481–560)
  PRA  Právo a veřejná správa         (561–640)
  UME  Umění a kreativní obory        (641–720)
  SLU  Služby a cestovní ruch         (721–800)
  VED  Věda a výzkum                  (801–880)
"""


def _p2(cat, text, a1, a2, a3, a4):
    """Part 2 single-choice question.
    Each answer: (text, {position_name: score, ...})
    """
    return {
        'text': text, 'type': 'single_choice', 'part': 2, 'category': cat,
        'answers': [{'text': t, 'position_scores': s} for t, s in (a1, a2, a3, a4)]
    }


def get_part2_questions():
    return [
        # ══════════════ ZEM: Zemědělství a lesnictví (1–80) ══════════════

        # --- Pracovní činnosti ---
        _p2('ZEM', 'Jakou činnost byste na farmě dělali nejraději?',
            ('Plánování osevních postupů a skladby plodin', {'Agronom': 3}),
            ('Ošetřování nemocných zvířat', {'Veterinární lékař': 3}),
            ('Údržba traktorů a kombajnů', {'Zemědělský technik': 3}),
            ('Péče o zahradu a okrasné rostliny', {'Zahradník': 3})),

        _p2('ZEM', 'Která pracovní náplň vás láká nejvíce?',
            ('Správa a obnova lesních porostů', {'Lesní inženýr': 3}),
            ('Denní krmení a kontrola zdraví stáda', {'Chovatel zvířat': 3}),
            ('Regulace stavů zvěře a péče o honitbu', {'Myslivec': 3}),
            ('Hodnocení vlivu hospodaření na krajinu', {'Ekolog': 3})),

        _p2('ZEM', 'Co by vás bavilo při práci na poli?',
            ('Odebírání vzorků půdy a analýza živin', {'Agronom': 3, 'Ekolog': 2}),
            ('Řízení sklízecí mlátičky při žních', {'Zemědělský technik': 3}),
            ('Výsadba a tvarový řez ovocných stromů', {'Zahradník': 3}),
            ('Očkování telat proti infekčním chorobám', {'Veterinární lékař': 3})),

        _p2('ZEM', 'Jak byste se nejraději podíleli na chovu hospodářských zvířat?',
            ('Sestavování krmných dávek a výživových plánů', {'Chovatel zvířat': 3, 'Agronom': 2}),
            ('Chirurgické zákroky a porodní asistence', {'Veterinární lékař': 4}),
            ('Návrh a údržba ustájovací technologie', {'Zemědělský technik': 3}),
            ('Sledování welfare zvířat a etiky chovu', {'Ekolog': 3})),

        _p2('ZEM', 'Která činnost v lese vás přitahuje?',
            ('Výběr stromů k těžbě podle hospodářského plánu', {'Lesní inženýr': 3}),
            ('Pozorování a sčítání lesní zvěře', {'Myslivec': 3}),
            ('Mapování výskytu chráněných druhů', {'Ekolog': 3}),
            ('Sběr lesních semen pro školkařskou výrobu', {'Zahradník': 3})),

        _p2('ZEM', 'Co byste dělali nejraději při jarních pracích?',
            ('Přípravu půdy a setí obilovin', {'Agronom': 3}),
            ('Vysazování sazenic do lesní kultury', {'Lesní inženýr': 3}),
            ('Zakládání záhonů a výsev letniček', {'Zahradník': 3}),
            ('Kontrolu zdravotního stavu březích klisen', {'Veterinární lékař': 3})),

        _p2('ZEM', 'Na podzim byste se nejvíce věnovali:',
            ('Sklizni plodin a uskladnění úrody', {'Agronom': 3, 'Zemědělský technik': 2}),
            ('Přípravě zvířat na zimní ustájení', {'Chovatel zvířat': 3}),
            ('Organizaci podzimních honů', {'Myslivec': 3}),
            ('Výsadbě cibulovin a přípravě záhonů na zimu', {'Zahradník': 3})),

        _p2('ZEM', 'Která laboratorní aktivita vás zaujme?',
            ('Rozbor kvality zrna a výnosu odrůd', {'Agronom': 3}),
            ('Mikrobiologické vyšetření vzorků krve zvířat', {'Veterinární lékař': 4}),
            ('Analýza kontaminantů v půdě a vodě', {'Ekolog': 3}),
            ('Testování klíčivosti osiva v sadbovačích', {'Zahradník': 3})),

        _p2('ZEM', 'Jakou práci byste vykonávali při ochraně rostlin?',
            ('Výběr a nasazení biologických přípravků', {'Agronom': 3, 'Ekolog': 2}),
            ('Seřizování a kalibraci postřikovače', {'Zemědělský technik': 3}),
            ('Identifikaci škůdců pod lupou', {'Zahradník': 3}),
            ('Zjišťování vlivu pesticidů na hmyz', {'Ekolog': 3})),

        _p2('ZEM', 'Při záchraně zraněného zvířete byste:',
            ('Provedli chirurgický zákrok v terénu', {'Veterinární lékař': 4}),
            ('Připravili provizorní přístřešek a krmivo', {'Chovatel zvířat': 3}),
            ('Kontaktovali záchrannou stanici a dokumentovali nález', {'Ekolog': 3}),
            ('Zajistili bezpečný převoz pomocí techniky', {'Zemědělský technik': 3})),

        # --- Pracovní prostředí ---
        _p2('ZEM', 'V jakém prostředí se cítíte nejlépe?',
            ('Na otevřeném poli mezi lány obilí', {'Agronom': 3}),
            ('V hluboké, tiché lese', {'Lesní inženýr': 3, 'Myslivec': 2}),
            ('Ve skleníku plném kvetoucích rostlin', {'Zahradník': 3}),
            ('Ve stáji mezi zvířaty', {'Chovatel zvířat': 3})),

        _p2('ZEM', 'Kde byste chtěli trávit pracovní den?',
            ('V kabině moderního traktoru s GPS navigací', {'Zemědělský technik': 3}),
            ('Ve veterinární ambulanci', {'Veterinární lékař': 3}),
            ('Na posedu při pozorování přírody', {'Myslivec': 3}),
            ('V terénu při ekologickém průzkumu', {'Ekolog': 3})),

        _p2('ZEM', 'Které pracoviště je vám nejbližší?',
            ('Pokusné pole s experimenty na odrůdách', {'Agronom': 3}),
            ('Lesní školka se sazenicemi', {'Lesní inženýr': 3, 'Zahradník': 2}),
            ('Dílna se zemědělskými stroji', {'Zemědělský technik': 3}),
            ('Laboratoř pro rozbor vody a bioty', {'Ekolog': 3})),

        _p2('ZEM', 'V jakém počasí pracujete nejraději?',
            ('V brzkém jarním ránu na poli při setí', {'Agronom': 3}),
            ('V dešti při kontrole lesních porostů', {'Lesní inženýr': 3}),
            ('Za svítání na posedu v mlze', {'Myslivec': 3}),
            ('V teplém skleníku bez ohledu na počasí', {'Zahradník': 3})),

        _p2('ZEM', 'Jaký typ budovy preferujete jako zázemí?',
            ('Moderní kravín s dojicí technikou', {'Chovatel zvířat': 3, 'Zemědělský technik': 2}),
            ('Hájenku na okraji lesa', {'Myslivec': 3}),
            ('Veterinární kliniku s operačním sálem', {'Veterinární lékař': 3}),
            ('Terénní stanici pro monitoring přírody', {'Ekolog': 3})),

        # --- Znalosti a dovednosti ---
        _p2('ZEM', 'Jaké znalosti byste si chtěli prohloubit?',
            ('Genetiku a šlechtění rostlin', {'Agronom': 4}),
            ('Anatomii a fyziologii zvířat', {'Veterinární lékař': 4}),
            ('Dendrologii a typologii lesů', {'Lesní inženýr': 3}),
            ('Floristiku a aranžování květin', {'Zahradník': 3})),

        _p2('ZEM', 'Který předmět na škole by vás zaujal nejvíce?',
            ('Pedologie – nauka o půdách', {'Agronom': 3, 'Ekolog': 2}),
            ('Fytotechnika – pěstování rostlin', {'Zahradník': 3}),
            ('Zootechnika – chov zvířat', {'Chovatel zvířat': 3}),
            ('Mechanizace zemědělství', {'Zemědělský technik': 3})),

        _p2('ZEM', 'Kterou dovednost považujete za nejcennější?',
            ('Schopnost rozpoznat choroby rostlin v poli', {'Agronom': 3}),
            ('Umění provést ultrazvukové vyšetření zvířete', {'Veterinární lékař': 4}),
            ('Orientace v lese a čtení stopy zvěře', {'Myslivec': 3}),
            ('Znalost ekosystémových služeb a biodiverzity', {'Ekolog': 3})),

        _p2('ZEM', 'Jaký typ odborného kurzu byste absolvovali?',
            ('Precizní zemědělství a satelitní snímkování', {'Agronom': 3, 'Zemědělský technik': 2}),
            ('Chirurgie malých zvířat', {'Veterinární lékař': 4}),
            ('Arboristika a péče o vzrostlé stromy', {'Zahradník': 3, 'Lesní inženýr': 2}),
            ('Managment chráněných území', {'Ekolog': 3})),

        _p2('ZEM', 'Které znalosti jsou podle vás nejdůležitější pro práci v krajině?',
            ('Hydrologie a meliorace', {'Lesní inženýr': 3, 'Ekolog': 2}),
            ('Výživa a krmivářství', {'Chovatel zvířat': 3}),
            ('Entomologie a ochrana proti škůdcům', {'Agronom': 3}),
            ('Myslivecké právo a etika lovu', {'Myslivec': 3})),

        # --- Nástroje a technologie ---
        _p2('ZEM', 'Který nástroj byste používali nejčastěji?',
            ('GPS a variabilní aplikátor hnojiv', {'Agronom': 3, 'Zemědělský technik': 2}),
            ('Stetoskop a otoskop pro zvířata', {'Veterinární lékař': 3}),
            ('Motorovou pilu a lesnický průměrku', {'Lesní inženýr': 3}),
            ('Zahradnické nůžky a nůžky na živé ploty', {'Zahradník': 3})),

        _p2('ZEM', 'Jakou techniku byste chtěli ovládat?',
            ('Sklízecí mlátičku s výnosovou mapou', {'Zemědělský technik': 3}),
            ('Rentgen a ultrazvuk ve veterinární praxi', {'Veterinární lékař': 4}),
            ('Harvestor pro těžbu dříví', {'Lesní inženýr': 3, 'Zemědělský technik': 2}),
            ('Automatický zavlažovací systém ve skleníku', {'Zahradník': 3})),

        _p2('ZEM', 'Který software je pro vaši práci nejužitečnější?',
            ('Systém pro řízení rostlinné výroby (FMIS)', {'Agronom': 3}),
            ('Veterinární informační systém', {'Veterinární lékař': 3}),
            ('GIS pro správu lesního hospodářského plánu', {'Lesní inženýr': 3}),
            ('Mapové vrstvy biodiverzity a NATURA 2000', {'Ekolog': 3})),

        _p2('ZEM', 'Jaký přístroj byste vzali do terénu?',
            ('Půdní sondu a pH metr', {'Agronom': 3}),
            ('Dalekohled a fotopast', {'Myslivec': 3, 'Ekolog': 2}),
            ('Diagnostický kufřík pro zvířata', {'Veterinární lékař': 3}),
            ('Botanickou lupu a herbářový lis', {'Zahradník': 3, 'Ekolog': 2})),

        _p2('ZEM', 'Který stroj vás fascinuje nejvíce?',
            ('Autonomní robotický traktor', {'Zemědělský technik': 4}),
            ('Dron pro mapování porostů', {'Agronom': 3, 'Lesní inženýr': 2}),
            ('Moderní dojicí robot', {'Chovatel zvířat': 3, 'Zemědělský technik': 2}),
            ('Terénní vozidlo pro ekologický monitoring', {'Ekolog': 3})),

        # --- Hodnoty a motivace ---
        _p2('ZEM', 'Co vás motivuje k práci v zemědělství?',
            ('Zajistit dostatek kvalitních potravin', {'Agronom': 3, 'Chovatel zvířat': 2}),
            ('Chránit zdraví a pohodu zvířat', {'Veterinární lékař': 3, 'Chovatel zvířat': 2}),
            ('Udržet a obnovit zdravé lesy', {'Lesní inženýr': 3}),
            ('Krášlit krajinu a veřejná prostranství', {'Zahradník': 3})),

        _p2('ZEM', 'Jaká hodnota je pro vás v práci nejdůležitější?',
            ('Ochrana biodiverzity a přírodních ekosystémů', {'Ekolog': 4}),
            ('Tradice a udržitelné hospodaření na půdě', {'Agronom': 3}),
            ('Rovnováha mezi lovem a ochranou zvěře', {'Myslivec': 3}),
            ('Technologický pokrok v zemědělství', {'Zemědělský technik': 3})),

        _p2('ZEM', 'Proč je práce s přírodou důležitá?',
            ('Produkce potravin pro společnost', {'Agronom': 3, 'Chovatel zvířat': 2}),
            ('Prevence a léčba nemocí zvířat', {'Veterinární lékař': 3}),
            ('Zachování lesů pro budoucí generace', {'Lesní inženýr': 3, 'Ekolog': 2}),
            ('Vytváření krásného a funkčního prostředí', {'Zahradník': 3})),

        _p2('ZEM', 'Co by vás nejvíce naplňovalo?',
            ('Vidět zdravé stádo, o které pečuji', {'Chovatel zvířat': 3}),
            ('Úspěšně obhospodařovat revír s pestrou zvěří', {'Myslivec': 3}),
            ('Publikovat výsledky ekologického výzkumu', {'Ekolog': 3}),
            ('Předat fungující farmu další generaci', {'Agronom': 3, 'Zemědělský technik': 2})),

        _p2('ZEM', 'Co vás žene k práci venku?',
            ('Kontakt s půdou a sledování růstu plodin', {'Agronom': 3}),
            ('Spojení s divokou přírodou a lesní samotou', {'Myslivec': 3, 'Lesní inženýr': 2}),
            ('Možnost pomáhat zvířatům v nesnázích', {'Veterinární lékař': 3}),
            ('Tvůrčí práce s živými rostlinami', {'Zahradník': 3})),

        # --- Řešení problémů ---
        _p2('ZEM', 'Na poli se objevily žluté skvrny – co uděláte?',
            ('Odeberete vzorky listů a určíte deficienci živin', {'Agronom': 4}),
            ('Zkontrolujete funkci aplikátoru hnojiv', {'Zemědělský technik': 3}),
            ('Prověříte, zda nejde o napadení hmyzem', {'Ekolog': 3}),
            ('Ověříte kvalitu závlahy a substrátu', {'Zahradník': 3})),

        _p2('ZEM', 'Kráva přestala žrát a je apatická – jaký je váš přístup?',
            ('Změříte teplotu a provedete klinické vyšetření', {'Veterinární lékař': 4}),
            ('Zkontrolujete složení krmné dávky', {'Chovatel zvířat': 3}),
            ('Prověříte ventilaci a teplotu v stáji', {'Zemědělský technik': 3}),
            ('Zjistíte, zda kráva nespásla jedovatou rostlinu', {'Agronom': 3})),

        _p2('ZEM', 'V lese najdete velké plochy suchých smrků – co navrhnete?',
            ('Naléhavou těžbu a následnou obnovu listnatými dřevinami', {'Lesní inženýr': 4}),
            ('Monitoring populace kůrovce pomocí feromonových lapačů', {'Ekolog': 3}),
            ('Organizaci nahodilé těžby a odvozu dříví', {'Zemědělský technik': 3}),
            ('Posouzení stavu zvěře, která brání přirozené obnově', {'Myslivec': 3})),

        _p2('ZEM', 'Záhony v parku chřadnou – jak problém řešíte?',
            ('Analýzou složení substrátu a úpravou hnojení', {'Zahradník': 3}),
            ('Studiem možného chemického znečištění', {'Ekolog': 3}),
            ('Kontrolou zavlažovacího systému', {'Zemědělský technik': 3}),
            ('Vyloučením nákazy houbovými patogeny', {'Agronom': 3})),

        _p2('ZEM', 'Divoká prasata ničí lány kukuřice – co doporučíte?',
            ('Plánovaný odstřel a regulaci populace', {'Myslivec': 4}),
            ('Instalaci elektrických ohradníků', {'Zemědělský technik': 3}),
            ('Změnu osevního postupu a výběr odolnějších plodin', {'Agronom': 3}),
            ('Posouzení migračních koridorů a biotopů', {'Ekolog': 3})),

        _p2('ZEM', 'Stádo ovcí trápí paraziti – jak zasáhnete?',
            ('Provedete koprologické vyšetření a odčervíte', {'Veterinární lékař': 4}),
            ('Změníte pastviny a rotaci pastvy', {'Chovatel zvířat': 3}),
            ('Zlepšíte hygienu ustájení a napájecích žlabů', {'Zemědělský technik': 3}),
            ('Vyhodnotíte vliv pastvy na biodiverzitu louky', {'Ekolog': 3})),

        _p2('ZEM', 'Na jahodách je plíseň šedá – vaše řešení?',
            ('Aplikace biologického fungicidu ve správném termínu', {'Agronom': 3}),
            ('Úprava vzdáleností sazenic a lepší proudění vzduchu', {'Zahradník': 3}),
            ('Kontrola a seřízení postřikovací techniky', {'Zemědělský technik': 3}),
            ('Posouzení rezistence odrůd a návrh šlechtitelský', {'Agronom': 2, 'Ekolog': 2})),

        _p2('ZEM', 'Eroze odnáší ornici z kopce – co navrhnete?',
            ('Založení protierozních mezí a zatravnění', {'Ekolog': 3, 'Agronom': 2}),
            ('Výsadbu větrolamů a remízků', {'Lesní inženýr': 3}),
            ('Přechod na bezorebné zpracování půdy', {'Zemědělský technik': 3}),
            ('Osázení svahu pokryvnými trvalkami', {'Zahradník': 3})),

        # --- Styl interakce ---
        _p2('ZEM', 'S kým nebo čím nejraději pracujete?',
            ('S hospodářskými zvířaty – kravami, prasaty, drůbeží', {'Chovatel zvířat': 3}),
            ('S psy, koni a loveckými dravci', {'Myslivec': 3}),
            ('S rostlinami a půdou', {'Zahradník': 3, 'Agronom': 2}),
            ('S daty a mapami krajiny', {'Ekolog': 3})),

        _p2('ZEM', 'Jak se nejlépe cítíte při týmové práci?',
            ('Vedu tým při organizaci žní', {'Agronom': 3, 'Zemědělský technik': 2}),
            ('Koordinuji naháňku s ostatními myslivci', {'Myslivec': 3}),
            ('Spolupracuji s chovateli na zdravotních plánech stáda', {'Veterinární lékař': 3}),
            ('Jednám s úřady o ochraně přírody', {'Ekolog': 3})),

        _p2('ZEM', 'Jaký typ komunikace vám vyhovuje?',
            ('Poradenství farmářům o správném hnojení', {'Agronom': 3}),
            ('Vysvětlování diagnózy chovatelům', {'Veterinární lékař': 3}),
            ('Prezentace lesního hospodářského plánu obci', {'Lesní inženýr': 3}),
            ('Vedení workshopu o kompostování pro veřejnost', {'Zahradník': 3, 'Ekolog': 2})),

        _p2('ZEM', 'V jaké roli se vidíte při řízení projektu?',
            ('Plánovač – navrhuji, co a kdy se zaseje', {'Agronom': 3}),
            ('Technik – zajišťuji funkčnost strojů a zařízení', {'Zemědělský technik': 3}),
            ('Ochránce – hlídám dopady na životní prostředí', {'Ekolog': 3}),
            ('Pečovatel – starám se o pohodu zvířat', {'Chovatel zvířat': 3})),

        _p2('ZEM', 'Jakým způsobem řešíte konflikty v krajině?',
            ('Hledám kompromis mezi zemědělci a ochranáři', {'Ekolog': 3}),
            ('Navrhuji technická řešení, která vyhovují všem', {'Zemědělský technik': 3}),
            ('Upravuji plán lovu podle stavu populace', {'Myslivec': 3}),
            ('Doporučuji vhodné odrůdy pro dané podmínky', {'Agronom': 3})),

        # --- Vzdělání a kariéra ---
        _p2('ZEM', 'Jaký studijní obor byste si vybrali?',
            ('Agronomie a rostlinná produkce', {'Agronom': 4}),
            ('Veterinární medicína', {'Veterinární lékař': 4}),
            ('Lesní inženýrství', {'Lesní inženýr': 4}),
            ('Zahradnictví a krajinářství', {'Zahradník': 4})),

        _p2('ZEM', 'Jaký typ dalšího vzdělávání upřednostníte?',
            ('Certifikát precizního zemědělství', {'Zemědělský technik': 3, 'Agronom': 2}),
            ('Specializace v chirurgii koní', {'Veterinární lékař': 4}),
            ('Lovecký lístek a sokolnické zkoušky', {'Myslivec': 4}),
            ('Kurz ekologického zemědělství', {'Ekolog': 3, 'Chovatel zvířat': 2})),

        _p2('ZEM', 'Která konference by vás zajímala?',
            ('Mezinárodní sympozium o šlechtění obilnin', {'Agronom': 3}),
            ('Veterinární kongres o reprodukci skotu', {'Veterinární lékař': 3}),
            ('Lesnický seminář o klimatické adaptaci lesů', {'Lesní inženýr': 3}),
            ('Zahradnický veletrh s novinkami v substrátech', {'Zahradník': 3})),

        _p2('ZEM', 'Kterou odbornou knihu byste četli?',
            ('Atlas chorob a škůdců polních plodin', {'Agronom': 3}),
            ('Učebnice vnitřních nemocí zvířat', {'Veterinární lékař': 3}),
            ('Průvodce myslivostí a loveckými tradicemi', {'Myslivec': 3}),
            ('Ekologie krajiny – principy a aplikace', {'Ekolog': 3})),

        _p2('ZEM', 'Kde se vidíte za 10 let?',
            ('Jako hlavní agronom velkého podniku', {'Agronom': 3}),
            ('Jako vedoucí veterinární kliniky', {'Veterinární lékař': 3}),
            ('Jako správce rozsáhlého lesního majetku', {'Lesní inženýr': 3}),
            ('Jako majitel zahradnické firmy', {'Zahradník': 3})),

        # --- Specifické situace ---
        _p2('ZEM', 'Při průchodu loukou si všimnete vzácné orchideje. Co uděláte?',
            ('Zaznamenáte GPS souřadnice a nahlásíte nález', {'Ekolog': 4}),
            ('Vyfotíte ji a určíte druh', {'Zahradník': 3}),
            ('Upravíte režim pastvy, aby místo nebylo poškozeno', {'Chovatel zvířat': 3}),
            ('Posoudíte, zda kosení neohrozí populaci', {'Lesní inženýr': 3})),

        _p2('ZEM', 'V sušině sena najdete jedovatý druh trávy – jak reagujete?',
            ('Identifikujete druh a varujete chovatele', {'Veterinární lékař': 3, 'Chovatel zvířat': 2}),
            ('Upravíte složení luční směsi pro příští rok', {'Agronom': 3}),
            ('Posoudíte důvody šíření invazního druhu', {'Ekolog': 3}),
            ('Přeladíte žací techniku na nižší strniště', {'Zemědělský technik': 3})),

        _p2('ZEM', 'Farmář chce vybudovat nový rybník – vaše role?',
            ('Hydrologický a ekologický posudek lokality', {'Ekolog': 3}),
            ('Technický projekt hráze a výpusti', {'Zemědělský technik': 3, 'Lesní inženýr': 2}),
            ('Plán osázení břehů dřevinami a trvalkami', {'Zahradník': 3}),
            ('Posouzení vlivu na migraci zvěře', {'Myslivec': 3})),

        _p2('ZEM', 'Při dojení se objeví mléko s příměsí krve – co je priorita?',
            ('Vyšetřit vemeno na mastitidu', {'Veterinární lékař': 4}),
            ('Zkontrolovat nastavení dojicího stroje', {'Zemědělský technik': 3}),
            ('Izolovat krávu a upravit krmení', {'Chovatel zvířat': 3}),
            ('Odeslat vzorek mléka do laboratoře', {'Agronom': 2, 'Veterinární lékař': 2})),

        _p2('ZEM', 'Obec chce revitalizovat alej podél cesty – co navrhujete?',
            ('Výběr vhodných druhů stromů a výsadbový plán', {'Zahradník': 3, 'Lesní inženýr': 2}),
            ('Biologické zhodnocení stávající zeleně', {'Ekolog': 3}),
            ('Zajištění techniky pro výsadbu velkých stromů', {'Zemědělský technik': 3}),
            ('Posouzení vlivu aleje na zvěřní migrační koridor', {'Myslivec': 3})),

        _p2('ZEM', 'Potřebujete zvýšit výnos pšenice – jaký postup zvolíte?',
            ('Analýzu půdních vzorků a optimalizaci hnojení', {'Agronom': 4}),
            ('Modernizaci secího stroje na přesný výsev', {'Zemědělský technik': 3}),
            ('Výběr rezistentních odrůd ze šlechtitelského katalogu', {'Agronom': 2, 'Ekolog': 2}),
            ('Zavedení polního zavlažovacího systému', {'Zemědělský technik': 3})),

        _p2('ZEM', 'Les trpí okusem mladých stromků – vaše doporučení?',
            ('Regulaci stavů spárkaté zvěře odstřelem', {'Myslivec': 4}),
            ('Individuální ochranu sazenic oplocením', {'Lesní inženýr': 3}),
            ('Výsadbu odolnějších dřevin, které zvěř neatakuje', {'Zahradník': 3}),
            ('Monitoring tlaku zvěře a mapování škod', {'Ekolog': 3})),

        _p2('ZEM', 'Včelstva v okolí farmy hynou – jak přispějete?',
            ('Omezíte použití insekticidů při postřicích', {'Agronom': 3}),
            ('Vysejete květnaté pásy pro opylovače', {'Zahradník': 3, 'Ekolog': 2}),
            ('Provedete laboratorní vyšetření včelstev', {'Veterinární lékař': 3}),
            ('Navrhnete biokoridory v krajině', {'Ekolog': 3})),

        # --- Další pracovní činnosti ---
        _p2('ZEM', 'Jak byste přistoupili k tvorbě nového pastvního systému?',
            ('Rozdělením pastvin na sektory s rotací', {'Chovatel zvířat': 3}),
            ('Výběrem vhodných travních směsí pro dosévy', {'Agronom': 3}),
            ('Stavbou a údržbou ohradníků a napajedel', {'Zemědělský technik': 3}),
            ('Posouzením únosnosti pastvy pro ekosystém', {'Ekolog': 3})),

        _p2('ZEM', 'Při inventarizaci lesa by vaše práce byla:',
            ('Měření výšek a průměrů stromů pro taxaci', {'Lesní inženýr': 4}),
            ('Sčítání zvěře na transektech', {'Myslivec': 3}),
            ('Záznam výskytu chráněných živočichů', {'Ekolog': 3}),
            ('Hodnocení zdravotního stavu stromů', {'Zahradník': 3, 'Lesní inženýr': 2})),

        _p2('ZEM', 'Jak byste zhodnotili nový krmný přídavek?',
            ('Klinickými testy na skupině zvířat', {'Veterinární lékař': 3}),
            ('Sledováním přírůstků a konverze krmiva', {'Chovatel zvířat': 3}),
            ('Laboratorním rozborem složení krmiva', {'Agronom': 3}),
            ('Analýzou nákladů a návratnosti investice', {'Zemědělský technik': 3})),

        _p2('ZEM', 'Při výsadbě nového sadu byste se starali o:',
            ('Výběr odrůd podle klimatu a půdy', {'Zahradník': 3, 'Agronom': 2}),
            ('Oplocení sadu proti zvěři', {'Myslivec': 3}),
            ('Přípravu techniky pro hloubení jam', {'Zemědělský technik': 3}),
            ('Začlenění sadu do krajinného plánu', {'Ekolog': 3})),

        _p2('ZEM', 'Na farmě se zavádí biogazová stanice – vaše úloha?',
            ('Posouzení vhodných vstupních surovin z rostlinné výroby', {'Agronom': 3}),
            ('Technický dozor nad instalací a provozem', {'Zemědělský technik': 4}),
            ('Hodnocení ekologických přínosů a rizik', {'Ekolog': 3}),
            ('Kontrola, zda digestát neškodí zvířatům na pastvinách', {'Veterinární lékař': 3})),

        # --- Nástroje a technologie (pokračování) ---
        _p2('ZEM', 'Jakou měřicí techniku byste používali nejčastěji?',
            ('Denzitometr pro měření hustoty porostu', {'Lesní inženýr': 3}),
            ('Refraktometr pro měření Brix ve šťávě plodů', {'Zahradník': 3}),
            ('Termokameru pro detekci zánětu u zvířat', {'Veterinární lékař': 3}),
            ('Tenzometry pro měření vlhkosti půdy', {'Agronom': 3})),

        _p2('ZEM', 'Který typ mapy je pro vás nejdůležitější?',
            ('Bonitovaná půdně-ekologická mapa', {'Agronom': 3}),
            ('Lesnická porostní mapa s věkovými třídami', {'Lesní inženýr': 3}),
            ('Mapa výskytu zvěře a loveckých oblastí', {'Myslivec': 3}),
            ('Mapa biotopů a chráněných území', {'Ekolog': 3})),

        _p2('ZEM', 'Jaký typ záznamu vedete nejpečlivěji?',
            ('Výnosové mapy a agronomický deník', {'Agronom': 3}),
            ('Zdravotní karty a vakcinační záznamy zvířat', {'Veterinární lékař': 3, 'Chovatel zvířat': 2}),
            ('Plán mysliveckého hospodaření a statistika lovu', {'Myslivec': 3}),
            ('Protokoly z terénních šetření přírody', {'Ekolog': 3})),

        # --- Hodnoty (pokračování) ---
        _p2('ZEM', 'Co považujete za největší úspěch ve své práci?',
            ('Rekordní výnos při zachování kvality půdy', {'Agronom': 3}),
            ('Záchranu života těžce nemocného zvířete', {'Veterinární lékař': 4}),
            ('Úspěšnou obnovu lesa po kalamitě', {'Lesní inženýr': 3}),
            ('Vytvoření zahrady, která přežije generace', {'Zahradník': 3})),

        _p2('ZEM', 'Jaký přínos vaší práce je pro vás nejcennější?',
            ('Zdravá a bezpečná zvířata ve stádě', {'Chovatel zvířat': 3}),
            ('Stabilní a rozmanitá populace zvěře v revíru', {'Myslivec': 3}),
            ('Ozdravení degradovaného ekosystému', {'Ekolog': 4}),
            ('Fungující a spolehlivý strojový park', {'Zemědělský technik': 3})),

        _p2('ZEM', 'Co byste chtěli po sobě zanechat?',
            ('Úrodnou půdu pro budoucí generace', {'Agronom': 3, 'Ekolog': 2}),
            ('Zdravé lesní porosty odolné klimatickým změnám', {'Lesní inženýr': 3}),
            ('Tradici odpovědného lovectví', {'Myslivec': 3}),
            ('Krásné parky a zahrady ve městech', {'Zahradník': 3})),

        # --- Řešení problémů (pokračování) ---
        _p2('ZEM', 'Těžké sucho ohrožuje úrodu – co doporučíte?',
            ('Přechod na suchu odolné odrůdy a minimální zpracování', {'Agronom': 3}),
            ('Instalaci kapkové závlahy z akumulačních nádrží', {'Zemědělský technik': 3}),
            ('Výsadbu stínících stromů v agrolesnictví', {'Lesní inženýr': 3, 'Ekolog': 2}),
            ('Mulčování záhonů pro zadržení vody', {'Zahradník': 3})),

        _p2('ZEM', 'V chovu drůbeže propuká ptačí chřipka – jak jednáte?',
            ('Nařizuji karanténu a odebírám vzorky na diagnostiku', {'Veterinární lékař': 4}),
            ('Dezinfekuji prostory a zajišťuji hermetizaci hal', {'Zemědělský technik': 3}),
            ('Upravuji krmení a posiluji imunitu stáda', {'Chovatel zvířat': 3}),
            ('Sleduji migraci volně žijících ptáků jako vektor nákazy', {'Ekolog': 3})),

        _p2('ZEM', 'Jarní mrazy poškodily květy ovocných stromů. Co uděláte?',
            ('Hodnotíte škody a plánujete náhradní výsadbu', {'Zahradník': 3}),
            ('Navrhujete systém protimrazové ochrany – postřiky, ohřev', {'Zemědělský technik': 3}),
            ('Vybíráte pozdně kvetoucí odrůdy do dalšího roku', {'Agronom': 3}),
            ('Zajistíte přikrmení opylovačů s nedostatkem nektaru', {'Ekolog': 3})),

        _p2('ZEM', 'Na pastvině se objevil invazní bolševník – vaše řešení?',
            ('Mechanická likvidace a monitoring dalších ohnisek', {'Ekolog': 3}),
            ('Herbicidní ošetření cílenými přípravky', {'Agronom': 3}),
            ('Přemístění zvířat na bezpečnou pastvinu', {'Chovatel zvířat': 3}),
            ('Zabezpečení prostoru před kontaktem dětí s rostlinou', {'Zahradník': 3})),

        # --- Styl interakce (pokračování) ---
        _p2('ZEM', 'Jak reagujete, když uvidíte zraněného zajíce na poli?',
            ('Pokusím se ho odchytit a zajistit veterinární pomoc', {'Veterinární lékař': 3}),
            ('Zaznamenám nález a kontaktuji myslivce', {'Myslivec': 3}),
            ('Dokumentuji pro ekologický monitoring populace', {'Ekolog': 3}),
            ('Prověřím, zda nebyl zraněn mechanizací', {'Zemědělský technik': 3})),

        _p2('ZEM', 'Školní třída přijede na exkurzi na farmu – co jim ukážete?',
            ('Jak se pěstuje obilí od setí po sklizeň', {'Agronom': 3}),
            ('Stáj a jak se správně pečuje o zvířata', {'Chovatel zvířat': 3}),
            ('Jak funguje traktor a sklízecí mlátička', {'Zemědělský technik': 3}),
            ('Zahradu s bylinkami a ukázku kompostování', {'Zahradník': 3})),

        _p2('ZEM', 'Jak se zapojíte do komunitního projektu údržby krajiny?',
            ('Poradím s výsadbou krajinných prvků a remízků', {'Lesní inženýr': 3}),
            ('Dovedu dobrovolníky při sčítání ptáků', {'Ekolog': 3}),
            ('Pomůžu s údržbou krmných políček pro zvěř', {'Myslivec': 3}),
            ('Navrhnu květinové záhony pro veřejný prostor', {'Zahradník': 3})),

        # --- Specifické úkoly a situace ---
        _p2('ZEM', 'Při plánování nového roku na farmě byste se zaměřili na:',
            ('Osevní plán, přípravu osiv a hnojení', {'Agronom': 3}),
            ('Plán inseminace a reprodukce stáda', {'Chovatel zvířat': 3, 'Veterinární lékař': 2}),
            ('Servis a obnovu strojového parku', {'Zemědělský technik': 3}),
            ('Plán péče o zeleň a ozdobné výsadby', {'Zahradník': 3})),

        _p2('ZEM', 'Jaké téma diplomové práce byste zvolili?',
            ('Vliv střídání plodin na výskyt chorob obilnin', {'Agronom': 3}),
            ('Porovnání anestetických protokolů u psů', {'Veterinární lékař': 4}),
            ('Obnova přirozené skladby lesů po kalamitě', {'Lesní inženýr': 3}),
            ('Management populací jelení zvěře v Čechách', {'Myslivec': 3})),

        _p2('ZEM', 'Co děláte jako první ráno při příchodu do práce?',
            ('Kontroluji stav plodin a počasí na webu', {'Agronom': 3}),
            ('Obcházím stáj a kontroluji zvířata', {'Chovatel zvířat': 3}),
            ('Startuji stroje a kontroluji provozní kapaliny', {'Zemědělský technik': 3}),
            ('Procházím skleník a zalévám rostliny', {'Zahradník': 3})),

        _p2('ZEM', 'Na jakou otázku hledáte odpověď nejčastěji?',
            ('Které odrůdy jsou nejvýnosnější pro naše podmínky?', {'Agronom': 3}),
            ('Jaká je příčina chřadnutí tohoto zvířete?', {'Veterinární lékař': 3}),
            ('Jak rychle tento porost dorůstá mýtního věku?', {'Lesní inženýr': 3}),
            ('Jak se vyvíjí biodiverzita v naší lokalitě?', {'Ekolog': 3})),

        _p2('ZEM', 'Při cestě na pracoviště pozorujete krajinu. Co si všímáte?',
            ('Stavu porostů a fáze vývoje plodin', {'Agronom': 3}),
            ('Stop zvěře a značek zvířat v terénu', {'Myslivec': 3}),
            ('Kvality a pestrosti zeleně podél cest', {'Zahradník': 3}),
            ('Stavu přírodních biotopů a vodních toků', {'Ekolog': 3})),

        _p2('ZEM', 'Co vás inspiruje k inovacím?',
            ('Nové technologie v precizním zemědělství', {'Zemědělský technik': 3, 'Agronom': 2}),
            ('Moderní diagnostické metody ve veterinární medicíně', {'Veterinární lékař': 3}),
            ('Přírodě blízké hospodaření v lesích Skandinávie', {'Lesní inženýr': 3}),
            ('Zahraniční projekty obnovy biodiverzity', {'Ekolog': 3})),

        # ══════════════ STA: Stavebnictví a architektura (81–160) ══════════════
        # --- Pracovní činnosti ---
        _p2('STA', 'Jakou činnost byste na stavbě vykonávali nejraději?',
            ('Navrhování vzhledu a dispozice budovy', {'Architekt': 3}),
            ('Koordinaci pracovních čet a subdodavatelů', {'Stavbyvedoucí': 3}),
            ('Zdění nosných stěn a příček', {'Zedník': 3}),
            ('Montáž vodovodních a odpadních rozvodů', {'Instalatér': 3})),

        _p2('STA', 'Která pracovní náplň ve stavebnictví vás láká nejvíce?',
            ('Zpracování projektové dokumentace a statických výpočtů', {'Projektant': 3}),
            ('Zaměřování pozemků a vytváření geodetických map', {'Geodet': 3}),
            ('Sestavování rozpočtů a cenových nabídek', {'Rozpočtář staveb': 3}),
            ('Navrhování interiérů a výběr materiálů', {'Interiérový designér': 3})),

        _p2('STA', 'Co byste nejraději dělali při rekonstrukci domu?',
            ('Vytvářeli architektonický koncept přestavby', {'Architekt': 3}),
            ('Řídili postup prací a hlídali harmonogram', {'Stavbyvedoucí': 3}),
            ('Omítali stěny a pokládali obklady', {'Zedník': 3}),
            ('Zapojovali topení a radiátory', {'Instalatér': 3})),

        _p2('STA', 'Jak byste se zapojili do výstavby obchodního centra?',
            ('Kalkulací celkových nákladů stavby', {'Rozpočtář staveb': 3}),
            ('Vytvořením podrobné výkresové dokumentace', {'Projektant': 3}),
            ('Zaměřením staveniště a kontrolou přesnosti', {'Geodet': 3}),
            ('Návrhem designu obchodních prostor', {'Interiérový designér': 3})),

        _p2('STA', 'Co vás baví na práci s budovami?',
            ('Hledání esteticky i funkčně dokonalého tvaru', {'Architekt': 3, 'Interiérový designér': 2}),
            ('Přeměna výkresů v reálnou stavbu vlastníma rukama', {'Zedník': 3}),
            ('Organizace celého stavebního procesu', {'Stavbyvedoucí': 3}),
            ('Technické řešení rozvodů vody a tepla', {'Instalatér': 3})),

        _p2('STA', 'Jakou roli byste chtěli při stavbě rodinného domu?',
            ('Navrhnout dispozici a fasádu domu', {'Architekt': 3}),
            ('Spočítat materiálové a finanční náklady', {'Rozpočtář staveb': 3}),
            ('Provádět betonáž základů a podlah', {'Zedník': 3}),
            ('Nainstalovat rozvody pitné a teplé vody', {'Instalatér': 3})),

        _p2('STA', 'Co by vás nejvíc bavilo na urbanistickém projektu?',
            ('Navrhování celkové koncepce zástavby', {'Architekt': 3}),
            ('Geodetické zaměření území a výškopis', {'Geodet': 3}),
            ('Zpracování technické dokumentace inženýrských sítí', {'Projektant': 3}),
            ('Řízení realizace a stavební dozor', {'Stavbyvedoucí': 3})),

        _p2('STA', 'Při výstavbě mostu byste nejraději…',
            ('Vypočítali únosnost a navrhli konstrukci', {'Projektant': 3, 'Architekt': 2}),
            ('Koordinovali práce jeřábů a bednění', {'Stavbyvedoucí': 3}),
            ('Zaměřovali a kontrolovali geometrii pilířů', {'Geodet': 3}),
            ('Vytvořili položkový rozpočet stavby', {'Rozpočtář staveb': 3})),

        _p2('STA', 'Co vás přitahuje na práci v interiérech?',
            ('Výběr barev, tapet a osvětlení', {'Interiérový designér': 3}),
            ('Kladení dlažby a obkladů', {'Zedník': 3}),
            ('Instalace podlahového topení', {'Instalatér': 3}),
            ('Návrh dispozičního řešení místností', {'Architekt': 3})),

        _p2('STA', 'Kterou část stavebního projektu byste rádi zajišťovali?',
            ('Výběrové řízení na dodavatele a porovnávání nabídek', {'Rozpočtář staveb': 3}),
            ('Kontrolu souladu stavby s projektem', {'Stavbyvedoucí': 3}),
            ('Katastrální zaměření hranic pozemku', {'Geodet': 3}),
            ('Návrh a vizualizaci koupelny', {'Interiérový designér': 3})),

        # --- Pracovní prostředí ---
        _p2('STA', 'V jakém prostředí byste chtěli pracovat?',
            ('V architektonickém ateliéru u výkresů a modelů', {'Architekt': 3}),
            ('Přímo na staveništi v terénu', {'Stavbyvedoucí': 3, 'Zedník': 2}),
            ('V kanceláři s výpočetní technikou a CAD softwarem', {'Projektant': 3}),
            ('V showroomu s ukázkami materiálů a nábytku', {'Interiérový designér': 3})),

        _p2('STA', 'Kde se cítíte nejlépe při práci?',
            ('Na lešení při omítání fasády', {'Zedník': 3}),
            ('V kotelně při montáži potrubí', {'Instalatér': 3}),
            ('Venku s teodolitem a GPS přijímačem', {'Geodet': 3}),
            ('U stolu nad rozpočtovými tabulkami', {'Rozpočtář staveb': 3})),

        _p2('STA', 'Jaké pracovní podmínky vám vyhovují?',
            ('Kreativní atmosféra designového studia', {'Interiérový designér': 3, 'Architekt': 2}),
            ('Dynamické prostředí velkého staveniště', {'Stavbyvedoucí': 3}),
            ('Přesná práce v terénu za každého počasí', {'Geodet': 3}),
            ('Fyzicky náročná práce s cihlami a maltou', {'Zedník': 3})),

        _p2('STA', 'Kde byste trávili svůj typický pracovní den?',
            ('Střídavě na stavbě a v kanceláři při koordinaci', {'Stavbyvedoucí': 3}),
            ('V projekční kanceláři nad výkresy', {'Projektant': 3}),
            ('Na stavbě při instalaci a údržbě rozvodů', {'Instalatér': 3}),
            ('Na terénních měřeních pro katastr', {'Geodet': 3})),

        _p2('STA', 'Jaká pracovní atmosféra vám sedí?',
            ('Týmová spolupráce řemeslníků na stavbě', {'Zedník': 3, 'Instalatér': 2}),
            ('Samostatná kreativní práce nad návrhy', {'Architekt': 3}),
            ('Analytická práce s čísly a cenami', {'Rozpočtář staveb': 3}),
            ('Setkávání s klienty a prezentace návrhů', {'Interiérový designér': 3})),

        # --- Nástroje a technologie ---
        _p2('STA', 'S jakými nástroji byste chtěli pracovat?',
            ('S CAD softwarem pro 3D modelování budov', {'Architekt': 3, 'Projektant': 2}),
            ('S nivelačním přístrojem a totální stanicí', {'Geodet': 3}),
            ('Se zednickou lžící, vodováhou a míchačkou', {'Zedník': 3}),
            ('S klešťovými kleštěmi a páječkou na trubky', {'Instalatér': 3})),

        _p2('STA', 'Která technologie vás nejvíce zajímá?',
            ('BIM – informační model budovy', {'Projektant': 3, 'Architekt': 2}),
            ('Dron pro letecké zaměřování staveniště', {'Geodet': 3}),
            ('Software pro automatické oceňování staveb', {'Rozpočtář staveb': 3}),
            ('Vizualizační programy pro návrhy interiérů', {'Interiérový designér': 3})),

        _p2('STA', 'Jaký software byste se chtěli naučit?',
            ('ArchiCAD nebo Revit pro architektonické návrhy', {'Architekt': 3}),
            ('AutoCAD pro technické výkresy', {'Projektant': 3}),
            ('KROS pro stavební rozpočty', {'Rozpočtář staveb': 3}),
            ('SketchUp pro vizualizaci interiérů', {'Interiérový designér': 3})),

        _p2('STA', 'S jakým vybavením byste rádi pracovali denně?',
            ('S laserovou rotační nivelací', {'Geodet': 3}),
            ('S řezačkou obkladů a maltovací pistolí', {'Zedník': 3}),
            ('S tlakovacím čerpadlem pro zkoušky potrubí', {'Instalatér': 3}),
            ('S plánovacím softwarem pro stavby', {'Stavbyvedoucí': 3})),

        _p2('STA', 'Který nástroj považujete za nejdůležitější?',
            ('Projekční software pro statické výpočty', {'Projektant': 3}),
            ('Tabulkový procesor pro kalkulace nákladů', {'Rozpočtář staveb': 3}),
            ('3D tiskárnu pro makety budov', {'Architekt': 3}),
            ('Vzorkovník materiálů a barev', {'Interiérový designér': 3})),

        # --- Dovednosti a schopnosti ---
        _p2('STA', 'Jaká dovednost je ve stavebnictví vaší silnou stránkou?',
            ('Prostorová představivost a smysl pro estetiku', {'Architekt': 3}),
            ('Organizační schopnosti a vedení lidí', {'Stavbyvedoucí': 3}),
            ('Přesnost při měření a výpočtech', {'Geodet': 3, 'Projektant': 2}),
            ('Zručnost a manuální šikovnost', {'Zedník': 3})),

        _p2('STA', 'Která schopnost vás nejlépe vystihuje?',
            ('Dokážu rychle kalkulovat náklady v hlavě', {'Rozpočtář staveb': 3}),
            ('Mám cit pro barvy a kompozici', {'Interiérový designér': 3}),
            ('Umím číst a kreslit technické výkresy', {'Projektant': 3}),
            ('Zvládám práci s potrubím a armaturami', {'Instalatér': 3})),

        _p2('STA', 'Co považujete za svou nejcennější schopnost?',
            ('Schopnost vizualizovat hotovou stavbu z plánu', {'Architekt': 3}),
            ('Schopnost řídit více činností současně', {'Stavbyvedoucí': 3}),
            ('Preciznost při geodetickém měření', {'Geodet': 3}),
            ('Schopnost pracovat s rozpočtovými položkami', {'Rozpočtář staveb': 3})),

        _p2('STA', 'Jaká vlastnost je pro práci ve stavebnictví klíčová?',
            ('Kreativita při navrhování prostor', {'Interiérový designér': 3, 'Architekt': 2}),
            ('Fyzická zdatnost a vytrvalost', {'Zedník': 3}),
            ('Technická zručnost při montáži', {'Instalatér': 3}),
            ('Analytické myšlení pro statiku', {'Projektant': 3})),

        _p2('STA', 'V čem vynikáte oproti ostatním?',
            ('V komunikaci s klienty a prezentaci návrhů', {'Architekt': 3, 'Interiérový designér': 2}),
            ('V řešení logistických problémů na stavbě', {'Stavbyvedoucí': 3}),
            ('V práci s mapovými podklady a souřadnicemi', {'Geodet': 3}),
            ('Ve vyjednávání cen s dodavateli', {'Rozpočtář staveb': 3})),

        # --- Hodnoty a motivace ---
        _p2('STA', 'Co vás ve stavebnictví motivuje nejvíce?',
            ('Vytvořit stavbu, která změní podobu města', {'Architekt': 3}),
            ('Úspěšně dokončit stavbu v termínu a rozpočtu', {'Stavbyvedoucí': 3}),
            ('Vidět, jak se z výkresů stane realita', {'Projektant': 3}),
            ('Vytvořit útulný a funkční prostor pro lidi', {'Interiérový designér': 3})),

        _p2('STA', 'Proč byste chtěli pracovat ve stavebnictví?',
            ('Baví mě fyzicky náročná a viditelná práce', {'Zedník': 3}),
            ('Chci zajistit lidem fungující vodu a topení', {'Instalatér': 3}),
            ('Rád pracuji s přesnými měřicími přístroji', {'Geodet': 3}),
            ('Zajímají mě finanční stránky stavebních projektů', {'Rozpočtář staveb': 3})),

        _p2('STA', 'Co je pro vás na práci nejdůležitější?',
            ('Estetický dojem a harmonie budovy s okolím', {'Architekt': 3}),
            ('Bezpečnost a kvalita provedení stavby', {'Stavbyvedoucí': 3, 'Zedník': 2}),
            ('Přesnost a spolehlivost technického řešení', {'Projektant': 3}),
            ('Spokojenost klienta s výsledným interiérem', {'Interiérový designér': 3})),

        _p2('STA', 'Co vás žene k lepšímu výkonu?',
            ('Uznání za originální architektonický návrh', {'Architekt': 3}),
            ('Hladký průběh stavby bez komplikací', {'Stavbyvedoucí': 3}),
            ('Přesný rozpočet bez odchylek', {'Rozpočtář staveb': 3}),
            ('Perfektně funkční instalace bez úniků', {'Instalatér': 3})),

        _p2('STA', 'Jaký přínos chcete mít pro společnost?',
            ('Navrhovat udržitelné a ekologické budovy', {'Architekt': 3, 'Projektant': 2}),
            ('Přesně dokumentovat hranice pozemků', {'Geodet': 3}),
            ('Stavět kvalitní a trvanlivé zdi a konstrukce', {'Zedník': 3}),
            ('Šetřit klientům peníze chytrými návrhy interiérů', {'Interiérový designér': 3})),

        # --- Řešení problémů ---
        _p2('STA', 'Jak byste řešili zpoždění stavby o dva týdny?',
            ('Přeorganizoval harmonogram a nasadil více čet', {'Stavbyvedoucí': 3}),
            ('Hledal úspory v rozpočtu pro urychlení', {'Rozpočtář staveb': 3}),
            ('Upravil projektovou dokumentaci pro zjednodušení', {'Projektant': 3}),
            ('Nabídl nadčasy a osobně pomohl se zděním', {'Zedník': 3})),

        _p2('STA', 'Na stavbě se objevila prasklina ve zdi – co uděláte?',
            ('Posoudím statiku a navrhnu sanaci', {'Projektant': 3}),
            ('Zaměřím deformaci a sleduju její vývoj', {'Geodet': 3}),
            ('Opravu praskliny provedu výztužnou maltou', {'Zedník': 3}),
            ('Zkontroluju, zda prasklina nezasahuje rozvody', {'Instalatér': 3})),

        _p2('STA', 'Klient chce změnit dispozici bytu v průběhu stavby – jak reagujete?',
            ('Navrhnu novou dispozici respektující nosné zdi', {'Architekt': 3}),
            ('Přepočítám dopad změny na rozpočet', {'Rozpočtář staveb': 3}),
            ('Upravím termíny a koordinaci řemesel', {'Stavbyvedoucí': 3}),
            ('Předělám návrh interiéru dle nového půdorysu', {'Interiérový designér': 3})),

        _p2('STA', 'Při kopání základů narazíte na podzemní vodu – co navrhnete?',
            ('Geodetický průzkum hladiny spodní vody', {'Geodet': 3}),
            ('Změnu projektu na jinou technologii zakládání', {'Projektant': 3}),
            ('Kalkulaci víceprací a úpravu rozpočtu', {'Rozpočtář staveb': 3}),
            ('Koordinaci čerpání vody a úpravu postupu', {'Stavbyvedoucí': 3})),

        _p2('STA', 'V bytě neteče teplá voda – jak postupujete?',
            ('Zkontroluju kotel, čerpadlo a termostat', {'Instalatér': 3}),
            ('Zkontroluji, zda je potrubí správně zaizolováno', {'Instalatér': 2, 'Projektant': 2}),
            ('Zjistím náklady na opravu nebo výměnu', {'Rozpočtář staveb': 3}),
            ('Provedu kontrolní měření teploty v potrubí', {'Geodet': 2, 'Instalatér': 2})),

        # --- Vzdělání a rozvoj ---
        _p2('STA', 'Jaký kurz byste si vybrali?',
            ('Architektonický design a kompozice', {'Architekt': 3}),
            ('Řízení stavební výroby a plánování', {'Stavbyvedoucí': 3}),
            ('Statika a dimenzování konstrukcí', {'Projektant': 3}),
            ('Moderní trendy v interiérovém designu', {'Interiérový designér': 3})),

        _p2('STA', 'Kterou odbornou literaturu byste četli?',
            ('Knihy o slavných architektonických dílech', {'Architekt': 3}),
            ('Příručku geodetického měření a kartografie', {'Geodet': 3}),
            ('Ceníky stavebních prací a materiálů', {'Rozpočtář staveb': 3}),
            ('Návody na správnou instalaci potrubních systémů', {'Instalatér': 3})),

        _p2('STA', 'Jaký seminář byste navštívili?',
            ('Pasivní a nízkoenergetické domy', {'Architekt': 3, 'Projektant': 2}),
            ('Bezpečnost a ochrana zdraví na stavbách', {'Stavbyvedoucí': 3}),
            ('Nové zdicí materiály a technologie', {'Zedník': 3}),
            ('Rozpočtování veřejných zakázek', {'Rozpočtář staveb': 3})),

        _p2('STA', 'Co byste studovali na vysoké škole?',
            ('Architekturu a urbanismus', {'Architekt': 3}),
            ('Stavební inženýrství – konstrukce a dopravní stavby', {'Projektant': 3}),
            ('Geodézii a kartografii', {'Geodet': 3}),
            ('Ekonomiku a řízení stavebnictví', {'Rozpočtář staveb': 3, 'Stavbyvedoucí': 2})),

        _p2('STA', 'Jakou praxi byste si vybrali?',
            ('Stáž v architektonickém ateliéru', {'Architekt': 3}),
            ('Praxi na stavbě pod vedením stavbyvedoucího', {'Stavbyvedoucí': 3, 'Zedník': 2}),
            ('Praxi u geodetické firmy', {'Geodet': 3}),
            ('Stáž v designovém studiu', {'Interiérový designér': 3})),

        # --- Týmová práce ---
        _p2('STA', 'Jakou roli zastáváte v týmu na stavbě?',
            ('Lídr, který koordinuje všechny profese', {'Stavbyvedoucí': 3}),
            ('Tvůrčí mozek s originálními nápady', {'Architekt': 3}),
            ('Pečlivý plánovač rozpočtu a zdrojů', {'Rozpočtář staveb': 3}),
            ('Spolehlivý řemeslník, co dotáhne práci do konce', {'Zedník': 3})),

        _p2('STA', 'Jak přispíváte k úspěchu stavebního projektu?',
            ('Přesnou projektovou dokumentací bez chyb', {'Projektant': 3}),
            ('Přesným zaměřením a vytyčením stavby', {'Geodet': 3}),
            ('Kvalitní montáží technického zařízení', {'Instalatér': 3}),
            ('Návrhem příjemného a funkčního prostředí', {'Interiérový designér': 3})),

        _p2('STA', 'S kým nejraději spolupracujete?',
            ('S investorem při ladění architektonické vize', {'Architekt': 3}),
            ('S řemeslníky při denním řízení stavby', {'Stavbyvedoucí': 3}),
            ('S dodavateli při vyjednávání cen', {'Rozpočtář staveb': 3}),
            ('S klientem při výběru vybavení interiéru', {'Interiérový designér': 3})),

        _p2('STA', 'Jak reagujete na konflikt na stavbě mezi profesemi?',
            ('Svolám koordinační poradu a vyřeším spor', {'Stavbyvedoucí': 3}),
            ('Ověřím v projektu, kdo má pravdu', {'Projektant': 3}),
            ('Navrhnu kompromis v nákladech', {'Rozpočtář staveb': 3}),
            ('Pomohu prakticky s řešením na místě', {'Zedník': 3, 'Instalatér': 2})),

        _p2('STA', 'Co oceňujete u kolegů ve stavebnictví?',
            ('Kreativitu a odvahu zkoušet nové přístupy', {'Architekt': 3, 'Interiérový designér': 2}),
            ('Spolehlivost a dodržování termínů', {'Stavbyvedoucí': 3}),
            ('Přesnost a pečlivost v detailech', {'Geodet': 3, 'Projektant': 2}),
            ('Řemeslnou zručnost a pracovitost', {'Zedník': 3})),

        # --- Situační otázky ---
        _p2('STA', 'Dostanete zakázku na novostavbu školy – co uděláte první?',
            ('Navrhnu koncept budovy a její zasazení do okolí', {'Architekt': 3}),
            ('Zaměřím pozemek a prověřím terénní podmínky', {'Geodet': 3}),
            ('Připravím předběžný rozpočet stavby', {'Rozpočtář staveb': 3}),
            ('Naplánuji fáze výstavby a objednám materiál', {'Stavbyvedoucí': 3})),

        _p2('STA', 'Obec chce revitalizovat náměstí – jaká je vaše role?',
            ('Vytvořím urbanistický návrh s novým mobiliářem', {'Architekt': 3}),
            ('Zpracuji technickou dokumentaci zpevněných ploch', {'Projektant': 3}),
            ('Provedu polohopisné a výškopisné zaměření', {'Geodet': 3}),
            ('Navrhnu osvětlení a materiály povrchů', {'Interiérový designér': 2, 'Architekt': 2})),

        _p2('STA', 'Při kontrolním dni zjistíte nedostatky v kvalitě zdiva – co uděláte?',
            ('Nařídím opravu a zapíšu do stavebního deníku', {'Stavbyvedoucí': 3}),
            ('Osobně předělám špatně vyzděný úsek', {'Zedník': 3}),
            ('Posoudím vliv na statiku konstrukce', {'Projektant': 3}),
            ('Přepočítám náklady na opravu', {'Rozpočtář staveb': 3})),

        _p2('STA', 'Zákazník si přeje luxusní koupelnu – jak postupujete?',
            ('Navrhnu design s prémiovou dlažbou a sanitou', {'Interiérový designér': 3}),
            ('Připravím rozvody vody, odpadu a podlahového topení', {'Instalatér': 3}),
            ('Obložím stěny velkoformátovým obkladem', {'Zedník': 3}),
            ('Zpracuji detailní rozpočet materiálu a prací', {'Rozpočtář staveb': 3})),

        _p2('STA', 'Na stavbě bytového domu je třeba řešit parkování – co navrhujete?',
            ('Architektonické řešení podzemních garáží', {'Architekt': 3}),
            ('Statické posouzení podzemní konstrukce', {'Projektant': 3}),
            ('Zaměření úrovní terénu pro sjezd do garáží', {'Geodet': 3}),
            ('Organizaci výkopových prací a odvoz zeminy', {'Stavbyvedoucí': 3})),

        # --- Specializace a preference ---
        _p2('STA', 'Jaký typ stavby vás láká nejvíce?',
            ('Výškové budovy s originální architekturou', {'Architekt': 3}),
            ('Průmyslové haly s velkými rozpony', {'Projektant': 3}),
            ('Rodinné domy se zahradou', {'Zedník': 3, 'Instalatér': 2}),
            ('Hotely a restaurace s designovými interiéry', {'Interiérový designér': 3})),

        _p2('STA', 'V jaké fázi stavby se cítíte nejužitečnější?',
            ('Na začátku – při tvorbě konceptu a studie', {'Architekt': 3}),
            ('Při realizaci – na stavbě mezi dělníky', {'Stavbyvedoucí': 3, 'Zedník': 2}),
            ('Při dokončování – finální úpravy interiéru', {'Interiérový designér': 3}),
            ('Před stavbou – při přípravě rozpočtu a smluv', {'Rozpočtář staveb': 3})),

        _p2('STA', 'Co vás na stavařině fascinuje?',
            ('Spojení techniky a umění v architektuře', {'Architekt': 3}),
            ('Přesnost geodetických měření na milimetry', {'Geodet': 3}),
            ('Proměna surového materiálu v hotovou stěnu', {'Zedník': 3}),
            ('Fungující systém rozvodů ukrytý ve zdech', {'Instalatér': 3})),

        _p2('STA', 'Jaký projekt byste chtěli vést?',
            ('Stavbu nového koncertního sálu', {'Architekt': 3, 'Stavbyvedoucí': 2}),
            ('Rekonstrukci historické památky', {'Projektant': 3, 'Zedník': 2}),
            ('Výstavbu rezidenčního komplexu s bazénem', {'Instalatér': 2, 'Interiérový designér': 2}),
            ('Katastrální mapování celé obce', {'Geodet': 3})),

        _p2('STA', 'Jaký aspekt stavby vás zajímá nejvíce?',
            ('Energetická účinnost a zateplení', {'Projektant': 3, 'Architekt': 2}),
            ('Požární bezpečnost a únikové cesty', {'Stavbyvedoucí': 3}),
            ('Akustika a zvuková izolace interiérů', {'Interiérový designér': 3}),
            ('Hydroizolace a odvodnění základů', {'Zedník': 3, 'Instalatér': 2})),

        # --- Další pracovní situace ---
        _p2('STA', 'Jak byste prezentovali stavební projekt investorovi?',
            ('3D vizualizací a animací budovy', {'Architekt': 3}),
            ('Podrobným harmonogramem s milníky', {'Stavbyvedoucí': 3}),
            ('Detailním položkovým rozpočtem', {'Rozpočtář staveb': 3}),
            ('Vizualizací interiérů s materiálovými vzorky', {'Interiérový designér': 3})),

        _p2('STA', 'Co děláte, když zjistíte nesoulad mezi výkresem a skutečností?',
            ('Provedu kontrolní zaměření a porovnám data', {'Geodet': 3}),
            ('Upravím projektovou dokumentaci', {'Projektant': 3}),
            ('Okamžitě zastavím práce a informuji vedení', {'Stavbyvedoucí': 3}),
            ('Přepočítám dopad na celkový rozpočet', {'Rozpočtář staveb': 3})),

        _p2('STA', 'Jakou inovaci byste zavedli na stavbě?',
            ('Použití prefabrikovaných modulů', {'Projektant': 3, 'Stavbyvedoucí': 2}),
            ('Smart home technologie v interiérech', {'Interiérový designér': 3}),
            ('Použití dronu pro sledování postupu prací', {'Geodet': 3}),
            ('Nové izolační materiály do zdí', {'Zedník': 3})),

        _p2('STA', 'Co kontrolujete na stavbě jako první?',
            ('Soulad provedení s projektovou dokumentací', {'Stavbyvedoucí': 3, 'Projektant': 2}),
            ('Geometrickou přesnost konstrukcí', {'Geodet': 3}),
            ('Těsnost vodovodních a plynových spojů', {'Instalatér': 3}),
            ('Kvalitu malty a vazbu cihel', {'Zedník': 3})),

        _p2('STA', 'Jak přistupujete k ekologii ve stavebnictví?',
            ('Navrhuji budovy s minimální uhlíkovou stopou', {'Architekt': 3}),
            ('Hledám ekologické materiály za rozumnou cenu', {'Rozpočtář staveb': 3}),
            ('Používám recyklované stavební hmoty', {'Zedník': 3}),
            ('Instaluji systémy na využití dešťové vody', {'Instalatér': 3})),

        _p2('STA', 'Jak řešíte nedostatek materiálu na stavbě?',
            ('Hledám alternativního dodavatele a porovnávám ceny', {'Rozpočtář staveb': 3}),
            ('Přeorganizuji práce, aby se stavba nezpozdila', {'Stavbyvedoucí': 3}),
            ('Navrhnu alternativní technické řešení', {'Projektant': 3}),
            ('Improvizuji s materiálem, co je k dispozici', {'Zedník': 3})),

        _p2('STA', 'Co je pro vás důležité při výběru povolání ve stavebnictví?',
            ('Možnost tvořit něco krásného a trvalého', {'Architekt': 3, 'Interiérový designér': 2}),
            ('Jistota práce a stabilní příjem', {'Zedník': 3, 'Instalatér': 2}),
            ('Kariérní růst do manažerských pozic', {'Stavbyvedoucí': 3}),
            ('Práce s moderními technologiemi', {'Geodet': 3, 'Projektant': 2})),

        _p2('STA', 'Jakou odpovědnost přijímáte nejraději?',
            ('Za celkový vzhled a koncepci budovy', {'Architekt': 3}),
            ('Za dodržení termínů a bezpečnosti práce', {'Stavbyvedoucí': 3}),
            ('Za správnost technických výpočtů', {'Projektant': 3}),
            ('Za přesnost geodetických podkladů', {'Geodet': 3})),

        _p2('STA', 'Co vás napadne jako první, když vidíte novou budovu?',
            ('Hodnotím proporce, fasádu a zasazení do prostoru', {'Architekt': 3}),
            ('Odhaduji náklady na stavbu', {'Rozpočtář staveb': 3}),
            ('Představuji si, jak bych navrhl interiér', {'Interiérový designér': 3}),
            ('Zajímá mě kvalita zdiva a provedení detailů', {'Zedník': 3})),

        _p2('STA', 'Jak trávíte čas, když čekáte na stavební povolení?',
            ('Dopracovávám architektonické detaily a vizualizace', {'Architekt': 3}),
            ('Precizuji projektovou dokumentaci pro realizaci', {'Projektant': 3}),
            ('Vyjednávám ceny s dodavateli materiálu', {'Rozpočtář staveb': 3}),
            ('Připravuji harmonogram a objednávky mechanizace', {'Stavbyvedoucí': 3})),

        _p2('STA', 'Jaký typ klienta vám vyhovuje nejvíce?',
            ('Klient s jasnou vizí, co chce architektonicky', {'Architekt': 3}),
            ('Developer, který chce rychle a efektivně stavět', {'Stavbyvedoucí': 3, 'Rozpočtář staveb': 2}),
            ('Rodina, která si staví svůj první dům', {'Zedník': 3, 'Instalatér': 2}),
            ('Klient, který dá volnou ruku při designu interiéru', {'Interiérový designér': 3})),

        _p2('STA', 'Jaká část dokumentace vás zajímá nejvíc?',
            ('Architektonická studie s vizualizacemi', {'Architekt': 3}),
            ('Technická zpráva a statický výpočet', {'Projektant': 3}),
            ('Geodetický plán a situační výkres', {'Geodet': 3}),
            ('Výkaz výměr a soupis prací', {'Rozpočtář staveb': 3})),

        _p2('STA', 'Jakou specializaci byste si vybrali v rámci stavebnictví?',
            ('Udržitelná a ekologická architektura', {'Architekt': 3}),
            ('Betonové a železobetonové konstrukce', {'Projektant': 3, 'Zedník': 2}),
            ('Vytápění, ventilace a klimatizace', {'Instalatér': 3}),
            ('Satelitní geodézie a GIS systémy', {'Geodet': 3})),

        _p2('STA', 'Co vás inspiruje k práci ve stavebnictví?',
            ('Slavné stavby – Sagrada Familia, Tančící dům', {'Architekt': 3}),
            ('Megaprojekty – tunely, přehrady, mrakodrapy', {'Stavbyvedoucí': 3, 'Projektant': 2}),
            ('Řemeslná tradice předávaná z generace na generaci', {'Zedník': 3}),
            ('Proměna prázdných prostor v krásné interiéry', {'Interiérový designér': 3})),

        _p2('STA', 'Jaký problém ve stavebnictví byste chtěli vyřešit?',
            ('Nedostatek dostupného bydlení v městech', {'Architekt': 3, 'Rozpočtář staveb': 2}),
            ('Nízkou přesnost stavebních prací', {'Geodet': 3, 'Stavbyvedoucí': 2}),
            ('Zastaralé topenářské systémy v panelových domech', {'Instalatér': 3}),
            ('Nedostatek kvalifikovaných řemeslníků', {'Zedník': 3})),

        _p2('STA', 'Co řešíte při dokončovacích pracích?',
            ('Finální vzhled povrchů a omítek', {'Zedník': 3}),
            ('Napouštění a tlakové zkoušky topení', {'Instalatér': 3}),
            ('Celkovou vizuální koncepci prostoru', {'Interiérový designér': 3}),
            ('Závěrečné zaměření skutečného stavu', {'Geodet': 3})),

        _p2('STA', 'Jak vnímáte digitalizaci ve stavebnictví?',
            ('BIM přináší revoluci v projektování', {'Projektant': 3, 'Architekt': 2}),
            ('Digitální zaměřování zefektivňuje geodezii', {'Geodet': 3}),
            ('Softwarové rozpočtování šetří čas a chyby', {'Rozpočtář staveb': 3}),
            ('Online koordinace zrychluje řízení stavby', {'Stavbyvedoucí': 3})),

        _p2('STA', 'Jak byste řešili zatékání střechou na novostavbě?',
            ('Zaměřím a zdokumentuji místa průsaku', {'Geodet': 3}),
            ('Navrhnu opravu hydroizolace a klempířských prvků', {'Projektant': 3}),
            ('Osobně opravím a přeomítnu viditelné škody', {'Zedník': 3}),
            ('Zajistím, že voda nezasáhla rozvody a kotel', {'Instalatér': 3})),

        _p2('STA', 'Jak přistupujete k práci s historickými stavbami?',
            ('Navrhnu citlivou rekonstrukci respektující původní sloh', {'Architekt': 3}),
            ('Vyberu autentické materiály a barvy do interiéru', {'Interiérový designér': 3}),
            ('Použiji tradiční zednické techniky', {'Zedník': 3}),
            ('Kalkuluji vyšší náklady na restaurátorské práce', {'Rozpočtář staveb': 3})),

        _p2('STA', 'Jaké stavební normy a předpisy vás zajímají?',
            ('Normy pro navrhování konstrukčních systémů', {'Projektant': 3}),
            ('Požární předpisy a únikové cesty', {'Stavbyvedoucí': 3, 'Architekt': 2}),
            ('Geodetické předpisy a katastrální zákon', {'Geodet': 3}),
            ('Normy pro vnitřní vodovodní a kanalizační rozvody', {'Instalatér': 3})),

        _p2('STA', 'Co byste dělali při přípravě stavby dálnice?',
            ('Navrhoval architektonické řešení mostů a tunelů', {'Architekt': 3}),
            ('Zaměřoval trasu a vytyčoval osu komunikace', {'Geodet': 3}),
            ('Zpracoval rozpočet jednotlivých úseků', {'Rozpočtář staveb': 3}),
            ('Koordinoval práce desítek subdodavatelů', {'Stavbyvedoucí': 3})),

        _p2('STA', 'Jak postupujete při stavebně-technickém průzkumu?',
            ('Provedu statický posudek nosných prvků', {'Projektant': 3}),
            ('Zaměřím skutečný stav objektu laserovým skenerem', {'Geodet': 3}),
            ('Zkontroluju stav zdiva, omítek a betonů', {'Zedník': 3}),
            ('Prověřím stav rozvodů vody, topení a plynu', {'Instalatér': 3})),

        _p2('STA', 'Co děláte, když investor překročí schválený rozpočet?',
            ('Hledám úspornější varianty materiálů a technologií', {'Rozpočtář staveb': 3}),
            ('Upravím architektonický návrh k nižším nákladům', {'Architekt': 3}),
            ('Přeplánuji harmonogram pro efektivnější postup', {'Stavbyvedoucí': 3}),
            ('Zjednoduším technické řešení v projektu', {'Projektant': 3})),

        _p2('STA', 'Jaký přístup volíte při navrhování veřejných budov?',
            ('Důraz na bezbariérovost a ergonomii prostor', {'Architekt': 3}),
            ('Zodpovědný přístup k veřejným financím v rozpočtu', {'Rozpočtář staveb': 3}),
            ('Kvalitní materiály a provedení pro vysokou životnost', {'Zedník': 3, 'Instalatér': 2}),
            ('Elegantní a funkční vybavení interiéru', {'Interiérový designér': 3})),

        _p2('STA', 'Jak se udržujete v oboru aktuální?',
            ('Sleduji světové architektonické soutěže a bienále', {'Architekt': 3}),
            ('Studuji nové normy a technické předpisy', {'Projektant': 3, 'Stavbyvedoucí': 2}),
            ('Navštěvuji veletrhy stavebních materiálů a nářadí', {'Zedník': 3, 'Instalatér': 2}),
            ('Testuji nové geodetické přístroje a software', {'Geodet': 3})),

        # ══════════════ STR: Strojírenství a elektrotechnika (81–160) ══════════════

        # --- Pracovní činnosti ---
        _p2('STR', 'Jakou činnost byste ve strojírenství vykonávali nejraději?',
            ('Navrhování strojních součástí v CAD systému', {'Strojní konstruktér': 3}),
            ('Programování CNC obráběcího centra', {'Programátor CNC': 3}),
            ('Svařování ocelových konstrukcí', {'Svářeč': 3}),
            ('Diagnostiku závad elektronických systémů vozidel', {'Autotronik': 3})),

        _p2('STR', 'Která pracovní náplň vás nejvíce láká?',
            ('Vypracování technologických postupů výroby', {'Strojní technolog': 3}),
            ('Návrh a zapojení elektroinstalací', {'Elektrotechnik': 3}),
            ('Soustružení a frézování přesných dílů', {'Obráběč kovů': 3}),
            ('Integrace mechaniky s elektronikou a softwarem', {'Mechatronik': 3})),

        _p2('STR', 'Co byste dělali při vývoji nového stroje?',
            ('Vytvářel 3D model a výrobní dokumentaci', {'Strojní konstruktér': 3}),
            ('Navrhoval optimální výrobní postup', {'Strojní technolog': 3}),
            ('Programoval řídicí systém stroje', {'Mechatronik': 3}),
            ('Svařoval nosný rám dle výkresu', {'Svářeč': 3})),

        _p2('STR', 'Jak byste se zapojili do výroby automobilových dílů?',
            ('Konstrukcí forem a přípravků', {'Strojní konstruktér': 3}),
            ('Programováním obráběcích operací v CAM', {'Programátor CNC': 3}),
            ('Přesným soustružením a broušením dílů', {'Obráběč kovů': 3}),
            ('Testováním elektrických komponentů', {'Elektrotechnik': 3})),

        _p2('STR', 'Co vás na strojírenství baví nejvíc?',
            ('Pevnostní výpočty a simulace zatížení', {'Strojní konstruktér': 3}),
            ('Optimalizace výrobního procesu', {'Strojní technolog': 3}),
            ('Spojování kovů různými metodami svařování', {'Svářeč': 3}),
            ('Opravy a seřizování elektroniky v autě', {'Autotronik': 3})),

        _p2('STR', 'Jakou roli byste chtěli při montáži výrobní linky?',
            ('Navrhnout mechanický layout linky', {'Strojní konstruktér': 3}),
            ('Zapojit silovou a řídící elektroinstalaci', {'Elektrotechnik': 3}),
            ('Naprogramovat PLC a senzory na lince', {'Mechatronik': 3}),
            ('Vyrobit speciální díly na soustruhu', {'Obráběč kovů': 3})),

        _p2('STR', 'Co byste dělali v autoservisu?',
            ('Diagnostiku závad pomocí OBD skeneru', {'Autotronik': 3}),
            ('Svařování výfukových systémů a rámů', {'Svářeč': 3}),
            ('Opravy elektrických systémů a kabeláže', {'Elektrotechnik': 3, 'Autotronik': 2}),
            ('Výrobu náhradních dílů na CNC stroji', {'Programátor CNC': 3})),

        _p2('STR', 'Při výrobě prototypu nového zařízení byste nejraději…',
            ('Kreslil výkresy a 3D modely', {'Strojní konstruktér': 3}),
            ('Určoval materiály a technologické podmínky', {'Strojní technolog': 3}),
            ('Obráběl zkušební kusy na frézce', {'Obráběč kovů': 3}),
            ('Oživoval elektroniku a řídicí software', {'Mechatronik': 3})),

        _p2('STR', 'Jak byste přispěli k údržbě strojního parku?',
            ('Diagnostikou opotřebení a plánem oprav', {'Strojní technolog': 3}),
            ('Opravou elektrických motorů a rozvaděčů', {'Elektrotechnik': 3}),
            ('Výrobou náhradních dílců na soustruhu', {'Obráběč kovů': 3}),
            ('Svařováním prasklých součástí', {'Svářeč': 3})),

        _p2('STR', 'Co vás přitahuje na práci s vozidly?',
            ('Elektronická diagnostika a programování řídících jednotek', {'Autotronik': 3}),
            ('Konstrukce a úpravy podvozků a karoserií', {'Strojní konstruktér': 3, 'Svářeč': 2}),
            ('Montáž a údržba elektroinstalace vozidel', {'Elektrotechnik': 3}),
            ('Výroba speciálních dílů a úpravy na CNC', {'Programátor CNC': 3})),

        # --- Pracovní prostředí ---
        _p2('STR', 'V jakém prostředí byste chtěli pracovat?',
            ('V konstrukční kanceláři u dvou monitorů s CAD softwarem', {'Strojní konstruktér': 3}),
            ('V dílně u CNC obráběcího centra', {'Programátor CNC': 3, 'Obráběč kovů': 2}),
            ('Ve svářečské dílně s ochrannou výbavou', {'Svářeč': 3}),
            ('V autoservisu s moderní diagnostikou', {'Autotronik': 3})),

        _p2('STR', 'Kde se cítíte nejlépe?',
            ('V technologické přípravě výroby', {'Strojní technolog': 3}),
            ('U rozvaděče při zapojování elektrických obvodů', {'Elektrotechnik': 3}),
            ('U soustruhu při obrábění rotačních dílů', {'Obráběč kovů': 3}),
            ('V laboratoři při testování mechatronických celků', {'Mechatronik': 3})),

        _p2('STR', 'Jaké pracovní podmínky vám vyhovují?',
            ('Čistá kancelář s výkonným PC pro konstruování', {'Strojní konstruktér': 3}),
            ('Výrobní hala s moderními stroji', {'Strojní technolog': 3, 'Obráběč kovů': 2}),
            ('Mobilní pracoviště – servis přímo u zákazníka', {'Autotronik': 3}),
            ('Dílna s přístupem k různým svařovacím aparátům', {'Svářeč': 3})),

        _p2('STR', 'Kde byste trávili typický pracovní den?',
            ('U počítače s konstrukčním softwarem', {'Strojní konstruktér': 3}),
            ('Na výrobní lince s kontrolou kvality', {'Strojní technolog': 3}),
            ('Na střeše při instalaci fotovoltaiky', {'Elektrotechnik': 3}),
            ('V garáži při opravách a seřizování aut', {'Autotronik': 3})),

        _p2('STR', 'Jaká pracovní atmosféra vám sedí?',
            ('Tichá kancelář soustředěná na výpočty', {'Strojní konstruktér': 3}),
            ('Rušná dílna plná zvuků strojů', {'Obráběč kovů': 3, 'Svářeč': 2}),
            ('Technologicky vybavená laboratoř', {'Mechatronik': 3}),
            ('Dynamický servis s různými zakázkami každý den', {'Autotronik': 3})),

        # --- Nástroje a technologie ---
        _p2('STR', 'S jakými nástroji byste chtěli pracovat?',
            ('S CAD/CAM systémy – SolidWorks, Inventor', {'Strojní konstruktér': 3}),
            ('S CNC řídicím systémem Fanuc nebo Siemens', {'Programátor CNC': 3}),
            ('S osciloskopem a multimetrem', {'Elektrotechnik': 3}),
            ('S TIG svařovacím aparátem na nerez', {'Svářeč': 3})),

        _p2('STR', 'Která technologie vás nejvíce zajímá?',
            ('3D tisk kovů a aditivní výroba', {'Strojní konstruktér': 3, 'Strojní technolog': 2}),
            ('Průmyslové roboty a jejich programování', {'Mechatronik': 3}),
            ('Elektromobilita a bateriové systémy', {'Autotronik': 3, 'Elektrotechnik': 2}),
            ('Vysokorychlostní obrábění HSC', {'Obráběč kovů': 3})),

        _p2('STR', 'Jaký software byste se chtěli naučit?',
            ('ANSYS nebo ABAQUS pro simulace a analýzy', {'Strojní konstruktér': 3}),
            ('Mastercam nebo Edgecam pro CAM programování', {'Programátor CNC': 3}),
            ('EPLAN pro projektování elektroinstalací', {'Elektrotechnik': 3}),
            ('TIA Portal pro programování PLC', {'Mechatronik': 3})),

        _p2('STR', 'S jakým vybavením byste rádi pracovali denně?',
            ('S přesným mikrometrem a úchylkoměrem', {'Obráběč kovů': 3}),
            ('S diagnostickým počítačem a OBD čtečkou', {'Autotronik': 3}),
            ('Se svařovacím poloautomatem MIG/MAG', {'Svářeč': 3}),
            ('S technologickým softwarem pro plánování výroby', {'Strojní technolog': 3})),

        _p2('STR', 'Který nástroj považujete za nepostradatelný?',
            ('Parametrický modelář pro 3D konstrukci', {'Strojní konstruktér': 3}),
            ('G-kód editor pro ladění CNC programů', {'Programátor CNC': 3}),
            ('Termokameru pro kontrolu svarů a spojů', {'Svářeč': 3, 'Elektrotechnik': 2}),
            ('Programovatelný automat (PLC) pro řízení', {'Mechatronik': 3})),

        # --- Dovednosti a schopnosti ---
        _p2('STR', 'Jaká dovednost je ve strojírenství vaší silnou stránkou?',
            ('Technické kreslení a prostorová představivost', {'Strojní konstruktér': 3}),
            ('Znalost výrobních technologií a materiálů', {'Strojní technolog': 3}),
            ('Přesná manuální práce s kovy', {'Obráběč kovů': 3}),
            ('Porozumění elektronickým schématům', {'Elektrotechnik': 3})),

        _p2('STR', 'Která schopnost vás nejlépe vystihuje?',
            ('Dokážu navrhnout funkční mechanismus', {'Strojní konstruktér': 3}),
            ('Umím diagnostikovat závadu auta podle symptomů', {'Autotronik': 3}),
            ('Zvládám svařovat v různých polohách', {'Svářeč': 3}),
            ('Dokážu propojit mechaniku s elektronikou', {'Mechatronik': 3})),

        _p2('STR', 'Co považujete za svou nejcennější schopnost?',
            ('Schopnost optimalizovat výrobní časy', {'Strojní technolog': 3}),
            ('Precizní obrábění na setiny milimetru', {'Obráběč kovů': 3}),
            ('Efektivní programování složitých tvarů v G-kódu', {'Programátor CNC': 3}),
            ('Zapojení a oživení elektrického rozvaděče', {'Elektrotechnik': 3})),

        _p2('STR', 'Jaká vlastnost je pro práci ve strojírenství klíčová?',
            ('Analytické myšlení pro konstrukční problémy', {'Strojní konstruktér': 3}),
            ('Trpělivost při nastavování obráběcích strojů', {'Obráběč kovů': 3, 'Programátor CNC': 2}),
            ('Zodpovědnost při práci s vysokým napětím', {'Elektrotechnik': 3}),
            ('Systematický přístup k integraci systémů', {'Mechatronik': 3})),

        _p2('STR', 'V čem vynikáte oproti ostatním?',
            ('V rychlém řešení konstrukčních kolizí', {'Strojní konstruktér': 3}),
            ('Ve znalosti materiálových vlastností kovů', {'Strojní technolog': 3}),
            ('V čtení elektrických schémat a zapojení', {'Elektrotechnik': 3, 'Autotronik': 2}),
            ('Ve sváření obtížně svařitelných materiálů', {'Svářeč': 3})),

        # --- Hodnoty a motivace ---
        _p2('STR', 'Co vás ve strojírenství motivuje nejvíce?',
            ('Navrhnout stroj, který bude fungovat roky', {'Strojní konstruktér': 3}),
            ('Zvýšit efektivitu výroby o desítky procent', {'Strojní technolog': 3}),
            ('Vyrobit díl s perfektní povrchovou úpravou', {'Obráběč kovů': 3}),
            ('Oživit složitý mechatronický systém', {'Mechatronik': 3})),

        _p2('STR', 'Proč byste chtěli pracovat ve strojírenství?',
            ('Fascinují mě stroje a mechanismy', {'Strojní konstruktér': 3}),
            ('Rád řeším elektrické problémy', {'Elektrotechnik': 3}),
            ('Miluju zvuk frézky při obrábění kovu', {'Obráběč kovů': 3}),
            ('Zajímají mě moderní auta a jejich technika', {'Autotronik': 3})),

        _p2('STR', 'Co je pro vás na práci nejdůležitější?',
            ('Přesnost a kvalita výsledného produktu', {'Obráběč kovů': 3, 'Svářeč': 2}),
            ('Inovace a neustálé zlepšování procesů', {'Strojní technolog': 3}),
            ('Bezpečnost elektrických instalací', {'Elektrotechnik': 3}),
            ('Spolehlivost a funkčnost navrženého zařízení', {'Strojní konstruktér': 3})),

        _p2('STR', 'Co vás žene k lepšímu výkonu?',
            ('Dokonale naprogramovaný CNC program bez zmetků', {'Programátor CNC': 3}),
            ('Čistý a pevný svar bez vad', {'Svářeč': 3}),
            ('Spokojený zákazník po opravě auta', {'Autotronik': 3}),
            ('Úspěšně automatizovaná výrobní linka', {'Mechatronik': 3})),

        _p2('STR', 'Jaký přínos chcete mít pro společnost?',
            ('Navrhovat energeticky úsporné stroje', {'Strojní konstruktér': 3}),
            ('Zefektivnit výrobu a snížit odpad', {'Strojní technolog': 3}),
            ('Zajistit bezpečné elektrické rozvody', {'Elektrotechnik': 3}),
            ('Vyrábět přesné a kvalitní díly', {'Obráběč kovů': 3, 'Programátor CNC': 2})),

        # --- Řešení problémů ---
        _p2('STR', 'CNC stroj vyrábí díly mimo toleranci – co uděláte?',
            ('Zkontroluju a upravím CNC program', {'Programátor CNC': 3}),
            ('Přeměřím díl mikrometrem a hledám příčinu', {'Obráběč kovů': 3}),
            ('Analyzuji řezné podmínky a materiál', {'Strojní technolog': 3}),
            ('Zkontroluju servomotory a encodéry stroje', {'Mechatronik': 3})),

        _p2('STR', 'Na výrobní lince vypadává jistič – jak postupujete?',
            ('Změřím proudové odběry a hledám zkrat', {'Elektrotechnik': 3}),
            ('Zkontroluju mechanické příčiny přetížení', {'Strojní technolog': 3}),
            ('Provedu diagnostiku řídicího systému', {'Mechatronik': 3}),
            ('Zkontroluji, zda motory nejsou přetížené od obrábění', {'Programátor CNC': 2, 'Obráběč kovů': 2})),

        _p2('STR', 'Auto zákazníka má podivný zvuk z motoru – co uděláte?',
            ('Připojím diagnostiku a přečtu chybové kódy', {'Autotronik': 3}),
            ('Zkontroluju výfukový systém a svary', {'Svářeč': 3}),
            ('Posoudím stav ložisek a mechanických dílů', {'Strojní technolog': 2, 'Obráběč kovů': 2}),
            ('Změřím elektrické parametry zapalování', {'Elektrotechnik': 3})),

        _p2('STR', 'Při svařování praská svar – jak problém vyřešíte?',
            ('Upravím parametry svařování a předehřev', {'Svářeč': 3}),
            ('Zvolím jiný přídavný materiál dle materiálového listu', {'Strojní technolog': 3}),
            ('Přepočítám konstrukční uzel pro jiný typ spoje', {'Strojní konstruktér': 3}),
            ('Zkontroluji, zda teplo nepoškodilo blízkou elektroniku', {'Elektrotechnik': 2, 'Mechatronik': 2})),

        _p2('STR', 'Robot na lince se zastaví uprostřed cyklu – co navrhnete?',
            ('Zkontroluju PLC program a senzory', {'Mechatronik': 3}),
            ('Ověřím elektrické napájení a kabely', {'Elektrotechnik': 3}),
            ('Zkontroluju mechanické díly a vedení robota', {'Strojní technolog': 3}),
            ('Upravím dráhu robota v programu', {'Programátor CNC': 2, 'Mechatronik': 2})),

        # --- Vzdělání a rozvoj ---
        _p2('STR', 'Jaký kurz byste si vybrali?',
            ('Pokročilé 3D modelování a simulace', {'Strojní konstruktér': 3}),
            ('Certifikace pro svařování dle EN norem', {'Svářeč': 3}),
            ('Programování průmyslových robotů', {'Mechatronik': 3}),
            ('Diagnostika moderních hybridních vozidel', {'Autotronik': 3})),

        _p2('STR', 'Kterou odbornou literaturu byste četli?',
            ('Strojnické tabulky a příručku konstruktéra', {'Strojní konstruktér': 3}),
            ('Normy pro svařování a NDT kontrolu', {'Svářeč': 3}),
            ('Učebnici elektrotechniky a elektroniky', {'Elektrotechnik': 3}),
            ('Manuál CNC řídicího systému', {'Programátor CNC': 3})),

        _p2('STR', 'Jaký seminář byste navštívili?',
            ('Průmysl 4.0 a digitální dvojčata', {'Mechatronik': 3, 'Strojní technolog': 2}),
            ('Nové trendy v automobilové elektronice', {'Autotronik': 3}),
            ('Vysokorychlostní a tvrdé obrábění', {'Obráběč kovů': 3}),
            ('Optimalizace technologických postupů', {'Strojní technolog': 3})),

        _p2('STR', 'Co byste studovali na vysoké škole?',
            ('Strojní inženýrství – konstruování', {'Strojní konstruktér': 3}),
            ('Elektrotechniku a silnoproudou energetiku', {'Elektrotechnik': 3}),
            ('Mechatroniku a robotiku', {'Mechatronik': 3}),
            ('Výrobní technologie a management', {'Strojní technolog': 3})),

        _p2('STR', 'Jakou praxi byste si vybrali?',
            ('Stáž v konstrukční kanceláři strojírenské firmy', {'Strojní konstruktér': 3}),
            ('Praxi v autoservisu s moderní diagnostikou', {'Autotronik': 3}),
            ('Praxi ve svářečské firmě s certifikací', {'Svářeč': 3}),
            ('Praxi u výrobce CNC strojů', {'Programátor CNC': 3, 'Obráběč kovů': 2})),

        # --- Týmová práce ---
        _p2('STR', 'Jakou roli zastáváte v týmu?',
            ('Navrhuji řešení a kreslím výkresy', {'Strojní konstruktér': 3}),
            ('Koordinuji výrobní proces a kvalitu', {'Strojní technolog': 3}),
            ('Programuji stroje a laděním procesů', {'Programátor CNC': 3}),
            ('Zajišťuji elektrické zapojení a bezpečnost', {'Elektrotechnik': 3})),

        _p2('STR', 'Jak přispíváte k úspěchu výrobního projektu?',
            ('Přesnou a kompletní výrobní dokumentací', {'Strojní konstruktér': 3}),
            ('Kvalitními a pevnými svary', {'Svářeč': 3}),
            ('Přesnými obrobky dle tolerancí', {'Obráběč kovů': 3}),
            ('Funkčním řízením a automatizací', {'Mechatronik': 3})),

        _p2('STR', 'S kým nejraději spolupracujete?',
            ('S technology při optimalizaci výkresu pro výrobu', {'Strojní konstruktér': 3, 'Strojní technolog': 2}),
            ('S elektrikáři při zapojování robotických buněk', {'Mechatronik': 3}),
            ('S ostatními svářeči na velkých konstrukcích', {'Svářeč': 3}),
            ('S mechaniky a diagnostiky v servisu', {'Autotronik': 3})),

        _p2('STR', 'Jak reagujete na výrobní problém v týmu?',
            ('Analyzuji data a navrhnu úpravu konstrukce', {'Strojní konstruktér': 3}),
            ('Změním technologický postup nebo řezné podmínky', {'Strojní technolog': 3}),
            ('Přeprogramuji CNC operaci', {'Programátor CNC': 3}),
            ('Zkontroluju a opravím elektrické zapojení', {'Elektrotechnik': 3})),

        _p2('STR', 'Co oceňujete u kolegů?',
            ('Preciznost a dodržování výkresových tolerancí', {'Obráběč kovů': 3, 'Strojní konstruktér': 2}),
            ('Spolehlivost a kvalitu svarů', {'Svářeč': 3}),
            ('Schopnost rychle diagnostikovat závadu', {'Autotronik': 3, 'Mechatronik': 2}),
            ('Znalost elektrotechnických předpisů', {'Elektrotechnik': 3})),

        # --- Situační otázky ---
        _p2('STR', 'Firma potřebuje navrhnout nový jednoúčelový stroj – jaká je vaše role?',
            ('Navrhnout celkovou koncepci a 3D model', {'Strojní konstruktér': 3}),
            ('Určit výrobní postup a vybrat materiály', {'Strojní technolog': 3}),
            ('Naprogramovat obrábění klíčových dílů', {'Programátor CNC': 3}),
            ('Navrhnout a zapojit elektrický systém stroje', {'Elektrotechnik': 3})),

        _p2('STR', 'Zákazník reklamuje nekvalitní povrch obrobku – co uděláte?',
            ('Upravím řezné podmínky a zvolím jemnější operaci', {'Obráběč kovů': 3}),
            ('Přepíšu CNC program s lepší strategií obrábění', {'Programátor CNC': 3}),
            ('Provedu rozbor příčin a upravím technologii', {'Strojní technolog': 3}),
            ('Zkontroluju, zda vibrace nemají elektrickou příčinu', {'Mechatronik': 2, 'Elektrotechnik': 2})),

        _p2('STR', 'Do firmy přichází nový typ oceli k obrábění – jak se přizpůsobíte?',
            ('Navrhnuji vhodné řezné podmínky a nástroje', {'Strojní technolog': 3}),
            ('Zkusím testovací obrábění na CNC a ladím program', {'Programátor CNC': 3, 'Obráběč kovů': 2}),
            ('Ověřím svařitelnost a navrhnu parametry svařování', {'Svářeč': 3}),
            ('Přepočítám pevnost konstrukce z nového materiálu', {'Strojní konstruktér': 3})),

        _p2('STR', 'Máte navrhnout automatizované pracoviště – jak začnete?',
            ('Studiem zadání a konceptem mechanické části', {'Strojní konstruktér': 3}),
            ('Výběrem senzorů, akčních členů a řídicího systému', {'Mechatronik': 3}),
            ('Návrhem elektro projektu a rozvaděče', {'Elektrotechnik': 3}),
            ('Analýzou současného procesu a výrobních časů', {'Strojní technolog': 3})),

        _p2('STR', 'Elektromobil nepojede – jak byste postupovali?',
            ('Diagnostikoval bych řídící jednotku a bateriový management', {'Autotronik': 3}),
            ('Změřil bych izolační stav a napětí silových obvodů', {'Elektrotechnik': 3}),
            ('Zkontroloval bych mechanické spojení motoru a převodovky', {'Strojní technolog': 2, 'Strojní konstruktér': 2}),
            ('Ověřil bych komunikaci řídicích systémů na sběrnici', {'Mechatronik': 3})),

        # --- Specializace a preference ---
        _p2('STR', 'Jaký typ výroby vás láká nejvíce?',
            ('Kusová výroba přesných strojních dílů', {'Obráběč kovů': 3}),
            ('Sériová výroba s automatizovanými linkami', {'Strojní technolog': 3, 'Mechatronik': 2}),
            ('Svařované ocelové konstrukce – haly, mosty', {'Svářeč': 3}),
            ('Vývoj a prototypová výroba', {'Strojní konstruktér': 3})),

        _p2('STR', 'V jaké fázi výrobního procesu se cítíte nejužitečnější?',
            ('V přípravě – konstrukce a projektování', {'Strojní konstruktér': 3}),
            ('Ve výrobě – přímo u stroje', {'Obráběč kovů': 3, 'Svářeč': 2}),
            ('V programování a seřizování CNC', {'Programátor CNC': 3}),
            ('V oživování a testování hotového zařízení', {'Mechatronik': 3})),

        _p2('STR', 'Co vás na technice fascinuje?',
            ('Elegance precizně navržené konstrukce', {'Strojní konstruktér': 3}),
            ('Síla elektrického proudu a jeho řízení', {'Elektrotechnik': 3}),
            ('Proměna hrubého materiálu v přesný výrobek', {'Obráběč kovů': 3}),
            ('Jak software oživuje mechanické systémy', {'Mechatronik': 3})),

        _p2('STR', 'Jaký projekt byste chtěli realizovat?',
            ('Návrh průmyslového robota', {'Strojní konstruktér': 3, 'Mechatronik': 2}),
            ('Obrábění součástek pro letecký průmysl', {'Obráběč kovů': 3, 'Programátor CNC': 2}),
            ('Elektroinstalaci solární elektrárny', {'Elektrotechnik': 3}),
            ('Přestavbu závodního vozu', {'Autotronik': 3, 'Svářeč': 2})),

        _p2('STR', 'Jaký aspekt strojírenství vás zajímá nejvíce?',
            ('Pevnostní analýzy a výpočty metodou MKP', {'Strojní konstruktér': 3}),
            ('Řízení jakosti a statistická kontrola', {'Strojní technolog': 3}),
            ('Laserové a hybridní metody svařování', {'Svářeč': 3}),
            ('ADAS systémy a autonomní řízení vozidel', {'Autotronik': 3})),

        # --- Další pracovní situace ---
        _p2('STR', 'Jak byste prezentovali nový výrobek zákazníkovi?',
            ('3D modelem a technickou dokumentací', {'Strojní konstruktér': 3}),
            ('Popisem výrobního postupu a kalkulací', {'Strojní technolog': 3}),
            ('Ukázkovým obrobkem s perfektním povrchem', {'Obráběč kovů': 3}),
            ('Funkční ukázkou s osazenou elektronikou', {'Mechatronik': 3})),

        _p2('STR', 'Co děláte, když výrobek nesplňuje kvalitativní požadavky?',
            ('Hledám konstrukční příčinu a upravím výkres', {'Strojní konstruktér': 3}),
            ('Měním technologické parametry výroby', {'Strojní technolog': 3}),
            ('Seřizuji stroj a kontroluji upnutí obrobku', {'Obráběč kovů': 3}),
            ('Ověřuji svařovací protokol a vizuální kontrolu svaru', {'Svářeč': 3})),

        _p2('STR', 'Jakou inovaci byste zavedli ve strojírenské firmě?',
            ('Digitální dvojče výrobní linky', {'Mechatronik': 3, 'Strojní technolog': 2}),
            ('Robotizované svařovací pracoviště', {'Svářeč': 3}),
            ('Pětiosé CNC obráběcí centrum', {'Programátor CNC': 3}),
            ('Prediktivní údržbu s IoT senzory', {'Elektrotechnik': 3})),

        _p2('STR', 'Co kontrolujete jako první po dokončení výrobní operace?',
            ('Rozměry obrobku dle výkresu', {'Obráběč kovů': 3}),
            ('Kvalitu svarového spoje vizuálně i kapilárně', {'Svářeč': 3}),
            ('Správnost elektrického zapojení', {'Elektrotechnik': 3}),
            ('Funkčnost řídicího systému a senzorů', {'Mechatronik': 3})),

        _p2('STR', 'Jak přistupujete k bezpečnosti práce?',
            ('Dodržování předpisů o práci pod napětím', {'Elektrotechnik': 3}),
            ('Používání ochranné svářečské kukly a rukavic', {'Svářeč': 3}),
            ('Kontrola bezpečnostních krytů na CNC stroji', {'Programátor CNC': 3, 'Obráběč kovů': 2}),
            ('Funkční test nouzového zastavení strojů', {'Mechatronik': 3})),

        _p2('STR', 'Jak řešíte nedostatek náhradních dílů?',
            ('Navrhnuji díl a vytvořím výkres pro výrobu', {'Strojní konstruktér': 3}),
            ('Vyrobím díl na soustruhu nebo frézce', {'Obráběč kovů': 3}),
            ('Naprogramuji výrobu dílu na CNC', {'Programátor CNC': 3}),
            ('Hledám alternativní řešení z dostupných komponent', {'Strojní technolog': 3})),

        _p2('STR', 'Co je pro vás důležité při výběru povolání ve strojírenství?',
            ('Možnost se kreativně realizovat v konstrukci', {'Strojní konstruktér': 3}),
            ('Pracovat rukama a vidět výsledek své práce', {'Obráběč kovů': 3, 'Svářeč': 2}),
            ('Být na špičce moderních technologií', {'Mechatronik': 3, 'Autotronik': 2}),
            ('Stabilní zaměstnání s jasnou kariérou', {'Elektrotechnik': 3, 'Strojní technolog': 2})),

        _p2('STR', 'Jakou odpovědnost přijímáte nejraději?',
            ('Za správnost a funkčnost konstrukce', {'Strojní konstruktér': 3}),
            ('Za dodržení rozměrových tolerancí', {'Obráběč kovů': 3}),
            ('Za bezpečnost elektrických zařízení', {'Elektrotechnik': 3}),
            ('Za spolehlivost automotive diagnostiky', {'Autotronik': 3})),

        _p2('STR', 'Co vás napadne, když vidíte složitý stroj?',
            ('Analyzuji jeho konstrukci a kinematiku', {'Strojní konstruktér': 3}),
            ('Zajímá mě technologický postup jeho výroby', {'Strojní technolog': 3}),
            ('Přemýšlím, jak jsou propojeny díly a zda bych je vyrobil', {'Obráběč kovů': 3}),
            ('Přemýšlím, jak je řízen a jaké senzory používá', {'Mechatronik': 3})),

        _p2('STR', 'Jaký typ údržby preferujete?',
            ('Preventivní revize elektrických zařízení', {'Elektrotechnik': 3}),
            ('Diagnostiku a opravu řídicí elektroniky aut', {'Autotronik': 3}),
            ('Opravu a renovaci opotřebených strojních dílů', {'Obráběč kovů': 3, 'Svářeč': 2}),
            ('Údržbu a kalibraci CNC strojů', {'Programátor CNC': 3})),

        _p2('STR', 'Jakou specializaci byste si vybrali?',
            ('Konstrukce převodovek a pohonných systémů', {'Strojní konstruktér': 3}),
            ('Technologie svařování nerezových ocelí a hliníku', {'Svářeč': 3}),
            ('Průmyslová automatizace a IoT ve výrobě', {'Mechatronik': 3}),
            ('CNC programování víceosých strojů', {'Programátor CNC': 3})),

        _p2('STR', 'Co vás inspiruje k inovacím?',
            ('Nové CAD/CAE nástroje pro konstruktéry', {'Strojní konstruktér': 3}),
            ('Pokroky v elektromobilitě a nabíjecích systémech', {'Autotronik': 3, 'Elektrotechnik': 2}),
            ('Nové obráběcí strategie a materiály nástrojů', {'Obráběč kovů': 3, 'Programátor CNC': 2}),
            ('Kolaborativní roboty (coboty) ve výrobě', {'Mechatronik': 3})),

        _p2('STR', 'Jaký problém byste chtěli ve strojírenství vyřešit?',
            ('Zkrátit dobu vývoje nových produktů', {'Strojní konstruktér': 3}),
            ('Snížit výrobní náklady bez ztráty kvality', {'Strojní technolog': 3}),
            ('Automatizovat repetitivní a nebezpečné práce', {'Mechatronik': 3, 'Programátor CNC': 2}),
            ('Zvýšit spolehlivost elektrických systémů', {'Elektrotechnik': 3})),

        _p2('STR', 'Jak vnímáte budoucnost strojírenství?',
            ('V digitalizaci a parametrickém konstruování', {'Strojní konstruktér': 3}),
            ('V plné automatizaci a bezobslužné výrobě', {'Mechatronik': 3, 'Strojní technolog': 2}),
            ('V pokročilých svařovacích technologiích – laser, elektron', {'Svářeč': 3}),
            ('V elektrizaci dopravy a chytré energetice', {'Elektrotechnik': 3, 'Autotronik': 2})),

        _p2('STR', 'Jak postupujete při zavádění nového výrobku do sériové výroby?',
            ('Dopracuji výrobní dokumentaci a výkresy', {'Strojní konstruktér': 3}),
            ('Navrhnu optimální výrobní postup a přípravky', {'Strojní technolog': 3}),
            ('Naprogramuji všechny CNC operace', {'Programátor CNC': 3}),
            ('Připravím zkušební protokoly pro elektrické testy', {'Elektrotechnik': 3})),

        _p2('STR', 'Co děláte, když se změní materiálová specifikace uprostřed zakázky?',
            ('Přepočítám konstrukci na nový materiál', {'Strojní konstruktér': 3}),
            ('Upravím technologické parametry obrábění', {'Strojní technolog': 3}),
            ('Změním svařovací postup a přídavný materiál', {'Svářeč': 3}),
            ('Přeladím řezné podmínky v CNC programu', {'Programátor CNC': 3, 'Obráběč kovů': 2})),

        _p2('STR', 'Jak řešíte reklamaci od odběratele?',
            ('Analyzuji příčinu v konstrukci a navrhnu úpravu', {'Strojní konstruktér': 3}),
            ('Zkontroluju dodržení technologického postupu', {'Strojní technolog': 3}),
            ('Přeměřím rozměry obrobku a hledám odchylky', {'Obráběč kovů': 3}),
            ('Provedu defektoskopii svarů ultrazvukem', {'Svářeč': 3})),

        _p2('STR', 'Jakou činnost byste vykonávali při montáži rozvaděče?',
            ('Zapojení silových a řídících obvodů', {'Elektrotechnik': 3}),
            ('Programování PLC a HMI panelu', {'Mechatronik': 3}),
            ('Výrobu montážních plechů a úchytů', {'Obráběč kovů': 3}),
            ('Svaření nosné konstrukce rozvaděčové skříně', {'Svářeč': 3})),

        _p2('STR', 'Jak přistupujete k úspoře energie ve výrobě?',
            ('Navrhuji lehčí konstrukce se zachováním pevnosti', {'Strojní konstruktér': 3}),
            ('Optimalizuji řezné podmínky pro nižší spotřebu', {'Strojní technolog': 3}),
            ('Dimenzuji elektrické pohony s vyšší účinností', {'Elektrotechnik': 3}),
            ('Implementuji rekuperaci energie u robotických os', {'Mechatronik': 3})),

        _p2('STR', 'Co vás přitahuje na práci s nerezovými materiály?',
            ('Náročné TIG svařování vyžadující přesnost', {'Svářeč': 3}),
            ('Obrábění s odlišnými řeznými podmínkami', {'Obráběč kovů': 3}),
            ('Konstrukce potravinářských strojů z nerezu', {'Strojní konstruktér': 3}),
            ('Antikorozní vlastnosti pro chemický průmysl', {'Strojní technolog': 3})),

        _p2('STR', 'Jak byste zlepšili kvalitu ve výrobním procesu?',
            ('Zavedl bych statistickou kontrolu procesů SPC', {'Strojní technolog': 3}),
            ('Navrhl přípravky zajišťující přesné upnutí', {'Strojní konstruktér': 3}),
            ('Kalibroval a seřídil měřicí přístroje a stroje', {'Obráběč kovů': 3, 'Programátor CNC': 2}),
            ('Implementoval automatizovanou vizuální kontrolu', {'Mechatronik': 3})),

        _p2('STR', 'Jakou roli hrajete při uvádění stroje do provozu?',
            ('Kontroluji soulad výroby s konstrukční dokumentací', {'Strojní konstruktér': 3}),
            ('Oživuji elektroinstalaci a testuji bezpečnostní prvky', {'Elektrotechnik': 3}),
            ('Nahrávám a laděním řídicí software', {'Mechatronik': 3}),
            ('Provádím zkušební chod a seřizuji mechaniku', {'Strojní technolog': 3, 'Obráběč kovů': 2})),

        _p2('STR', 'Co děláte, když zákazník požaduje kratší dodací lhůtu?',
            ('Optimalizuji konstrukci pro rychlejší výrobu', {'Strojní konstruktér': 3}),
            ('Přepracuji technologický postup pro paralelní operace', {'Strojní technolog': 3}),
            ('Naprogramuji efektivnější CNC dráhy nástrojů', {'Programátor CNC': 3}),
            ('Nasadím více svářečů nebo použiji rychlejší metodu', {'Svářeč': 3})),

        _p2('STR', 'Jak reagujete na poruchu výrobního stroje v nočním provozu?',
            ('Diagnostikuji elektrickou závadu na dálku přes systém', {'Elektrotechnik': 3}),
            ('Zkontroluji mechanické uzly a opotřebení dílů', {'Strojní technolog': 3}),
            ('Přeprogramuji řídicí systém a restartuji automat', {'Mechatronik': 3}),
            ('Vyrobím nebo upravím poškozený díl na soustruhu', {'Obráběč kovů': 3})),

        _p2('STR', 'Jak vnímáte význam certifikací ve strojírenství?',
            ('Certifikace svářeče dle EN ISO 9606 je základ kvality', {'Svářeč': 3}),
            ('Autorizační zkoušky pro práci pod napětím jsou nezbytné', {'Elektrotechnik': 3}),
            ('Certifikát CNC programátora zvyšuje konkurenceschopnost', {'Programátor CNC': 3}),
            ('Certifikace autodiagnostiky otevírá dveře k moderním vozidlům', {'Autotronik': 3})),

        # ══════════════ DOP: Doprava a logistika (161–240) ══════════════

        # --- Pracovní činnosti ---
        _p2('DOP', 'Jaká denní činnost v dopravě vás láká nejvíce?',
            ('Plánování optimálních tras pro flotilu kamionů', {'Logistik': 3}),
            ('Provedení předletové kontroly a navigace', {'Pilot': 3}),
            ('Řízení nákladního vozidla na dálkové trase', {'Řidič': 3}),
            ('Sledování polohy vozidel na dispečerské mapě', {'Dispečer': 3})),

        _p2('DOP', 'Která pracovní náplň vás zaujme?',
            ('Řízení vlakové soupravy podle jízdního řádu', {'Strojvedoucí': 3}),
            ('Navigace nákladní lodi přes úzký průplav', {'Kapitán plavidla': 3}),
            ('Příjem a kontrola zásilek na příjmové rampě', {'Skladník': 3}),
            ('Kontrola dokumentů a zboží na hraničním přechodu', {'Celník': 3})),

        _p2('DOP', 'Co byste dělali nejraději v logistickém centru?',
            ('Optimalizoval/a dodavatelský řetězec a zásoby', {'Logistik': 3}),
            ('Naskladňoval/a palety pomocí vysokozdvižného vozíku', {'Skladník': 3}),
            ('Koordinoval/a příjezdy a odjezdy kamionů', {'Dispečer': 3}),
            ('Kontroloval/a celní dokumenty pro exportní zásilky', {'Celník': 3})),

        _p2('DOP', 'Jakou aktivitu na letišti byste preferovali?',
            ('Řízení letadla na přistávací dráhu při bočním větru', {'Pilot': 4}),
            ('Plánování vytížení cargo letů a distribuce nákladu', {'Logistik': 3}),
            ('Řízení follow-me vozidla po letištní ploše', {'Řidič': 3}),
            ('Koordinace letového provozu mezi věží a posádkami', {'Dispečer': 3})),

        _p2('DOP', 'S čím se ráno v práci nejraději pustíte do díla?',
            ('Kontrola jízdního řádu a stavu kolejových vozidel', {'Strojvedoucí': 3}),
            ('Příprava lodi k vyplutí – kontrola strojovny a palub', {'Kapitán plavidla': 3}),
            ('Ruční inventura zásob ve skladu', {'Skladník': 3}),
            ('Přezkoumání celních prohlášení k dnešním zásilkám', {'Celník': 3})),

        _p2('DOP', 'Jaký typ přepravy byste chtěli organizovat?',
            ('Multimodální přepravu kontejnerů přes tři kontinenty', {'Logistik': 4}),
            ('Pravidelnou autobusovou linku v městské dopravě', {'Řidič': 3}),
            ('Nákladní vlakovou soupravu s nebezpečným zbožím', {'Strojvedoucí': 3}),
            ('Říční přepravu sypkých materiálů na bárce', {'Kapitán plavidla': 3})),

        _p2('DOP', 'Která činnost v přístavu vás přitahuje?',
            ('Navigování tankeru k molu za špatné viditelnosti', {'Kapitán plavidla': 4}),
            ('Organizace nakládky a vykládky kontejnerů', {'Logistik': 3, 'Skladník': 2}),
            ('Celní prohlídka kontejnerů pomocí rentgenu', {'Celník': 3}),
            ('Řízení portálového jeřábu při překládce', {'Skladník': 3})),

        _p2('DOP', 'Jak byste se nejraději zapojili do mezinárodní přepravy?',
            ('Vyjednáváním smluvních podmínek s dopravci', {'Logistik': 3}),
            ('Přepravou zásilek jako řidič kamionu přes Evropu', {'Řidič': 3}),
            ('Kontrolou dodržování celních předpisů EU', {'Celník': 3}),
            ('Pilotováním cargo letadla na mezikontinentální lince', {'Pilot': 3})),

        _p2('DOP', 'Která činnost při řízení dopravy vás oslovuje?',
            ('Sledování a optimalizace spotřeby paliva flotily', {'Logistik': 3}),
            ('Komunikace s řidiči a řešení dopravních komplikací', {'Dispečer': 3}),
            ('Dodržování bezpečnostních přestávek za volantem', {'Řidič': 3}),
            ('Evidence a kontrola přepravních dokladů', {'Celník': 3})),

        _p2('DOP', 'Co byste dělali na železniční stanici?',
            ('Řídil/a lokomotivu při posunu vagónů na seřaďovacím nádraží', {'Strojvedoucí': 3}),
            ('Koordinoval/a vlakový provoz z dispečerského centra', {'Dispečer': 3}),
            ('Organizoval/a překládku zboží z vlaku do skladu', {'Skladník': 3}),
            ('Plánoval/a optimální nakládku vlakové soupravy', {'Logistik': 3})),

        # --- Pracovní prostředí ---
        _p2('DOP', 'Ve kterém prostředí byste se cítili nejlépe?',
            ('V kokpitu letadla vysoko nad oblaky', {'Pilot': 4}),
            ('V kabině kamionu na otevřené dálnici', {'Řidič': 3}),
            ('Na kapitánském můstku nákladní lodi', {'Kapitán plavidla': 3}),
            ('V lokomotivě projíždějící krajinou', {'Strojvedoucí': 3})),

        _p2('DOP', 'Jaký typ pracoviště vám vyhovuje?',
            ('Kancelář s monitory a logistickým softwarem', {'Logistik': 3}),
            ('Dispečerské centrum s přehledovými obrazovkami', {'Dispečer': 3}),
            ('Velký sklad s regály a manipulační technikou', {'Skladník': 3}),
            ('Celní úřad nebo hraniční přechod', {'Celník': 3})),

        _p2('DOP', 'Jaký pracovní režim vám vyhovuje?',
            ('Pravidelné směny podle jízdního řádu', {'Strojvedoucí': 3}),
            ('Nepravidelný letový rozvrh s pobytem v zahraničí', {'Pilot': 3}),
            ('Dlouhé jízdy s přespáním v kabině kamionu', {'Řidič': 3}),
            ('Směnový provoz v dispečerském centru 24/7', {'Dispečer': 3})),

        _p2('DOP', 'Jak se stavíte k práci venku za každého počasí?',
            ('Nevadí mi – na palubě lodi jsem zvyklý/á', {'Kapitán plavidla': 3}),
            ('Pracuji venku při nakládce a vykládce', {'Skladník': 3}),
            ('Kontroluji vozidla a náklad i v dešti na hranici', {'Celník': 3}),
            ('Jsem v kabině – počasí řeším jen na trase', {'Řidič': 3})),

        _p2('DOP', 'Jaký pracovní tým preferujete?',
            ('Malá letová posádka – pilot a kopilot', {'Pilot': 3}),
            ('Posádka lodi – kapitán, strojník, námořníci', {'Kapitán plavidla': 3}),
            ('Práce převážně sám – já a lokomotiva', {'Strojvedoucí': 3}),
            ('Tým celníků při koordinované kontrole zboží', {'Celník': 3})),

        _p2('DOP', 'Jak vnímáte práci pod časovým tlakem?',
            ('Dokážu rychle přeplánovat trasy při zpoždění', {'Logistik': 3}),
            ('Zvládám přistání v krátkém časovém okně', {'Pilot': 3}),
            ('Koordinuji provoz i při kumulaci mimořádností', {'Dispečer': 3}),
            ('Rychle vyskladním a připravím zásilku k odeslání', {'Skladník': 3})),

        _p2('DOP', 'Kde byste trávili většinu pracovní doby?',
            ('Na vodě – řeky, průplavy nebo moře', {'Kapitán plavidla': 3}),
            ('Na kolejích – mezi stanicemi a depem', {'Strojvedoucí': 3}),
            ('Na silnici – mezi městy a zeměmi', {'Řidič': 3}),
            ('V kanceláři – analýza dat a plánování logistiky', {'Logistik': 3})),

        _p2('DOP', 'Jak se stavíte k práci v noci?',
            ('Noční lety mají zvláštní kouzlo', {'Pilot': 3}),
            ('Noční směna v dispečinku je klidnější a soustředěnější', {'Dispečer': 3}),
            ('Noční jízda po prázdné dálnici mi vyhovuje', {'Řidič': 3}),
            ('Noční inventura skladu probíhá nerušeně', {'Skladník': 3})),

        _p2('DOP', 'Jaké pracovní tempo preferujete?',
            ('Dynamické – každý den jiná trasa a náklad', {'Řidič': 3}),
            ('Systematické – plánuji dodávky na týdny dopředu', {'Logistik': 3}),
            ('Střídavé – klidné úseky a pak intenzivní manévry', {'Kapitán plavidla': 3}),
            ('Pravidelné – přesný jízdní řád a osvědčené postupy', {'Strojvedoucí': 3})),

        _p2('DOP', 'Jakou míru cestování v práci preferujete?',
            ('Celosvětové lety s pobyty na různých kontinentech', {'Pilot': 4}),
            ('Mezinárodní kamionové trasy po celé Evropě', {'Řidič': 3}),
            ('Zůstávám na jednom místě – celní úřad nebo přechod', {'Celník': 3}),
            ('Plánuji globální logistiku z jedné kanceláře', {'Logistik': 3})),

        # --- Nástroje a vybavení ---
        _p2('DOP', 'S jakým zařízením byste chtěli pracovat?',
            ('S navigačním radarem a autopilotem v kokpitu', {'Pilot': 3}),
            ('S GPS sledováním vozidel na velké digitální mapě', {'Dispečer': 3}),
            ('S vysokozdvižným vozíkem a čtečkou čárových kódů', {'Skladník': 3}),
            ('S rentgenovým skenerem na celní prohlídku', {'Celník': 3})),

        _p2('DOP', 'Jaký software byste se rádi naučili ovládat?',
            ('WMS – systém pro řízení skladu', {'Skladník': 3, 'Logistik': 2}),
            ('TMS – systém pro řízení přepravy a plánování tras', {'Logistik': 3}),
            ('ETCS – evropský vlakový zabezpečovací systém', {'Strojvedoucí': 3}),
            ('NCTS – systém pro celní tranzitní režim', {'Celník': 3})),

        _p2('DOP', 'Který přístroj nebo systém vás fascinuje?',
            ('Letový simulátor s plnou instrumentací', {'Pilot': 4}),
            ('Lodní sonar a elektronické námořní mapy ECDIS', {'Kapitán plavidla': 3}),
            ('Digitální tachograf a systém eCall', {'Řidič': 3}),
            ('Automatický třídící systém v logistickém centru', {'Logistik': 3})),

        _p2('DOP', 'S jakou technikou byste pracovali nejraději?',
            ('S návěsovou soupravou nebo tahačem', {'Řidič': 3}),
            ('S elektrickou lokomotivou řady 380', {'Strojvedoucí': 3}),
            ('S retraky a paletovými vozíky ve skladu', {'Skladník': 3}),
            ('S pásovým dopravníkem a váhou při kontrole zásilek', {'Celník': 3})),

        _p2('DOP', 'Jakou komunikační techniku chcete používat?',
            ('Leteckou radiostanici a komunikaci s ATC', {'Pilot': 3}),
            ('Námořní VHF radiostanici a systém AIS', {'Kapitán plavidla': 3}),
            ('Dispečerský komunikační systém s GPS', {'Dispečer': 3}),
            ('CB radiostanici a hands-free v kabině kamionu', {'Řidič': 3})),

        _p2('DOP', 'Které technologie pro sledování zásilek vás zajímají?',
            ('RFID štítky a IoT senzory na kontejnerech', {'Logistik': 3}),
            ('GPS tracking a telematiká vozidel v reálném čase', {'Dispečer': 3}),
            ('Čtečky čárových kódů a automatické skenery', {'Skladník': 3}),
            ('Celní pečetě s elektronickým zabezpečením', {'Celník': 3})),

        _p2('DOP', 'S jakým dopravním prostředkem byste chtěli pracovat?',
            ('Velkokapacitní dopravní letadlo Boeing nebo Airbus', {'Pilot': 4}),
            ('Říční tlačný remorkér s člunovou sestavou', {'Kapitán plavidla': 3}),
            ('Rychlíková motorová jednotka na regionální trati', {'Strojvedoucí': 3}),
            ('Tahač s chladírenským návěsem', {'Řidič': 3})),

        _p2('DOP', 'Jaký typ mapy nebo navigace používáte nejraději?',
            ('Letecké mapy VFR/IFR s navigačními body', {'Pilot': 3}),
            ('Námořní mapy s hloubkovými údaji a proudy', {'Kapitán plavidla': 3}),
            ('Logistický software s optimalizací tras', {'Logistik': 3}),
            ('Systém vizualizace aktuální polohy všech vlaků', {'Dispečer': 3})),

        _p2('DOP', 'Který bezpečnostní systém vás zajímá nejvíce?',
            ('TCAS – protisrážkový systém v letadle', {'Pilot': 3}),
            ('ABS a EBS v nákladních vozidlech', {'Řidič': 3}),
            ('Automatické vedení vlaku a nouzové brzdění', {'Strojvedoucí': 3}),
            ('Detektory kontrabandu rentgenem a psovody', {'Celník': 3})),

        # --- Dovednosti a schopnosti ---
        _p2('DOP', 'Která dovednost vás nejlépe vystihuje?',
            ('Prostorová orientace a čtení přístrojů', {'Pilot': 3}),
            ('Organizační schopnosti a řízení zásob', {'Logistik': 3}),
            ('Manuální zručnost při manipulaci s nákladem', {'Skladník': 3}),
            ('Znalost právních předpisů a důslednost', {'Celník': 3})),

        _p2('DOP', 'V čem vynikáte?',
            ('Ve schopnosti rychle reagovat na měnící se situaci', {'Dispečer': 3}),
            ('V přesném dodržování signalizace a předpisů', {'Strojvedoucí': 3}),
            ('V řízení velkých vozidel v náročných podmínkách', {'Řidič': 3}),
            ('Ve vedení posádky a rozhodování na moři', {'Kapitán plavidla': 3})),

        _p2('DOP', 'Jaké schopnosti považujete za svou silnou stránku?',
            ('Analytické myšlení a práce s daty o dodávkách', {'Logistik': 3}),
            ('Trpělivost a pečlivost při kontrole dokumentace', {'Celník': 3}),
            ('Fyzická zdatnost a schopnost práce s břemeny', {'Skladník': 3}),
            ('Klidné nervy při řízení za špatné viditelnosti', {'Pilot': 3})),

        _p2('DOP', 'Co je pro vás v práci nejdůležitější?',
            ('Přesnost – každá minuta zpoždění stojí peníze', {'Strojvedoucí': 3, 'Dispečer': 2}),
            ('Bezpečnost – zodpovědnost za životy cestujících', {'Pilot': 3}),
            ('Spolehlivost – zásilka dorazí včas a nepoškozená', {'Řidič': 3}),
            ('Pořádek – vše evidováno a na svém místě', {'Skladník': 3})),

        _p2('DOP', 'Jakou cizí jazykovou dovednost využijete nejvíce?',
            ('Leteckou angličtinu pro komunikaci s ATC', {'Pilot': 4}),
            ('Námořní angličtinu a IMO komunikační fráze', {'Kapitán plavidla': 3}),
            ('Znalost celní terminologie v několika jazycích', {'Celník': 3}),
            ('Obchodní angličtinu pro jednání s dodavateli', {'Logistik': 3})),

        _p2('DOP', 'Jak se nejlépe rozhodujete pod tlakem?',
            ('Sleduji přístroje a postupuji podle checklistu', {'Pilot': 3}),
            ('Rychle přeorganizuji trasy a komunikuji s řidiči', {'Dispečer': 3}),
            ('Spolehnu se na zkušenosti z tisíců kilometrů', {'Řidič': 3}),
            ('Vyhodnotím situaci a vydám rozkazy posádce', {'Kapitán plavidla': 3})),

        _p2('DOP', 'Který typ znalostí vás přitahuje?',
            ('Meteorologie a letová mechanika', {'Pilot': 3}),
            ('Supply chain management a lean logistika', {'Logistik': 3}),
            ('Předpisy ADR pro přepravu nebezpečného zboží', {'Řidič': 3}),
            ('Celní nomenklatury a harmonizovaný systém', {'Celník': 3})),

        _p2('DOP', 'Jaký typ odpovědnosti vám vyhovuje?',
            ('Za bezpečnost stovek cestujících ve vlaku', {'Strojvedoucí': 3}),
            ('Za správné uskladnění zboží za miliony korun', {'Skladník': 3}),
            ('Za koordinaci desítek vozidel v reálném čase', {'Dispečer': 3}),
            ('Za dodržení celních předpisů při dovozu', {'Celník': 3})),

        _p2('DOP', 'Ve které oblasti se chcete neustále vzdělávat?',
            ('Nové letové postupy a avionika', {'Pilot': 3}),
            ('Automatizace skladů a robotizace', {'Skladník': 3, 'Logistik': 2}),
            ('Námořní legislativa a aktualizace plavebních map', {'Kapitán plavidla': 3}),
            ('Nové celní předpisy EU a elektronické celní řízení', {'Celník': 3})),

        _p2('DOP', 'Jak se vyrovnáváte s monotónní prací?',
            ('Sleduji krajinu a dbám na bezpečnost za volantem', {'Řidič': 3}),
            ('Kontroluji signály a dodržuji rychlostní profil', {'Strojvedoucí': 3}),
            ('Systematicky zpracovávám zásilku po zásilce', {'Skladník': 3}),
            ('Zůstávám ostražitý – pašeráci se spoléhají na rutinu', {'Celník': 3})),

        # --- Hodnoty a preference ---
        _p2('DOP', 'Co vás na dopravě přitahuje nejvíce?',
            ('Svoboda a nezávislost na otevřené silnici', {'Řidič': 3}),
            ('Technická dokonalost a preciznost letectví', {'Pilot': 3}),
            ('Efektivita – dostat správnou věc na správné místo', {'Logistik': 3}),
            ('Právní řád – zajistit férový obchod přes hranice', {'Celník': 3})),

        _p2('DOP', 'Proč byste si vybrali práci v dopravě?',
            ('Chci vidět svět z kokpitu letadla', {'Pilot': 3}),
            ('Fascinuje mě síla a rychlost vlaků', {'Strojvedoucí': 3}),
            ('Přitahuje mě moře a život na vodě', {'Kapitán plavidla': 3}),
            ('Baví mě koordinovat a řídit složité operace', {'Dispečer': 3})),

        _p2('DOP', 'Jaká hodnota je pro vás v práci klíčová?',
            ('Bezpečnost – nikdy nerisknout životy', {'Pilot': 3, 'Strojvedoucí': 2}),
            ('Efektivita – minimalizovat náklady a čas', {'Logistik': 3}),
            ('Poctivost – odhalit podvod a chránit stát', {'Celník': 3}),
            ('Spolehlivost – vždy dodat co bylo slíbeno', {'Řidič': 3})),

        _p2('DOP', 'Co je pro vás v zaměstnání nejvíce motivující?',
            ('Zodpovědnost za bezpečnou plavbu a náklad', {'Kapitán plavidla': 3}),
            ('Vidět plynulý provoz, který jsem zorganizoval/a', {'Dispečer': 3}),
            ('Přehledný a dokonale uspořádaný sklad', {'Skladník': 3}),
            ('Úspěšně optimalizovaný řetězec od výroby po zákazníka', {'Logistik': 3})),

        _p2('DOP', 'Jaký přínos chcete mít pro společnost?',
            ('Zajistit bezpečnou přepravu cestujících po kolejích', {'Strojvedoucí': 3}),
            ('Chránit ekonomiku před nelegálním dovozem', {'Celník': 3}),
            ('Zásobovat obchody a nemocnice včas', {'Řidič': 3}),
            ('Snižovat uhlíkovou stopu dopravy optimalizací', {'Logistik': 3})),

        _p2('DOP', 'Jaký vztah máte k pravidlům a předpisům?',
            ('Jsou základ letové bezpečnosti – dodržuji je striktně', {'Pilot': 3}),
            ('Znám dopravní předpisy nazpaměť', {'Řidič': 3}),
            ('Železniční předpisy jsou moje denní četba', {'Strojvedoucí': 3}),
            ('Celní legislativa je komplexní a zajímavá', {'Celník': 3})),

        _p2('DOP', 'Jak vnímáte fyzickou náročnost práce?',
            ('Stojím většinu směny a nosím těžké balíky', {'Skladník': 3}),
            ('Sedím dlouho za volantem, ale musím být fit', {'Řidič': 3}),
            ('Na lodi střídám fyzickou práci s navigací', {'Kapitán plavidla': 3}),
            ('Celní kontrola v terénu vyžaduje kondici', {'Celník': 3})),

        _p2('DOP', 'Jaký typ kariérního růstu vás zajímá?',
            ('Od kopilota přes kapitána k instruktorovi', {'Pilot': 4}),
            ('Od dispečera k vedoucímu dopravního centra', {'Dispečer': 3}),
            ('Od skladníka k vedoucímu logistiky', {'Skladník': 2, 'Logistik': 3}),
            ('Od celníka k vedoucímu celního úřadu', {'Celník': 3})),

        # --- Řešení problémů ---
        _p2('DOP', 'Dálnice je uzavřena kvůli nehodě – co uděláte?',
            ('Přeplánuji trasy celé flotily přes alternativní silnice', {'Logistik': 3}),
            ('Informuji řidiče a navrhnuji objízdné trasy', {'Dispečer': 3}),
            ('Klidně sjedu na vedlejší silnici a pokračuji', {'Řidič': 3}),
            ('Přehodnotím dodací lhůty a aktualizuji zákazníky', {'Logistik': 2, 'Dispečer': 3})),

        _p2('DOP', 'Na lodi se porouchal hlavní motor – jak zareagujete?',
            ('Vydám rozkaz zakotvit a organizuji opravu', {'Kapitán plavidla': 4}),
            ('Kontaktuji nejbližší přístav a organizuji odtah', {'Dispečer': 3}),
            ('Přeplánuji dodávku náhradní trasou', {'Logistik': 3}),
            ('Zkontroluji, zda náklad vyžaduje zvláštní celní režim', {'Celník': 3})),

        _p2('DOP', 'Zásilka na skladu neodpovídá dokumentaci – co děláte?',
            ('Zastavím výdej a provedu fyzickou rekontrolu', {'Skladník': 3}),
            ('Prověřím celní dokumenty a původ zásilky', {'Celník': 3}),
            ('Kontaktuji odesílatele a řeším reklamaci', {'Logistik': 3}),
            ('Informuji řidiče, že nakládka se odkládá', {'Dispečer': 3})),

        _p2('DOP', 'Vlak zastaví na trati kvůli poruše signalizace – vaše reakce?',
            ('Postupuji podle předpisu pro jízdu na rozkaz', {'Strojvedoucí': 3}),
            ('Kontaktuji dispečera a čekám na pokyny', {'Strojvedoucí': 2, 'Dispečer': 3}),
            ('Přeplánuji dotčené vlakové spoje na jiné koleje', {'Dispečer': 3}),
            ('Zajistím náhradní autobusovou dopravu pro cestující', {'Logistik': 3})),

        _p2('DOP', 'Motor letadla hlásí varování za letu – co je klíčové?',
            ('Dodržet nouzový postup z checklistu a informovat ATC', {'Pilot': 4}),
            ('Připravit nejbližší letiště na nouzové přistání', {'Dispečer': 3}),
            ('Zajistit pozemní logistiku pro přesměrované cestující', {'Logistik': 3}),
            ('Ověřit, že záchranné vybavení na palubě je kompletní', {'Kapitán plavidla': 2, 'Pilot': 2})),

        _p2('DOP', 'Řidič kamionu hlásí poruchu chladícího agregátu – vaše řešení?',
            ('Najdu nejbližší servis a přesměruji náklad', {'Dispečer': 3}),
            ('Zastavím na bezpečném místě a zkontoluji agregát', {'Řidič': 3}),
            ('Přeplánuji distribuci, aby náklad nestihl se zkazit', {'Logistik': 3}),
            ('Připravím sklad na urgentní příjem zboží', {'Skladník': 3})),

        _p2('DOP', 'Podezřelá zásilka na celnici – jak postupujete?',
            ('Provedu důkladnou fyzickou kontrolu obsahu', {'Celník': 4}),
            ('Zadržím zásilku a informuji nadřízené orgány', {'Celník': 3}),
            ('Ověřím kompletní dokumentaci a historii odesílatele', {'Celník': 3, 'Logistik': 2}),
            ('Zkontroluju naskladnění a separuji zásilku', {'Skladník': 3})),

        _p2('DOP', 'Na řece je nízký stav vody – co jako kapitán uděláte?',
            ('Snížím ponor lodi a redukuji náklad', {'Kapitán plavidla': 3}),
            ('Přeplánuji trasu na jiný vodní tok nebo přístav', {'Logistik': 3}),
            ('Informuji dispečink o omezení plavby', {'Dispečer': 3}),
            ('Připravím sklad na dočasné uskladnění přebytku', {'Skladník': 3})),

        _p2('DOP', 'Elektronický mýtný systém ve vozidle nefunguje – vaše akce?',
            ('Zastavím a kontaktuji dispečink pro pokyny', {'Řidič': 3}),
            ('Eviduji trasu ručně a řeším problém na nejbližší stanici', {'Řidič': 2, 'Dispečer': 3}),
            ('Přepočítám náklady na mýtné pro alternativní trasu', {'Logistik': 3}),
            ('Zkontoluji, zda porucha neovlivní celní evidenci přejezdu', {'Celník': 3})),

        _p2('DOP', 'Sklad je přeplněný a další dodávka přijíždí – řešení?',
            ('Reorganizuji skladové pozice a maximalizuji kapacitu', {'Skladník': 3}),
            ('Přesměruji zásilku do jiného distribučního centra', {'Logistik': 3}),
            ('Koordinuji s řidiči posunutí dodacích časů', {'Dispečer': 3}),
            ('Ověřím celní status – některé zboží lze propustit dříve', {'Celník': 3})),

        # --- Znalosti a vzdělání ---
        _p2('DOP', 'Který vzdělávací obor vás přitahuje?',
            ('Letecká doprava a pilotní výcvik', {'Pilot': 4}),
            ('Logistika a Supply Chain Management', {'Logistik': 3}),
            ('Námořní akademie a lodní důstojnictví', {'Kapitán plavidla': 3}),
            ('Celní správa a mezinárodní obchod', {'Celník': 3})),

        _p2('DOP', 'Jaký kurz nebo školení byste absolvovali?',
            ('Profesní průkaz řidiče skupiny C+E', {'Řidič': 3}),
            ('Typový kurz na konkrétní letadlo', {'Pilot': 3}),
            ('Školení na drážní předpisy a signalizaci', {'Strojvedoucí': 3}),
            ('Kurz obsluhy VZV a manipulační techniky', {'Skladník': 3})),

        _p2('DOP', 'Která oblast práva vás zajímá?',
            ('Letecké právo a mezinárodní předpisy ICAO', {'Pilot': 3}),
            ('Celní kodex Evropské unie', {'Celník': 3}),
            ('Drážní legislativa a zákon o drahách', {'Strojvedoucí': 3}),
            ('Námořní právo a úmluva SOLAS', {'Kapitán plavidla': 3})),

        _p2('DOP', 'Jaký typ zkoušky byste skládali nejraději?',
            ('Teoretické a praktické pilotní zkoušky ATPL', {'Pilot': 4}),
            ('Zkoušky způsobilosti strojvedoucího', {'Strojvedoucí': 3}),
            ('Zkoušky odborné způsobilosti celníka', {'Celník': 3}),
            ('Certifikaci APICS pro logistiku', {'Logistik': 3})),

        _p2('DOP', 'Který předmět ve škole vás bavil nejvíce?',
            ('Fyzika – mechanika a aerodynamika', {'Pilot': 3}),
            ('Zeměpis – světový obchod a dopravní sítě', {'Logistik': 3}),
            ('Matematika – kalkulace a optimalizace', {'Logistik': 2, 'Dispečer': 3}),
            ('Právo – legislativa a předpisy', {'Celník': 3})),

        _p2('DOP', 'Jaký odborný časopis byste četli?',
            ('Flying Revue – český letecký magazín', {'Pilot': 3}),
            ('Systémy logistiky – odborný měsíčník', {'Logistik': 3}),
            ('Trucker – magazín pro profesionální řidiče', {'Řidič': 3}),
            ('Železničář – časopis Českých drah', {'Strojvedoucí': 3})),

        # --- Situační a osobnostní ---
        _p2('DOP', 'Jak reagujete na neočekávanou změnu plánu?',
            ('Rychle přepočítám varianty a vyberu nejefektivnější', {'Logistik': 3}),
            ('Klidně upravím kurz a informuji posádku', {'Kapitán plavidla': 3}),
            ('Přeorganizuji dispečink a přidělím nové úkoly', {'Dispečer': 3}),
            ('Přizpůsobím svoji trasu a popojíždím dál', {'Řidič': 3})),

        _p2('DOP', 'Jaký úkol v týmu přebíráte přirozeně?',
            ('Velení – jsem zvyklý řídit posádku', {'Kapitán plavidla': 3}),
            ('Koordinaci – propojuji lidi a informace', {'Dispečer': 3}),
            ('Realizaci – pracuji rukama a dodávám výsledky', {'Skladník': 3}),
            ('Kontrolu – ověřuji, že vše je v souladu s předpisy', {'Celník': 3})),

        _p2('DOP', 'Jak se cítíte při práci s velkými stroji?',
            ('Skvěle – lokomotivu ovládám s respektem', {'Strojvedoucí': 3}),
            ('Rád/a – kamion je můj druhý domov', {'Řidič': 3}),
            ('Výborně – letadlo je zázrak techniky', {'Pilot': 3}),
            ('Dobře – VZV a manipulátory znám zblízka', {'Skladník': 3})),

        _p2('DOP', 'Jak zvládáte stres z odpovědnosti za drahý náklad?',
            ('Dodržuji certifikované postupy a mám pojištění', {'Logistik': 3}),
            ('Pečlivě fixuji a kontroluji uložení nákladu', {'Skladník': 3}),
            ('Jedu opatrně a dodržuji přepravní podmínky', {'Řidič': 3}),
            ('Ověřím kompletní dokumentaci a pojistné krytí', {'Celník': 3})),

        _p2('DOP', 'Co děláte jako první po příchodu do práce?',
            ('Kontroluji stav zásilek a denní plán vychystávání', {'Skladník': 3}),
            ('Přebírám směnu a kontroluji stav dopravní situace', {'Dispečer': 3}),
            ('Provádím předjízdní kontrolu vlakové soupravy', {'Strojvedoucí': 3}),
            ('Studuji aktuální letovou dokumentaci a NOTAM', {'Pilot': 3})),

        _p2('DOP', 'Jak přistupujete k administrativní práci?',
            ('Pečlivě vyplňuji přepravní a celní dokumenty', {'Celník': 3}),
            ('Vedu evidenci zásob a inventární karty', {'Skladník': 3}),
            ('Zpracovávám faktury za dopravu a optimalizuji náklady', {'Logistik': 3}),
            ('Zapisuji do lodního deníku všechny události', {'Kapitán plavidla': 3})),

        _p2('DOP', 'Jakou formu profesní komunikace preferujete?',
            ('Standardní frazeologie s řízením letového provozu', {'Pilot': 3}),
            ('Rádiová komunikace s řidiči a operátory', {'Dispečer': 3}),
            ('Osobní kontakt s posádkou na palubě', {'Kapitán plavidla': 3}),
            ('Formální písemná komunikace a protokoly', {'Celník': 3})),

        _p2('DOP', 'Jak se stavíte k práci o víkendech a svátcích?',
            ('Letový provoz nezná svátky – jsem připraven/a', {'Pilot': 3}),
            ('Směnový provoz dispečinku běží non-stop', {'Dispečer': 3}),
            ('Kamion jede i o víkendu, pokud to předpisy dovolí', {'Řidič': 3}),
            ('Vlaky jezdí denně – jsem na to zvyklý/á', {'Strojvedoucí': 3})),

        _p2('DOP', 'Jaký aspekt BOZP je pro vás nejdůležitější?',
            ('Dodržování letových minim a přísná bezpečnost', {'Pilot': 3}),
            ('Reflexní vesty a bezpečné postupy ve skladu', {'Skladník': 3}),
            ('Doba řízení a povinné přestávky dle nařízení', {'Řidič': 3}),
            ('Bezpečnostní kontroly na přístavním terminálu', {'Kapitán plavidla': 3})),

        _p2('DOP', 'Jak reagujete, když kolega poruší bezpečnostní předpis?',
            ('Ihned zasáhnu – v letectví jde o životy', {'Pilot': 3}),
            ('Nahlásím to – na železnici platí nulová tolerance', {'Strojvedoucí': 3}),
            ('Upozorním ho – v logistice znamená chyba škodu', {'Logistik': 3}),
            ('Sepíšu protokol – předpisy jsou závazné', {'Celník': 3})),

        _p2('DOP', 'Jak byste přispěli k ekologické dopravě?',
            ('Optimalizací tras a snížením prázdných jízd', {'Logistik': 3}),
            ('Úsporným stylem jízdy a eco-drivingem', {'Řidič': 3}),
            ('Přechodem nákladní dopravy na železnici', {'Strojvedoucí': 3}),
            ('Využíváním říční dopravy s nízkou emisní zátěží', {'Kapitán plavidla': 3})),

        _p2('DOP', 'Jaký trend v dopravě vás fascinuje?',
            ('Autonomní létání a drony pro cargo', {'Pilot': 3}),
            ('Automatizované sklady s roboty a AI', {'Skladník': 2, 'Logistik': 3}),
            ('Hyperloop a vysokorychlostní železnice', {'Strojvedoucí': 3}),
            ('Blockchain v celním řízení a sledování zboží', {'Celník': 3})),

        _p2('DOP', 'Máte raději práci se zbožím, lidmi, nebo stroji?',
            ('Se zbožím – rád/a organizuji skladové zásoby', {'Skladník': 3}),
            ('S lidmi – koordinuji provoz a komunikuji', {'Dispečer': 3}),
            ('Se stroji – ovládám lokomotivu nebo vozidlo', {'Strojvedoucí': 3, 'Řidič': 2}),
            ('S dokumenty – kontroluji a analyzuji data', {'Celník': 3})),

        _p2('DOP', 'Jaký typ rozhodnutí děláte nejraději?',
            ('Strategická – plánuji řetězce na měsíce dopředu', {'Logistik': 3}),
            ('Operativní – řeším situaci tady a teď v provozu', {'Dispečer': 3}),
            ('Technická – vyhodnocuji bezpečnost za letu', {'Pilot': 3}),
            ('Navigační – volím optimální kurz a rychlost', {'Kapitán plavidla': 3})),

        _p2('DOP', 'Jak byste řešili zpožděnou dodávku klíčového materiálu?',
            ('Přepláuji zásobování z alternativního skladu', {'Logistik': 3}),
            ('Koordinuji urgentní svoz s nejbližším řidičem', {'Dispečer': 3}),
            ('Jedu expresně a dodržuji maximum povolené rychlosti', {'Řidič': 3}),
            ('Připravím dokumentaci pro zrychlené celní odbavení', {'Celník': 3})),

        _p2('DOP', 'Co vás motivuje k neustálému zlepšování?',
            ('Každá ušetřená minuta v dodávkovém řetězci se počítá', {'Logistik': 3}),
            ('Bezchybný provoz vlaku je otázka profesní cti', {'Strojvedoucí': 3}),
            ('Precizní navigace a bezpečné přistání pokaždé', {'Pilot': 3}),
            ('Dokonale organizovaný sklad bez ztrát a manko', {'Skladník': 3})),

        _p2('DOP', 'Jak se vyrovnáváte s dlouhodobým odloučením od rodiny?',
            ('Na moři jsem zvyklý/á – návrat domů si o to víc užiji', {'Kapitán plavidla': 3}),
            ('Přelety přes časová pásma jsou součást profese', {'Pilot': 3}),
            ('Několikadenní trasy kamionem mě neodradí', {'Řidič': 3}),
            ('Směnný provoz na dispečinku je náročný, ale zvladatelný', {'Dispečer': 3})),

        # ══════════════ IT: Informační technologie (241–320) ══════════════

        # --- Pracovní činnosti ---
        _p2('IT', 'Jaká denní činnost v IT vás láká nejvíce?',
            ('Psaní kódu a vývoj nových funkcí aplikace', {'Programátor': 3}),
            ('Sběr a analýza požadavků od zákazníků', {'Analytik IT': 3}),
            ('Správa serverů a síťové infrastruktury', {'Správce sítí': 3}),
            ('Návrh uživatelského rozhraní a grafických prvků', {'Webdesigner': 3})),

        _p2('IT', 'Která pracovní náplň vás zaujme?',
            ('Testování softwaru a hledání chyb', {'Tester': 3}),
            ('Tvorba datových pipeline a ETL procesů', {'Datový inženýr': 3}),
            ('Provádění penetračních testů firemní sítě', {'Kybernetik': 3}),
            ('Programování herní mechaniky a gameplay logiků', {'Herní vývojář': 3})),

        _p2('IT', 'S čím se ráno v práci nejraději pustíte do díla?',
            ('Debugování složitého bugu v produkčním kódu', {'Programátor': 3}),
            ('Příprava specifikace nového modulu systému', {'Analytik IT': 3}),
            ('Kontrola logů a monitorovacích dashboardů', {'Správce sítí': 3}),
            ('Prototypování nového designu v nástroji Figma', {'Webdesigner': 3})),

        _p2('IT', 'Co byste dělali nejraději při vývoji softwaru?',
            ('Implementaci algoritmů a datových struktur', {'Programátor': 3, 'Datový inženýr': 2}),
            ('Psaní automatizovaných testovacích scénářů', {'Tester': 3}),
            ('Modelování 3D postav a prostředí ve hře', {'Herní vývojář': 3}),
            ('Nastavení firewallových pravidel a bezpečnostních politik', {'Kybernetik': 3})),

        _p2('IT', 'Jakou činnost byste preferovali na IT oddělení?',
            ('Analýzu byznys procesů a návrh jejich digitalizace', {'Analytik IT': 3}),
            ('Konfiguraci Active Directory a správu uživatelských účtů', {'Správce sítí': 3}),
            ('Tvorbu responzivních webových stránek', {'Webdesigner': 3}),
            ('Optimalizaci SQL dotazů pro rychlejší reporting', {'Datový inženýr': 3})),

        _p2('IT', 'Která aktivita na herním studiu vás přitahuje?',
            ('Programování shaderů a vizuálních efektů', {'Herní vývojář': 4}),
            ('Testování herních levelů a reportování bugů', {'Tester': 3}),
            ('Kódování serverové části pro multiplayerovou hru', {'Programátor': 3}),
            ('Návrh herního UI a menu systému', {'Webdesigner': 3})),

        _p2('IT', 'Co byste dělali v rámci kybernetické bezpečnosti?',
            ('Analyzoval/a bezpečnostní incidenty v SIEM systému', {'Kybernetik': 4}),
            ('Monitoroval/a síťový provoz a detekoval/a anomálie', {'Správce sítí': 3}),
            ('Psal/a skripty pro automatizaci bezpečnostních kontrol', {'Programátor': 3}),
            ('Vyhodnocoval/a rizika a připravoval/a reporty pro vedení', {'Analytik IT': 3})),

        _p2('IT', 'Jakou činnost v datovém týmu byste si vybrali?',
            ('Navrhování datového skladu a dimenzionálních modelů', {'Datový inženýr': 4}),
            ('Psaní skriptů pro transformaci a čištění dat', {'Programátor': 3}),
            ('Vizualizaci dat v BI dashboardech', {'Analytik IT': 3}),
            ('Ověřování správnosti dat pomocí testovacích sad', {'Tester': 3})),

        _p2('IT', 'Jakou úlohu na projektu byste zastávali nejraději?',
            ('Code review a mentoring juniorních kolegů', {'Programátor': 3}),
            ('Tvorba use-case diagramů a procesních map', {'Analytik IT': 3}),
            ('Správa CI/CD pipeline a nasazení na servery', {'Správce sítí': 3, 'Programátor': 2}),
            ('Tvorba wireframů a klikacích prototypů', {'Webdesigner': 3})),

        _p2('IT', 'Co vás baví při práci na webovém projektu?',
            ('Kódování backendu v Pythonu nebo Javě', {'Programátor': 3}),
            ('Stylování stránek pomocí CSS a animací', {'Webdesigner': 3}),
            ('Psaní end-to-end testů v Seleniu', {'Tester': 3}),
            ('Propojení webu s databází a API endpointy', {'Datový inženýr': 3})),

        # --- Pracovní prostředí ---
        _p2('IT', 'V jakém prostředí byste nejraději pracovali?',
            ('V serverovně mezi racky a síťovými prvky', {'Správce sítí': 3}),
            ('V kreativním studiu s grafickými tablety', {'Webdesigner': 3}),
            ('V izolované laboratoři pro forenzní analýzu', {'Kybernetik': 3}),
            ('Ve studiu s motion capture a herním engine', {'Herní vývojář': 3})),

        _p2('IT', 'Jaký pracovní režim vám vyhovuje?',
            ('Pravidelné sprinty s denními standupy', {'Programátor': 3}),
            ('Workshopy a jednání s klienty', {'Analytik IT': 3}),
            ('Směnný provoz s pohotovostí na telefonu', {'Správce sítí': 3}),
            ('Noční testovací maratony před releasem', {'Tester': 3})),

        _p2('IT', 'Kde byste se cítili nejvíce ve svém živlu?',
            ('Na hackathonu, kde za víkend vznikne prototyp', {'Programátor': 3, 'Herní vývojář': 2}),
            ('Na konferenci o UX designu a trendech', {'Webdesigner': 3}),
            ('Na školení o nových bezpečnostních hrozbách', {'Kybernetik': 3}),
            ('Na workshopu o big data a datových platformách', {'Datový inženýr': 3})),

        _p2('IT', 'Jaký typ týmové spolupráce preferujete?',
            ('Párové programování s kolegou', {'Programátor': 3}),
            ('Prezentace analytických výstupů stakeholderům', {'Analytik IT': 3}),
            ('Koordinace s dodavateli síťových technologií', {'Správce sítí': 3}),
            ('Spolupráce s game designérem na herních levelech', {'Herní vývojář': 3})),

        _p2('IT', 'Jak chcete trávit čas mimo kancelář?',
            ('Účast na bug bounty programech online', {'Kybernetik': 3}),
            ('Vývoj vlastní indie hry ve volném čase', {'Herní vývojář': 3}),
            ('Tvorba open-source knihovny na GitHubu', {'Programátor': 3}),
            ('Blogování o datové analytice a vizualizaci', {'Datový inženýr': 3})),

        # --- Nástroje a technologie ---
        _p2('IT', 'Který nástroj byste se chtěli naučit jako první?',
            ('Visual Studio Code nebo IntelliJ IDEA', {'Programátor': 3}),
            ('Figma nebo Adobe XD pro design', {'Webdesigner': 3}),
            ('Wireshark pro analýzu síťového provozu', {'Správce sítí': 3, 'Kybernetik': 2}),
            ('Unity nebo Unreal Engine pro vývoj her', {'Herní vývojář': 3})),

        _p2('IT', 'S jakým nástrojem byste nejraději pracovali denně?',
            ('JIRA pro správu testovacích případů', {'Tester': 3}),
            ('Power BI nebo Tableau pro vizualizaci dat', {'Datový inženýr': 3, 'Analytik IT': 2}),
            ('Kali Linux pro penetrační testy', {'Kybernetik': 3}),
            ('Git a terminál pro správu kódu', {'Programátor': 3})),

        _p2('IT', 'Která technologie vás fascinuje nejvíce?',
            ('Kontejnerizace a Kubernetes orchestrace', {'Správce sítí': 3, 'Programátor': 2}),
            ('Apache Spark a distribuované zpracování dat', {'Datový inženýr': 4}),
            ('Selenium a Cypress pro automatizaci testů', {'Tester': 3}),
            ('HTML5, CSS3 a moderní frontendové frameworky', {'Webdesigner': 3})),

        _p2('IT', 'Jakou platformu byste chtěli ovládnout?',
            ('AWS nebo Azure pro cloudovou infrastrukturu', {'Správce sítí': 3}),
            ('Snowflake nebo BigQuery pro datové sklady', {'Datový inženýr': 3}),
            ('Unreal Engine 5 pro fotorealistickou grafiku', {'Herní vývojář': 4}),
            ('Splunk nebo IBM QRadar pro bezpečnostní monitoring', {'Kybernetik': 3})),

        _p2('IT', 'Který programovací jazyk vás přitahuje?',
            ('Python pro rychlý vývoj a automatizaci', {'Programátor': 3, 'Datový inženýr': 2}),
            ('SQL pro práci s relačními databázemi', {'Datový inženýr': 3}),
            ('C# v kombinaci s Unity pro herní vývoj', {'Herní vývojář': 3}),
            ('JavaScript a TypeScript pro webové aplikace', {'Webdesigner': 3, 'Programátor': 2})),

        _p2('IT', 'S jakým operačním systémem chcete pracovat nejčastěji?',
            ('Linux – správa serverů a shellové skripty', {'Správce sítí': 3}),
            ('Windows Server s Active Directory', {'Správce sítí': 3, 'Kybernetik': 2}),
            ('macOS pro grafický a UX design', {'Webdesigner': 3}),
            ('Kali Linux pro etický hacking', {'Kybernetik': 3})),

        _p2('IT', 'Která databázová technologie vás zajímá?',
            ('PostgreSQL a pokročilé SQL dotazy', {'Datový inženýr': 3}),
            ('MongoDB a NoSQL přístupy', {'Programátor': 3}),
            ('Elasticsearch pro logovou analytiku', {'Kybernetik': 3, 'Správce sítí': 2}),
            ('Redis pro cachování herních stavů', {'Herní vývojář': 3})),

        _p2('IT', 'Jaký framework byste rádi používali?',
            ('Django nebo Spring Boot pro backend', {'Programátor': 3}),
            ('React nebo Vue.js pro frontend', {'Webdesigner': 3}),
            ('Apache Airflow pro orchestraci datových pipeline', {'Datový inženýr': 3}),
            ('Robot Framework pro automatizované testování', {'Tester': 3})),

        # --- Dovednosti a schopnosti ---
        _p2('IT', 'Jakou dovednost považujete za svou nejsilnější?',
            ('Logické a algoritmické myšlení', {'Programátor': 3}),
            ('Komunikace a prezentační schopnosti', {'Analytik IT': 3}),
            ('Systematičnost a důslednost při testování', {'Tester': 3}),
            ('Cit pro estetiku a vizuální kompozici', {'Webdesigner': 3})),

        _p2('IT', 'Co vám jde nejlépe?',
            ('Rychle pochopit síťovou topologii a odhalit slabinu', {'Správce sítí': 3}),
            ('Analyzovat velké datasety a najít v nich vzorce', {'Datový inženýr': 3}),
            ('Myslet jako útočník a předvídat hrozby', {'Kybernetik': 3}),
            ('Navrhnout vtahující herní svět a příběh', {'Herní vývojář': 3})),

        _p2('IT', 'Které schopnosti byste chtěli zdokonalit?',
            ('Čistý kód a architektonické vzory (SOLID, DRY)', {'Programátor': 3}),
            ('Vedení analytických workshopů s byznysem', {'Analytik IT': 3}),
            ('Responzivní design a přístupnost (a11y)', {'Webdesigner': 3}),
            ('Performance testing a load testing', {'Tester': 3})),

        _p2('IT', 'Jaká vlastnost vás nejlépe vystihuje?',
            ('Trpělivost při hledání příčiny chyby', {'Tester': 3, 'Programátor': 2}),
            ('Kreativita při vizuálním zpracování', {'Webdesigner': 3, 'Herní vývojář': 2}),
            ('Analytické myšlení při vyhodnocování rizik', {'Kybernetik': 3}),
            ('Preciznost při modelování datových struktur', {'Datový inženýr': 3})),

        _p2('IT', 'V čem vynikáte oproti ostatním?',
            ('Dokážu rychle rozložit složitý problém na menší části', {'Programátor': 3, 'Analytik IT': 2}),
            ('Mám přehled o aktuálních bezpečnostních hrozbách', {'Kybernetik': 3}),
            ('Umím nadesignovat intuitivní uživatelskou cestu', {'Webdesigner': 3}),
            ('Zvládnu optimalizovat dotazy na milionových tabulkách', {'Datový inženýr': 3})),

        # --- Hodnoty a motivace ---
        _p2('IT', 'Co vás motivuje k práci v IT nejvíce?',
            ('Vytvářet funkční aplikace, které lidé denně používají', {'Programátor': 3}),
            ('Chránit organizace před kybernetickými útoky', {'Kybernetik': 3}),
            ('Přinášet zákazníkům přehledná datová řešení', {'Datový inženýr': 3}),
            ('Tvořit vizuálně krásné a použitelné weby', {'Webdesigner': 3})),

        _p2('IT', 'Jaký dopad chcete svou prací mít?',
            ('Zabezpečit firemní síť tak, aby neunikla žádná data', {'Kybernetik': 3}),
            ('Navrhnout systém, který zefektivní práci stovek lidí', {'Analytik IT': 3}),
            ('Zajistit stabilní a dostupnou infrastrukturu 24/7', {'Správce sítí': 3}),
            ('Vytvořit hru, která přinese radost milionům hráčů', {'Herní vývojář': 3})),

        _p2('IT', 'Co je pro vás v práci nejdůležitější?',
            ('Neustálé učení se novým technologiím', {'Programátor': 3, 'Datový inženýr': 2}),
            ('Spolupráce s lidmi z různých oddělení', {'Analytik IT': 3}),
            ('Kvalita výstupu – žádný bug nesmí projít', {'Tester': 3}),
            ('Bezpečnost a ochrana citlivých informací', {'Kybernetik': 3})),

        _p2('IT', 'Proč byste chtěli pracovat v IT?',
            ('Fascinuje mě tvorba her a interaktivních světů', {'Herní vývojář': 3}),
            ('Chci pomáhat firmám lépe pochopit data', {'Datový inženýr': 3, 'Analytik IT': 2}),
            ('Baví mě řešit technické problémy se sítěmi', {'Správce sítí': 3}),
            ('Chci navrhovat weby, které se lidem dobře používají', {'Webdesigner': 3})),

        _p2('IT', 'Co oceňujete na IT kariéře?',
            ('Možnost vzdáleně pracovat odkudkoli na světě', {'Programátor': 3, 'Webdesigner': 2}),
            ('Vysokou poptávku po specialistech na bezpečnost', {'Kybernetik': 3}),
            ('Práci s nejmodernějšími datovými technologiemi', {'Datový inženýr': 3}),
            ('Jasně měřitelné výsledky – testy buď projdou, nebo ne', {'Tester': 3})),

        # --- Řešení problémů a scénáře ---
        _p2('IT', 'Webová aplikace padá při vysoké zátěži. Co uděláte jako první?',
            ('Analyzuji kód a hledám memory leaky', {'Programátor': 3}),
            ('Zkontroluji kapacitu serverů a síťové propustnosti', {'Správce sítí': 3}),
            ('Spustím load testy a identifikuji bottleneck', {'Tester': 3}),
            ('Prozkoumám databázové dotazy a jejich výkon', {'Datový inženýr': 3})),

        _p2('IT', 'Zákazník hlásí, že systém nefunguje správně. Jak reagujete?',
            ('Sepíšu požadavky a ověřím je proti specifikaci', {'Analytik IT': 3}),
            ('Replikuji chybu v testovacím prostředí', {'Tester': 3}),
            ('Prověřím logy na serveru a síťové spojení', {'Správce sítí': 3}),
            ('Opravím bug v kódu a nasadím hotfix', {'Programátor': 3})),

        _p2('IT', 'Firma chce nový e-shop. Co je vaše první akce?',
            ('Zmapuji business požadavky a nakreslím procesní mapu', {'Analytik IT': 3}),
            ('Navrhnu vizuální styl, barvy a layout stránek', {'Webdesigner': 3}),
            ('Zvolím technologický stack a začnu kódovat', {'Programátor': 3}),
            ('Připravím testovací plán a kritéria přijetí', {'Tester': 3})),

        _p2('IT', 'V síti se objevil podezřelý provoz. Co uděláte?',
            ('Spustím forenzní analýzu a hledám indikátory kompromitace', {'Kybernetik': 4}),
            ('Izoaluji postižený segment sítě a zkontroluji firewall', {'Správce sítí': 3}),
            ('Analyzuji logy a koreluji události v SIEM', {'Kybernetik': 3}),
            ('Zkontroluji, zda útok neexfiltroval data z databáze', {'Datový inženýr': 3})),

        _p2('IT', 'Hra se zasekává při vykreslování složité scény. Řešení?',
            ('Optimalizuji shadery a snížím polygon count', {'Herní vývojář': 4}),
            ('Profiluji kód a hledám neefektivní smyčky', {'Programátor': 3}),
            ('Testuji na různých konfiguracích hardwaru', {'Tester': 3}),
            ('Zkontroluji, zda server stíhá posílat game state', {'Správce sítí': 3})),

        _p2('IT', 'Databáze je pomalá a reporty trvají hodiny. Jak to vyřešíte?',
            ('Přestavím datový model a přidám vhodné indexy', {'Datový inženýr': 4}),
            ('Navrhnu přechod na inkrementální ETL místo full load', {'Datový inženýr': 3}),
            ('Přepíšu dotazy a optimalizuji je', {'Programátor': 3}),
            ('Navýším kapacitu serveru a přidám paměť', {'Správce sítí': 3})),

        _p2('IT', 'Uživatelé si stěžují, že web je nepřehledný. Co navrhnete?',
            ('Provedu uživatelský výzkum a A/B testování', {'Webdesigner': 3}),
            ('Přepracuji navigaci a informační architekturu', {'Webdesigner': 3, 'Analytik IT': 2}),
            ('Přidám analytiku chování uživatelů na stránce', {'Datový inženýr': 3}),
            ('Otestuji přístupnost webu pomocí screen readeru', {'Tester': 3})),

        _p2('IT', 'Manažer chce do týdne nasadit novou funkci. Jak postupujete?',
            ('Naprogramuji MVP a iterativně vylepšuji', {'Programátor': 3}),
            ('Rychle navrhnu mockup a ověřím s uživateli', {'Webdesigner': 3}),
            ('Vytvořím smoke testy, aby se nic nerozbilo', {'Tester': 3}),
            ('Analyzuji dopad na existující procesy a systémy', {'Analytik IT': 3})),

        _p2('IT', 'Do firmy přišel ransomware útok. Co je vaše role?',
            ('Izoluji napadené systémy a zahájím incident response', {'Kybernetik': 4}),
            ('Obnovím data ze zálohy a zkontroluju integritu', {'Správce sítí': 3}),
            ('Analyzuji vektor útoku a připravím report', {'Kybernetik': 3}),
            ('Ověřím, zda zálohy databáze nejsou kompromitované', {'Datový inženýr': 3})),

        _p2('IT', 'Při testování se objeví kritická chyba den před releasem. Co děláte?',
            ('Zdokumentuji chybu a připravím detailní bug report', {'Tester': 3}),
            ('Okamžitě lokalizuji a opravím příčinu v kódu', {'Programátor': 3}),
            ('Posoudím dopad na business procesy a dohodnu se se stakeholdery', {'Analytik IT': 3}),
            ('Ověřím, že oprava nezpůsobí bezpečnostní zranitelnost', {'Kybernetik': 3})),

        # --- Mix: dovednosti, hodnoty, scénáře ---
        _p2('IT', 'Jak nejraději dokumentujete svou práci?',
            ('Komentáři v kódu a README soubory', {'Programátor': 3}),
            ('Analytickými dokumenty a diagramy', {'Analytik IT': 3}),
            ('Testovacími reporty a screenshot důkazy', {'Tester': 3}),
            ('Síťovými diagramy a konfiguračními záznamy', {'Správce sítí': 3})),

        _p2('IT', 'Který certifikát byste chtěli získat?',
            ('CCNA – Cisco síťová certifikace', {'Správce sítí': 3}),
            ('CEH – Certified Ethical Hacker', {'Kybernetik': 3}),
            ('ISTQB – certifikace softwarového testera', {'Tester': 3}),
            ('Google Professional Data Engineer', {'Datový inženýr': 3})),

        _p2('IT', 'Na jaké téma byste přednášeli na konferenci?',
            ('Clean architecture a návrhové vzory', {'Programátor': 3}),
            ('Jak provádět efektivní UX audit webu', {'Webdesigner': 3}),
            ('Zero trust architektura a moderní bezpečnost', {'Kybernetik': 3}),
            ('Real-time datové pipeline v Apache Kafka', {'Datový inženýr': 3})),

        _p2('IT', 'Jaký vedlejší projekt byste si zvolili?',
            ('Vývoj mobilní aplikace pro osobní potřebu', {'Programátor': 3}),
            ('Sestavení vlastního domácího serveru a NAS', {'Správce sítí': 3}),
            ('Tvorba 2D indie hry s originálním příběhem', {'Herní vývojář': 3}),
            ('Redesign portfoliového webu s animacemi', {'Webdesigner': 3})),

        _p2('IT', 'Jaký typ problémů řešíte nejraději?',
            ('Logické hádanky a optimalizační úlohy', {'Programátor': 3, 'Datový inženýr': 2}),
            ('Komunikační problémy mezi odděleními', {'Analytik IT': 3}),
            ('Výpadky služeb a hledání root cause', {'Správce sítí': 3}),
            ('Vizuální nekonzistence a UX problémy', {'Webdesigner': 3})),

        _p2('IT', 'Jak reagujete na novou technologii na trhu?',
            ('Okamžitě si ji vyzkouším v side projektu', {'Programátor': 3, 'Herní vývojář': 2}),
            ('Posoudím, jaký přínos by měla pro naše procesy', {'Analytik IT': 3}),
            ('Zkontroluji její bezpečnostní posudky a CVE', {'Kybernetik': 3}),
            ('Vyhodnotím, jak se integruje s naší datovou platformou', {'Datový inženýr': 3})),

        _p2('IT', 'Co vás na práci v IT frustruje nejvíce?',
            ('Špatně napsaná specifikace, která se neustále mění', {'Analytik IT': 3}),
            ('Legacy kód bez testů a dokumentace', {'Tester': 3, 'Programátor': 2}),
            ('Ignorování bezpečnostních doporučení vedením', {'Kybernetik': 3}),
            ('Pomalé servery a neoptimalizovaná infrastruktura', {'Správce sítí': 3})),

        _p2('IT', 'Jaký je váš přístup k učení nových věcí?',
            ('Čtu dokumentaci a píšu vlastní kód', {'Programátor': 3}),
            ('Sleduji tutoriály o game designu na YouTube', {'Herní vývojář': 3}),
            ('Procvičuji se na CTF (Capture The Flag) výzvách', {'Kybernetik': 3}),
            ('Experimentuji s novými CSS technikami a animacemi', {'Webdesigner': 3})),

        _p2('IT', 'Co byste dělali, kdybyste měli volný den na sebevzdělávání?',
            ('Řešil/a algoritmické úlohy na LeetCode', {'Programátor': 3}),
            ('Studoval/a ISO 27001 a připravoval/a se na audit', {'Kybernetik': 3}),
            ('Učil/a se nový BI nástroj pro vizualizaci dat', {'Datový inženýr': 3}),
            ('Zkoušel/a nové pluginy a efekty v herním engine', {'Herní vývojář': 3})),

        _p2('IT', 'Jak přistupujete ke zpětné vazbě od uživatelů?',
            ('Analyzuji data z uživatelských session recordings', {'Webdesigner': 3}),
            ('Zařadím bug reporty do backlogu a priorizuji', {'Tester': 3, 'Programátor': 2}),
            ('Provedu strukturovaný rozhovor a zmapuji požadavky', {'Analytik IT': 3}),
            ('Vyhodnotím, zda stížnosti neindikují bezpečnostní problém', {'Kybernetik': 3})),

        _p2('IT', 'Firma migruje do cloudu. Jaká je vaše úloha?',
            ('Přestavím síťovou architekturu pro cloud', {'Správce sítí': 3}),
            ('Migrace databází a nastavení cloudových datových služeb', {'Datový inženýr': 3}),
            ('Přepíšu aplikaci tak, aby využívala cloudové služby', {'Programátor': 3}),
            ('Ověřím bezpečnostní konfiguraci cloudového prostředí', {'Kybernetik': 3})),

        _p2('IT', 'Na čem záleží při návrhu herního levelu?',
            ('Na plynulém gameplay a vyváženosti obtížnosti', {'Herní vývojář': 3}),
            ('Na vizuální atraktivitě a atmosféře prostředí', {'Webdesigner': 3, 'Herní vývojář': 2}),
            ('Na stabilitě – žádné pády ani grafické glitche', {'Tester': 3}),
            ('Na efektivním načítání assetů z disku', {'Programátor': 3})),

        _p2('IT', 'Kolega chce nasadit neotestovaný kód do produkce. Co uděláte?',
            ('Zastavím deployment a trvám na code review', {'Programátor': 3}),
            ('Rychle spustím regresní testy', {'Tester': 3}),
            ('Upozorním na potenciální bezpečnostní riziko', {'Kybernetik': 3}),
            ('Posoudím dopad na byznys procesy', {'Analytik IT': 3})),

        _p2('IT', 'Jaký typ grafiky vás přitahuje?',
            ('3D modely postav a herních prostředí', {'Herní vývojář': 3}),
            ('Moderní webový design s micro-interakcemi', {'Webdesigner': 3}),
            ('Datové vizualizace – grafy, heatmapy, dashboardy', {'Datový inženýr': 3}),
            ('UML diagramy a procesní flowcharty', {'Analytik IT': 3})),

        _p2('IT', 'Jak si představujete ideální páteční odpoledne v práci?',
            ('Refaktoring kódu a zlepšování architektury', {'Programátor': 3}),
            ('Retrospektiva sprintu a plánování dalšího', {'Analytik IT': 3}),
            ('Zálohy, aktualizace serverů a patch management', {'Správce sítí': 3}),
            ('Hraní právě vydané verze vlastní hry', {'Herní vývojář': 3})),

        _p2('IT', 'Jaký IT problém byste chtěli vyřešit pro celý svět?',
            ('Zabezpečit internet a eliminovat phishing', {'Kybernetik': 3}),
            ('Zpřístupnit web všem lidem bez ohledu na handicap', {'Webdesigner': 3}),
            ('Demokratizovat přístup k datům a analytice', {'Datový inženýr': 3}),
            ('Zjednodušit programování tak, aby ho zvládl každý', {'Programátor': 3})),

        _p2('IT', 'Při pohovoru na IT pozici vás zaujme otázka:',
            ('Jak byste navrhli architekturu mikroslužeb?', {'Programátor': 3}),
            ('Jak byste provedli threat modeling pro tuto aplikaci?', {'Kybernetik': 3}),
            ('Jaký postup zvolíte při analýze nového projektu?', {'Analytik IT': 3}),
            ('Jak byste pokryli testováním kritické funkcionality?', {'Tester': 3})),

        _p2('IT', 'Co je pro vás hlavní měřítko úspěchu projektu?',
            ('Stabilní a bezchybný kód s vysokým pokrytím testy', {'Tester': 3, 'Programátor': 2}),
            ('Spokojený zákazník, který systém efektivně využívá', {'Analytik IT': 3}),
            ('Nulový počet bezpečnostních incidentů', {'Kybernetik': 3}),
            ('Vizuálně atraktivní produkt s pozitivními recenzemi', {'Webdesigner': 3, 'Herní vývojář': 2})),

        _p2('IT', 'Jakou knihu byste si přečetli jako první?',
            ('Clean Code od Roberta C. Martina', {'Programátor': 3}),
            ('The Design of Everyday Things od Dona Normana', {'Webdesigner': 3}),
            ('The Art of Game Design od Jesse Schella', {'Herní vývojář': 3}),
            ('Designing Data-Intensive Applications od M. Kleppmanna', {'Datový inženýr': 3})),

        _p2('IT', 'Jaký výstup vaší práce vás potěší nejvíce?',
            ('Zelené testy – všechny prošly bez chyby', {'Tester': 3}),
            ('Funkční síť bez výpadků po celý měsíc', {'Správce sítí': 3}),
            ('Úspěšně odražený kybernetický útok', {'Kybernetik': 3}),
            ('Hra, kterou recenzenti ohodnotili na 9/10', {'Herní vývojář': 3})),

        _p2('IT', 'Co děláte, když narazíte na problém, který neumíte vyřešit?',
            ('Hledám odpovědi na Stack Overflow a v dokumentaci', {'Programátor': 3}),
            ('Konzultuji s bezpečnostním komunitou a CERT týmy', {'Kybernetik': 3}),
            ('Navrhnu A/B test, abych problém lépe pochopil/a', {'Webdesigner': 3}),
            ('Zapojím do analýzy další stakeholdery', {'Analytik IT': 3})),

        _p2('IT', 'Jaký aspekt vývoje mobilní aplikace vás baví nejvíce?',
            ('Programování business logiky a API', {'Programátor': 3}),
            ('Návrh UI a uživatelské navigace', {'Webdesigner': 3}),
            ('Testování na různých zařízeních a OS verzích', {'Tester': 3}),
            ('Implementace herních prvků a gamifikace', {'Herní vývojář': 3})),

        _p2('IT', 'V týmu zastáváte roli člověka, který:',
            ('Píše spolehlivý a udržovatelný kód', {'Programátor': 3}),
            ('Překládá technický jazyk do řeči byznysu', {'Analytik IT': 3}),
            ('Hlídá kvalitu a nikdy nepřehlédne chybu', {'Tester': 3}),
            ('Řeší problémy s připojením a infrastrukturou', {'Správce sítí': 3})),

        _p2('IT', 'Jakou roli byste hráli ve startupovém týmu?',
            ('CTO – architekturu a vývoj produktu', {'Programátor': 3}),
            ('Datového specialistu – analytiku a metriky', {'Datový inženýr': 3}),
            ('Bezpečnostního poradce – ochranu od začátku', {'Kybernetik': 3}),
            ('UX designéra – vzhled a použitelnost produktu', {'Webdesigner': 3})),

        _p2('IT', 'Jak přistupujete k automatizaci?',
            ('Píšu skripty pro automatizaci opakujících se úloh', {'Programátor': 3}),
            ('Automatizuji regresní a smoke testy', {'Tester': 3}),
            ('Automatizuji provisioning serverů pomocí Ansible', {'Správce sítí': 3}),
            ('Automatizuji datové pipeline a scheduling', {'Datový inženýr': 3})),

        _p2('IT', 'Co vás nejvíce baví na práci s daty?',
            ('Navrhování efektivních datových modelů', {'Datový inženýr': 3}),
            ('Extrakce business insights z analytických reportů', {'Analytik IT': 3}),
            ('Detekce anomálií jako známek bezpečnostních hrozeb', {'Kybernetik': 3}),
            ('Procedurální generování herního obsahu z dat', {'Herní vývojář': 3})),

        _p2('IT', 'Jaký typ testování vás zajímá nejvíce?',
            ('Manuální explorativní testování nových funkcí', {'Tester': 3}),
            ('Penetrační testování webových aplikací', {'Kybernetik': 3}),
            ('Testování výkonu a škálovatelnosti datových pipeline', {'Datový inženýr': 3}),
            ('Testování uživatelské přívětivosti (usability testing)', {'Webdesigner': 3})),

        _p2('IT', 'Jak reagujete, když se dozvíte o nové zranitelnosti (CVE)?',
            ('Okamžitě zkontroluju, zda se týká naší infrastruktury', {'Správce sítí': 3}),
            ('Ověřím, zda náš kód neobsahuje zranitelnou závislost', {'Programátor': 3}),
            ('Provedu analýzu dopadu a navrhnu mitigaci', {'Kybernetik': 4}),
            ('Přidám test case pro ověření, že jsme chráněni', {'Tester': 3})),

        _p2('IT', 'Při prezentaci IT projektu se zaměřujete na:',
            ('Technickou architekturu a použité technologie', {'Programátor': 3}),
            ('Byznys hodnotu a návratnost investice', {'Analytik IT': 3}),
            ('Vizuální demo a uživatelskou zkušenost', {'Webdesigner': 3}),
            ('Kvalitu, pokrytí testy a nulovou chybovost', {'Tester': 3})),

        _p2('IT', 'Jakou herní žánrovou disciplínu byste chtěli ovládnout?',
            ('Fyzikální simulace a procedurální animace', {'Herní vývojář': 4}),
            ('Síťový kód pro multiplayer v reálném čase', {'Programátor': 3, 'Herní vývojář': 2}),
            ('Herní AI a pathfinding algoritmy', {'Programátor': 3}),
            ('Zvukový design a integraci audio engine', {'Herní vývojář': 3})),

        _p2('IT', 'Jaký cloud-native přístup vás nejvíce oslovuje?',
            ('Serverless funkce a event-driven architektura', {'Programátor': 3}),
            ('Správa Kubernetes clusterů a service mesh', {'Správce sítí': 3}),
            ('Cloud-based datové jezírko a analytické služby', {'Datový inženýr': 3}),
            ('Cloud security posture management (CSPM)', {'Kybernetik': 3})),

        _p2('IT', 'Jak si představujete svůj kariérní růst v IT?',
            ('Od juniora přes seniora k softwarovému architektovi', {'Programátor': 3}),
            ('Od testera k vedoucímu QA oddělení', {'Tester': 3}),
            ('Od síťového technika k cloud solutions architektovi', {'Správce sítí': 3}),
            ('Od datového analytika k chief data officerovi', {'Datový inženýr': 3})),

        _p2('IT', 'Jaký projekt ve škole byste si vybrali?',
            ('Naprogramovat chatbota s umělou inteligencí', {'Programátor': 3}),
            ('Analyzovat požadavky a navrhnout informační systém', {'Analytik IT': 3}),
            ('Vytvořit portfolio web s vlastním designem', {'Webdesigner': 3}),
            ('Vyvinout jednoduchou počítačovou hru', {'Herní vývojář': 3})),

        _p2('IT', 'Při práci na API se zaměřujete hlavně na:',
            ('Čistý kód, RESTful konvence a dokumentaci', {'Programátor': 3}),
            ('Správné ošetření autentizace a autorizace', {'Kybernetik': 3}),
            ('Efektivní datové struktury a rychlost odpovědí', {'Datový inženýr': 3}),
            ('Automatizované testy endpointů a edge casů', {'Tester': 3})),

        _p2('IT', 'Co byste zlepšili na firemním intranetu?',
            ('Přepsali legacy kód do moderního frameworku', {'Programátor': 3}),
            ('Vylepšili design, navigaci a mobilní verzi', {'Webdesigner': 3}),
            ('Zvýšili bezpečnost přihlašování o MFA', {'Kybernetik': 3}),
            ('Přidali dashboardy s firemními KPI z datového skladu', {'Datový inženýr': 3})),

        _p2('IT', 'Jak řešíte, když kolegovi nefunguje počítač?',
            ('Přihlásím se vzdáleně a zkontroluju síťové nastavení', {'Správce sítí': 3}),
            ('Zeptám se na detaily a systematicky diagnostikuji', {'Analytik IT': 3}),
            ('Zkontroluju, zda nejde o malware nebo bezpečnostní incident', {'Kybernetik': 3}),
            ('Ověřím, zda problém neovlivňuje i ostatní – spustím smoke test', {'Tester': 3})),

        _p2('IT', 'Jaký přínos pro tým je vám nejbližší?',
            ('Dodávám kvalitní a optimalizovaný kód', {'Programátor': 3}),
            ('Propojuji technický a byznys svět', {'Analytik IT': 3}),
            ('Starám se o stabilní infrastrukturu pro všechny', {'Správce sítí': 3}),
            ('Zajistím, že žádná chyba se nedostane k uživateli', {'Tester': 3})),

        # ══════════════ ZDR: Zdravotnictví a medicína (321–400) ══════════════

        # 321
        _p2('ZDR', 'Co vás nejvíce přitahuje na práci ve zdravotnictví?',
            ('Diagnostikovat nemoci a navrhovat léčbu', {'Lékař': 4}),
            ('Připravovat a vydávat léčivé přípravky', {'Farmaceut': 3}),
            ('Poskytovat první pomoc v krizových situacích', {'Záchranář': 3}),
            ('Pečovat o pacienty a monitorovat jejich stav', {'Zdravotní sestra': 3})),

        # 322
        _p2('ZDR', 'Jak byste řešili pacienta s bolestí zad?',
            ('Provedl bych fyzikální vyšetření a navrhl rehabilitační plán', {'Fyzioterapeut': 4}),
            ('Zkontroloval bych rentgen a zvážil další diagnostiku', {'Lékař': 3}),
            ('Doporučil bych vhodné analgetikum a sledoval interakce', {'Farmaceut': 3}),
            ('Zhodnotil bych výživový stav a navrhl protizánětlivou dietu', {'Nutriční terapeut': 3})),

        # 323
        _p2('ZDR', 'Která činnost je vám nejbližší?',
            ('Provádění operačních zákroků', {'Lékař': 4}),
            ('Ošetření zubního kazu a nasazení korunky', {'Zubař': 4}),
            ('Resuscitace a stabilizace pacienta na místě nehody', {'Záchranář': 3}),
            ('Kalibrace a údržba zdravotnických přístrojů', {'Biomedicínský inženýr': 3})),

        # 324
        _p2('ZDR', 'Co byste dělali na ranní směně v nemocnici?',
            ('Vizitu u pacientů, kontrolu výsledků a ordinaci léčby', {'Lékař': 4}),
            ('Podávání léků, měření vitálních funkcí, převazy', {'Zdravotní sestra': 4}),
            ('Rehabilitační cvičení s pacienty po operaci', {'Fyzioterapeut': 3}),
            ('Kontrolu funkčnosti přístrojů na oddělení', {'Biomedicínský inženýr': 3})),

        # 325
        _p2('ZDR', 'Jak byste přistoupili k pacientovi s cukrovkou?',
            ('Nastavil bych léčbu inzulínem a sledoval glykémii', {'Lékař': 3}),
            ('Připravil bych individuální dietní plán', {'Nutriční terapeut': 4}),
            ('Poradil bych s výběrem vhodného glukometru', {'Biomedicínský inženýr': 2}),
            ('Edukoval bych pacienta o správném užívání léků', {'Farmaceut': 3})),

        # 326
        _p2('ZDR', 'Na čem byste rádi pracovali v laboratoři?',
            ('Na vývoji nových léčivých přípravků', {'Farmaceut': 4}),
            ('Na testování a validaci zdravotnických přístrojů', {'Biomedicínský inženýr': 4}),
            ('Na analýze krevních vzorků pro diagnostiku', {'Lékař': 2}),
            ('Na nutričním screeningu hospitalizovaných pacientů', {'Nutriční terapeut': 3})),

        # 327
        _p2('ZDR', 'Jak reagujete na akutní situaci – člověk kolabuje na ulici?',
            ('Okamžitě zahájím resuscitaci a volám záchranku', {'Záchranář': 4}),
            ('Zjistím anamnézu a provedu orientační vyšetření', {'Lékař': 3}),
            ('Zkontroluju, zda nemá u sebe léky, a pomohu je podat', {'Farmaceut': 2}),
            ('Zajistím stabilní polohu a monitoruji vitální funkce', {'Zdravotní sestra': 3})),

        # 328
        _p2('ZDR', 'Co vás láká na zubním lékařství?',
            ('Estetická stomatologie – bělení, fazety, korunky', {'Zubař': 4}),
            ('Chirurgické zavádění zubních implantátů', {'Zubař': 3, 'Lékař': 2}),
            ('Ortodontická léčba – rovnátka a alignery', {'Zubař': 4}),
            ('Prevence a dentální hygiena u dětí', {'Zubař': 3, 'Zdravotní sestra': 2})),

        # 329
        _p2('ZDR', 'Jaký typ výzkumu vás zajímá?',
            ('Klinické studie nových léků', {'Farmaceut': 4, 'Lékař': 2}),
            ('Vývoj nositelných zdravotnických senzorů', {'Biomedicínský inženýr': 4}),
            ('Vliv výživy na prevenci civilizačních chorob', {'Nutriční terapeut': 4}),
            ('Nové rehabilitační metody po úrazech', {'Fyzioterapeut': 4})),

        # 330
        _p2('ZDR', 'Jak byste pomohli pacientovi po mozkové příhodě?',
            ('Navrhl bych komplexní rehabilitační program', {'Fyzioterapeut': 4}),
            ('Řídil bych akutní léčbu a farmakoterapii', {'Lékař': 3}),
            ('Monitoroval bych vitální funkce a podával léky', {'Zdravotní sestra': 3}),
            ('Upravil bych stravu pro snadné polykání', {'Nutriční terapeut': 3})),

        # 331
        _p2('ZDR', 'Která z těchto dovedností je vám nejbližší?',
            ('Manuální zručnost při operacích a zákrocích', {'Lékař': 3, 'Zubař': 3}),
            ('Komunikace s pacientem a psychická podpora', {'Zdravotní sestra': 3}),
            ('Technické myšlení a práce s přístroji', {'Biomedicínský inženýr': 4}),
            ('Rychlé rozhodování pod tlakem', {'Záchranář': 4})),

        # 332
        _p2('ZDR', 'Co byste dělali v lékárně?',
            ('Poradenství pacientům o správném užívání léků', {'Farmaceut': 4}),
            ('Přípravu individuálních magistraliter přípravků', {'Farmaceut': 4}),
            ('Řízení lékárny a objednávání zásob', {'Farmaceut': 3}),
            ('Sledování nežádoucích účinků léků – farmakovigilanci', {'Farmaceut': 3, 'Lékař': 2})),

        # 333
        _p2('ZDR', 'Jak přistoupíte ke sportovci po zranění kolena?',
            ('Navrhnu cvičební program pro návrat ke sportu', {'Fyzioterapeut': 4}),
            ('Provedu artroskopii a zhodnotím rozsah poranění', {'Lékař': 4}),
            ('Doporučím vhodné ortézy a kompenzační pomůcky', {'Biomedicínský inženýr': 2, 'Fyzioterapeut': 2}),
            ('Sestavím výživový plán pro rychlejší rekonvalescenci', {'Nutriční terapeut': 3})),

        # 334
        _p2('ZDR', 'Který aspekt urgentní medicíny vás přitahuje?',
            ('Triáž pacientů při hromadném neštěstí', {'Záchranář': 4}),
            ('Transport a stabilizace pacienta v sanitce', {'Záchranář': 4}),
            ('Akutní diagnostika a rozhodování o léčbě', {'Lékař': 3}),
            ('Obsluha defibrilátoru a monitorovacích přístrojů', {'Záchranář': 3, 'Biomedicínský inženýr': 2})),

        # 335
        _p2('ZDR', 'Co byste zlepšili ve zdravotnictví pomocí technologií?',
            ('Zavedl bych telemedicínu pro vzdálené konzultace', {'Biomedicínský inženýr': 3, 'Lékař': 2}),
            ('Vyvinul bych mobilní aplikaci pro sledování vitálních funkcí', {'Biomedicínský inženýr': 4}),
            ('Digitalizoval bych lékárenský systém pro lepší evidenci', {'Farmaceut': 2, 'Biomedicínský inženýr': 2}),
            ('Automatizoval bych nutriční screening pacientů', {'Nutriční terapeut': 2, 'Biomedicínský inženýr': 2})),

        # 336
        _p2('ZDR', 'Jak byste edukovali pacienta o zdravém životním stylu?',
            ('Sestavil bych individuální jídelníček s makronutrienty', {'Nutriční terapeut': 4}),
            ('Doporučil bych vhodný pohybový režim a cviky', {'Fyzioterapeut': 3}),
            ('Vysvětlil bych důležitost pravidelných preventivních prohlídek', {'Lékař': 3}),
            ('Poradil bych s doplňky stravy a jejich interakcemi s léky', {'Farmaceut': 3})),

        # 337
        _p2('ZDR', 'Jakou specializaci byste si vybrali?',
            ('Kardiologie – léčba srdečních onemocnění', {'Lékař': 4}),
            ('Klinická farmacie – optimalizace farmakoterapie', {'Farmaceut': 4}),
            ('Intenzivní péče – emergentní ošetřovatelství', {'Zdravotní sestra': 4}),
            ('Sportovní medicína a rehabilitace', {'Fyzioterapeut': 4})),

        # 338
        _p2('ZDR', 'Co děláte, když pacient odmítá léčbu?',
            ('Trpělivě vysvětlím rizika a hledám kompromis', {'Lékař': 3}),
            ('Empaticky vyslechnu obavy a nabídnu alternativy', {'Zdravotní sestra': 3}),
            ('Navrhnu změnu formy léku – např. z tablet na sirup', {'Farmaceut': 3}),
            ('Zapojím do léčby výživové intervence místo léků', {'Nutriční terapeut': 3})),

        # 339
        _p2('ZDR', 'Který předmět na škole vás nejvíce bavil?',
            ('Biologie a anatomie člověka', {'Lékař': 3, 'Zubař': 2}),
            ('Chemie a biochemie', {'Farmaceut': 3}),
            ('Fyzika a technika', {'Biomedicínský inženýr': 4}),
            ('Tělesná výchova a nauka o pohybu', {'Fyzioterapeut': 3, 'Záchranář': 2})),

        # 340
        _p2('ZDR', 'Jak byste pomohli obéznímu pacientovi?',
            ('Vytvořil bych kalorický deficit s vyváženou stravou', {'Nutriční terapeut': 4}),
            ('Navrhl bych pohybový program přizpůsobený jeho stavu', {'Fyzioterapeut': 3}),
            ('Zvážil bych farmakologickou léčbu obezity', {'Lékař': 3}),
            ('Zkontroloval bych interakce léků ovlivňujících hmotnost', {'Farmaceut': 3})),

        # 341
        _p2('ZDR', 'Co byste dělali s novým zdravotnickým přístrojem?',
            ('Provedl bych validaci a kalibraci přístroje', {'Biomedicínský inženýr': 4}),
            ('Napsal bych protokol pro jeho klinické použití', {'Lékař': 2, 'Biomedicínský inženýr': 2}),
            ('Proškolil bych zdravotní sestry v jeho obsluze', {'Biomedicínský inženýr': 3}),
            ('Ověřil bych jeho bezpečnost pro pacienty', {'Biomedicínský inženýr': 3, 'Lékař': 2})),

        # 342
        _p2('ZDR', 'Jak přistupujete k práci v týmu?',
            ('Koordinuji léčebný plán a vedu tým', {'Lékař': 3}),
            ('Jsem spojka mezi pacientem a lékařem', {'Zdravotní sestra': 4}),
            ('Poskytuji odborné konzultace v oblasti výživy', {'Nutriční terapeut': 3}),
            ('Zajišťuji technickou podporu pro celé oddělení', {'Biomedicínský inženýr': 3})),

        # 343
        _p2('ZDR', 'Jaký typ pacienta byste chtěli ošetřovat?',
            ('Akutní pacienty na urgentním příjmu', {'Záchranář': 3, 'Lékař': 2}),
            ('Děti v zubní ordinaci', {'Zubař': 4}),
            ('Seniory v domácí péči', {'Zdravotní sestra': 3}),
            ('Sportovce po úrazech', {'Fyzioterapeut': 4})),

        # 344
        _p2('ZDR', 'Co vás zajímá na farmakologii?',
            ('Mechanismus účinku léků na molekulární úrovni', {'Farmaceut': 4}),
            ('Správné dávkování a lékové interakce', {'Farmaceut': 3, 'Lékař': 2}),
            ('Vliv léků na nutriční stav pacienta', {'Nutriční terapeut': 3}),
            ('Vývoj nových lékových forem a nosičů', {'Farmaceut': 3, 'Biomedicínský inženýr': 2})),

        # 345
        _p2('ZDR', 'Jak byste zvládli stresovou situaci na pracovišti?',
            ('Soustředím se na prioritizaci – nejdřív zachraňuji život', {'Záchranář': 4}),
            ('Zachovám klid a systematicky řeším problém', {'Lékař': 3}),
            ('Komunikuji s kolegy a sdílíme úkoly', {'Zdravotní sestra': 3}),
            ('Držím se technických postupů a protokolů', {'Biomedicínský inženýr': 3})),

        # 346
        _p2('ZDR', 'Která pracovní náplň vás oslovuje?',
            ('Provádění odběrů krve a biologického materiálu', {'Zdravotní sestra': 4}),
            ('Sestavování rehabilitačních cvičebních programů', {'Fyzioterapeut': 4}),
            ('Analýza nutričního příjmu hospitalizovaných', {'Nutriční terapeut': 4}),
            ('Správa nemocničního informačního systému', {'Biomedicínský inženýr': 4})),

        # 347
        _p2('ZDR', 'Co vás motivuje k práci ve zdravotnictví?',
            ('Zachraňovat životy v terénu', {'Záchranář': 4}),
            ('Pomáhat lidem zbavit se bolesti zubů', {'Zubař': 4}),
            ('Vracet lidem pohyblivost po úrazech', {'Fyzioterapeut': 3}),
            ('Zajistit bezpečnou farmakoterapii', {'Farmaceut': 3})),

        # 348
        _p2('ZDR', 'Jak byste řešili výživu pacienta na JIP?',
            ('Zavedl bych enterální výživu sondou', {'Nutriční terapeut': 3, 'Lékař': 2}),
            ('Monitoroval bych příjem živin a tekutin', {'Nutriční terapeut': 4}),
            ('Kontroloval bych kompatibilitu výživy s podávanými léky', {'Farmaceut': 3}),
            ('Sledoval bych vitální funkce a bilanci tekutin', {'Zdravotní sestra': 3})),

        # 349
        _p2('ZDR', 'Jaký výkon byste chtěli provádět?',
            ('Endoskopické vyšetření trávicího traktu', {'Lékař': 4}),
            ('Zubní implantaci s náhradou chybějícího zubu', {'Zubař': 4}),
            ('Manuální terapii páteře a kloubů', {'Fyzioterapeut': 4}),
            ('Defibrilaci a zajištění dýchacích cest', {'Záchranář': 4})),

        # 350
        _p2('ZDR', 'Jak přistupujete k prevenci?',
            ('Osvětou o hygieně dutiny ústní a pravidelnými prohlídkami', {'Zubař': 4}),
            ('Edukací o zdravé výživě a vyvážené stravě', {'Nutriční terapeut': 4}),
            ('Očkováním a screeningovými programy', {'Lékař': 3}),
            ('Poradenstvím o správném užívání volně prodejných léků', {'Farmaceut': 3})),

        # 351
        _p2('ZDR', 'Který pracovní den je vám nejbližší?',
            ('Operační sál – asistovat při chirurgickém výkonu', {'Lékař': 4}),
            ('Záchranná služba – výjezdy k pacientům', {'Záchranář': 4}),
            ('Lékárna – výdej a příprava léků', {'Farmaceut': 4}),
            ('Ambulance – rehabilitační cvičení s pacienty', {'Fyzioterapeut': 4})),

        # 352
        _p2('ZDR', 'Jak byste využili znalost anatomie?',
            ('K přesné diagnostice onemocnění pohybového aparátu', {'Lékař': 3}),
            ('K provádění zubních extrakcí a chirurgických zákroků', {'Zubař': 4}),
            ('K cílenému terapeutickému cvičení a mobilizacím', {'Fyzioterapeut': 4}),
            ('K přesnému zavedení intravenózní kanyly', {'Zdravotní sestra': 3})),

        # 353
        _p2('ZDR', 'Jakým způsobem byste pomáhali dětem?',
            ('Pediatrickým vyšetřením a léčbou dětských nemocí', {'Lékař': 4}),
            ('Péčí o dětského pacienta na oddělení', {'Zdravotní sestra': 3}),
            ('Vývojovou rehabilitací a senzomotorickou stimulací', {'Fyzioterapeut': 3}),
            ('Sestavením jídelníčku pro zdravý růst a vývoj', {'Nutriční terapeut': 3})),

        # 354
        _p2('ZDR', 'Co vás zajímá na protetice v zubním lékařství?',
            ('Navrhování a zhotovování zubních náhrad', {'Zubař': 4}),
            ('Výběr biokompatibilních materiálů pro implantáty', {'Zubař': 3, 'Biomedicínský inženýr': 2}),
            ('Digitální 3D plánování protetických prací', {'Zubař': 2, 'Biomedicínský inženýr': 3}),
            ('Pooperační péče a kontrola hojení', {'Zdravotní sestra': 3})),

        # 355
        _p2('ZDR', 'Jak byste přistoupili k léčbě chronické bolesti?',
            ('Multidisciplinárním přístupem a nastavením medikace', {'Lékař': 4}),
            ('Fyzioterapeutickými metodami – elektroterapie, laser', {'Fyzioterapeut': 4}),
            ('Konzultací o analgetikách a jejich bezpečném užívání', {'Farmaceut': 3}),
            ('Protizánětlivou dietou a suplementací', {'Nutriční terapeut': 3})),

        # 356
        _p2('ZDR', 'Jaký druh dokumentace je vám nejbližší?',
            ('Lékařská zpráva a dekurz z vizity', {'Lékař': 4}),
            ('Ošetřovatelská dokumentace a plán péče', {'Zdravotní sestra': 4}),
            ('Protokol o kalibraci zdravotnického přístroje', {'Biomedicínský inženýr': 4}),
            ('Záznam o nutričním screeningu a dietním plánu', {'Nutriční terapeut': 4})),

        # 357
        _p2('ZDR', 'Kterou technologii byste chtěli ovládat?',
            ('CT a MRI diagnostické přístroje', {'Lékař': 2, 'Biomedicínský inženýr': 3}),
            ('Moderní CAD/CAM systémy pro zubní protetiku', {'Zubař': 3, 'Biomedicínský inženýr': 2}),
            ('Plicní ventilátory a monitory vitálních funkcí', {'Záchranář': 3, 'Biomedicínský inženýr': 2}),
            ('Software pro analýzu tělesného složení', {'Nutriční terapeut': 3})),

        # 358
        _p2('ZDR', 'Jak vidíte svou roli v nemocnici?',
            ('Jako vedoucí operačního týmu', {'Lékař': 4}),
            ('Jako odborník na technické zázemí nemocnice', {'Biomedicínský inženýr': 4}),
            ('Jako ten, kdo je s pacientem 24 hodin denně', {'Zdravotní sestra': 4}),
            ('Jako poradce v oblasti výživové podpory', {'Nutriční terapeut': 3})),

        # 359
        _p2('ZDR', 'Co byste dělali při dopravní nehodě?',
            ('Provedl vyprošťování a triáž zraněných', {'Záchranář': 4}),
            ('Řídil bych resuscitaci a stabilizaci', {'Záchranář': 3, 'Lékař': 2}),
            ('Zajistil bych žilní vstup a podal infuzi', {'Zdravotní sestra': 3}),
            ('Připravil bych přístroje pro urgentní ošetření', {'Biomedicínský inženýr': 2, 'Záchranář': 2})),

        # 360
        _p2('ZDR', 'Kterou oblast nutriční terapie preferujete?',
            ('Klinická výživa u onkologických pacientů', {'Nutriční terapeut': 4}),
            ('Sportovní výživa a suplementace', {'Nutriční terapeut': 3, 'Fyzioterapeut': 2}),
            ('Dětská výživa a potravinové alergie', {'Nutriční terapeut': 4}),
            ('Výživa u pacientů s renálním selháním', {'Nutriční terapeut': 3, 'Lékař': 2})),

        # 361
        _p2('ZDR', 'Jak byste řešili infekci na oddělení?',
            ('Identifikoval bych patogen a nasadil antibiotika', {'Lékař': 4}),
            ('Zavedl bych izolační režim a bariérovou péči', {'Zdravotní sestra': 4}),
            ('Zkontroloval bych interakce antibiotik s ostatními léky', {'Farmaceut': 3}),
            ('Ověřil bych sterilizaci přístrojů a nástrojů', {'Biomedicínský inženýr': 3})),

        # 362
        _p2('ZDR', 'Jakou roli byste chtěli mít při porodu?',
            ('Vést porod a řešit případné komplikace', {'Lékař': 4}),
            ('Asistovat u porodu a pečovat o novorozence', {'Zdravotní sestra': 4}),
            ('Připravit záchranné vybavení pro neonatální resuscitaci', {'Záchranář': 3}),
            ('Poradit rodičce s výživou v šestinedělí', {'Nutriční terapeut': 3})),

        # 363
        _p2('ZDR', 'Co vás přitahuje na ergonomii?',
            ('Ergonomické úpravy pracoviště pro prevenci bolesti', {'Fyzioterapeut': 4}),
            ('Návrh ergonomických zdravotnických pomůcek', {'Biomedicínský inženýr': 3}),
            ('Edukace pacientů o správném držení těla', {'Fyzioterapeut': 3}),
            ('Správné nastavení zubařského křesla a nástrojů', {'Zubař': 2, 'Fyzioterapeut': 2})),

        # 364
        _p2('ZDR', 'Jak byste komunikovali špatnou zprávu pacientovi?',
            ('Osobně, citlivě a s nabídkou dalšího postupu', {'Lékař': 4}),
            ('S empatií a nabídkou psychické podpory', {'Zdravotní sestra': 3}),
            ('Vysvětlil bych možnosti léčby včetně experimentální', {'Farmaceut': 2, 'Lékař': 2}),
            ('Nabídl bych nutriční podporu pro zlepšení kvality života', {'Nutriční terapeut': 3})),

        # 365
        _p2('ZDR', 'Který aspekt fyzioterapie vás nejvíce oslovuje?',
            ('Manuální terapie a mobilizace kloubů', {'Fyzioterapeut': 4}),
            ('Neurologická rehabilitace po mozkových příhodách', {'Fyzioterapeut': 4}),
            ('Respirační fyzioterapie u plicních pacientů', {'Fyzioterapeut': 3, 'Zdravotní sestra': 2}),
            ('Vodoléčba a balneoterapie', {'Fyzioterapeut': 3})),

        # 366
        _p2('ZDR', 'Jak byste řešili alergickou reakci pacienta?',
            ('Okamžitě podám adrenalin a zajistím dýchací cesty', {'Záchranář': 4, 'Lékař': 2}),
            ('Provedu monitoraci a připravím infuzní terapii', {'Zdravotní sestra': 3}),
            ('Zkontroluju, zda alergii nezpůsobil některý z léků', {'Farmaceut': 4}),
            ('Upravím dietu a vyloučím alergeny z jídelníčku', {'Nutriční terapeut': 3})),

        # 367
        _p2('ZDR', 'Jaká je vaše představa o kontinuálním vzdělávání?',
            ('Účast na lékařských konferencích a čtení studií', {'Lékař': 3}),
            ('Certifikační kurzy pro zdravotnickou techniku', {'Biomedicínský inženýr': 4}),
            ('Workshopy o nových rehabilitačních metodách', {'Fyzioterapeut': 3}),
            ('Kurzy přednemocniční neodkladné péče', {'Záchranář': 3})),

        # 368
        _p2('ZDR', 'Co byste zkoumali ve výzkumu?',
            ('Účinnost nových onkologických léků', {'Farmaceut': 3, 'Lékař': 3}),
            ('Biomechaniku lidského pohybu', {'Fyzioterapeut': 3, 'Biomedicínský inženýr': 2}),
            ('Vliv mikrobimu na zdraví a imunitu', {'Nutriční terapeut': 3, 'Lékař': 2}),
            ('Nové materiály pro dentální implantáty', {'Zubař': 3, 'Biomedicínský inženýr': 2})),

        # 369
        _p2('ZDR', 'Jak byste pomáhali v rozvojové zemi?',
            ('Operoval bych v polní nemocnici', {'Lékař': 4}),
            ('Poskytoval bych první pomoc v uprchlických táborech', {'Záchranář': 4}),
            ('Distribuoval bych léky a edukoval o jejich užívání', {'Farmaceut': 3}),
            ('Řešil bych podvýživu dětí nutričními intervencemi', {'Nutriční terapeut': 4})),

        # 370
        _p2('ZDR', 'Jak se stavíte k nočním směnám?',
            ('Zvládám je – na urgentním příjmu se pořád něco děje', {'Záchranář': 3, 'Lékař': 2}),
            ('Noční služby na oddělení mě neodradí', {'Zdravotní sestra': 4}),
            ('Preferuji denní práci v laboratoři nebo dílně', {'Biomedicínský inženýr': 3}),
            ('Raději pravidelný režim v ambulanci', {'Fyzioterapeut': 2, 'Nutriční terapeut': 2})),

        # 371
        _p2('ZDR', 'Co byste dělali při epidemii chřipky?',
            ('Koordinoval bych očkovací kampaň a léčbu', {'Lékař': 4}),
            ('Vydával bych antivirotika a radil s dávkováním', {'Farmaceut': 4}),
            ('Monitoroval bych pacienty na infekčním oddělení', {'Zdravotní sestra': 3}),
            ('Zajistil bych funkčnost ventilátorů na JIP', {'Biomedicínský inženýr': 3})),

        # 372
        _p2('ZDR', 'Jak byste přistoupili k pacientovi po amputaci?',
            ('Navrhnu rehabilitační plán a nácvik chůze s protézou', {'Fyzioterapeut': 4}),
            ('Řeším pooperační péči a hojení pahýlu', {'Lékař': 3}),
            ('Převazuji ránu a sleduji známky infekce', {'Zdravotní sestra': 3}),
            ('Nastavím výživu pro optimální hojení tkání', {'Nutriční terapeut': 3})),

        # 373
        _p2('ZDR', 'Který typ ordinace je vám sympatický?',
            ('Všeobecné praktické lékařství', {'Lékař': 4}),
            ('Stomatologická ordinace s moderním vybavením', {'Zubař': 4}),
            ('Fyzioterapeutická ambulance', {'Fyzioterapeut': 4}),
            ('Nutriční poradna', {'Nutriční terapeut': 4})),

        # 374
        _p2('ZDR', 'Jak přistupujete k lékařské technice?',
            ('Zajímá mě, jak funguje uvnitř – elektronika, software', {'Biomedicínský inženýr': 4}),
            ('Chci ji umět správně obsluhovat pro péči o pacienta', {'Zdravotní sestra': 3}),
            ('Používám ji pro diagnostiku a rozhodování', {'Lékař': 3}),
            ('Využívám ji pro přesné měření v záchranné službě', {'Záchranář': 3})),

        # 375
        _p2('ZDR', 'Co byste dělali na oddělení rehabilitace?',
            ('Vedl bych skupinová cvičení pro pacienty', {'Fyzioterapeut': 4}),
            ('Aplikoval bych fyzikální terapii – ultrazvuk, laser', {'Fyzioterapeut': 3}),
            ('Pečoval bych o pacienty a pomáhal s hygienou', {'Zdravotní sestra': 3}),
            ('Připravil bych dietu pro pacienty s omezenou mobilitou', {'Nutriční terapeut': 3})),

        # 376
        _p2('ZDR', 'Jak se díváte na alternativní medicínu?',
            ('Zajímá mě fytoterapie s důkazovou základnou', {'Farmaceut': 3}),
            ('Využívám prvky jako akupresuru v rehabilitaci', {'Fyzioterapeut': 3}),
            ('Preferuji pouze medicínu založenou na důkazech', {'Lékař': 3}),
            ('Hodnotím její dopad na výživový stav pacientů', {'Nutriční terapeut': 2, 'Lékař': 2})),

        # 377
        _p2('ZDR', 'Jaký typ záchranné akce preferujete?',
            ('Leteckou záchrannou službu ve vrtulníku', {'Záchranář': 4}),
            ('Výjezdy rychlé zdravotnické pomoci v sanitce', {'Záchranář': 4}),
            ('Urgentní příjem v nemocnici', {'Lékař': 3, 'Zdravotní sestra': 2}),
            ('Technickou pomoc při dekontaminaci', {'Záchranář': 2, 'Biomedicínský inženýr': 2})),

        # 378
        _p2('ZDR', 'Jak byste řešili poruchy příjmu potravy?',
            ('Komplexním nutričním plánem a psychoedukací', {'Nutriční terapeut': 4}),
            ('Diagnostikou a psychiatrickou léčbou', {'Lékař': 3}),
            ('Monitorováním zdravotního stavu a hmotnosti', {'Zdravotní sestra': 3}),
            ('Kontrolou medikace a doplňků stravy', {'Farmaceut': 3})),

        # 379
        _p2('ZDR', 'Co je pro vás důležité na pracovním prostředí?',
            ('Sterilní a přesné prostředí operačního sálu', {'Lékař': 3, 'Zubař': 2}),
            ('Dynamické prostředí záchranné služby', {'Záchranář': 4}),
            ('Klidná laboratoř s moderními přístroji', {'Biomedicínský inženýr': 3, 'Farmaceut': 2}),
            ('Kontakt s pacientem v ambulanci', {'Fyzioterapeut': 3, 'Nutriční terapeut': 2})),

        # 380
        _p2('ZDR', 'Jak přistupujete k parodontitidě u pacienta?',
            ('Provedu hloubkové čištění a ošetření dásní', {'Zubař': 4}),
            ('Předepíšu antibiotika a antiseptický ústní roztok', {'Zubař': 3, 'Farmaceut': 2}),
            ('Doporučím vitamíny a minerály podporující hojení', {'Nutriční terapeut': 3}),
            ('Edukuji o správné technice čištění zubů', {'Zubař': 3, 'Zdravotní sestra': 2})),

        # 381
        _p2('ZDR', 'Jaký typ pacienta je pro vás největší výzvou?',
            ('Polytraumatizovaný pacient po nehodě', {'Záchranář': 3, 'Lékař': 3}),
            ('Nespolupracující pacient v zubním křesle', {'Zubař': 4}),
            ('Pacient s komplexní polypragmazií', {'Farmaceut': 4}),
            ('Pacient s těžkou malnutricí', {'Nutriční terapeut': 4})),

        # 382
        _p2('ZDR', 'Co vás baví na zdravotnickém IT?',
            ('Vývoj a správa nemocničního informačního systému', {'Biomedicínský inženýr': 4}),
            ('Digitální zobrazování a PACS systémy', {'Biomedicínský inženýr': 3, 'Lékař': 2}),
            ('Elektronická preskripce a lékový záznam', {'Farmaceut': 2, 'Biomedicínský inženýr': 2}),
            ('Wearables pro vzdálený monitoring pacientů', {'Biomedicínský inženýr': 4})),

        # 383
        _p2('ZDR', 'Jak byste vedli skupinu studentů na praxi?',
            ('Ukázal bych postup klinického vyšetření', {'Lékař': 4}),
            ('Demonstroval bych odběr krve a ošetřovatelské postupy', {'Zdravotní sestra': 4}),
            ('Učil bych techniky manuální terapie', {'Fyzioterapeut': 4}),
            ('Předvedl bych přípravu magistraliter v lékárně', {'Farmaceut': 4})),

        # 384
        _p2('ZDR', 'Jak hodnotíte roli výživy v léčbě?',
            ('Výživa je základ – ovlivňuje průběh i prognózu', {'Nutriční terapeut': 4}),
            ('Je důležitá, ale klíčová je správná farmakoterapie', {'Farmaceut': 3}),
            ('Kombinuji nutriční doporučení s léčebným plánem', {'Lékař': 3}),
            ('Pomáhá při rehabilitaci – svalovou regeneraci', {'Fyzioterapeut': 2, 'Nutriční terapeut': 2})),

        # 385
        _p2('ZDR', 'Jakou roli hrajete v preventivním programu?',
            ('Provádím preventivní prohlídky a screeningy', {'Lékař': 4}),
            ('Kontroluji správnost očkovacích schémat', {'Farmaceut': 3}),
            ('Učím správnou hygienu dutiny ústní na školách', {'Zubař': 4}),
            ('Navrhuji stravovací programy pro firmy', {'Nutriční terapeut': 3})),

        # 386
        _p2('ZDR', 'Co vás přitahuje na intenzivní péči?',
            ('Komplexní léčba kriticky nemocných pacientů', {'Lékař': 4}),
            ('Kontinuální monitoring a péče u lůžka', {'Zdravotní sestra': 4}),
            ('Správa a obsluha přístrojů na JIP', {'Biomedicínský inženýr': 3}),
            ('Parenterální a enterální výživa u kritických pacientů', {'Nutriční terapeut': 3})),

        # 387
        _p2('ZDR', 'Jaký je váš přístup ke kvalitě léčiv?',
            ('Kontroluji šarže, exspirace a podmínky skladování', {'Farmaceut': 4}),
            ('Hlásím nežádoucí účinky léků – farmakovigilance', {'Farmaceut': 4}),
            ('Sleduji, zda léky nezhoršují nutriční stav', {'Nutriční terapeut': 2, 'Farmaceut': 2}),
            ('Zajímám se o klinické studie a evidence-based přístup', {'Lékař': 3})),

        # 388
        _p2('ZDR', 'Jak byste řešili bolest u dětí?',
            ('Použil bych dětské škály bolesti a nastavil analgetika', {'Lékař': 4}),
            ('Zklidnil bych dítě hrou a podal lék v sirupu', {'Zdravotní sestra': 3, 'Farmaceut': 2}),
            ('Aplikoval bych lokální anestezii před zákrokem', {'Zubař': 3}),
            ('Odvedl bych pozornost a použil nefarmakologické metody', {'Zdravotní sestra': 3})),

        # 389
        _p2('ZDR', 'Která oblast biomedicínského inženýrství vás láká?',
            ('Vývoj protetických a ortotických pomůcek', {'Biomedicínský inženýr': 4}),
            ('Zobrazovací techniky – ultrazvuk, rentgen, CT', {'Biomedicínský inženýr': 4}),
            ('Návrh nemocničních informačních systémů', {'Biomedicínský inženýr': 4}),
            ('Bioinformatika a analýza genomických dat', {'Biomedicínský inženýr': 3, 'Farmaceut': 2})),

        # 390
        _p2('ZDR', 'Jak vnímáte spolupráci s jinými profesemi?',
            ('Konzilium s kolegy různých specializací je klíčové', {'Lékař': 3}),
            ('Dobrá komunikace se sestrami zlepšuje péči', {'Zdravotní sestra': 3}),
            ('Spolupráce s inženýry posouvá diagnostiku kupředu', {'Biomedicínský inženýr': 3}),
            ('Koordinace s nutričním terapeutem urychluje léčbu', {'Nutriční terapeut': 3})),

        # 391
        _p2('ZDR', 'Jak byste prezentovali svou práci na konferenci?',
            ('Kazuistiku zajímavého chirurgického případu', {'Lékař': 4}),
            ('Výsledky studie o novém lékovém přípravku', {'Farmaceut': 4}),
            ('Inovativní rehabilitační metodu s výsledky', {'Fyzioterapeut': 3}),
            ('Technické řešení nového diagnostického přístroje', {'Biomedicínský inženýr': 4})),

        # 392
        _p2('ZDR', 'Co děláte, když má pacient strach ze zákroku?',
            ('Vysvětlím postup, podám anxiolytikum při potřebě', {'Lékař': 3}),
            ('Klidně komunikuji a provádím zákrok šetrně', {'Zubař': 4}),
            ('Držím pacienta za ruku a uklidňuji ho', {'Zdravotní sestra': 4}),
            ('Doporučím relaxační techniky a dechová cvičení', {'Fyzioterapeut': 2, 'Zdravotní sestra': 2})),

        # 393
        _p2('ZDR', 'Jak řešíte etické dilema ve zdravotnictví?',
            ('Konzultuji s etickou komisí a řídím se guidelines', {'Lékař': 4}),
            ('Respektuji autonomii pacienta a informovaný souhlas', {'Zdravotní sestra': 3}),
            ('Zvažuji poměr přínosů a rizik farmakoterapie', {'Farmaceut': 3}),
            ('Zohledňuji přání pacienta i při výživové podpoře', {'Nutriční terapeut': 2, 'Lékař': 2})),

        # 394
        _p2('ZDR', 'Jak přistupujete k hygieniakým standardům?',
            ('Sterilizuji nástroje po každém pacientovi', {'Zubař': 4}),
            ('Dodržuji bariérovou ošetřovatelskou péči', {'Zdravotní sestra': 4}),
            ('Provádím validaci sterilizátorů a autoklávů', {'Biomedicínský inženýr': 4}),
            ('Kontroluji čistotu prostor při přípravě léčiv', {'Farmaceut': 3})),

        # 395
        _p2('ZDR', 'Co byste dělali v domácí péči?',
            ('Návštěvy pacientů a kontrola zdravotního stavu', {'Zdravotní sestra': 4}),
            ('Rehabilitační cvičení v domácím prostředí', {'Fyzioterapeut': 4}),
            ('Kontrolu správného užívání léků a compliance', {'Farmaceut': 3}),
            ('Sestavení domácího dietního plánu pro seniory', {'Nutriční terapeut': 3})),

        # 396
        _p2('ZDR', 'Jak vnímáte ortodontickou léčbu?',
            ('Jako fascinující biomechaniku pohybu zubů', {'Zubař': 4}),
            ('Jako příležitost pro 3D tisk a digitální plánování', {'Biomedicínský inženýr': 3, 'Zubař': 2}),
            ('Jako dlouhodobý proces vyžadující trpělivost s pacienty', {'Zubař': 3}),
            ('Jako zásah ovlivňující žvýkání a příjem potravy', {'Nutriční terapeut': 2, 'Zubař': 2})),

        # 397
        _p2('ZDR', 'Jak byste přispěli ke zvýšení bezpečnosti pacientů?',
            ('Zavedením systému hlášení nežádoucích událostí', {'Lékař': 3, 'Zdravotní sestra': 2}),
            ('Kontrolou lékových interakcí při preskripci', {'Farmaceut': 4}),
            ('Pravidelnou údržbou a kontrolou přístrojů', {'Biomedicínský inženýr': 4}),
            ('Správnou identifikací pacienta a verifikací výkonů', {'Zdravotní sestra': 3})),

        # 398
        _p2('ZDR', 'Jak si představujete budoucnost zdravotnictví?',
            ('Personalizovaná medicína na základě genomiky', {'Lékař': 3, 'Farmaceut': 2}),
            ('Robotické operace a AI diagnostika', {'Biomedicínský inženýr': 4}),
            ('Preventivní přístup založený na výživě a životním stylu', {'Nutriční terapeut': 3}),
            ('Domácí rehabilitace s virtuální realitou', {'Fyzioterapeut': 3, 'Biomedicínský inženýr': 2})),

        # 399
        _p2('ZDR', 'Jak reagujete na zástavu srdce u pacienta?',
            ('Zahajuji KPR a používám AED', {'Záchranář': 4}),
            ('Podávám adrenalin a řídím resuscitační tým', {'Lékař': 4}),
            ('Připravuji léky a asistím při resuscitaci', {'Zdravotní sestra': 3}),
            ('Zajišťuji funkčnost defibrilátoru a monitoru', {'Biomedicínský inženýr': 2, 'Záchranář': 2})),

        # 400
        _p2('ZDR', 'Co je pro vás nejdůležitější hodnota ve zdravotnictví?',
            ('Zachraňovat životy a zmírňovat utrpení', {'Lékař': 3, 'Záchranář': 3}),
            ('Bezpečná a účinná farmakoterapie pro každého', {'Farmaceut': 3}),
            ('Holistický přístup – tělo, mysl i výživa', {'Nutriční terapeut': 3, 'Fyzioterapeut': 2}),
            ('Inovace a technologický pokrok v péči', {'Biomedicínský inženýr': 4})),

        # ══════════════ OBC: Obchod a služby (401–480) ══════════════

        # --- Pracovní činnosti ---
        # 401
        _p2('OBC', 'Jakou obchodní činnost byste dělali nejraději?',
            ('Jednání se zákazníky a prezentace produktů', {'Obchodní zástupce': 4}),
            ('Plánování marketingových kampaní na sociálních sítích', {'Marketingový specialista': 4}),
            ('Vyjednávání cenových podmínek s dodavateli', {'Nákupčí': 4}),
            ('Přípravu originálních koktejlů za barem', {'Barman': 3})),

        # 402
        _p2('OBC', 'Která pracovní náplň vás láká nejvíce?',
            ('Provázení turistů po historických památkách', {'Průvodce': 4}),
            ('Přijímání hostů a správa rezervací na recepci', {'Recepční': 4}),
            ('Organizace prohlídek nemovitostí a uzavírání smluv', {'Realitní makléř': 4}),
            ('Tvorba jídelního menu a příprava pokrmů', {'Kuchař': 4})),

        # 403
        _p2('OBC', 'Co by vás bavilo při práci v obchodě?',
            ('Budování dlouhodobých vztahů s B2B klienty', {'Obchodní zástupce': 3, 'Nákupčí': 2}),
            ('Analýza trhu a identifikace nových příležitostí', {'Marketingový specialista': 3}),
            ('Správa CRM systému a sledování obchodních případů', {'Obchodní zástupce': 3}),
            ('Organizace slevových akcí a propagace produktů', {'Marketingový specialista': 3, 'Obchodní zástupce': 2})),

        # 404
        _p2('OBC', 'Jak byste se nejraději podíleli na provozu restaurace?',
            ('Přípravou pokrmů podle receptur i vlastní invence', {'Kuchař': 4}),
            ('Mixováním nápojů a obsluhou hostů u baru', {'Barman': 4}),
            ('Vyjednáváním výhodných cen surovin u dodavatelů', {'Nákupčí': 3}),
            ('Propagací restaurace na internetu a sociálních sítích', {'Marketingový specialista': 3})),

        # 405
        _p2('OBC', 'Která činnost v cestovním ruchu vás přitahuje?',
            ('Výklad o historii a kultuře navštívených míst', {'Průvodce': 4}),
            ('Organizace skupinových zájezdů a výletů', {'Průvodce': 3, 'Recepční': 2}),
            ('Komunikace s hosty v několika jazycích', {'Recepční': 3, 'Průvodce': 2}),
            ('Prodej zájezdů a ubytování klientům', {'Obchodní zástupce': 3, 'Realitní makléř': 2})),

        # 406
        _p2('OBC', 'Co byste dělali nejraději v oblasti nemovitostí?',
            ('Provádění prohlídek bytů a domů s klienty', {'Realitní makléř': 4}),
            ('Zpracování cenových odhadů nemovitostí', {'Realitní makléř': 3}),
            ('Přípravu kupních a nájemních smluv', {'Realitní makléř': 3, 'Nákupčí': 2}),
            ('Fotografie a prezentace nemovitostí online', {'Marketingový specialista': 3, 'Realitní makléř': 2})),

        # 407
        _p2('OBC', 'Na kterou denní aktivitu v hotelu se těšíte?',
            ('Přivítání hostů a check-in na recepci', {'Recepční': 4}),
            ('Koordinaci úklidu pokojů a řešení požadavků', {'Recepční': 3}),
            ('Přípravu snídaňového rautu v kuchyni', {'Kuchař': 3}),
            ('Večerní barový servis a míchání drinků', {'Barman': 3})),

        # 408
        _p2('OBC', 'Která laboratorní nebo analytická aktivita vás zaujme?',
            ('Analýza prodejních dat a trendů v CRM', {'Obchodní zástupce': 3, 'Marketingový specialista': 2}),
            ('SEO analýza webových stránek a klíčových slov', {'Marketingový specialista': 4}),
            ('Srovnání cenových nabídek od více dodavatelů', {'Nákupčí': 4}),
            ('Dodržování HACCP předpisů a kontrola surovin', {'Kuchař': 3})),

        # 409
        _p2('OBC', 'Co vás baví na práci s lidmi?',
            ('Přesvědčování zákazníků o výhodách produktu', {'Obchodní zástupce': 4}),
            ('Vyprávění příběhů o historii a zajímavostech místa', {'Průvodce': 4}),
            ('Řešení stížností a požadavků hotelových hostů', {'Recepční': 3}),
            ('Konverzace s hosty u baru a vytváření atmosféry', {'Barman': 3})),

        # 410
        _p2('OBC', 'Jakým způsobem byste nejraději podporovali prodej?',
            ('Osobními schůzkami a prezentacemi u klientů', {'Obchodní zástupce': 4}),
            ('Tvorbou reklamních kampaní a PPC reklam', {'Marketingový specialista': 4}),
            ('Hledáním levnějších a kvalitnějších dodavatelů', {'Nákupčí': 3}),
            ('Organizací degustačních akcí a ochutnávek', {'Kuchař': 2, 'Barman': 3})),

        # --- Pracovní prostředí ---
        # 411
        _p2('OBC', 'V jakém prostředí byste nejraději pracovali?',
            ('V kanceláři s přístupem k obchodním datům a CRM', {'Obchodní zástupce': 3, 'Marketingový specialista': 2}),
            ('V profesionální kuchyni plné vůní a ruchu', {'Kuchař': 4}),
            ('Za barovým pultem s řadou lahví a nástrojů', {'Barman': 4}),
            ('Na recepci luxusního hotelu', {'Recepční': 3})),

        # 412
        _p2('OBC', 'Které pracovní místo vám vyhovuje?',
            ('Kancelář s telefonem a počítačem pro obchodní jednání', {'Obchodní zástupce': 3, 'Nákupčí': 2}),
            ('Venkovní prostředí – historická centra a příroda', {'Průvodce': 4}),
            ('Realitní kancelář s přístupem k databázi nemovitostí', {'Realitní makléř': 3}),
            ('Marketingová agentura s kreativním týmem', {'Marketingový specialista': 3})),

        # 413
        _p2('OBC', 'Jaké tempo práce preferujete?',
            ('Rychlé – pod tlakem objednávek v kuchyni', {'Kuchař': 4}),
            ('Výzvové – rychlé míchání drinků ve špičce', {'Barman': 4}),
            ('Klidné – trpělivé vyjednávání a jednání', {'Nákupčí': 3, 'Obchodní zástupce': 2}),
            ('Flexibilní – dle potřeb klientů a prohlídek', {'Realitní makléř': 3})),

        # 414
        _p2('OBC', 'Jak se cítíte při práci o víkendech a svátcích?',
            ('Nevadí mi to – gastronomie to vyžaduje', {'Kuchař': 3, 'Barman': 3}),
            ('Rád/a – víkendové prohlídky jsou nejčastější', {'Realitní makléř': 3}),
            ('Ano – turisté cestují nejvíce o víkendech', {'Průvodce': 3}),
            ('Preferuji klasický pracovní týden', {'Nákupčí': 3, 'Marketingový specialista': 2})),

        # 415
        _p2('OBC', 'Preferujete práci samostatnou nebo týmovou?',
            ('Samostatně – obchodní teritorium řídím sám/sama', {'Obchodní zástupce': 3}),
            ('V týmu – v kuchyni musí vše klapnout koordinovaně', {'Kuchař': 3}),
            ('Kombinaci – zpracuji analýzu a prezentuji týmu', {'Marketingový specialista': 3}),
            ('S klientem – provázím individuálně i skupiny', {'Průvodce': 3, 'Realitní makléř': 2})),

        # 416
        _p2('OBC', 'Jaký dress code vám vyhovuje?',
            ('Formální oblek pro obchodní jednání', {'Obchodní zástupce': 3, 'Realitní makléř': 2}),
            ('Uniforma recepčního s jmenovkou', {'Recepční': 3}),
            ('Kuchařský rondon a čepice', {'Kuchař': 3}),
            ('Casual s firemním trič­kem a zástěrou', {'Barman': 3})),

        # 417
        _p2('OBC', 'Jak daleko jste ochotni za prací cestovat?',
            ('Cestování po regionu za klienty je pro mě běžné', {'Obchodní zástupce': 4}),
            ('Cestuji s turisty po celé zemi i zahraničí', {'Průvodce': 4}),
            ('Pracuji převážně na jednom místě – v kuchyni', {'Kuchař': 3}),
            ('Jezdím na prohlídky nemovitostí po městě', {'Realitní makléř': 3})),

        # 418
        _p2('OBC', 'Jakou atmosféru při práci preferujete?',
            ('Energickou s hudbou a společenským ruchem', {'Barman': 4}),
            ('Klidnou a profesionální na recepci', {'Recepční': 3}),
            ('Kreativní v marketingovém týmu', {'Marketingový specialista': 3}),
            ('Napínavou při vyjednávání obchodních podmínek', {'Nákupčí': 3, 'Obchodní zástupce': 2})),

        # 419
        _p2('OBC', 'Kde si představujete svůj pracovní stůl?',
            ('V otevřeném obchodním oddělení firmy', {'Obchodní zástupce': 3}),
            ('Na recepci s výhledem na lobby', {'Recepční': 3}),
            ('Nemám stůl – pracuji v kuchyni u linky', {'Kuchař': 3}),
            ('V realitní kanceláři s mapou města', {'Realitní makléř': 3})),

        # 420
        _p2('OBC', 'Jaký typ kontaktu s klienty vám vyhovuje?',
            ('Osobní schůzky a prezentace', {'Obchodní zástupce': 3, 'Realitní makléř': 2}),
            ('Telefonická a e-mailová komunikace', {'Recepční': 3, 'Nákupčí': 2}),
            ('Online marketing a sociální sítě', {'Marketingový specialista': 4}),
            ('Přímý kontakt u baru nebo v restauraci', {'Barman': 3, 'Kuchař': 2})),

        # --- Nástroje a technologie ---
        # 421
        _p2('OBC', 'Který software nebo nástroj byste používali nejraději?',
            ('CRM systém pro správu kontaktů a obchodních příležitostí', {'Obchodní zástupce': 4}),
            ('Google Analytics a nástroje pro SEO analýzu', {'Marketingový specialista': 4}),
            ('ERP systém pro řízení nákupu a skladových zásob', {'Nákupčí': 4}),
            ('Pokladní systém a rezervační software', {'Recepční': 3})),

        # 422
        _p2('OBC', 'S jakým vybavením byste pracovali nejraději?',
            ('Sada profesionálních kuchyňských nožů', {'Kuchař': 4}),
            ('Shakerový set a barové náčiní', {'Barman': 4}),
            ('Projektor a notebook pro obchodní prezentace', {'Obchodní zástupce': 3}),
            ('Měřicí přístroje pro odhad nemovitostí', {'Realitní makléř': 3})),

        # 423
        _p2('OBC', 'Jakou digitální platformu používáte nejčastěji?',
            ('LinkedIn pro obchodní networking', {'Obchodní zástupce': 3, 'Marketingový specialista': 2}),
            ('Instagram a Facebook pro propagaci', {'Marketingový specialista': 4}),
            ('Booking.com a hotelový rezervační systém', {'Recepční': 3}),
            ('Sreality.cz a realitní portály', {'Realitní makléř': 3})),

        # 424
        _p2('OBC', 'Který nástroj je pro vaši práci nepostradatelný?',
            ('Telefon – jednání se zákazníky na denním pořádku', {'Obchodní zástupce': 3, 'Recepční': 2}),
            ('Konvektomat a moderní kuchyňská technika', {'Kuchař': 4}),
            ('Mikrofon a průvodcovský systém pro skupiny', {'Průvodce': 4}),
            ('E-aukční platforma pro výběrová řízení', {'Nákupčí': 4})),

        # 425
        _p2('OBC', 'Jakou technologii byste chtěli ovládnout?',
            ('Marketingovou automatizaci a e-mail marketing', {'Marketingový specialista': 4}),
            ('Molekulární gastronomii a sous-vide techniku', {'Kuchař': 4}),
            ('Flair bartending a pokročilé techniky míchání', {'Barman': 4}),
            ('Virtuální prohlídky nemovitostí v 3D', {'Realitní makléř': 3})),

        # 426
        _p2('OBC', 'Jaký typ prezentace vám je nejbližší?',
            ('PowerPoint s grafy prodejních výsledků', {'Obchodní zástupce': 3}),
            ('Vizuální mood board pro marketingovou kampaň', {'Marketingový specialista': 3}),
            ('Tabulka srovnání dodavatelských nabídek', {'Nákupčí': 3}),
            ('Video prohlídka nemovitosti s komentářem', {'Realitní makléř': 3})),

        # 427
        _p2('OBC', 'Kterou aplikaci byste si stáhli jako první?',
            ('Obchodní skener vizitek a CRM mobilní appku', {'Obchodní zástupce': 3}),
            ('Canva pro tvorbu vizuálního obsahu', {'Marketingový specialista': 3}),
            ('Aplikaci s recepty a kalkulací food costu', {'Kuchař': 3}),
            ('Překladač a offline mapy pro průvodce', {'Průvodce': 3})),

        # 428
        _p2('OBC', 'Jaký systém evidence byste používali?',
            ('Evidenci obchodních příležitostí v pipeline', {'Obchodní zástupce': 3, 'Marketingový specialista': 2}),
            ('Skladovou evidenci surovin a inventuru', {'Kuchař': 3, 'Nákupčí': 2}),
            ('Hotelový PMS pro správu pokojů a hostů', {'Recepční': 4}),
            ('Databázi nemovitostí s fotodokumentací', {'Realitní makléř': 3})),

        # 429
        _p2('OBC', 'S jakým typem dat nejraději pracujete?',
            ('Prodejní čísla a konverzní poměry', {'Obchodní zástupce': 3}),
            ('Metriky kampaní – CTR, ROI, engagement', {'Marketingový specialista': 4}),
            ('Ceny, marže a dodací podmínky', {'Nákupčí': 3}),
            ('Cenové mapy a statistiky realitního trhu', {'Realitní makléř': 3})),

        # 430
        _p2('OBC', 'Jakou techniku komunikace ovládáte nejlépe?',
            ('Obchodní vyjednávání a uzavírání obchodu', {'Obchodní zástupce': 4}),
            ('Copywriting a tvorba reklamních textů', {'Marketingový specialista': 4}),
            ('Výklad a storytelling pro turisty', {'Průvodce': 3}),
            ('Telefonická komunikace a řešení stížností', {'Recepční': 3})),

        # --- Odborné znalosti ---
        # 431
        _p2('OBC', 'Která odborná znalost je vám nejbližší?',
            ('Obchodní právo a smluvní podmínky', {'Obchodní zástupce': 3, 'Realitní makléř': 2}),
            ('Principy SEO a digitálního marketingu', {'Marketingový specialista': 4}),
            ('Pravidla veřejných zakázek a tenderu', {'Nákupčí': 4}),
            ('Hygienické normy HACCP v gastronomii', {'Kuchař': 4})),

        # 432
        _p2('OBC', 'O čem byste se rádi dozvěděli více?',
            ('O technikách prodeje a psychologii zákazníka', {'Obchodní zástupce': 3}),
            ('O historii a architektuře českých měst', {'Průvodce': 4}),
            ('O vinařství, destilaci a sommeliérství', {'Barman': 4}),
            ('O oceňování nemovitostí a hypotečním trhu', {'Realitní makléř': 3})),

        # 433
        _p2('OBC', 'Jakou odbornou certifikaci byste chtěli získat?',
            ('Certifikát profesionálního obchodníka', {'Obchodní zástupce': 3}),
            ('Google Ads a Facebook Blueprint certifikace', {'Marketingový specialista': 4}),
            ('Certifikát průvodce cestovního ruchu', {'Průvodce': 4}),
            ('Certifikát barmana IBA', {'Barman': 4})),

        # 434
        _p2('OBC', 'Kterou oblast ekonomiky považujete za nejzajímavější?',
            ('B2B obchod a firemní prodej', {'Obchodní zástupce': 3, 'Nákupčí': 2}),
            ('Digitální ekonomika a e-commerce', {'Marketingový specialista': 3}),
            ('Realitní trh a investice do nemovitostí', {'Realitní makléř': 4}),
            ('Gastronomický průmysl a food business', {'Kuchař': 3, 'Barman': 2})),

        # 435
        _p2('OBC', 'Jaký typ školení byste uvítali?',
            ('Trénink vyjednávacích dovedností', {'Obchodní zástupce': 3, 'Nákupčí': 3}),
            ('Workshop kreativní kuchyně a food stylingu', {'Kuchař': 4}),
            ('Kurz cizích jazyků pro průvodce', {'Průvodce': 3, 'Recepční': 2}),
            ('Seminář o content marketingu a brand buildingu', {'Marketingový specialista': 3})),

        # 436
        _p2('OBC', 'Která znalost je ve vaší profesi klíčová?',
            ('Znalost produktové nabídky a konkurence', {'Obchodní zástupce': 3}),
            ('Přehled o aktuální nabídce nemovitostí v regionu', {'Realitní makléř': 3}),
            ('Znalost receptur a gastronomických trendů', {'Kuchař': 3, 'Barman': 2}),
            ('Znalost hotelových standardů a etikety', {'Recepční': 3})),

        # 437
        _p2('OBC', 'Co byste studovali na vysoké škole?',
            ('Marketing a komunikaci', {'Marketingový specialista': 4}),
            ('Mezinárodní obchod', {'Obchodní zástupce': 3, 'Nákupčí': 2}),
            ('Hotelnictví a turismus', {'Recepční': 3, 'Průvodce': 2}),
            ('Gastronomii a potravinářství', {'Kuchař': 3})),

        # 438
        _p2('OBC', 'Jaký předmět ve škole vás bavil nejvíce?',
            ('Ekonomie a základy podnikání', {'Obchodní zástupce': 3, 'Nákupčí': 2}),
            ('Dějepis a zeměpis', {'Průvodce': 4}),
            ('Chemie – reakce a směsi', {'Barman': 2, 'Kuchař': 2}),
            ('Informatika a grafický design', {'Marketingový specialista': 3})),

        # 439
        _p2('OBC', 'Jaké právní normy byste měli znát?',
            ('Občanský zákoník – kupní smlouvy a záruky', {'Obchodní zástupce': 3, 'Realitní makléř': 2}),
            ('Zákon o veřejných zakázkách', {'Nákupčí': 4}),
            ('Zákon o ochraně spotřebitele a GDPR', {'Marketingový specialista': 3}),
            ('Živnostenský zákon a hygienické předpisy', {'Kuchař': 3, 'Barman': 2})),

        # 440
        _p2('OBC', 'Jaké jazykové znalosti jsou pro vás nejdůležitější?',
            ('Obchodní angličtina pro B2B jednání', {'Obchodní zástupce': 3, 'Nákupčí': 2}),
            ('Několik jazyků pro komunikaci s turisty', {'Průvodce': 4}),
            ('Anglická a německá hotelová terminologie', {'Recepční': 3}),
            ('Anglické názvosloví koktejlů a nápojů', {'Barman': 3})),

        # --- Řešení problémů ---
        # 441
        _p2('OBC', 'Zákazník není spokojen s cenou – jak reagujete?',
            ('Nabídnu mu alternativní balíček s přidanou hodnotou', {'Obchodní zástupce': 4}),
            ('Vysvětlím složení ceny a kvalitu surovin', {'Nákupčí': 3, 'Kuchař': 2}),
            ('Připravím srovnávací analýzu s konkurencí', {'Marketingový specialista': 3}),
            ('Nabídnu slevu z provize pro rychlé uzavření', {'Realitní makléř': 3})),

        # 442
        _p2('OBC', 'Dodavatel nedodal suroviny včas – co uděláte?',
            ('Kontaktuji záložního dodavatele z databáze', {'Nákupčí': 4}),
            ('Upravím jídelní lístek podle dostupných surovin', {'Kuchař': 3}),
            ('Informuji hosty a nabídnu alternativu', {'Recepční': 3}),
            ('Improvizuji s dostupnými ingrediencemi za barem', {'Barman': 3})),

        # 443
        _p2('OBC', 'Turistická skupina se opozdila – jak to řešíte?',
            ('Zkrátím výklad a zaměřím se na nejdůležitější body', {'Průvodce': 4}),
            ('Informuji další stanoviště o změně časového plánu', {'Průvodce': 3, 'Recepční': 2}),
            ('Nabídnu skupině rychlé občerstvení mezitím', {'Barman': 2, 'Kuchař': 2}),
            ('Využiji čekání k propagaci dalších aktivit', {'Marketingový specialista': 2, 'Obchodní zástupce': 2})),

        # 444
        _p2('OBC', 'Klient chce nemovitost mimo váš rozpočet – co navrhnete?',
            ('Ukážu alternativní lokality s lepším poměrem cena/výkon', {'Realitní makléř': 4}),
            ('Doporučím hypotečního poradce pro financování', {'Realitní makléř': 3}),
            ('Navrhnu pronájem místo koupě', {'Realitní makléř': 3, 'Obchodní zástupce': 2}),
            ('Vytvořím prezentaci srovnání nemovitostí', {'Marketingový specialista': 2, 'Realitní makléř': 2})),

        # 445
        _p2('OBC', 'Recenze na internetu kritizuje vaši provozovnu – jak reagujete?',
            ('Odpovím profesionálně a nabídnu nápravu', {'Recepční': 3, 'Marketingový specialista': 2}),
            ('Analyzuji zpětnou vazbu a upravím procesy', {'Marketingový specialista': 3}),
            ('Prověřím kvalitu jídla a zlepším přípravu', {'Kuchař': 3}),
            ('Nabídnu nespokojenému hostovi drink na účet podniku', {'Barman': 3})),

        # 446
        _p2('OBC', 'Obchodní partner požaduje nereálnou slevu – co uděláte?',
            ('Vyjednám kompromis s přidanou hodnotou místo slevy', {'Obchodní zástupce': 4}),
            ('Ověřím reálné tržní ceny a argumentuji daty', {'Nákupčí': 3}),
            ('Navrhnu delší smluvní období výměnou za lepší cenu', {'Obchodní zástupce': 3, 'Nákupčí': 2}),
            ('Připravím cenovou kalkulaci se zdůvodněním nákladů', {'Nákupčí': 3})),

        # 447
        _p2('OBC', 'Host v hotelu si stěžuje na hluk – jak zasáhnete?',
            ('Omluvím se a nabídnu přesun do tišího pokoje', {'Recepční': 4}),
            ('Prověřím zdroj hluku a zajistím nápravu', {'Recepční': 3}),
            ('Nabídnu hostovi doplňkovou službu jako kompenzaci', {'Recepční': 2, 'Barman': 2}),
            ('Zaeviduji stížnost do systému pro budoucí prevenci', {'Recepční': 3, 'Marketingový specialista': 2})),

        # 448
        _p2('OBC', 'Kampaň na sociálních sítích nefunguje – co změníte?',
            ('Analyzuji metriky a upravím cílovou skupinu', {'Marketingový specialista': 4}),
            ('Změním vizuály a texty na základě A/B testu', {'Marketingový specialista': 4}),
            ('Oslovím klienty osobně a zjistím preference', {'Obchodní zástupce': 3}),
            ('Vytvořím video obsah místo statických obrázků', {'Marketingový specialista': 3, 'Barman': 2})),

        # 449
        _p2('OBC', 'Při prohlídce se kuchyně pokazí důležité zařízení – co uděláte?',
            ('Rychle přeorganizuji přípravu na dostupných spotřebičích', {'Kuchař': 4}),
            ('Kontaktuji servisního technika a nákupčího pro náhradu', {'Nákupčí': 3}),
            ('Informuji hosty o možném zpoždění a nabídnu aperitiv', {'Barman': 3}),
            ('Komunikuji situaci směrem k vedení a hostům', {'Recepční': 3})),

        # 450
        _p2('OBC', 'Konkurence nabízí nižší ceny – jak se odlišíte?',
            ('Zdůrazním prémiovou kvalitu a osobní přístup', {'Obchodní zástupce': 3}),
            ('Vytvořím silnější brand a content marketing', {'Marketingový specialista': 4}),
            ('Vyjednám s dodavateli lepší nákupní podmínky', {'Nákupčí': 3}),
            ('Nabídnu unikátní gastronomický zážitek', {'Kuchař': 3, 'Barman': 2})),

        # --- Osobnostní preference ---
        # 451
        _p2('OBC', 'Co vás motivuje k práci?',
            ('Uzavření úspěšného obchodu a provize', {'Obchodní zástupce': 4}),
            ('Kreativita a viditelné výsledky kampaní', {'Marketingový specialista': 3}),
            ('Spokojení hosté a jejich úsměv', {'Recepční': 3, 'Průvodce': 2}),
            ('Dokonale připravený pokrm nebo koktejl', {'Kuchař': 3, 'Barman': 3})),

        # 452
        _p2('OBC', 'Jaká vlastnost vás nejlépe vystihuje?',
            ('Přesvědčivost a komunikativnost', {'Obchodní zástupce': 3}),
            ('Kreativita a analytické myšlení', {'Marketingový specialista': 3}),
            ('Preciznost a vyjednávací schopnosti', {'Nákupčí': 3}),
            ('Pohostinnost a empatie', {'Recepční': 3, 'Průvodce': 2})),

        # 453
        _p2('OBC', 'Jak reagujete na stresové situace?',
            ('Zachovám klid a soustředím se na prioritu', {'Kuchař': 3, 'Recepční': 2}),
            ('Rychle improvizuji a hledám řešení', {'Barman': 3, 'Průvodce': 2}),
            ('Analyzuji situaci a jednám systematicky', {'Nákupčí': 3, 'Marketingový specialista': 2}),
            ('Jednám asertivně a hledám kompromis', {'Obchodní zástupce': 3, 'Realitní makléř': 2})),

        # 454
        _p2('OBC', 'Co je pro vás důležitější – jistota nebo výzva?',
            ('Výzva – každý obchod je jiný a motivující', {'Obchodní zástupce': 3}),
            ('Výzva – každá nemovitost a klient jsou unikátní', {'Realitní makléř': 3}),
            ('Jistota – spolehlivá práce na recepci', {'Recepční': 3}),
            ('Výzva – nové recepty a gastronomické experimenty', {'Kuchař': 3, 'Barman': 2})),

        # 455
        _p2('OBC', 'Jak trávíte volný čas?',
            ('Sleduji marketingové trendy a podcasty', {'Marketingový specialista': 3}),
            ('Vařím pro přátele a experimentuji s recepty', {'Kuchař': 4}),
            ('Cestuji a poznávám nová místa', {'Průvodce': 3}),
            ('Míchám doma koktejly a ochutnávám nové nápoje', {'Barman': 3})),

        # 456
        _p2('OBC', 'Co je pro vás největší profesní úspěch?',
            ('Uzavření velkého kontraktu s klíčovým klientem', {'Obchodní zástupce': 4}),
            ('Úspěšný prodej nemovitosti za vynikající cenu', {'Realitní makléř': 4}),
            ('Virální marketingová kampaň s vysokým ROI', {'Marketingový specialista': 4}),
            ('Dlouhodobá úspora díky vyjednaným cenám', {'Nákupčí': 3})),

        # 457
        _p2('OBC', 'Jaký typ zpětné vazby vás potěší nejvíce?',
            ('Klient doporučí mé služby dalším lidem', {'Obchodní zástupce': 3, 'Realitní makléř': 2}),
            ('Hosté pochválí jídlo a vrátí se znovu', {'Kuchař': 4}),
            ('Turisté dají pětihvězdičkovou recenzi výletu', {'Průvodce': 3}),
            ('Kampaň překoná stanovené KPI', {'Marketingový specialista': 3})),

        # 458
        _p2('OBC', 'Jak přistupujete k novým výzvám?',
            ('S nadšením – rád/a hledám nové klienty', {'Obchodní zástupce': 3}),
            ('Analyticky – nejdříve zmapuji situaci', {'Nákupčí': 3, 'Marketingový specialista': 2}),
            ('Kreativně – vymýšlím nové postupy a recepty', {'Kuchař': 3, 'Barman': 2}),
            ('Diplomaticky – hledám cestu k dohodě', {'Recepční': 3, 'Realitní makléř': 2})),

        # 459
        _p2('OBC', 'Co vás na práci štve nejvíce?',
            ('Nedodržování dohodnutých termínů dodavateli', {'Nákupčí': 3}),
            ('Nerozhodní klienti při uzavírání obchodu', {'Obchodní zástupce': 3, 'Realitní makléř': 2}),
            ('Nedostatek kreativity a rutinní úkoly', {'Marketingový specialista': 3}),
            ('Nepořádní kolegové v kuchyni', {'Kuchař': 3})),

        # 460
        _p2('OBC', 'Jakým způsobem se nejlépe učíte?',
            ('Praxí – jednáním s reálnými zákazníky', {'Obchodní zástupce': 3, 'Realitní makléř': 2}),
            ('Pozorováním zkušeného kuchaře v kuchyni', {'Kuchař': 3}),
            ('Online kurzy a analýzou případových studií', {'Marketingový specialista': 3}),
            ('Cestováním a poznáváním nových míst a kultur', {'Průvodce': 4})),

        # --- Situační otázky ---
        # 461
        _p2('OBC', 'Máte připravit prezentaci nového produktu – jak postupujete?',
            ('Připravím demo a klíčové argumenty pro klienta', {'Obchodní zástupce': 4}),
            ('Vytvořím marketingový plán s cílovkou a kanály', {'Marketingový specialista': 4}),
            ('Provedu průzkum konkurenčních nabídek a cen', {'Nákupčí': 3}),
            ('Připravím degustační menu s novým produktem', {'Kuchař': 3, 'Barman': 2})),

        # 462
        _p2('OBC', 'Organizujete firemní akci – co máte na starosti?',
            ('Zajištění cateringu a menu pro akci', {'Kuchař': 3}),
            ('Přípravu nápojového menu a barový servis', {'Barman': 3}),
            ('Propagaci a pozvánky na sociálních sítích', {'Marketingový specialista': 3}),
            ('Koordinaci programu a přivítání hostů', {'Recepční': 3, 'Průvodce': 2})),

        # 463
        _p2('OBC', 'Klient hledá dům k pronájmu – co uděláte jako první?',
            ('Zjistím požadavky na lokaci, velikost a rozpočet', {'Realitní makléř': 4}),
            ('Vyhledám v databázi vhodné nemovitosti', {'Realitní makléř': 3}),
            ('Nabídnu mu doprovodné služby – pojištění, stěhování', {'Obchodní zástupce': 3}),
            ('Připravím srovnávací tabulku dostupných možností', {'Nákupčí': 2, 'Realitní makléř': 2})),

        # 464
        _p2('OBC', 'Otevíráte nový bar – co řešíte jako první?',
            ('Výběr lokace a jednání s pronajímatelem', {'Realitní makléř': 3, 'Obchodní zástupce': 2}),
            ('Sestavení nápojového lístku a nákup ingrediencí', {'Barman': 4}),
            ('Výběr dodavatelů nápojů za nejlepší ceny', {'Nákupčí': 3}),
            ('Marketingovou strategii a propagaci otevření', {'Marketingový specialista': 3})),

        # 465
        _p2('OBC', 'Turista se ptá na doporučení k jídlu – co poradíte?',
            ('Doporučím tradiční českou restauraci a popíši pokrmy', {'Průvodce': 4}),
            ('Připravím mu specialitu zdejší kuchyně', {'Kuchař': 3}),
            ('Nabídnu mu lokální craft pivo nebo koktejl', {'Barman': 3}),
            ('Zařídím rezervaci v partnerském podniku', {'Recepční': 3})),

        # 466
        _p2('OBC', 'Firma expanduje na nový trh – jaká je vaše role?',
            ('Identifikuji klíčové klienty a zahajuji obchodní jednání', {'Obchodní zástupce': 4}),
            ('Zpracuji analýzu trhu a konkurenční prostředí', {'Marketingový specialista': 3, 'Nákupčí': 2}),
            ('Vyhledám a vyhodnotím lokální dodavatele', {'Nákupčí': 3}),
            ('Zajistím nemovitost pro novou pobočku', {'Realitní makléř': 3})),

        # 467
        _p2('OBC', 'Připravujete menu pro banket – jak postupujete?',
            ('Sestavím sezónní menu s ohledem na alergie hostů', {'Kuchař': 4}),
            ('Navrhnu párování vín a koktejlů k jednotlivým chodům', {'Barman': 3}),
            ('Zajistím nákup surovin za nejvýhodnější ceny', {'Nákupčí': 3}),
            ('Koordinuji průběh banketu a komunikuji s hosty', {'Recepční': 3})),

        # 468
        _p2('OBC', 'Vedete prohlídku zámku pro zahraniční skupinu – co děláte?',
            ('Provádím výklad v angličtině a němčině s příběhy', {'Průvodce': 4}),
            ('Překládám a asistuju průvodci s organizací', {'Recepční': 2, 'Průvodce': 2}),
            ('Propaguju prohlídku na zahraničních portálech', {'Marketingový specialista': 3}),
            ('Nabízím suvenýry a merchandising produkty', {'Obchodní zástupce': 3})),

        # 469
        _p2('OBC', 'Váš e-shop má nízkou konverzi – co uděláte?',
            ('Optimalizuji produktové stránky a UX', {'Marketingový specialista': 4}),
            ('Spustím remarketingovou kampaň', {'Marketingový specialista': 3}),
            ('Zavolám klíčovým zákazníkům a zjistím zpětnou vazbu', {'Obchodní zástupce': 3}),
            ('Upravím cenovou strategii na základě analýzy trhu', {'Nákupčí': 3, 'Obchodní zástupce': 2})),

        # 470
        _p2('OBC', 'Na baru je plno a objednávky se hromadí – jak to zvládnete?',
            ('Zjednodušším nabídku a zvýším efektivitu přípravy', {'Barman': 4}),
            ('Organizuji frontu hostů a komunikuji čekací dobu', {'Recepční': 3}),
            ('Pomohu s jednoduchými objednávkami a úklidem', {'Kuchař': 2, 'Barman': 2}),
            ('Prezentuji čekajícím hostům nabídku dalších služeb', {'Obchodní zástupce': 2, 'Marketingový specialista': 2})),

        # --- Trendy a inovace ---
        # 471
        _p2('OBC', 'Jaký trend ve vašem oboru vás zaujal?',
            ('Account-based marketing a personalizace B2B', {'Obchodní zástupce': 3, 'Marketingový specialista': 2}),
            ('Zero-waste kuchyně a udržitelná gastronomie', {'Kuchař': 4}),
            ('Craft koktejly s lokálními ingrediencemi', {'Barman': 4}),
            ('Virtuální realita při prohlídkách nemovitostí', {'Realitní makléř': 3})),

        # 472
        _p2('OBC', 'Jak by podle vás měla vypadat budoucnost obchodu?',
            ('Plně digitalizovaný prodejní proces s AI asistenty', {'Obchodní zástupce': 3, 'Marketingový specialista': 2}),
            ('Automatizovaný nákup s prediktivní analytikou', {'Nákupčí': 4}),
            ('Personalizovaný zážitkový turismus', {'Průvodce': 3}),
            ('Smart hotely s automatickým check-inem', {'Recepční': 3})),

        # 473
        _p2('OBC', 'Jakou inovaci byste zavedli ve své provozovně?',
            ('Chatbota pro komunikaci se zákazníky 24/7', {'Marketingový specialista': 3, 'Obchodní zástupce': 2}),
            ('Robotického kuchaře pro opakující se úkoly', {'Kuchař': 3}),
            ('Mobilní objednávkový systém u baru', {'Barman': 3}),
            ('Online virtuální prohlídky nemovitostí', {'Realitní makléř': 4})),

        # 474
        _p2('OBC', 'Jak vnímáte vliv sociálních sítí na vaši práci?',
            ('Jsou klíčové pro budování osobní značky prodejce', {'Obchodní zástupce': 3}),
            ('Jsou hlavním kanálem pro oslovení zákazníků', {'Marketingový specialista': 4}),
            ('Instagram je skvělý pro prezentaci jídel', {'Kuchař': 3}),
            ('Recenze na sociálních sítích ovlivňují návštěvnost', {'Recepční': 2, 'Průvodce': 2})),

        # 475
        _p2('OBC', 'Jaký udržitelný přístup je vám nejbližší?',
            ('Lokální sourcing a podpora regionálních dodavatelů', {'Nákupčí': 3, 'Kuchař': 2}),
            ('Ekologický turismus s respektem k přírodě', {'Průvodce': 4}),
            ('Energeticky úsporné nemovitosti a zelené budovy', {'Realitní makléř': 3}),
            ('Redukce plýtvání potravinami v kuchyni', {'Kuchař': 3})),

        # 476
        _p2('OBC', 'Jaká technologická novinka vás fascinuje?',
            ('AI generování marketingového obsahu', {'Marketingový specialista': 4}),
            ('3D tisk jídla a automatizace v gastronomii', {'Kuchař': 3}),
            ('Blockchain pro transparentní dodavatelský řetězec', {'Nákupčí': 3}),
            ('Drony pro focení nemovitostí z ptačí perspektivy', {'Realitní makléř': 3})),

        # 477
        _p2('OBC', 'Jak se připravujete na změny v oboru?',
            ('Sleduji obchodní a prodejní webináře', {'Obchodní zástupce': 3}),
            ('Navštěvuji gastronomické veletrhy a festivaly', {'Kuchař': 3, 'Barman': 2}),
            ('Čtu marketingové blogy a case studies', {'Marketingový specialista': 3}),
            ('Absolvuji kurzy realitního práva a oceňování', {'Realitní makléř': 3})),

        # 478
        _p2('OBC', 'Jak byste zvýšili tržby provozovny?',
            ('Zavedením věrnostního programu pro klienty', {'Obchodní zástupce': 3, 'Marketingový specialista': 2}),
            ('Novým konceptem tematických gastronomických večerů', {'Kuchař': 3, 'Barman': 2}),
            ('Cílenou kampaní na lokální zákazníky', {'Marketingový specialista': 3}),
            ('Spoluprací s turistickými agenturami', {'Průvodce': 3, 'Recepční': 2})),

        # 479
        _p2('OBC', 'Co považujete za budoucnost zákaznického servisu?',
            ('Omnichannel přístup – zákazník komunikuje kdekoliv', {'Marketingový specialista': 3, 'Obchodní zástupce': 2}),
            ('Personalizované doporučení na základě dat', {'Marketingový specialista': 3}),
            ('Lidský kontakt zůstane nenahraditelný', {'Recepční': 3, 'Průvodce': 2}),
            ('Zážitkový přístup – jde o celkový dojem', {'Barman': 3, 'Kuchař': 2})),

        # 480
        _p2('OBC', 'Co je pro vás nejdůležitější hodnota v obchodu a službách?',
            ('Férové jednání a dlouhodobé partnerství', {'Obchodní zástupce': 3, 'Nákupčí': 3}),
            ('Kreativita a schopnost zaujmout zákazníka', {'Marketingový specialista': 3, 'Barman': 2}),
            ('Pohostinnost a péče o každého hosta', {'Recepční': 3, 'Průvodce': 2}),
            ('Řemeslná dokonalost a vášeň pro detail', {'Kuchař': 3, 'Realitní makléř': 2})),

        # ══════════════ SKO: Školství a vzdělávání (481–560) ══════════════

        # --- Pracovní činnosti ---
        _p2('SKO', 'Jakou činnost ve školství byste vykonávali nejraději?',
            ('Výuku žáků na základní nebo střední škole', {'Učitel': 3}),
            ('Vedení firemního školení pro dospělé', {'Lektor': 3}),
            ('Provádění výzkumu a publikování vědeckých článků', {'Vědecký pracovník': 3}),
            ('Individuální koučovací rozhovory s klienty', {'Kouč': 3})),

        _p2('SKO', 'Která pracovní náplň vás láká nejvíce?',
            ('Příprava tréninkových plánů a kondiční příprava sportovců', {'Trenér': 3}),
            ('Organizace volnočasových aktivit v družině', {'Vychovatel': 3}),
            ('Práce s žáky se speciálními vzdělávacími potřebami', {'Speciální pedagog': 3}),
            ('Správa knihovního fondu a katalogizace', {'Knihovník': 3})),

        _p2('SKO', 'Co byste nejraději dělali v rámci vzdělávání?',
            ('Připravovali hodiny a přizpůsobovali výuku žákům', {'Učitel': 3}),
            ('Tvořili e-learningový kurz pro firemní klienty', {'Lektor': 3}),
            ('Psali grantovou žádost na výzkumný projekt', {'Vědecký pracovník': 3}),
            ('Motivovali klienta k dosažení osobních cílů', {'Kouč': 3})),

        _p2('SKO', 'Jak byste se nejraději podíleli na rozvoji druhých?',
            ('Přípravou sportovců na soutěže a závody', {'Trenér': 3}),
            ('Vedením kroužků a táborových programů', {'Vychovatel': 3}),
            ('Diagnostikou a podporou žáků s handicapem', {'Speciální pedagog': 3}),
            ('Přípravou rešerší a doporučení odborné literatury', {'Knihovník': 3})),

        _p2('SKO', 'Jakou aktivitou byste chtěli začínat svůj pracovní den?',
            ('Kontrolou sešitů a přípravou pomůcek na hodinu', {'Učitel': 3}),
            ('Přípravou materiálů pro workshop', {'Lektor': 3}),
            ('Čtením nejnovějších vědeckých článků ve svém oboru', {'Vědecký pracovník': 3}),
            ('Plánováním koučovacích sezení s klienty', {'Kouč': 3})),

        _p2('SKO', 'Kterou z těchto činností byste dělali s největším nadšením?',
            ('Nácvik taktiky a herních situací s týmem', {'Trenér': 3}),
            ('Organizaci výletů a mimoškolních akcí pro děti', {'Vychovatel': 3}),
            ('Sestavování individuálního vzdělávacího plánu', {'Speciální pedagog': 3}),
            ('Digitalizaci vzácných knih a dokumentů', {'Knihovník': 3})),

        _p2('SKO', 'Co vás nejvíce naplňuje při práci s lidmi?',
            ('Když žáci pochopí obtížnou látku díky mému výkladu', {'Učitel': 3}),
            ('Když účastníci školení získají prakticky využitelné dovednosti', {'Lektor': 3}),
            ('Když výzkum přinese nové poznatky pro obor', {'Vědecký pracovník': 3}),
            ('Když klient překoná svůj limit a dosáhne cíle', {'Kouč': 3})),

        _p2('SKO', 'Jakou roli byste chtěli zastávat ve vzdělávacím procesu?',
            ('Vedení sportovního tréninku a příprava na mistrovství', {'Trenér': 3}),
            ('Dohlížení na děti po vyučování a zajištění smysluplného programu', {'Vychovatel': 3}),
            ('Logopedická péče a náprava řečových vad', {'Speciální pedagog': 3}),
            ('Podpora čtenářské gramotnosti a informačního vzdělávání', {'Knihovník': 3})),

        _p2('SKO', 'Co považujete za svou hlavní pracovní činnost?',
            ('Hodnocení a klasifikaci žáků', {'Učitel': 3}),
            ('Tvorbu vzdělávacích programů na míru firmám', {'Lektor': 3, 'Kouč': 2}),
            ('Provádění experimentů a sběr dat', {'Vědecký pracovník': 3}),
            ('Rozvíjení potenciálu klientů formou rozhovorů', {'Kouč': 3})),

        _p2('SKO', 'Jaký typ práce vás baví na denní bázi?',
            ('Příprava kondiční a silové přípravy pro sportovce', {'Trenér': 3}),
            ('Plánování programu družiny a volnočasových aktivit', {'Vychovatel': 3}),
            ('Práce s kompenzačními pomůckami pro žáky s postižením', {'Speciální pedagog': 3}),
            ('Vyhledávání informací a rešeršní činnost', {'Knihovník': 3})),

        # --- Pracovní prostředí ---
        _p2('SKO', 'V jakém prostředí byste chtěli pracovat?',
            ('Ve školní třídě plné žáků', {'Učitel': 3}),
            ('V moderní školící místnosti s technikou', {'Lektor': 3}),
            ('V univerzitní laboratoři nebo výzkumném ústavu', {'Vědecký pracovník': 3}),
            ('V klidné koučovací místnosti při rozhovoru s klientem', {'Kouč': 3})),

        _p2('SKO', 'Kde se cítíte nejlépe při práci?',
            ('Ve sportovní hale nebo na hřišti', {'Trenér': 3}),
            ('Ve školní družině nebo na letním táboře', {'Vychovatel': 3}),
            ('V pedagogicko-psychologické poradně', {'Speciální pedagog': 3}),
            ('V tiché knihovně mezi regály knih', {'Knihovník': 3})),

        _p2('SKO', 'Jaké pracovní podmínky vám vyhovují?',
            ('Strukturovaný rozvrh hodin a školní rok', {'Učitel': 3}),
            ('Cestování za klienty a různá školící místa', {'Lektor': 3}),
            ('Akademické prostředí s volností výzkumu', {'Vědecký pracovník': 3}),
            ('Flexibilní rozvrh individuálních sezení', {'Kouč': 3})),

        _p2('SKO', 'Kde byste trávili typický pracovní den?',
            ('Na stadionu při vedení tréninku', {'Trenér': 3}),
            ('S dětmi v herně, na hřišti i v přírodě', {'Vychovatel': 3}),
            ('V poradenském zařízení s klienty', {'Speciální pedagog': 3}),
            ('U počítače a mezi knihami v knihovně', {'Knihovník': 3})),

        _p2('SKO', 'Jaká pracovní atmosféra vám sedí?',
            ('Živá třída plná dětské energie a otázek', {'Učitel': 3, 'Vychovatel': 2}),
            ('Profesionální firemní prostředí při školení', {'Lektor': 3}),
            ('Soustředěná atmosféra vědecké konference', {'Vědecký pracovník': 3}),
            ('Důvěrná atmosféra osobního rozvoje', {'Kouč': 3})),

        # --- Znalosti a dovednosti ---
        _p2('SKO', 'Jaká dovednost je ve vzdělávání vaší silnou stránkou?',
            ('Srozumitelný výklad a didaktické schopnosti', {'Učitel': 3}),
            ('Schopnost zaujmout a motivovat dospělé posluchače', {'Lektor': 3}),
            ('Analytické a kritické myšlení', {'Vědecký pracovník': 3}),
            ('Aktivní naslouchání a kladení správných otázek', {'Kouč': 3})),

        _p2('SKO', 'Která schopnost vás nejlépe vystihuje?',
            ('Schopnost takticky připravit tým na soupeře', {'Trenér': 3}),
            ('Kreativita při vymýšlení her a aktivit pro děti', {'Vychovatel': 3}),
            ('Trpělivost a empatie při práci s handicapovanými', {'Speciální pedagog': 3}),
            ('Preciznost při katalogizaci a třídění informací', {'Knihovník': 3})),

        _p2('SKO', 'Co považujete za svou nejcennější schopnost?',
            ('Dokážu přizpůsobit výklad různým úrovním žáků', {'Učitel': 3}),
            ('Umím navrhnout kompletní vzdělávací program', {'Lektor': 3, 'Kouč': 2}),
            ('Ovládám metodologii vědeckého výzkumu', {'Vědecký pracovník': 3}),
            ('Dokážu vést efektivní koučovací rozhovor', {'Kouč': 3})),

        _p2('SKO', 'Jaká vlastnost je pro vaši práci klíčová?',
            ('Fyzická zdatnost a znalost sportovní fyziologie', {'Trenér': 3}),
            ('Zkušenosti s volnočasovou pedagogikou', {'Vychovatel': 3}),
            ('Znalost speciálněpedagogické diagnostiky', {'Speciální pedagog': 3}),
            ('Orientace v knihovnických standardech a databázích', {'Knihovník': 3})),

        _p2('SKO', 'V čem vynikáte oproti ostatním?',
            ('Ve schopnosti nadchnout žáky pro učivo', {'Učitel': 3}),
            ('V prezentačních dovednostech před skupinou', {'Lektor': 3}),
            ('Ve schopnosti publikovat v impaktovaných časopisech', {'Vědecký pracovník': 3}),
            ('V práci se sportovci a jejich mentálním nastavením', {'Trenér': 3, 'Kouč': 2})),

        # --- Nástroje a technologie ---
        _p2('SKO', 'S jakými nástroji byste chtěli pracovat?',
            ('S interaktivní tabulí a vzdělávacím softwarem', {'Učitel': 3}),
            ('S platformou pro e-learning a video konference', {'Lektor': 3}),
            ('S laboratorním vybavením a statistickým softwarem', {'Vědecký pracovník': 3}),
            ('S koučovacími kartami a diagnostickými nástroji', {'Kouč': 3})),

        _p2('SKO', 'Která technologie vás nejvíce zajímá?',
            ('Sportovní analytika a GPS tracking hráčů', {'Trenér': 3}),
            ('Vzdělávací hry a kreativní aplikace pro děti', {'Vychovatel': 3}),
            ('Augmentativní komunikační systémy pro žáky', {'Speciální pedagog': 3}),
            ('Knihovní informační systém a digitální archivy', {'Knihovník': 3})),

        _p2('SKO', 'Jaký software byste se chtěli naučit?',
            ('Systém Bakaláři pro správu školní agendy', {'Učitel': 3}),
            ('Moodle nebo jiný LMS pro online vzdělávání', {'Lektor': 3}),
            ('SPSS nebo R pro statistickou analýzu dat', {'Vědecký pracovník': 3}),
            ('Koučovací a CRM platformu pro správu klientů', {'Kouč': 3})),

        _p2('SKO', 'S jakým vybavením byste rádi pracovali denně?',
            ('S video analýzou pohybu a stopkami na hřišti', {'Trenér': 3}),
            ('S výtvarnými potřebami a herními pomůckami', {'Vychovatel': 3}),
            ('S logopedickými pomůckami a speciálními testy', {'Speciální pedagog': 3}),
            ('Se skenerem a systémem pro digitalizaci tisků', {'Knihovník': 3})),

        _p2('SKO', 'Který nástroj považujete za nejdůležitější?',
            ('Učebnice a metodické materiály pro výuku', {'Učitel': 3}),
            ('Prezentační nástroje a flipchart', {'Lektor': 3}),
            ('Vědecké databáze a citační systémy', {'Vědecký pracovník': 3}),
            ('Katalogizační pravidla a online OPAC', {'Knihovník': 3})),

        # --- Hodnoty a motivace ---
        _p2('SKO', 'Co vás ve vzdělávání motivuje nejvíce?',
            ('Vidět pokrok svých žáků a jejich úspěchy', {'Učitel': 3}),
            ('Pomáhat dospělým získat nové kompetence pro práci', {'Lektor': 3}),
            ('Objevit něco nového, co posune lidské poznání', {'Vědecký pracovník': 3}),
            ('Vidět, jak klient nachází vlastní cestu k úspěchu', {'Kouč': 3})),

        _p2('SKO', 'Proč byste chtěli pracovat v oblasti vzdělávání?',
            ('Chci předávat svou vášeň pro sport dalším generacím', {'Trenér': 3}),
            ('Chci vytvářet bezpečné a inspirující prostředí pro děti', {'Vychovatel': 3}),
            ('Chci pomáhat dětem s handicapem dosáhnout maxima', {'Speciální pedagog': 3}),
            ('Chci zpřístupňovat vědění a kulturu široké veřejnosti', {'Knihovník': 3})),

        _p2('SKO', 'Co je pro vás na práci nejdůležitější?',
            ('Vychovat zodpovědné a vzdělané mladé lidi', {'Učitel': 3}),
            ('Přinášet praktické výsledky do firemní praxe', {'Lektor': 3}),
            ('Přispět k pokroku ve vědě publikacemi a výzkumem', {'Vědecký pracovník': 3}),
            ('Pomoci klientovi najít jeho vnitřní motivaci', {'Kouč': 3})),

        _p2('SKO', 'Co vás žene k lepšímu výkonu?',
            ('Úspěch svěřenců na závodech a mistrovstvích', {'Trenér': 3}),
            ('Radost dětí z dobře připraveného programu', {'Vychovatel': 3}),
            ('Pokroky žáků se speciálními potřebami', {'Speciální pedagog': 3}),
            ('Když čtenáři najdou přesně to, co hledali', {'Knihovník': 3})),

        _p2('SKO', 'Jaký přínos chcete mít pro společnost?',
            ('Vzdělávat budoucí generace kvalitní výukou', {'Učitel': 3, 'Lektor': 2}),
            ('Posouvat hranice lidského poznání výzkumem', {'Vědecký pracovník': 3}),
            ('Rozvíjet potenciál lidí pomocí koučování', {'Kouč': 3}),
            ('Zajistit rovný přístup ke vzdělání pro všechny', {'Speciální pedagog': 3, 'Vychovatel': 2})),

        # --- Řešení problémů ---
        _p2('SKO', 'Žák má dlouhodobě špatné výsledky – jak postupujete?',
            ('Upravím metody výuky a připravím doučování', {'Učitel': 3}),
            ('Navrhnu individuální vzdělávací přístup', {'Speciální pedagog': 3}),
            ('Vedu motivační rozhovor se žákem o jeho cílech', {'Kouč': 3}),
            ('Doporučím vhodné knihy a zdroje k samostudiu', {'Knihovník': 3, 'Učitel': 2})),

        _p2('SKO', 'Účastníci školení ztrácí pozornost – co uděláte?',
            ('Zařadím aktivizující metodu nebo skupinovou práci', {'Lektor': 3}),
            ('Připravím soutěžní aktivitu, aby se zapojili', {'Trenér': 2, 'Vychovatel': 2}),
            ('Zeptám se na jejich očekávání a přizpůsobím obsah', {'Kouč': 3}),
            ('Změním formát na praktický workshop', {'Lektor': 2, 'Učitel': 2})),

        _p2('SKO', 'Výzkumný projekt nedosahuje očekávaných výsledků – jak reagujete?',
            ('Přehodnotím hypotézy a upravím metodologii', {'Vědecký pracovník': 3}),
            ('Konzultuji s kolegy a hledám novou perspektivu', {'Vědecký pracovník': 2, 'Lektor': 2}),
            ('Analyzuji data z jiného úhlu pohledu', {'Vědecký pracovník': 3}),
            ('Provedu rešerši, zda někdo neřešil podobný problém', {'Knihovník': 3})),

        _p2('SKO', 'Dítě v družině se straní kolektivu – co uděláte?',
            ('Zapojím ho do skupinových her a aktivit', {'Vychovatel': 3}),
            ('Promluvím s ním o tom, co ho trápí', {'Kouč': 3, 'Vychovatel': 2}),
            ('Provedu diagnostiku sociálních kompetencí', {'Speciální pedagog': 3}),
            ('Informuji třídního učitele a rodiče', {'Učitel': 3})),

        _p2('SKO', 'Sportovec přichází o motivaci k tréninkům – jak zasáhnete?',
            ('Upravím tréninkový plán, aby byl pestřejší', {'Trenér': 3}),
            ('Povedu koučovací rozhovor o jeho cílech a hodnotách', {'Kouč': 3}),
            ('Zorganizuji přátelský zápas jako motivaci', {'Trenér': 2, 'Vychovatel': 2}),
            ('Doporučím mu literaturu o sportovní psychologii', {'Knihovník': 2, 'Kouč': 2})),

        # --- Vzdělání a kariéra ---
        _p2('SKO', 'Jaký kurz byste si vybrali?',
            ('Moderní didaktika a pedagogická psychologie', {'Učitel': 3}),
            ('Lektorské dovednosti a práce se skupinou', {'Lektor': 3}),
            ('Metodologie vědeckého výzkumu', {'Vědecký pracovník': 3}),
            ('Certifikace v profesionálním koučování (ICF)', {'Kouč': 3})),

        _p2('SKO', 'Kterou odbornou literaturu byste četli?',
            ('Knihy o sportovním tréninku a periodizaci', {'Trenér': 3}),
            ('Příručky volnočasové pedagogiky a animace', {'Vychovatel': 3}),
            ('Odborné texty o speciálněpedagogické diagnostice', {'Speciální pedagog': 3}),
            ('Standardy katalogizace a knihovní vědy', {'Knihovník': 3})),

        _p2('SKO', 'Jaký seminář byste navštívili?',
            ('Jak učit efektivně s využitím technologií', {'Učitel': 3}),
            ('Jak vytvořit poutavý e-learningový kurz', {'Lektor': 3}),
            ('Jak prezentovat výsledky na vědecké konferenci', {'Vědecký pracovník': 3}),
            ('Jak vést koučovací rozhovor podle GROW modelu', {'Kouč': 3})),

        _p2('SKO', 'Co byste studovali na vysoké škole?',
            ('Učitelství pro ZŠ nebo SŠ v konkrétním oboru', {'Učitel': 3}),
            ('Andragogiku nebo vzdělávání dospělých', {'Lektor': 3}),
            ('Doktorský program ve zvoleném vědním oboru', {'Vědecký pracovník': 3}),
            ('Speciální pedagogiku nebo logopedii', {'Speciální pedagog': 3})),

        _p2('SKO', 'Jakou praxi byste si vybrali?',
            ('Stáž na sportovním akademickém centru', {'Trenér': 3}),
            ('Vedení letního příměstského tábora', {'Vychovatel': 3}),
            ('Praxi v pedagogicko-psychologické poradně', {'Speciální pedagog': 3}),
            ('Stáž v krajské vědecké knihovně', {'Knihovník': 3})),

        # --- Styl interakce ---
        _p2('SKO', 'Jakou roli zastáváte v týmu?',
            ('Učitel, který vede a inspiruje skupinu', {'Učitel': 3}),
            ('Facilitátor, který moderuje diskuzi a sdílení', {'Lektor': 3}),
            ('Výzkumník, který přináší data a fakta', {'Vědecký pracovník': 3}),
            ('Kouč, který pomáhá ostatním najít řešení', {'Kouč': 3})),

        _p2('SKO', 'Jak přispíváte k úspěchu vzdělávacího projektu?',
            ('Přípravou sportovců na reprezentaci', {'Trenér': 3}),
            ('Organizací zázemí a péčí o děti', {'Vychovatel': 3}),
            ('Odbornou diagnostikou a nápravnou péčí', {'Speciální pedagog': 3}),
            ('Zpřístupněním informačních zdrojů všem', {'Knihovník': 3})),

        _p2('SKO', 'S kým nejraději spolupracujete?',
            ('Se žáky a jejich rodiči', {'Učitel': 3}),
            ('S firemním HR oddělením a managementem', {'Lektor': 3}),
            ('S kolegou vědcem na společném projektu', {'Vědecký pracovník': 3}),
            ('S klientem při hledání jeho životní vize', {'Kouč': 3})),

        _p2('SKO', 'Jak reagujete na neshodu v pedagogickém sboru?',
            ('Hledám kompromis a dodržuji školní řád', {'Učitel': 3}),
            ('Mediuji diskuzi a hledám společný cíl', {'Kouč': 3, 'Lektor': 2}),
            ('Argumentuji výzkumnými daty a důkazy', {'Vědecký pracovník': 3}),
            ('Nabídnu kompenzační přístupy pro různé názory', {'Speciální pedagog': 3})),

        _p2('SKO', 'Co oceňujete u kolegů?',
            ('Sportovní férovost a disciplínu', {'Trenér': 3}),
            ('Ochotu věnovat se dětem i nad rámec povinností', {'Vychovatel': 3}),
            ('Empatii a trpělivost s náročnými žáky', {'Speciální pedagog': 3}),
            ('Systematičnost a pečlivost v práci s informacemi', {'Knihovník': 3})),

        # --- Specifické situace ---
        _p2('SKO', 'Škola zavádí nový vzdělávací program – jaká je vaše role?',
            ('Přizpůsobím svou výuku novému ŠVP', {'Učitel': 3}),
            ('Připravím školení pro kolegy o nových metodách', {'Lektor': 3}),
            ('Provedu evaluaci programu na základě dat', {'Vědecký pracovník': 3}),
            ('Pomohu učitelům identifikovat potřeby žáků', {'Speciální pedagog': 3, 'Kouč': 2})),

        _p2('SKO', 'Město chce zřídit komunitní vzdělávací centrum – jak se zapojíte?',
            ('Navrhnu kurzy osobního rozvoje pro veřejnost', {'Kouč': 3}),
            ('Připravím sportovní programy pro všechny věkové skupiny', {'Trenér': 3}),
            ('Zorganizuji volnočasové aktivity pro děti a mládež', {'Vychovatel': 3}),
            ('Vybuduji knihovnu a informační zázemí centra', {'Knihovník': 3})),

        _p2('SKO', 'Na konferenci máte prezentovat svou práci – co představíte?',
            ('Inovativní metody výuky a jejich dopady na žáky', {'Učitel': 3}),
            ('Případovou studii úspěšného firemního školení', {'Lektor': 3}),
            ('Výsledky svého nejnovějšího výzkumu', {'Vědecký pracovník': 3}),
            ('Metodiku koučování ve školním prostředí', {'Kouč': 3})),

        _p2('SKO', 'Do školy nastoupí žák s tělesným postižením – co uděláte?',
            ('Přizpůsobím výuku a materiály jeho potřebám', {'Učitel': 3}),
            ('Vypracuji individuální vzdělávací plán (IVP)', {'Speciální pedagog': 3}),
            ('Zajistím bezpečné zapojení do volnočasových aktivit', {'Vychovatel': 3}),
            ('Připravím bezbariérový přístup k informačním zdrojům', {'Knihovník': 3})),

        _p2('SKO', 'Tým se připravuje na krajské mistrovství – jaký je váš přístup?',
            ('Provedu analýzu soupeřů a připravím taktický plán', {'Trenér': 3}),
            ('Podpořím sportovce koučovacími technikami před závodem', {'Kouč': 3}),
            ('Zajistím logistiku a doprovod na soutěž', {'Vychovatel': 3, 'Učitel': 2}),
            ('Vyhledám informace o pravidlech a historii soutěže', {'Knihovník': 2, 'Trenér': 2})),

        # --- Další pracovní činnosti ---
        _p2('SKO', 'Jakému úkolu byste dali přednost?',
            ('Třídnické hodiny a komunikace s rodiči', {'Učitel': 3}),
            ('Vytvoření obsahu a scénáře pro vzdělávací video', {'Lektor': 3}),
            ('Příprava přednášky pro univerzitní studenty', {'Vědecký pracovník': 3}),
            ('Vedení skupinového koučování v organizaci', {'Kouč': 3})),

        _p2('SKO', 'Jaký typ úkolu plníte nejefektivněji?',
            ('Vedení rozcvičky a kondiční přípravy', {'Trenér': 3}),
            ('Příprava her a soutěží pro dětský den', {'Vychovatel': 3}),
            ('Spolupráce s psychologem na diagnostice žáka', {'Speciální pedagog': 3}),
            ('Akvizice nových knih a aktualizace fondu', {'Knihovník': 3})),

        _p2('SKO', 'Co byste dělali o prázdninách ve svém oboru?',
            ('Připravovali tematické plány na nový školní rok', {'Učitel': 3}),
            ('Absolvovali odborné stáže a konference', {'Vědecký pracovník': 3}),
            ('Organizovali příměstský tábor pro děti', {'Vychovatel': 3}),
            ('Vedli letní sportovní soustředění', {'Trenér': 3})),

        _p2('SKO', 'Jakou agendu byste na pracovišti zvládli nejlépe?',
            ('Psaní výzkumných zpráv a grantových projektů', {'Vědecký pracovník': 3}),
            ('Správu databáze čtenářů a výpůjční systém', {'Knihovník': 3}),
            ('Přípravu podkladů pro integraci žáků se SVP', {'Speciální pedagog': 3}),
            ('Sestavení ročního plánu školení pro firmu', {'Lektor': 3})),

        _p2('SKO', 'Co děláte jako poslední před koncem pracovního dne?',
            ('Kontroluji domácí úkoly a připravuji zítřejší hodinu', {'Učitel': 3}),
            ('Zapisuji zpětnou vazbu od účastníků kurzu', {'Lektor': 3}),
            ('Aktualizuji záznamy z výzkumu v protokolu', {'Vědecký pracovník': 3}),
            ('Rekapituluji pokroky klientů v koučovacím deníku', {'Kouč': 3})),

        # --- Nástroje a technologie (pokračování) ---
        _p2('SKO', 'Jakou pomůcku byste chtěli mít vždy po ruce?',
            ('Časovou osu a nástěnku s učební látkou', {'Učitel': 3}),
            ('Sadu workshopových materiálů a případových studií', {'Lektor': 3}),
            ('Mikroskop nebo jiné laboratorní přístroje', {'Vědecký pracovník': 3}),
            ('Sadu koučovacích otázek a wheel of life šablonu', {'Kouč': 3})),

        _p2('SKO', 'S jakou technologií pracujete nejradéji?',
            ('Se sportovním fitness trackerem a analytickými aplikacemi', {'Trenér': 3}),
            ('S dramatickými a pohybovými hrami pro děti', {'Vychovatel': 3}),
            ('S alternativní a augmentativní komunikací (AAK)', {'Speciální pedagog': 3}),
            ('S elektronickými databázemi a vyhledávači', {'Knihovník': 3})),

        # --- Hodnoty (pokračování) ---
        _p2('SKO', 'Co je pro vás nejsilnější motivací k práci?',
            ('Vidina sportovního úspěchu svěřenců', {'Trenér': 3}),
            ('Štěstí dětí a jejich smysluplně strávený čas', {'Vychovatel': 3}),
            ('Překonání bariér u žáků se speciálními potřebami', {'Speciální pedagog': 3}),
            ('Šíření vzdělanosti a kultury prostřednictvím knih', {'Knihovník': 3})),

        _p2('SKO', 'Jaký cíl si ve své práci stanovujete?',
            ('Aby každý žák dosáhl svého maxima', {'Učitel': 3, 'Speciální pedagog': 2}),
            ('Aby účastníci odcházeli s prakticky využitelnými znalostmi', {'Lektor': 3}),
            ('Aby můj výzkum byl publikován v prestižním časopise', {'Vědecký pracovník': 3}),
            ('Aby klient získal jasný plán pro svůj rozvoj', {'Kouč': 3})),

        # --- Řešení problémů (pokračování) ---
        _p2('SKO', 'Knihovna potřebuje přilákat více čtenářů – co navrhnete?',
            ('Program čtenářských klubů a autorských besed', {'Knihovník': 3}),
            ('Workshop kreativního psaní a storytellingu', {'Lektor': 3}),
            ('Dětský čtenářský kroužek s dramatizací', {'Vychovatel': 3}),
            ('Výzkum čtenářských preferencí v komunitě', {'Vědecký pracovník': 3})),

        _p2('SKO', 'Žák s poruchou učení nezvládá tempo třídy – jak pomůžete?',
            ('Provedu speciálněpedagogickou diagnostiku', {'Speciální pedagog': 3}),
            ('Přizpůsobím výukové materiály a hodnocení', {'Učitel': 3}),
            ('Doporučím koučovací techniky pro budování sebedůvěry', {'Kouč': 3}),
            ('Navrhnu vhodné kompenzační pomůcky a literaturu', {'Knihovník': 2, 'Speciální pedagog': 2})),

        _p2('SKO', 'Firma potřebuje proškolit 200 zaměstnanců za měsíc – jak to řešíte?',
            ('Navrhnu blended-learning program s e-learningem', {'Lektor': 3}),
            ('Připravím strukturovaný harmonogram školení', {'Lektor': 2, 'Učitel': 2}),
            ('Vytvořím knihovnu vzdělávacích materiálů online', {'Knihovník': 3}),
            ('Zjistím individuální potřeby a rozvojové cíle', {'Kouč': 3})),

        # --- Styl interakce (pokračování) ---
        _p2('SKO', 'Jak komunikujete se svými svěřenci nebo klienty?',
            ('Pravidelným hodnocením a zpětnou vazbou ve výuce', {'Učitel': 3}),
            ('Aktivním nasloucháním a podporujícími otázkami', {'Kouč': 3}),
            ('Povzbuzováním a osobním přístupem na tréninku', {'Trenér': 3}),
            ('Trpělivým opakováním a individuální péčí', {'Speciální pedagog': 3})),

        _p2('SKO', 'Jak přistupujete k novým trendům ve svém oboru?',
            ('Sleduji vývoj kurikula a implementuji novinky do výuky', {'Učitel': 3}),
            ('Zkoumám nové vědecké metody a publikuji výsledky', {'Vědecký pracovník': 3}),
            ('Absolvuji pokročilá koučovací školení a supervize', {'Kouč': 3}),
            ('Sleduji moderní knihovnické platformy a digitalizaci', {'Knihovník': 3})),

        # --- Situační otázky ---
        _p2('SKO', 'Rodiče si stěžují na přísné hodnocení – jak reagujete?',
            ('Vysvětlím kritéria hodnocení a nabídnu konzultaci', {'Učitel': 3}),
            ('Doporučím koučovací přístup k motivaci dítěte', {'Kouč': 3}),
            ('Navrhnu úpravu hodnocení pro žáky se SVP', {'Speciální pedagog': 3}),
            ('Podpořím dítě mimoškolními aktivitami pro posílení sebevědomí', {'Vychovatel': 3})),

        _p2('SKO', 'Na pracovišti se má zavádět nový informační systém – co uděláte?',
            ('Naučím se ho rychle a pomohu kolegům s adaptací', {'Učitel': 3, 'Lektor': 2}),
            ('Připravím školení pro kolegy na nový systém', {'Lektor': 3}),
            ('Zhodnotím dopad na výzkumné workflow', {'Vědecký pracovník': 3}),
            ('Zajistím migraci dat a katalogů do nového systému', {'Knihovník': 3})),

        _p2('SKO', 'Máte za úkol navrhnout celodenní vzdělávací akci – co připravíte?',
            ('Pedagogickou konferenci s dílnami pro učitele', {'Učitel': 3, 'Lektor': 2}),
            ('Vědecký seminář s prezentacemi výsledků', {'Vědecký pracovník': 3}),
            ('Sportovní den s ukázkami tréninkových metod', {'Trenér': 3}),
            ('Den otevřených dveří v knihovně s workshopy', {'Knihovník': 3, 'Vychovatel': 2})),

        _p2('SKO', 'Na jakém výzkumném projektu byste pracovali?',
            ('Efektivita různých metod výuky na ZŠ', {'Učitel': 3, 'Vědecký pracovník': 2}),
            ('Vliv koučování na pracovní výkon zaměstnanců', {'Kouč': 3, 'Vědecký pracovník': 2}),
            ('Optimalizace sportovního tréninku pomocí dat', {'Trenér': 3, 'Vědecký pracovník': 2}),
            ('Inkluzivní vzdělávání a jeho dopady na žáky', {'Speciální pedagog': 3, 'Vědecký pracovník': 2})),

        _p2('SKO', 'Jak byste pomohli komunitě ve svém okolí?',
            ('Bezplatným doučováním dětí ze znevýhodněného prostředí', {'Učitel': 3}),
            ('Přednáškami a workshopy pro veřejnost', {'Lektor': 3}),
            ('Sportovním kroužkem pro děti z okolí', {'Trenér': 3, 'Vychovatel': 2}),
            ('Komunitním programem v místní knihovně', {'Knihovník': 3})),

        # --- Specializace a preference ---
        _p2('SKO', 'Jaký typ vzdělávání vás přitahuje?',
            ('Formální vzdělávání na školách', {'Učitel': 3}),
            ('Neformální a celoživotní vzdělávání dospělých', {'Lektor': 3}),
            ('Akademické vzdělávání a vědecký výzkum', {'Vědecký pracovník': 3}),
            ('Individuální rozvoj a osobnostní růst', {'Kouč': 3})),

        _p2('SKO', 'S jakou věkovou skupinou pracujete nejraději?',
            ('S dětmi školního věku (6–15 let)', {'Učitel': 3, 'Vychovatel': 2}),
            ('S dospělými v produktivním věku', {'Lektor': 3, 'Kouč': 2}),
            ('S adolescenty a mladými sportovci', {'Trenér': 3}),
            ('S dětmi předškolního a mladšího školního věku', {'Vychovatel': 3, 'Speciální pedagog': 2})),

        _p2('SKO', 'Co vás na vaší profesi fascinuje nejvíce?',
            ('Dynamika třídy a každodenní interakce s žáky', {'Učitel': 3}),
            ('Možnost neustále se učit a předávat poznatky', {'Lektor': 3, 'Vědecký pracovník': 2}),
            ('Síla otázek, které mění pohled na svět', {'Kouč': 3}),
            ('Práce s textem, informacemi a kulturním dědictvím', {'Knihovník': 3})),

        _p2('SKO', 'Jaký aspekt práce je pro vás nejzajímavější?',
            ('Sportovní výkon a jeho měřitelné zlepšování', {'Trenér': 3}),
            ('Tvořivost a spontaneita při práci s dětmi', {'Vychovatel': 3}),
            ('Hledání cesty ke každému žákovi s handicapem', {'Speciální pedagog': 3}),
            ('Budování systematických znalostních databází', {'Knihovník': 3})),

        _p2('SKO', 'Jak byste popsali svůj přístup k práci?',
            ('Strukturovaně a systematicky plánuji výuku', {'Učitel': 3}),
            ('Pružně reaguji na potřeby školené skupiny', {'Lektor': 3}),
            ('Rigorózně dodržuji vědeckou metodologii', {'Vědecký pracovník': 3}),
            ('Empaticky a nedirektivně vedu rozhovor', {'Kouč': 3})),

        # --- Další situace ---
        _p2('SKO', 'Jaké téma diplomové práce byste zvolili?',
            ('Využití gamifikace ve výuce na SŠ', {'Učitel': 3}),
            ('Efektivita koučovacích rozhovorů v organizacích', {'Kouč': 3}),
            ('Vliv systematického tréninku na výkonnost mládeže', {'Trenér': 3}),
            ('Digitalizace historických fondů české knihovny', {'Knihovník': 3})),

        _p2('SKO', 'Na jakou otázku hledáte odpověď nejčastěji?',
            ('Jak nejlépe vysvětlit tuto látku žákům?', {'Učitel': 3}),
            ('Jak zvýšit zapojení účastníků ve školení?', {'Lektor': 3}),
            ('Jaký metodologický postup zvolím pro experiment?', {'Vědecký pracovník': 3}),
            ('Jaké logopedické cvičení bude pro tohoto žáka nejúčinnější?', {'Speciální pedagog': 3})),

        _p2('SKO', 'Co vás inspiruje k inovacím ve vaší práci?',
            ('Nové pedagogické směry ze zahraničí', {'Učitel': 3, 'Lektor': 2}),
            ('Nejnovější vědecké publikace a konference', {'Vědecký pracovník': 3}),
            ('Moderní koučovací přístupy a neurowěda', {'Kouč': 3}),
            ('Inovace ve sportovní vědě a fyziologii', {'Trenér': 3})),

        _p2('SKO', 'Při cestě na pracoviště přemýšlíte o:',
            ('Jak oživit dnešní hodinu pro žáky', {'Učitel': 3}),
            ('Jak zařídit zábavný program pro děti v družině', {'Vychovatel': 3}),
            ('Jak pomoci žákovi s IVP zvládnout dnešní zkoušku', {'Speciální pedagog': 3}),
            ('Jaké nové tituly zařadit do knihovního fondu', {'Knihovník': 3})),

        _p2('SKO', 'Co je pro vás nejdůležitější hodnota ve vzdělávání?',
            ('Spravedlnost a rovný přístup ke všem žákům', {'Učitel': 3, 'Speciální pedagog': 2}),
            ('Praktická využitelnost a relevance poznatků', {'Lektor': 3}),
            ('Pravdivost a ověřitelnost informací', {'Vědecký pracovník': 3, 'Knihovník': 2}),
            ('Důvěra a respekt v mezilidských vztazích', {'Kouč': 3, 'Vychovatel': 2})),

        _p2('SKO', 'Jakou odpovědnost přijímáte nejraději?',
            ('Za vzdělávací výsledky celé třídy', {'Učitel': 3}),
            ('Za přípravu a realizaci kvalitního školení', {'Lektor': 3}),
            ('Za vědeckou integritu a kvalitu výzkumu', {'Vědecký pracovník': 3}),
            ('Za bezpečnost a rozvoj dětí po vyučování', {'Vychovatel': 3, 'Trenér': 2})),

        # ══════════════ PRA: Právo a veřejná správa (561–640) ══════════════

        # --- Pracovní činnosti ---
        _p2('PRA', 'Jakou činnost v oblasti práva byste vykonávali nejraději?',
            ('Zastupování klientů před soudem v trestních i civilních věcech', {'Advokát': 3}),
            ('Rozhodování sporů a vynášení rozsudků', {'Soudce': 3}),
            ('Ověřování listin a sepisování notářských zápisů', {'Notář': 3}),
            ('Dozor nad zákonností a vedení trestního stíhání', {'Státní zástupce': 3})),

        _p2('PRA', 'Která pracovní náplň vás láká nejvíce?',
            ('Vymáhání pohledávek a vedení exekučního řízení', {'Exekutor': 3}),
            ('Vyšetřování trestných činů a provádění výslechů', {'Policista': 3}),
            ('Hašení požárů a záchranné akce při mimořádných událostech', {'Hasič': 3}),
            ('Zpracování správních žádostí a vydávání rozhodnutí', {'Úředník': 3})),

        _p2('PRA', 'Co byste nejraději dělali v rámci právní praxe?',
            ('Přípravu žalob a zastupování klientů u líčení', {'Advokát': 3}),
            ('Studium judikatury a vedení soudního jednání', {'Soudce': 3}),
            ('Vedení dědického řízení a správu úschov', {'Notář': 3}),
            ('Podávání obžalob a dozor nad přípravným řízením', {'Státní zástupce': 3})),

        _p2('PRA', 'Jak byste se nejraději podíleli na prosazování práva?',
            ('Zabavením majetku dlužníků na základě soudního rozhodnutí', {'Exekutor': 3}),
            ('Hlídkovou službou a prevencí kriminality v terénu', {'Policista': 3}),
            ('Technickou pomocí při dopravních nehodách a haváriích', {'Hasič': 3}),
            ('Vedením spisové služby a archivací dokumentů', {'Úředník': 3})),

        _p2('PRA', 'Jakou činností byste chtěli začínat svůj pracovní den?',
            ('Konzultací s klientem o jeho právním problému', {'Advokát': 3}),
            ('Studiem spisů a přípravou na soudní jednání', {'Soudce': 3, 'Státní zástupce': 2}),
            ('Ověřováním podpisů a legalizací dokumentů', {'Notář': 3}),
            ('Ranní poradou na služebně a přehledem aktuální situace', {'Policista': 3})),

        _p2('PRA', 'Kterou z těchto činností byste dělali s největším nadšením?',
            ('Sepis smluv a právních dokumentů pro klienty', {'Advokát': 3, 'Notář': 2}),
            ('Vydání rozsudku po pečlivém zvážení důkazů', {'Soudce': 3}),
            ('Nařízení a provedení exekuce na majetek dlužníka', {'Exekutor': 3}),
            ('Zásah u požáru a evakuace ohrožených osob', {'Hasič': 3})),

        _p2('PRA', 'Co vás nejvíce naplňuje při práci se zákony?',
            ('Obhajoba práv klienta a hledání právních argumentů', {'Advokát': 3}),
            ('Spravedlivé rozhodnutí sporu na základě zákona', {'Soudce': 3}),
            ('Zajištění právní jistoty ověřením důležité listiny', {'Notář': 3}),
            ('Stíhání pachatelů trestných činů ve veřejném zájmu', {'Státní zástupce': 3})),

        _p2('PRA', 'Jakou roli byste chtěli zastávat při řešení právních záležitostí?',
            ('Vymáhání dluhů a zajištění nároků věřitelů', {'Exekutor': 3}),
            ('Zajištění místa činu a ohledání stop', {'Policista': 3}),
            ('Preventivní kontroly budov a provozoven z hlediska požární bezpečnosti', {'Hasič': 3}),
            ('Vyřizování stavebních povolení a územních rozhodnutí', {'Úředník': 3})),

        _p2('PRA', 'Co považujete za svou hlavní pracovní činnost?',
            ('Přípravu právních rozborů a stanovisek pro klienty', {'Advokát': 3}),
            ('Řízení a organizaci soudního jednání', {'Soudce': 3}),
            ('Správu notářského archivu a vydávání opisů', {'Notář': 3}),
            ('Přípravu obžaloby a výslech svědků', {'Státní zástupce': 3})),

        _p2('PRA', 'Jaký typ práce vás baví na denní bázi?',
            ('Provádění soupisu majetku a jeho dražba', {'Exekutor': 3}),
            ('Operativní pátrání po pohřešovaných osobách', {'Policista': 3}),
            ('Nácvik zásahů a obsluha hasičské techniky', {'Hasič': 3}),
            ('Vedení správního řízení a příprava rozhodnutí', {'Úředník': 3})),

        # --- Pracovní prostředí ---
        _p2('PRA', 'V jakém prostředí byste chtěli pracovat?',
            ('V advokátní kanceláři a v soudní síni', {'Advokát': 3}),
            ('V soudní síni za soudcovským stolem', {'Soudce': 3}),
            ('V notářské kanceláři při jednání s klienty', {'Notář': 3}),
            ('Na státním zastupitelství s přístupem ke spisům', {'Státní zástupce': 3})),

        _p2('PRA', 'Kde se cítíte nejlépe při práci?',
            ('V terénu při provádění exekuce a zajišťování majetku', {'Exekutor': 3}),
            ('Na policejní služebně nebo v terénu při hlídce', {'Policista': 3}),
            ('Na hasičské stanici a při výjezdech k zásahům', {'Hasič': 3}),
            ('V kanceláři úřadu při vyřizování spisů', {'Úředník': 3})),

        _p2('PRA', 'Jaké pracovní podmínky vám vyhovují?',
            ('Práce pod tlakem termínů s množstvím právních kauz', {'Advokát': 3}),
            ('Nezávislé rozhodování v důstojném prostředí soudu', {'Soudce': 3}),
            ('Klidná kancelářská práce s úředními hodinami', {'Notář': 3, 'Úředník': 2}),
            ('Terénní práce s nepředvídatelnými situacemi', {'Policista': 3, 'Hasič': 2})),

        _p2('PRA', 'Kde byste trávili typický pracovní den?',
            ('Střídavě v kanceláři a u soudu při jednáních', {'Advokát': 3}),
            ('Na pracovišti státního zastupitelství nad spisy', {'Státní zástupce': 3}),
            ('V terénu u dlužníků při provádění exekuce', {'Exekutor': 3}),
            ('Na úřadě při příjmu žádostí a komunikaci s občany', {'Úředník': 3})),

        _p2('PRA', 'Jaká pracovní atmosféra vám sedí?',
            ('Formální prostředí soudní síně s přísným protokolem', {'Soudce': 3, 'Státní zástupce': 2}),
            ('Dynamická práce v terénu se střídáním situací', {'Policista': 3}),
            ('Týmová spolupráce při náročných záchranných akcích', {'Hasič': 3}),
            ('Soustředěná práce nad právními dokumenty v kanceláři', {'Notář': 3})),

        # --- Znalosti a dovednosti ---
        _p2('PRA', 'Jaká dovednost je v oblasti práva vaší silnou stránkou?',
            ('Rétorika, argumentace a přesvědčivý projev u soudu', {'Advokát': 3}),
            ('Analytické myšlení a schopnost nestranně posoudit důkazy', {'Soudce': 3}),
            ('Preciznost při sepisování právních dokumentů', {'Notář': 3}),
            ('Znalost trestního práva a schopnost vést obžalobu', {'Státní zástupce': 3})),

        _p2('PRA', 'Která schopnost vás nejlépe vystihuje?',
            ('Vyjednávací dovednosti a asertivní komunikace', {'Exekutor': 3}),
            ('Fyzická zdatnost a schopnost reagovat ve stresu', {'Policista': 3, 'Hasič': 2}),
            ('Odvaha a odolnost při nebezpečných zásazích', {'Hasič': 3}),
            ('Pečlivost a systematičnost ve správních řízeních', {'Úředník': 3})),

        _p2('PRA', 'Co považujete za svou nejcennější schopnost?',
            ('Umím najít právní argumenty ve složitých kauzách', {'Advokát': 3}),
            ('Dokážu spravedlivě rozhodnout i v nejednoznačných případech', {'Soudce': 3}),
            ('Ovládám práci s katastrem nemovitostí a veřejnými rejstříky', {'Notář': 3, 'Úředník': 2}),
            ('Umím efektivně vést přípravné řízení trestní kauzy', {'Státní zástupce': 3})),

        _p2('PRA', 'Jaká vlastnost je pro vaši práci klíčová?',
            ('Cílevědomost při vymáhání a znalost exekučního řádu', {'Exekutor': 3}),
            ('Postřeh a schopnost rychle vyhodnotit situaci', {'Policista': 3}),
            ('Odvaha vstoupit do hořícího objektu a zachraňovat životy', {'Hasič': 4}),
            ('Znalost správního řádu a schopnost formulovat rozhodnutí', {'Úředník': 3})),

        _p2('PRA', 'V čem vynikáte oproti ostatním?',
            ('V přesvědčivém vystupování před soudem a porotou', {'Advokát': 3}),
            ('V nestranném a důkladném posouzení všech důkazů', {'Soudce': 3}),
            ('Ve schopnosti klidně jednat s agresivními osobami', {'Policista': 3, 'Exekutor': 2}),
            ('V rychlém a koordinovaném jednání při záchranných operacích', {'Hasič': 3})),

        # --- Nástroje a technologie ---
        _p2('PRA', 'S jakými nástroji byste chtěli pracovat?',
            ('S právními informačními systémy a judikaturou (ASPI, Beck-online)', {'Advokát': 3, 'Soudce': 2}),
            ('Se soudním informačním systémem a elektronickým spisem', {'Soudce': 3}),
            ('S notářským razítkem, ověřovací knihou a CzechPOINTem', {'Notář': 3}),
            ('S evidenčními systémy trestního řízení', {'Státní zástupce': 3})),

        _p2('PRA', 'Která technologie vás nejvíce zajímá?',
            ('Software pro správu exekucí a centrální evidence', {'Exekutor': 3}),
            ('Kriminalistická technika – daktyloskopie, DNA analýza', {'Policista': 3}),
            ('Hasičská technika – čerpadla, výšková technika, dýchací přístroje', {'Hasič': 3}),
            ('Informační systém datových schránek a eGovernment', {'Úředník': 3})),

        _p2('PRA', 'Jaký software byste se chtěli naučit?',
            ('Právní databáze ASPI a systém pro správu kauz', {'Advokát': 3}),
            ('Systém ISIR pro insolvenční řízení', {'Soudce': 3, 'Exekutor': 2}),
            ('Evidenční systém katastru nemovitostí', {'Notář': 3, 'Úředník': 2}),
            ('Informační systém Policie ČR pro pátrání a evidence', {'Policista': 3})),

        _p2('PRA', 'S jakým vybavením byste rádi pracovali denně?',
            ('S právní knihovnou, notebookem a diktafonem v soudní síni', {'Advokát': 3}),
            ('Se služební zbraní, vysílačkou a ve služebním vozidle', {'Policista': 3}),
            ('S hasičským autem, hadicemi a zásahovým oblekem', {'Hasič': 3}),
            ('S úředním razítkem, formuláři a spisovou službou', {'Úředník': 3})),

        _p2('PRA', 'Který nástroj považujete za nejdůležitější?',
            ('Sbírku zákonů a komentáře k právním předpisům', {'Advokát': 3, 'Soudce': 2}),
            ('Notářský zápis jako veřejnou listinu s důkazní silou', {'Notář': 3}),
            ('Trestní spis a protokoly z přípravného řízení', {'Státní zástupce': 3}),
            ('Exekuční příkaz a součinnost s bankami a registry', {'Exekutor': 3})),

        # --- Hodnoty a motivace ---
        _p2('PRA', 'Co vás v oblasti práva motivuje nejvíce?',
            ('Obhájit nevinného člověka a chránit jeho práva', {'Advokát': 3}),
            ('Zajistit spravedlnost nestranným rozhodnutím', {'Soudce': 3}),
            ('Předcházet právním sporům kvalitním právním poradenstvím', {'Notář': 3}),
            ('Chránit společnost stíháním pachatelů závažné kriminality', {'Státní zástupce': 3})),

        _p2('PRA', 'Proč byste chtěli pracovat v oblasti práva a bezpečnosti?',
            ('Chci zajistit, aby dlužníci plnili své závazky', {'Exekutor': 3}),
            ('Chci chránit občany a udržovat veřejný pořádek', {'Policista': 3}),
            ('Chci zachraňovat životy a pomáhat lidem v nouzi', {'Hasič': 3}),
            ('Chci zajistit hladký chod veřejné správy pro občany', {'Úředník': 3})),

        _p2('PRA', 'Co je pro vás na práci nejdůležitější?',
            ('Spravedlnost a rovnost před zákonem', {'Soudce': 3, 'Advokát': 2}),
            ('Zákonnost a důsledné dodržování právního řádu', {'Státní zástupce': 3}),
            ('Pomoc lidem v ohrožení života a zdraví', {'Hasič': 3, 'Policista': 2}),
            ('Transparentní a efektivní veřejná správa', {'Úředník': 3})),

        _p2('PRA', 'Co vás žene k lepšímu výkonu?',
            ('Vyhraný soudní spor díky důkladné přípravě', {'Advokát': 3}),
            ('Spravedlivý rozsudek, který obstojí u odvolacího soudu', {'Soudce': 3}),
            ('Bezchybně provedené ověření důležité smlouvy', {'Notář': 3}),
            ('Úspěšný zásah u požáru bez zranění zasahujících', {'Hasič': 3})),

        _p2('PRA', 'Jaký přínos chcete mít pro společnost?',
            ('Chránit práva jednotlivců kvalitní právní pomocí', {'Advokát': 3}),
            ('Zajistit vymahatelnost práva a plnění povinností', {'Exekutor': 3, 'Státní zástupce': 2}),
            ('Zvýšit bezpečnost občanů prevencí a rychlým zásahem', {'Policista': 3, 'Hasič': 2}),
            ('Zlepšit služby veřejné správy pro občany', {'Úředník': 3})),

        # --- Řešení problémů ---
        _p2('PRA', 'Klient je obviněn z trestného činu, který nespáchal – jak postupujete?',
            ('Shromáždím důkazy neviny a připravím obhajobu u soudu', {'Advokát': 3}),
            ('Nezávisle posoudím všechny důkazy obžaloby i obhajoby', {'Soudce': 3}),
            ('Prověřím, zda bylo přípravné řízení vedeno zákonně', {'Státní zástupce': 3}),
            ('Zajistím kriminalistické stopy, které mohou obvinění vyvrátit', {'Policista': 3})),

        _p2('PRA', 'Dlužník odmítá spolupracovat a skrývá majetek – co uděláte?',
            ('Provedu lustrace v registrech a nařídím exekuci na účty', {'Exekutor': 3}),
            ('Poradím klientovi právní kroky k vymožení pohledávky', {'Advokát': 3}),
            ('Prověřím, zda nejde o trestný čin poškozování věřitele', {'Státní zástupce': 3}),
            ('Zaznamenám skutečnosti do spisu a postoupím orgánům', {'Úředník': 3})),

        _p2('PRA', 'V bytovém domě vypukne požár – jak reagujete?',
            ('Řídím zásah, evakuuji obyvatele a hasím požár', {'Hasič': 3}),
            ('Zajistím obvod, řídím dopravu a pomáhám s evakuací', {'Policista': 3}),
            ('Připravím pojistnou dokumentaci a právní poradenství poškodzeným', {'Advokát': 3}),
            ('Vyřídím žádosti poškozených o náhradu škody na úřadě', {'Úředník': 3})),

        _p2('PRA', 'Občan podá stížnost na průtahy ve správním řízení – jak to řešíte?',
            ('Prověřím spis, zjistím příčinu průtahů a zjednám nápravu', {'Úředník': 3}),
            ('Zastupuji občana a podám žalobu na nečinnost správního orgánu', {'Advokát': 3}),
            ('Posoudím zákonnost postupu správního orgánu', {'Soudce': 3}),
            ('Prověřím, zda nedošlo ke zneužití pravomoci úřední osoby', {'Státní zástupce': 3})),

        _p2('PRA', 'Dojde k dopravní nehodě s těžkým zraněním – jaká je vaše role?',
            ('Vyproštění zraněných z vraku a poskytnutí první pomoci', {'Hasič': 3}),
            ('Vyšetření nehody, zajištění stop a výslech svědků', {'Policista': 3}),
            ('Právní zastoupení poškozeného v řízení o náhradu škody', {'Advokát': 3}),
            ('Rozhodnutí o vině a trestu v případném soudním řízení', {'Soudce': 3})),

        # --- Vzdělání a kariéra ---
        _p2('PRA', 'Jaký kurz byste si vybrali?',
            ('Rétorika a argumentace pro právníky', {'Advokát': 3}),
            ('Soudcovská etika a nezávislost justice', {'Soudce': 3}),
            ('Notářský řád a dědické právo v praxi', {'Notář': 3}),
            ('Trestní právo procesní a kriminologie', {'Státní zástupce': 3})),

        _p2('PRA', 'Kterou odbornou literaturu byste četli?',
            ('Komentáře k exekučnímu řádu a občanskému soudnímu řádu', {'Exekutor': 3}),
            ('Příručky kriminalistiky a forenzní psychologie', {'Policista': 3}),
            ('Odborné texty o požární ochraně a taktice zásahů', {'Hasič': 3}),
            ('Komentáře ke správnímu řádu a zákonu o obcích', {'Úředník': 3})),

        _p2('PRA', 'Co byste studovali na vysoké škole?',
            ('Právo na právnické fakultě se zaměřením na civilní právo', {'Advokát': 3, 'Soudce': 2}),
            ('Právo se specializací na trestní právo', {'Státní zástupce': 3, 'Policista': 2}),
            ('Požární ochranu a bezpečnost na technické univerzitě', {'Hasič': 3}),
            ('Veřejnou správu a regionální rozvoj', {'Úředník': 3})),

        _p2('PRA', 'Jakou praxi byste si vybrali?',
            ('Koncipientskou praxi v advokátní kanceláři', {'Advokát': 3}),
            ('Justičního čekatele na okresním soudu', {'Soudce': 3}),
            ('Notářského kandidáta v notářské kanceláři', {'Notář': 3}),
            ('Právního čekatele na státním zastupitelství', {'Státní zástupce': 3})),

        _p2('PRA', 'Jaký seminář byste navštívili?',
            ('Novely občanského zákoníku a jejich dopad na praxi', {'Advokát': 3, 'Notář': 2}),
            ('Moderní metody kriminalistického vyšetřování', {'Policista': 3}),
            ('Taktika zásahů u průmyslových havárií', {'Hasič': 3}),
            ('Elektronizace veřejné správy a digitální služby', {'Úředník': 3})),

        # --- Styl interakce ---
        _p2('PRA', 'Jakou roli zastáváte v týmu?',
            ('Obhájce, který hájí zájmy klienta za každou cenu', {'Advokát': 3}),
            ('Nestranný rozhodce, který drží rovnováhu', {'Soudce': 3}),
            ('Důvěryhodný odborník, ke kterému se obrací s důležitými dokumenty', {'Notář': 3}),
            ('Strážce zákonnosti, který dohlíží na dodržování pravidel', {'Státní zástupce': 3})),

        _p2('PRA', 'Jak přispíváte k úspěchu svého pracoviště?',
            ('Efektivním vymáháním pohledávek a naplňováním exekučních titulů', {'Exekutor': 3}),
            ('Rychlým objasňováním trestné činnosti a ochranou občanů', {'Policista': 3}),
            ('Profesionálním zvládnutím každého zásahu a záchranou životů', {'Hasič': 3}),
            ('Bezchybným vyřizováním správních záležitostí a službou občanům', {'Úředník': 3})),

        _p2('PRA', 'S kým nejraději spolupracujete?',
            ('S klienty při řešení jejich právních problémů', {'Advokát': 3}),
            ('S přísedícími a soudním personálem při jednáních', {'Soudce': 3}),
            ('S kolegy hasiči jako sehraný tým při zásahu', {'Hasič': 3}),
            ('S ostatními úředníky a občany při vyřizování agendy', {'Úředník': 3})),

        _p2('PRA', 'Jak komunikujete s osobami ve vaší praxi?',
            ('Profesionálně a s empatií při sepisování závětí a smluv', {'Notář': 3}),
            ('Důrazně a věcně při výslechu podezřelých', {'Policista': 3, 'Státní zástupce': 2}),
            ('Asertivně při jednání s dlužníky o splnění závazků', {'Exekutor': 3}),
            ('Trpělivě a srozumitelně při styku s občany na úřadě', {'Úředník': 3})),

        _p2('PRA', 'Jak reagujete na konfliktní situaci?',
            ('Hledám právní argumenty a snažím se o smírné řešení', {'Advokát': 3}),
            ('Zachovám nestrannost a rozhodnu podle práva', {'Soudce': 3}),
            ('Zůstanu klidný a řídím se zákonnými postupy', {'Policista': 3}),
            ('Deeskaluji situaci a postupuji podle předpisů', {'Hasič': 2, 'Úředník': 2})),

        # --- Specifické situace ---
        _p2('PRA', 'Zemřel občan a pozůstalí se nemohou dohodnout na dědictví – co uděláte?',
            ('Jako soudní komisař provedu dědické řízení a zajistím spravedlivé vypořádání', {'Notář': 3}),
            ('Zastupuji jednoho z dědiců a hájím jeho zákonný podíl', {'Advokát': 3}),
            ('Rozhodnu o dědických nárocích, pokud se strany nedohodnou', {'Soudce': 3}),
            ('Zpracuji podklady a zapíšu změny vlastnictví v katastru', {'Úředník': 3})),

        _p2('PRA', 'Na veřejném shromáždění hrozí eskalace násilí – jak zasáhnete?',
            ('Zajistím veřejný pořádek a v případě potřeby zakročím', {'Policista': 3}),
            ('Posoudím, zda nedošlo k trestným činům, a zahájím stíhání', {'Státní zástupce': 3}),
            ('Připravím se na případný zásah u požáru nebo zranění', {'Hasič': 3}),
            ('Prověřím, zda bylo shromáždění řádně ohlášeno úřadu', {'Úředník': 3})),

        _p2('PRA', 'Firma systematicky podvádí své zákazníky – jaká je vaše role?',
            ('Zastupuji poškozené klienty a podám hromadnou žalobu', {'Advokát': 3}),
            ('Zahájím trestní stíhání odpovědných osob za podvod', {'Státní zástupce': 3}),
            ('Provedu exekuci na majetek firmy na základě rozsudku', {'Exekutor': 3}),
            ('Rozhodnu o vině a uložím odpovídající trest', {'Soudce': 3})),

        _p2('PRA', 'Při kontrole restaurace zjistíte závažné porušení požární bezpečnosti – co uděláte?',
            ('Nařídím odstranění závad a v případě ohrožení uzavřu provoz', {'Hasič': 3}),
            ('Zahájím správní řízení a uložím pokutu za porušení předpisů', {'Úředník': 3}),
            ('Zastupuji provozovatele ve správním řízení o pokutě', {'Advokát': 3}),
            ('Prověřím, zda nejde o trestný čin obecného ohrožení', {'Státní zástupce': 3, 'Policista': 2})),

        _p2('PRA', 'Manželé se rozvádějí a soupeří o svěření dětí – jak postupujete?',
            ('Zastupuji jednoho z manželů a prosazuji nejlepší zájem dítěte', {'Advokát': 3}),
            ('Nestranně posoudím situaci a rozhodnu ve prospěch dítěte', {'Soudce': 3}),
            ('Sepíšu dohodu rodičů o péči ve formě notářského zápisu', {'Notář': 3}),
            ('Zajistím sociální šetření a zpracuji podklady pro soud', {'Úředník': 3})),

        # --- Další pracovní činnosti ---
        _p2('PRA', 'Jakému úkolu byste dali přednost?',
            ('Přípravě kasační stížnosti k Nejvyššímu soudu', {'Advokát': 3}),
            ('Sjednocování judikatury a tvorbě právních stanovisek', {'Soudce': 3}),
            ('Sepisování společenských smluv a zakládání obchodních společností', {'Notář': 3}),
            ('Dozoru nad policejním vyšetřováním závažné kauzy', {'Státní zástupce': 3})),

        _p2('PRA', 'Jaký typ úkolu plníte nejefektivněji?',
            ('Lustrace majetku dlužníka a koordinace srážek ze mzdy', {'Exekutor': 3}),
            ('Zpracování trestního oznámení a zahájení vyšetřování', {'Policista': 3}),
            ('Likvidace následků povodní a technická pomoc obyvatelům', {'Hasič': 3}),
            ('Příprava podkladů pro zastupitelstvo a vedení obce', {'Úředník': 3})),

        _p2('PRA', 'Co byste dělali na konci pracovního týdne?',
            ('Kontrolu termínů a přípravu podání pro příští týden', {'Advokát': 3}),
            ('Vyhotovení rozsudků a usnesení z proběhlých jednání', {'Soudce': 3}),
            ('Archivaci notářských zápisů a uzavření týdenní agendy', {'Notář': 3}),
            ('Údržbu hasičské techniky a inventuru výstroje', {'Hasič': 3})),

        _p2('PRA', 'Jakou agendu byste na pracovišti zvládli nejlépe?',
            ('Přípravu obžalovacích spisů pro soud', {'Státní zástupce': 3}),
            ('Vedení evidence exekučních řízení a komunikaci s věřiteli', {'Exekutor': 3}),
            ('Dokumentaci a vyhodnocení kriminálních případů', {'Policista': 3}),
            ('Vydávání občanských průkazů a cestovních dokladů', {'Úředník': 3})),

        _p2('PRA', 'Co děláte jako poslední před koncem pracovního dne?',
            ('Odpovídám na e-maily klientů a plánuji zítřejší jednání', {'Advokát': 3}),
            ('Kontroluji zápisy z dnešních soudních jednání', {'Soudce': 3}),
            ('Předávám směnu a informuji kolegy o aktuálních událostech', {'Policista': 3, 'Hasič': 2}),
            ('Uzavírám denní agendu a ukládám spisy do registratury', {'Úředník': 3})),

        # --- Nástroje a technologie (pokračování) ---
        _p2('PRA', 'Jakou pomůcku byste chtěli mít vždy po ruce?',
            ('Aktuální znění zákonů a přístup k judikatuře online', {'Advokát': 3, 'Soudce': 2}),
            ('Notářský řád a formuláře pro jednotlivé úkony', {'Notář': 3}),
            ('Služební odznak, pouta a vysílačku', {'Policista': 3}),
            ('Zásahový oblek, přilbu a dýchací přístroj', {'Hasič': 3})),

        _p2('PRA', 'S jakou technologií pracujete nejraději?',
            ('S elektronickým platebním rozkazem a datovými schránkami', {'Soudce': 3, 'Úředník': 2}),
            ('S centrální evidencí exekucí a insolvenčním rejstříkem', {'Exekutor': 3}),
            ('S termokamerou a detektory nebezpečných látek', {'Hasič': 3}),
            ('S radarovým měřičem rychlosti a bodycamerou', {'Policista': 3})),

        # --- Hodnoty (pokračování) ---
        _p2('PRA', 'Co je pro vás nejsilnější motivací k práci?',
            ('Pocit, že jsem pomohl klientovi k jeho právu', {'Advokát': 3}),
            ('Vědomí, že mé rozhodnutí je spravedlivé a zákonné', {'Soudce': 3}),
            ('Jistota, že dokumenty, které zpracuji, mají právní sílu', {'Notář': 3}),
            ('Vědomí, že pachatel byl postaven před spravedlnost', {'Státní zástupce': 3})),

        _p2('PRA', 'Jaký cíl si ve své práci stanovujete?',
            ('Úspěšně vymoci co nejvíce oprávněných pohledávek', {'Exekutor': 3}),
            ('Snížit kriminalitu v mém obvodu kvalitní policejní prací', {'Policista': 3}),
            ('Minimalizovat ztráty na životech a majetku při zásazích', {'Hasič': 3}),
            ('Vyřídit všechny žádosti občanů včas a bez chyb', {'Úředník': 3})),

        # --- Řešení problémů (pokračování) ---
        _p2('PRA', 'Klient si stěžuje na vysoké náklady právního zastoupení – jak reagujete?',
            ('Vysvětlím strukturu nákladů a nabídnu splátkový kalendář', {'Advokát': 3}),
            ('Doporučím notářský zápis jako levnější alternativu k soudu', {'Notář': 3}),
            ('Odkážu klienta na bezplatnou právní pomoc nebo mediaci', {'Advokát': 2, 'Soudce': 2}),
            ('Informuji o možnosti požádat o osvobození od soudních poplatků', {'Úředník': 3})),

        _p2('PRA', 'Při exekuci narazíte na rodinu s malými dětmi – jak postupujete?',
            ('Dodržuji zákonné limity a zajistím základní potřeby rodiny', {'Exekutor': 3}),
            ('Ověřím, zda exekuce probíhá v souladu se zákonem', {'Soudce': 3}),
            ('Nabídnu právní pomoc a hledám řešení oddlužení', {'Advokát': 3}),
            ('Informuji sociální odbor a zajistím pomoc rodině', {'Úředník': 3, 'Policista': 2})),

        # --- Styl interakce (pokračování) ---
        _p2('PRA', 'Jak přistupujete k novým trendům ve svém oboru?',
            ('Sleduji novelizace zákonů a účastním se advokátních školení', {'Advokát': 3}),
            ('Studuji novou judikaturu Ústavního soudu a ESLP', {'Soudce': 3}),
            ('Absolvuji cvičení s novou hasičskou technikou', {'Hasič': 3}),
            ('Učím se pracovat s novými moduly informačního systému úřadu', {'Úředník': 3})),

        _p2('PRA', 'Jak reagujete na kritiku vaší práce?',
            ('Přezkoumám své právní argumenty a zdokonalím strategii', {'Advokát': 3}),
            ('Respektuji odvolací rozhodnutí a poučím se z něj', {'Soudce': 3}),
            ('Provedu analýzu zásahu a zapracuji připomínky do postupů', {'Hasič': 3, 'Policista': 2}),
            ('Překontroluji rozhodnutí a odstraním případné nedostatky', {'Úředník': 3})),

        # --- Situační otázky ---
        _p2('PRA', 'Máte za úkol navrhnout zlepšení v rámci svého oboru – co navrhnete?',
            ('Zavedení online právních konzultací pro klienty', {'Advokát': 3}),
            ('Digitalizaci soudních spisů a elektronické jednání', {'Soudce': 3}),
            ('Zrychlení notářských úkonů pomocí elektronického podpisu', {'Notář': 3}),
            ('Zefektivnění správního řízení zavedením formulářů online', {'Úředník': 3})),

        _p2('PRA', 'Na konferenci máte prezentovat svou práci – co představíte?',
            ('Úspěšnou obhajobu ve složité trestní kauze', {'Advokát': 3}),
            ('Statistiky objasněnosti trestné činnosti v našem obvodu', {'Policista': 3}),
            ('Analýzu zásahů a nové metody požární prevence', {'Hasič': 3}),
            ('Inovace ve správním řízení a spokojenost občanů', {'Úředník': 3})),

        _p2('PRA', 'Město plánuje bezpečnostní strategii – jak se zapojíte?',
            ('Navrhnu preventivní programy a posílení hlídek', {'Policista': 3}),
            ('Připravím plán požární ochrany a evakuační trasy', {'Hasič': 3}),
            ('Zpracuji právní rámec a vyhlášky pro bezpečnost', {'Úředník': 3}),
            ('Zajistím soulad strategie s právními normami', {'Advokát': 2, 'Státní zástupce': 2})),

        _p2('PRA', 'Jak byste pomohli komunitě ve svém okolí?',
            ('Bezplatným právním poradenstvím pro potřebné občany', {'Advokát': 3}),
            ('Preventivními přednáškami o kriminalitě na školách', {'Policista': 3}),
            ('Ukázkami hasičské techniky a školením první pomoci', {'Hasič': 3}),
            ('Poradním dnem pro občany na úřadě o dostupných službách', {'Úředník': 3})),

        # --- Specializace a preference ---
        _p2('PRA', 'Jaký typ právního případu vás přitahuje?',
            ('Složité obchodní spory a korporátní právo', {'Advokát': 3}),
            ('Závažné trestní kauzy s celospolečenským dopadem', {'Soudce': 3, 'Státní zástupce': 2}),
            ('Převody nemovitostí a zástavní práva', {'Notář': 3}),
            ('Správní delikty a přestupkové řízení', {'Úředník': 3})),

        _p2('PRA', 'S jakou cílovou skupinou pracujete nejraději?',
            ('S klienty, kteří potřebují právní zastoupení', {'Advokát': 3}),
            ('Se stranami sporu, kterým zajišťuji spravedlivý proces', {'Soudce': 3}),
            ('S obyvateli při krizových situacích a záchranných akcích', {'Hasič': 3, 'Policista': 2}),
            ('S občany, kteří vyřizují záležitosti na úřadě', {'Úředník': 3})),

        _p2('PRA', 'Co vás na vaší profesi fascinuje nejvíce?',
            ('Strategie a taktika právní argumentace v soudní síni', {'Advokát': 3}),
            ('Moc a zodpovědnost spravedlivě rozhodovat o osudech lidí', {'Soudce': 3}),
            ('Adrenalin při záchranných akcích a pocit pomoci druhým', {'Hasič': 3}),
            ('Detektivní práce při odhalování trestné činnosti', {'Policista': 3})),

        _p2('PRA', 'Jaký aspekt práce je pro vás nejzajímavější?',
            ('Dědické řízení a řešení složitých majetkových vztahů', {'Notář': 3}),
            ('Dozor nad vyšetřováním a příprava obžaloby', {'Státní zástupce': 3}),
            ('Provádění dražeb a zpeněžování majetku', {'Exekutor': 3}),
            ('Tvorba obecně závazných vyhlášek a nařízení', {'Úředník': 3})),

        _p2('PRA', 'Jak byste popsali svůj přístup k práci?',
            ('Bojovně hájím zájmy svého klienta v rámci zákona', {'Advokát': 3}),
            ('Nestranně a nezávisle rozhoduji na základě důkazů', {'Soudce': 3}),
            ('Důsledně a systematicky vymáhám oprávněné nároky', {'Exekutor': 3}),
            ('Disciplinovaně plním rozkazy a chrání veřejný pořádek', {'Policista': 3})),

        # --- Další situace ---
        _p2('PRA', 'Jaké téma diplomové práce byste zvolili?',
            ('Právo na spravedlivý proces v judikatuře ESLP', {'Advokát': 3, 'Soudce': 2}),
            ('Elektronizace notářské činnosti v České republice', {'Notář': 3}),
            ('Efektivita alternativních trestů a resocializace', {'Státní zástupce': 3}),
            ('Moderní metody požární prevence v průmyslových objektech', {'Hasič': 3})),

        _p2('PRA', 'Na jakou otázku hledáte odpověď nejčastěji?',
            ('Jaký právní předpis se na tento případ vztahuje?', {'Advokát': 3, 'Soudce': 2}),
            ('Jak nejefektivněji zajistit majetek dlužníka?', {'Exekutor': 3}),
            ('Jaká je příčina požáru a jak mu příště předejít?', {'Hasič': 3}),
            ('Jak správně aplikovat zákon v tomto správním řízení?', {'Úředník': 3})),

        _p2('PRA', 'Při cestě na pracoviště přemýšlíte o:',
            ('Strategii obhajoby pro dnešní soudní jednání', {'Advokát': 3}),
            ('Důkazech a argumentech pro rozhodnutí ve složité kauze', {'Soudce': 3}),
            ('Připravenosti jednotky na případný denní zásah', {'Hasič': 3}),
            ('Termínech a prioritách v dnešním správním řízení', {'Úředník': 3})),

        _p2('PRA', 'Jakou odpovědnost přijímáte nejraději?',
            ('Za právní obranu klienta a dosažení nejlepšího výsledku', {'Advokát': 3}),
            ('Za zákonnost a správnost svých rozhodnutí', {'Soudce': 3, 'Státní zástupce': 2}),
            ('Za bezpečnost a životy zachráněných osob', {'Hasič': 3, 'Policista': 2}),
            ('Za správnost úředních rozhodnutí a službu veřejnosti', {'Úředník': 3})),

        _p2('PRA', 'Co vás inspiruje k inovacím ve vaší práci?',
            ('Judikatura vyšších soudů a mezinárodní právní standardy', {'Advokát': 3, 'Soudce': 2}),
            ('Nové kriminalistické metody a technologie vyšetřování', {'Policista': 3}),
            ('Pokroky v hasičské technice a záchranářských postupech', {'Hasič': 3}),
            ('Koncepce Smart City a digitalizace veřejné správy', {'Úředník': 3})),

        _p2('PRA', 'Jakou formu celoživotního vzdělávání preferujete?',
            ('Semináře České advokátní komory o novinkách v právu', {'Advokát': 3}),
            ('Stáže u vyšších soudů a výměnné programy s justičními orgány', {'Soudce': 3, 'Státní zástupce': 2}),
            ('Pravidelná cvičení a školení u Hasičského záchranného sboru', {'Hasič': 3}),
            ('Kurzy správního práva a veřejné politiky', {'Úředník': 3})),

        _p2('PRA', 'Jak byste přispěli ke zlepšení právního povědomí občanů?',
            ('Pořádáním dnů otevřených dveří v advokátní kanceláři', {'Advokát': 3}),
            ('Veřejně přístupnými rozsudky a srozumitelnými odůvodněními', {'Soudce': 3}),
            ('Besedami o práci policie a bezpečnosti na školách', {'Policista': 3}),
            ('Informačními brožurami a online průvodci úředními postupy', {'Úředník': 3, 'Notář': 2})),

        _p2('PRA', 'Co oceňujete u kolegů ve svém oboru?',
            ('Důkladnou znalost práva a etický přístup k profesi', {'Advokát': 3, 'Notář': 2}),
            ('Nestrannost a odvahu rozhodovat i v kontroverzních kauzách', {'Soudce': 3}),
            ('Odvahu a spolehlivost při riskantních zásazích', {'Hasič': 3, 'Policista': 2}),
            ('Důslednost a vstřícnost při jednání s občany', {'Úředník': 3, 'Exekutor': 2})),

        # ══════════════ MAN: Management a podnikání (641–720) ══════════════

        # --- Pracovní činnosti ---
        _p2('MAN', 'Jakou manažerskou činnost byste vykonávali nejraději?',
            ('Stanovování dlouhodobé vize a strategie celé firmy', {'Generální ředitel': 4}),
            ('Koordinaci týmů a sledování milníků projektu', {'Projektový manažer': 3}),
            ('Analýzu finančních výkazů a tvorbu investičních doporučení', {'Finanční analytik': 3}),
            ('Vedení účetních knih a přípravu daňových přiznání', {'Účetní': 3})),

        _p2('MAN', 'Která pracovní náplň vás přitahuje nejvíce?',
            ('Nábor nových zaměstnanců a vedení pohovorů', {'HR specialista': 3}),
            ('Zavádění systémů řízení kvality dle ISO norem', {'Manažer kvality': 3}),
            ('Zakládání vlastního podniku a tvorba business plánu', {'Podnikatel': 3}),
            ('Sledování plnění rozpočtu a analýza odchylek', {'Controller': 3})),

        _p2('MAN', 'Co by vás bavilo v každodenní práci ve firmě?',
            ('Jednání s obchodními partnery a investory', {'Generální ředitel': 3, 'Podnikatel': 2}),
            ('Plánování harmonogramu a přidělování úkolů týmu', {'Projektový manažer': 3}),
            ('Vytváření finančních modelů a prognóz', {'Finanční analytik': 3}),
            ('Zpracování měsíční uzávěrky a fakturace', {'Účetní': 3})),

        _p2('MAN', 'Jak byste se nejraději podíleli na chodu organizace?',
            ('Organizací vzdělávacích programů pro zaměstnance', {'HR specialista': 3}),
            ('Prováděním interních auditů a zlepšováním procesů', {'Manažer kvality': 3}),
            ('Hledáním investorů a přípravou fundraisingu', {'Podnikatel': 3, 'Finanční analytik': 2}),
            ('Přípravou reportů o klíčových ukazatelích výkonnosti', {'Controller': 3})),

        _p2('MAN', 'Která činnost v oblasti řízení vás oslovuje?',
            ('Rozhodování o fúzích, akvizicích a vstupu na nové trhy', {'Generální ředitel': 4}),
            ('Řízení rizik projektu a příprava záložních plánů', {'Projektový manažer': 3}),
            ('Oceňování firem a vyhodnocování investičních příležitostí', {'Finanční analytik': 3}),
            ('Kontrola souladu účetnictví s legislativou a auditem', {'Účetní': 3, 'Controller': 2})),

        _p2('MAN', 'Co byste dělali při zahájení nového kvartálu?',
            ('Definoval strategické cíle a priority společnosti', {'Generální ředitel': 3}),
            ('Aktualizoval projektový plán a Ganttův diagram', {'Projektový manažer': 3}),
            ('Sestavil kvartální rozpočet a sledoval cash flow', {'Controller': 3}),
            ('Připravil plán náboru na nadcházející období', {'HR specialista': 3})),

        _p2('MAN', 'Která aktivita na poradě vedení je vám nejbližší?',
            ('Prezentace vize a strategického směřování firmy', {'Generální ředitel': 3}),
            ('Report o stavu běžících projektů a terminech', {'Projektový manažer': 3}),
            ('Představení finanční analýzy a trendů', {'Finanční analytik': 3}),
            ('Shrnutí výsledků auditu kvality a nápravných opatření', {'Manažer kvality': 3})),

        _p2('MAN', 'Na konci fiskálního roku byste raději:',
            ('Hodnotili celoroční výsledky a stanovovali novou strategii', {'Generální ředitel': 3}),
            ('Zpracovávali roční účetní závěrku a daňové přiznání', {'Účetní': 3}),
            ('Analyzovali odchylky skutečnosti od plánu', {'Controller': 3}),
            ('Vyhodnocovali spokojenost zaměstnanců a fluktuaci', {'HR specialista': 3})),

        _p2('MAN', 'Jakou roli byste chtěli hrát při expanzi firmy?',
            ('Vyjednávání se zahraničními partnery o spolupráci', {'Generální ředitel': 3, 'Podnikatel': 2}),
            ('Řízení expanzního projektu od plánu po realizaci', {'Projektový manažer': 3}),
            ('Analýzu návratnosti investice do nového trhu', {'Finanční analytik': 3}),
            ('Zajištění kvality produktů na novém trhu dle ISO', {'Manažer kvality': 3})),

        _p2('MAN', 'Co byste dělali při krizové situaci ve firmě?',
            ('Koordinoval krizový tým a komunikoval s médii', {'Generální ředitel': 3}),
            ('Přepracoval projektový plán a realokoval zdroje', {'Projektový manažer': 3}),
            ('Modeloval finanční dopady krize a scénáře obnovy', {'Finanční analytik': 3, 'Controller': 2}),
            ('Připravil plán podpory zaměstnanců a interní komunikaci', {'HR specialista': 3})),

        # --- Odborné znalosti ---
        _p2('MAN', 'Které znalosti považujete za nejdůležitější?',
            ('Metody strategického řízení – SWOT, PEST, Balanced Scorecard', {'Generální ředitel': 3}),
            ('Metodiky projektového řízení – PRINCE2, Scrum, Kanban', {'Projektový manažer': 3}),
            ('Finanční matematika, DCF analýza a valuační modely', {'Finanční analytik': 3}),
            ('České účetní standardy, zákon o účetnictví a daních', {'Účetní': 3})),

        _p2('MAN', 'Jaké odborné oblasti vás zajímají nejvíce?',
            ('Pracovní právo, zákoník práce a personální procesy', {'HR specialista': 3}),
            ('ISO 9001, ISO 14001 a systémy managementu kvality', {'Manažer kvality': 3}),
            ('Podnikatelské právo, živnostenský zákon a obchodní rejstřík', {'Podnikatel': 3}),
            ('Manažerské účetnictví, kalkulace a rozpočetnictví', {'Controller': 3})),

        _p2('MAN', 'Který předmět ze studia by vás bavil nejvíce?',
            ('Strategický management a leadership', {'Generální ředitel': 3}),
            ('Projektové řízení a time management', {'Projektový manažer': 3}),
            ('Podnikové finance a investiční rozhodování', {'Finanční analytik': 3}),
            ('Účetnictví a auditing', {'Účetní': 3, 'Controller': 2})),

        _p2('MAN', 'Které téma byste si vybrali pro odbornou práci?',
            ('Řízení lidských zdrojů a talent management', {'HR specialista': 3}),
            ('Total Quality Management a Lean Six Sigma', {'Manažer kvality': 3}),
            ('Startupový ekosystém a venture capital', {'Podnikatel': 3}),
            ('Controlling a performance management v praxi', {'Controller': 3})),

        _p2('MAN', 'Která certifikace vás láká?',
            ('MBA – Master of Business Administration', {'Generální ředitel': 3}),
            ('PMP – Project Management Professional', {'Projektový manažer': 3}),
            ('CFA – Chartered Financial Analyst', {'Finanční analytik': 4}),
            ('ACCA – certifikace pro účetní a auditory', {'Účetní': 3})),

        _p2('MAN', 'Jaký typ školení byste absolvovali nejraději?',
            ('Workshop o vedení lidí a motivačních technikách', {'HR specialista': 3, 'Generální ředitel': 2}),
            ('Kurz interního auditu a procesního řízení', {'Manažer kvality': 3}),
            ('Seminář o podnikatelských modelech a inovacích', {'Podnikatel': 3}),
            ('Školení o ERP systémech a reportingových nástrojích', {'Controller': 3})),

        _p2('MAN', 'Které znalosti byste chtěli prohloubit?',
            ('Corporate governance a jednání představenstva', {'Generální ředitel': 3}),
            ('Agilní metodiky a Scrum framework', {'Projektový manažer': 3}),
            ('Statistické metody pro finanční analýzu', {'Finanční analytik': 3}),
            ('DPH, daň z příjmu a mezinárodní účetní standardy IFRS', {'Účetní': 3})),

        _p2('MAN', 'Jaká znalost vám připadá pro praxi nejcennější?',
            ('Schopnost číst a interpretovat finanční výkazy', {'Finanční analytik': 3, 'Controller': 2}),
            ('Znalost procesního řízení a PDCA cyklu', {'Manažer kvality': 3}),
            ('Orientace v pracovněprávní legislativě', {'HR specialista': 3}),
            ('Schopnost sestavit a obhájit business plán', {'Podnikatel': 3})),

        _p2('MAN', 'Co je podle vás základ dobrého řízení firmy?',
            ('Jasná vize, mise a strategické cíle', {'Generální ředitel': 3}),
            ('Strukturované řízení projektů s jasnými milníky', {'Projektový manažer': 3}),
            ('Přesné vedení účetnictví a finanční disciplína', {'Účetní': 3}),
            ('Průběžný dohled nad náklady a výnosy pomocí KPI', {'Controller': 3})),

        _p2('MAN', 'Které analytické dovednosti jsou podle vás klíčové?',
            ('Variance analysis a analýza odchylek od rozpočtu', {'Controller': 3}),
            ('Fundamentální a technická analýza trhů', {'Finanční analytik': 3}),
            ('Analýza neshod a root cause analysis', {'Manažer kvality': 3}),
            ('Analýza trhu a konkurence pro nový podnik', {'Podnikatel': 3})),

        # --- Pracovní styl ---
        _p2('MAN', 'Jak nejraději pracujete?',
            ('Vedu celý tým a rozhoduji o směřování organizace', {'Generální ředitel': 3}),
            ('Koordinuji práci různých oddělení na společném cíli', {'Projektový manažer': 3}),
            ('Samostatně analyzuji data a připravuji reporty', {'Finanční analytik': 3}),
            ('Pečlivě a systematicky zpracovávám doklady', {'Účetní': 3})),

        _p2('MAN', 'Jaký pracovní styl vám vyhovuje?',
            ('Práce s lidmi – pohovory, školení, týmové aktivity', {'HR specialista': 3}),
            ('Systematická kontrola procesů a dokumentace', {'Manažer kvality': 3}),
            ('Dynamické prostředí startupu s rychlými změnami', {'Podnikatel': 3}),
            ('Pravidelný cyklus reportingu a rozpočtování', {'Controller': 3})),

        _p2('MAN', 'Co vás nejvíce motivuje v práci?',
            ('Vidět, jak firma roste díky mým rozhodnutím', {'Generální ředitel': 3, 'Podnikatel': 2}),
            ('Úspěšně dokončit projekt v termínu a rozpočtu', {'Projektový manažer': 3}),
            ('Odhalit skrytý trend ve finančních datech', {'Finanční analytik': 3}),
            ('Bezchybně uzavřené účetní období', {'Účetní': 3})),

        _p2('MAN', 'Jak přistupujete k řešení problémů?',
            ('Svolám poradu vedení a hledáme strategické řešení', {'Generální ředitel': 3}),
            ('Rozeberu problém na podúkoly a přiřadím odpovědnosti', {'Projektový manažer': 3}),
            ('Provedu PDCA cyklus a identifikuji kořenovou příčinu', {'Manažer kvality': 3}),
            ('Spočítám finanční dopad a navrhnu optimalizaci nákladů', {'Controller': 3})),

        _p2('MAN', 'Jaký je váš typický den v práci?',
            ('Schůzky s partnery, strategická rozhodnutí, reprezentace', {'Generální ředitel': 3}),
            ('Standupy s týmem, aktualizace statusu, řešení blokátorů', {'Projektový manažer': 3}),
            ('Práce v Excelu, tvorba grafů a finančních modelů', {'Finanční analytik': 3}),
            ('Účtování dokladů, kontrola saldokonta, komunikace s bankou', {'Účetní': 3})),

        _p2('MAN', 'Jak reagujete na nečekané změny?',
            ('Rychle přehodnotím strategii a komunikuji nový směr', {'Generální ředitel': 3}),
            ('Upravím projektový plán a přehodnotím priority', {'Projektový manažer': 3}),
            ('Přepočítám finanční dopady a připravím nové scénáře', {'Finanční analytik': 3, 'Controller': 2}),
            ('Přizpůsobím byznys model a hledám nové příležitosti', {'Podnikatel': 3})),

        _p2('MAN', 'Jak komunikujete s kolegy?',
            ('Naslouchám a poskytuji zpětnou vazbu zaměstnancům', {'HR specialista': 3}),
            ('Jasně definuji požadavky a sleduji jejich plnění', {'Manažer kvality': 3}),
            ('Prezentuji čísla a fakta v přehledných reportech', {'Controller': 3}),
            ('Přesvědčuji investory a zákazníky o hodnotě produktu', {'Podnikatel': 3})),

        _p2('MAN', 'Jak zvládáte stres a tlak?',
            ('Deleguju úkoly a soustředím se na klíčová rozhodnutí', {'Generální ředitel': 3}),
            ('Rozložím práci do sprintů a udržuji tempo týmu', {'Projektový manažer': 3}),
            ('Postupuji systematicky podle checklist a standardů', {'Manažer kvality': 3, 'Účetní': 2}),
            ('Motivuju sám sebe vidinou úspěchu svého podnikání', {'Podnikatel': 3})),

        _p2('MAN', 'Jaký typ rozhodování vám vyhovuje?',
            ('Strategická rozhodnutí s dlouhodobým dopadem', {'Generální ředitel': 3}),
            ('Operativní rozhodnutí o prioritách a zdrojích', {'Projektový manažer': 3}),
            ('Datově podložená rozhodnutí na základě analýz', {'Finanční analytik': 3, 'Controller': 2}),
            ('Rychlá podnikatelská rozhodnutí v nejistém prostředí', {'Podnikatel': 3})),

        _p2('MAN', 'Jak se cítíte při práci s čísly?',
            ('Rád je interpretuji a hledám strategické souvislosti', {'Generální ředitel': 2, 'Controller': 3}),
            ('Baví mě přesné účtování a bilancování', {'Účetní': 3}),
            ('Miluju finanční modelování a predikce', {'Finanční analytik': 3}),
            ('Zajímá mě hlavně, kolik vydělám a jaký je ROI', {'Podnikatel': 3})),

        # --- Řešení situací ---
        _p2('MAN', 'Firma ztrácí tržní podíl. Co uděláte jako první?',
            ('Přehodnotím celkovou strategii a hledám nové segmenty', {'Generální ředitel': 3}),
            ('Analyzuji finanční data a identifikuji ztrátové produkty', {'Finanční analytik': 3}),
            ('Prověřím kvalitu produktů a zavedou opatření na zlepšení', {'Manažer kvality': 3}),
            ('Navrhnu pivot business modelu a nové tržní příležitosti', {'Podnikatel': 3})),

        _p2('MAN', 'Projekt překračuje rozpočet. Jak reagujete?',
            ('Projednám situaci s vedením a žádám navýšení rozpočtu', {'Generální ředitel': 2, 'Projektový manažer': 3}),
            ('Analyzuji příčiny překročení a navrhnu úspory', {'Controller': 3}),
            ('Přepočítám finanční model a identifikuji rizika', {'Finanční analytik': 3}),
            ('Reviduju rozsah projektu a vyjednám změny se stakeholderem', {'Projektový manažer': 3})),

        _p2('MAN', 'Zaměstnanci jsou demotivovaní. Co navrhnete?',
            ('Průzkum spokojenosti a systém benefitů', {'HR specialista': 3}),
            ('Transparentní komunikaci ze strany vedení', {'Generální ředitel': 3}),
            ('Zapojení týmu do zlepšovacích návrhů dle Kaizen', {'Manažer kvality': 3}),
            ('Motivační bonusy navázané na KPI', {'Controller': 3, 'HR specialista': 2})),

        _p2('MAN', 'Firma čelí auditu od externích auditorů. Co zajistíte?',
            ('Kompletní účetní dokumentaci a podklady', {'Účetní': 3}),
            ('Přehled plnění rozpočtu a finanční kontrolu', {'Controller': 3}),
            ('Aktuální dokumentaci systému řízení kvality', {'Manažer kvality': 3}),
            ('Komunikaci s auditory za celou firmu', {'Generální ředitel': 3})),

        _p2('MAN', 'Konkurence přišla s inovativním produktem. Co uděláte?',
            ('Svolám strategickou poradu a definuji odpověď firmy', {'Generální ředitel': 3}),
            ('Spočítám, kolik by stálo vyvinout konkurenční řešení', {'Finanční analytik': 3}),
            ('Založím projekt vývoje nového produktu', {'Projektový manažer': 3, 'Podnikatel': 2}),
            ('Analyzuji, zda náš produkt splňuje standardy kvality', {'Manažer kvality': 3})),

        _p2('MAN', 'Do firmy nastupuje 20 nových zaměstnanců. Kdo to řeší?',
            ('Připravím onboarding program a adaptační plán', {'HR specialista': 4}),
            ('Zařídím, aby měli přístupy do účetního systému', {'Účetní': 2, 'Controller': 2}),
            ('Zajistím jejich proškolení v kvalitativních standardech', {'Manažer kvality': 3}),
            ('Zapojím je do běžících projektů dle kompetencí', {'Projektový manažer': 3})),

        _p2('MAN', 'Firma chce vstoupit na burzu. Co bude vaše role?',
            ('Vedení celého procesu IPO a komunikace s trhem', {'Generální ředitel': 4}),
            ('Příprava finančních podkladů a prospektu', {'Finanční analytik': 3, 'Účetní': 2}),
            ('Due diligence a ověření finanční stability', {'Controller': 3}),
            ('Příprava startupu nebo spin-offu pro IPO', {'Podnikatel': 3})),

        _p2('MAN', 'V účetnictví byla nalezena chyba za minulé období. Co uděláte?',
            ('Opravím účetní záznamy a podám opravné přiznání', {'Účetní': 4}),
            ('Analyzuji dopad chyby na finanční výkazy a reporting', {'Controller': 3}),
            ('Provedu root cause analýzu – proč chyba vznikla', {'Manažer kvality': 3}),
            ('Informuji vedení firmy o dopadech a řešení', {'Generální ředitel': 2, 'Finanční analytik': 2})),

        _p2('MAN', 'Zákazník reklamuje kvalitu dodávky. Jak postupujete?',
            ('Zahájím reklamační řízení a 8D report', {'Manažer kvality': 4}),
            ('Řeším projekt nápravných opatření s dodacím termínem', {'Projektový manažer': 3}),
            ('Spočítám náklady reklamace a dopad na marži', {'Controller': 3}),
            ('Osobně jednám se zákazníkem a nabídnu kompenzaci', {'Generální ředitel': 3, 'Podnikatel': 2})),

        _p2('MAN', 'Firma potřebuje snížit náklady o 15 %. Co navrhnete?',
            ('Detailní nákladovou analýzu a identifikaci úspor', {'Controller': 4}),
            ('Optimalizaci procesů eliminací plýtvání (Lean)', {'Manažer kvality': 3}),
            ('Strategické rozhodnutí o restrukturalizaci', {'Generální ředitel': 3}),
            ('Analýzu, které pozice optimalizovat a jak', {'HR specialista': 3})),

        # --- Osobnostní předpoklady ---
        _p2('MAN', 'Která vlastnost vás nejlépe vystihuje?',
            ('Vizionářství a odvaha přijímat velká rozhodnutí', {'Generální ředitel': 3}),
            ('Organizovanost a schopnost řídit více úkolů najednou', {'Projektový manažer': 3}),
            ('Analytické myšlení a smysl pro detail v číslech', {'Finanční analytik': 3}),
            ('Preciznost a spolehlivost v práci s dokumenty', {'Účetní': 3})),

        _p2('MAN', 'Jakou další vlastnost u sebe oceňujete?',
            ('Empatii a schopnost porozumět potřebám lidí', {'HR specialista': 3}),
            ('Systematičnost a důslednost při dodržování standardů', {'Manažer kvality': 3}),
            ('Podnikavost a ochotu riskovat pro úspěch', {'Podnikatel': 3}),
            ('Objektivitu a schopnost pracovat s tvrdými daty', {'Controller': 3})),

        _p2('MAN', 'Co je vaší nejsilnější stránkou?',
            ('Charisma a přesvědčivost při vedení lidí', {'Generální ředitel': 3, 'Podnikatel': 2}),
            ('Time management a dodržování deadlinů', {'Projektový manažer': 3}),
            ('Číselná gramotnost a finanční intuice', {'Finanční analytik': 3}),
            ('Trpělivost a pečlivost při zpracování dat', {'Účetní': 3})),

        _p2('MAN', 'Jak se projevujete v týmu?',
            ('Jsem přirozený lídr – lidi mě následují', {'Generální ředitel': 3}),
            ('Jsem organizátor – hlídám termíny a úkoly', {'Projektový manažer': 3}),
            ('Jsem mediátor – pomáhám řešit konflikty', {'HR specialista': 3}),
            ('Jsem kontrolor – hlídám dodržování pravidel a norem', {'Manažer kvality': 3, 'Controller': 2})),

        _p2('MAN', 'Co vás v práci nejvíce baví?',
            ('Vyjednávání a uzavírání obchodních dohod', {'Generální ředitel': 3, 'Podnikatel': 2}),
            ('Správa a optimalizace rozpočtů', {'Controller': 3}),
            ('Stavění finančních modelů v tabulkovém procesoru', {'Finanční analytik': 3}),
            ('Organizování firemních akcí a teambuildingů', {'HR specialista': 3})),

        _p2('MAN', 'Jaký přístup k riziku vám vyhovuje?',
            ('Přijímám kalkulovaná rizika pro růst firmy', {'Generální ředitel': 3}),
            ('Rizika identifikuji, kvantifikuji a mitiguju v projektu', {'Projektový manažer': 3}),
            ('Modeluji rizikové scénáře a jejich finanční dopad', {'Finanční analytik': 3}),
            ('Nebojím se riskovat – bez rizika není zisk', {'Podnikatel': 4})),

        _p2('MAN', 'Jak vnímáte pravidla a procesy?',
            ('Jsou důležité, ale lídr musí umět myslet za ně', {'Generální ředitel': 3}),
            ('Procesy jsou základ kvality a efektivity', {'Manažer kvality': 3}),
            ('Pravidla účetnictví jsou svatá – dodržuji je do detailu', {'Účetní': 3}),
            ('Proces rozpočtování a reportingu musí být jasný', {'Controller': 3})),

        _p2('MAN', 'Jak se cítíte před velkým publikem?',
            ('Rád prezentuju vizi firmy zaměstnancům i investorům', {'Generální ředitel': 3}),
            ('Klidně prezentuji status projektu a výsledky', {'Projektový manažer': 3}),
            ('Raději pracuji v zákulisí s daty a analýzami', {'Finanční analytik': 2, 'Controller': 2}),
            ('Nadchnu každého pro svůj podnikatelský záměr', {'Podnikatel': 3})),

        _p2('MAN', 'Jaký styl vedení vám vyhovuje?',
            ('Transformační – inspiruji lidi sdílenou vizí', {'Generální ředitel': 3}),
            ('Servant leadership – sloužím svému týmu', {'Projektový manažer': 3}),
            ('Koučovací – rozvíjím potenciál zaměstnanců', {'HR specialista': 3}),
            ('Podnikatelský – razím cestu a jdu příkladem', {'Podnikatel': 3})),

        _p2('MAN', 'Co děláte, když selže plán?',
            ('Rychle rozhodnu o novém směru a komunikuji změnu', {'Generální ředitel': 3}),
            ('Aktivuji záložní plán a upravím harmonogram', {'Projektový manažer': 3}),
            ('Analyzuji data a hledám, kde se stala chyba', {'Controller': 3, 'Finanční analytik': 2}),
            ('Beru to jako lekci a pivotuju svůj podnikatelský záměr', {'Podnikatel': 3})),

        # --- Nástroje a technologie ---
        _p2('MAN', 'Který software byste se naučili nejraději?',
            ('ERP systém (SAP, Oracle) pro řízení celé firmy', {'Generální ředitel': 2, 'Controller': 3}),
            ('MS Project nebo Jira pro řízení projektů', {'Projektový manažer': 3}),
            ('Bloomberg Terminal nebo Reuters pro finanční data', {'Finanční analytik': 4}),
            ('Pohoda, Money S3 nebo SAP pro účetnictví', {'Účetní': 3})),

        _p2('MAN', 'Který nástroj byste používali každý den?',
            ('HR informační systém pro správu zaměstnanců', {'HR specialista': 3}),
            ('Software pro řízení kvality a auditní modul', {'Manažer kvality': 3}),
            ('Canva, Pitch deck – prezentace pro investory', {'Podnikatel': 3}),
            ('Power BI nebo Tableau pro manažerský reporting', {'Controller': 3, 'Finanční analytik': 2})),

        _p2('MAN', 'Které tabulky a reporty vám dávají smysl?',
            ('Strategická mapa a Balanced Scorecard', {'Generální ředitel': 3}),
            ('Ganttův diagram a WBS (Work Breakdown Structure)', {'Projektový manažer': 3}),
            ('Cash flow statement a finanční výkazy', {'Finanční analytik': 3}),
            ('Hlavní kniha, obratová předvaha a rozvaha', {'Účetní': 3})),

        _p2('MAN', 'Jaký typ analýzy byste prováděli nejraději?',
            ('SWOT analýzu a analýzu konkurenčního prostředí', {'Generální ředitel': 3, 'Podnikatel': 2}),
            ('Earned Value Analysis pro kontrolu projektu', {'Projektový manažer': 3}),
            ('Regresní analýzu a finanční prognózování', {'Finanční analytik': 3}),
            ('Budget vs. Actual a variance analýzu', {'Controller': 3})),

        _p2('MAN', 'Který digitální nástroj vám usnadní práci?',
            ('Slack nebo Teams pro firemní komunikaci', {'Generální ředitel': 2, 'Projektový manažer': 2}),
            ('Applicant Tracking System pro nábor', {'HR specialista': 3}),
            ('Quality management software (např. MasterControl)', {'Manažer kvality': 3}),
            ('Účetní software s automatickou fakturací', {'Účetní': 3})),

        _p2('MAN', 'Které metriky sledujete nejraději?',
            ('EBITDA, tržby, tržní podíl – výkonnost celé firmy', {'Generální ředitel': 3}),
            ('ROI, NPV, IRR – návratnost investic', {'Finanční analytik': 3}),
            ('PPM, DPMO, Sigma level – kvalita produkce', {'Manažer kvality': 3}),
            ('Marže, cost ratio, budget variance – nákladovost', {'Controller': 3})),

        _p2('MAN', 'Jaký typ prezentace připravujete nejčastěji?',
            ('Strategický plán pro představenstvo', {'Generální ředitel': 3}),
            ('Statusový report projektu pro stakeholdery', {'Projektový manažer': 3}),
            ('Investiční doporučení s finančními modely', {'Finanční analytik': 3}),
            ('Pitch deck pro investory a partnery', {'Podnikatel': 3})),

        _p2('MAN', 'Který informační systém vás zajímá?',
            ('CRM systém pro řízení vztahů se zákazníky', {'Generální ředitel': 2, 'Podnikatel': 3}),
            ('Project portfolio management systém', {'Projektový manažer': 3}),
            ('Daňový a účetní portál finanční správy', {'Účetní': 3}),
            ('Business intelligence platforma pro controlling', {'Controller': 3})),

        _p2('MAN', 'Jakou metodu zlepšování procesů preferujete?',
            ('Lean management a eliminace plýtvání', {'Manažer kvality': 3}),
            ('Six Sigma a statistické řízení procesů', {'Manažer kvality': 3, 'Controller': 2}),
            ('Design Thinking pro inovace a podnikání', {'Podnikatel': 3}),
            ('Kaizen a kontinuální zlepšování ve výrobě', {'Manažer kvality': 3})),

        _p2('MAN', 'Který reportingový formát vám vyhovuje?',
            ('Executive summary pro top management', {'Generální ředitel': 3}),
            ('Detailní finanční report s komentáři odchylek', {'Controller': 3}),
            ('Dashboardy s KPI v reálném čase', {'Finanční analytik': 3, 'Projektový manažer': 2}),
            ('Auditní zprávy s nálezy a doporučeními', {'Manažer kvality': 3})),

        # --- Hodnoty a motivace ---
        _p2('MAN', 'Co vás žene vpřed v kariéře?',
            ('Touha řídit velkou organizaci a ovlivňovat trh', {'Generální ředitel': 3}),
            ('Radost z úspěšně dokončených projektů', {'Projektový manažer': 3}),
            ('Fascinace světem financí a kapitálových trhů', {'Finanční analytik': 3}),
            ('Jistota stabilní a přesné práce s jasnými pravidly', {'Účetní': 3})),

        _p2('MAN', 'Co považujete za nejdůležitější v podnikání?',
            ('Péči o zaměstnance jako o nejcennější kapitál', {'HR specialista': 3}),
            ('Kvalitu produktů a služeb bez kompromisů', {'Manažer kvality': 3}),
            ('Odvahu riskovat a realizovat svou vizi', {'Podnikatel': 3}),
            ('Finanční kontrolu a transparentní hospodaření', {'Controller': 3})),

        _p2('MAN', 'Jaký typ úspěchu vás nejvíce potěší?',
            ('Firma pod mým vedením zdvojnásobila hodnotu', {'Generální ředitel': 4}),
            ('Projekt byl dodán včas, v kvalitě a pod rozpočtem', {'Projektový manažer': 3}),
            ('Moje investiční doporučení přineslo klientům zisk', {'Finanční analytik': 3}),
            ('Roční závěrka prošla auditem bez výhrad', {'Účetní': 3})),

        _p2('MAN', 'Co vás motivuje ke studiu a rozvoji?',
            ('Chci porozumět lidem a pomáhat jim růst', {'HR specialista': 3}),
            ('Chci zvládnout ISO normy a prosadit kulturu kvality', {'Manažer kvality': 3}),
            ('Chci vybudovat úspěšnou firmu od nuly', {'Podnikatel': 4}),
            ('Chci rozumět každé koruně ve firmě', {'Controller': 3})),

        _p2('MAN', 'Kde se vidíte za 10 let?',
            ('V čele velké korporace nebo holdingu', {'Generální ředitel': 4}),
            ('Jako vedoucí PMO – kanceláře projektového řízení', {'Projektový manažer': 3}),
            ('Jako portfolio manažer v investiční společnosti', {'Finanční analytik': 3}),
            ('Jako majitel vlastní prosperující firmy', {'Podnikatel': 4})),

        _p2('MAN', 'Co je pro vás v práci nejdůležitější?',
            ('Vliv na směřování firmy a společnosti', {'Generální ředitel': 3}),
            ('Spravedlivé a motivující pracovní prostředí', {'HR specialista': 3}),
            ('Preciznost a bezchybnost v každém detailu', {'Účetní': 3, 'Manažer kvality': 2}),
            ('Transparentní a datově podložené rozhodování', {'Controller': 3})),

        _p2('MAN', 'Jaký přínos chcete mít pro společnost?',
            ('Vytvářet pracovní místa a ekonomický růst', {'Generální ředitel': 3, 'Podnikatel': 2}),
            ('Zajistit kvalitu a bezpečnost produktů pro spotřebitele', {'Manažer kvality': 3}),
            ('Pomáhat firmám efektivně hospodařit', {'Controller': 3, 'Finanční analytik': 2}),
            ('Budovat firemní kulturu kde se lidem dobře pracuje', {'HR specialista': 3})),

        _p2('MAN', 'Jakou hodnotu přinášíte zaměstnavateli?',
            ('Strategické myšlení a schopnost vést organizaci', {'Generální ředitel': 3}),
            ('Schopnost dodat projekt na čas a v kvalitě', {'Projektový manažer': 3}),
            ('Přesné a spolehlivé finanční informace pro rozhodování', {'Účetní': 3, 'Controller': 2}),
            ('Know-how v zakládání a škálování podnikání', {'Podnikatel': 3})),

        _p2('MAN', 'Co vás inspiruje v obchodním světě?',
            ('Příběhy legendárních CEO a business leaderů', {'Generální ředitel': 3}),
            ('Úspěšné startup příběhy od garáže k miliardám', {'Podnikatel': 3}),
            ('Sofistikované finanční strategie Warren Buffetta', {'Finanční analytik': 3}),
            ('Toyota Production System a cesta ke kvalitě', {'Manažer kvality': 3})),

        _p2('MAN', 'Proč je vaše role ve firmě nezbytná?',
            ('Bez vize a leadershipu firma ztratí směr', {'Generální ředitel': 3}),
            ('Bez projektového řízení se nic nedotáhne do konce', {'Projektový manažer': 3}),
            ('Bez správného účetnictví firma neobstojí před zákonem', {'Účetní': 3}),
            ('Bez controllingu firma neví, zda je zisková', {'Controller': 3})),

        # --- Situační otázky ---
        _p2('MAN', 'Představenstvo žádá plán na záchranu ztrátové divize. Co připravíte?',
            ('Strategický restrukturalizační plán se změnou portfolia', {'Generální ředitel': 3}),
            ('Detailní nákladovou analýzu a plán úspor', {'Controller': 3}),
            ('Projekt restrukturalizace s milníky a zodpovědnostmi', {'Projektový manažer': 3}),
            ('Analýzu, které zaměstnance přeřadit a jaká školení zajistit', {'HR specialista': 3})),

        _p2('MAN', 'Firma získala velkou zakázku. Jaká je vaše první akce?',
            ('Sestavím projektový tým a kick-off meeting', {'Projektový manažer': 3}),
            ('Spočítám kalkulaci a zajistím financování', {'Finanční analytik': 3, 'Controller': 2}),
            ('Provedu kapacitní plánování a nábor', {'HR specialista': 3}),
            ('Nastavím kvalitativní požadavky dle smlouvy', {'Manažer kvality': 3})),

        _p2('MAN', 'Investor žádá o finanční reporting za poslední 3 roky. Co připravíte?',
            ('Konsolidované finanční výkazy s auditorským výrokem', {'Účetní': 3}),
            ('Analýzu trendů, poměrových ukazatelů a peer srovnání', {'Finanční analytik': 3}),
            ('Controlling report s přehledem plnění KPI', {'Controller': 3}),
            ('Prezentaci výsledků a strategického výhledu firmy', {'Generální ředitel': 3})),

        _p2('MAN', 'Zaměstnanec podal výpověď v kritické pozici. Co uděláte?',
            ('Okamžitě zahájím nábor a oslovím headhuntery', {'HR specialista': 4}),
            ('Přerozdělím úkoly v projektu a zajistím kontinuitu', {'Projektový manažer': 3}),
            ('Zvážím protinahídku a jednám o podmínkách setrvání', {'Generální ředitel': 3}),
            ('Zdokumentuji jeho know-how a procesy pro nástupce', {'Manažer kvality': 3})),

        _p2('MAN', 'Dodavatele je třeba změnit kvůli kvalitě. Jak postupujete?',
            ('Provedu audit dodavatele a vyhodnotím neshody', {'Manažer kvality': 4}),
            ('Spočítám náklady na změnu a dopad na rozpočet', {'Controller': 3}),
            ('Vyjednám nové podmínky nebo vyberu nového dodavatele', {'Generální ředitel': 3, 'Podnikatel': 2}),
            ('Naplánuji přechod na nového dodavatele jako projekt', {'Projektový manažer': 3})),

        _p2('MAN', 'Firma chce zavést nový ERP systém. Co je vaše úloha?',
            ('Řídím implementační projekt od analýzy po Go-Live', {'Projektový manažer': 3}),
            ('Definuji požadavky na účetní a finanční modul', {'Účetní': 3, 'Controller': 2}),
            ('Zajistím migraci dat a školení uživatelů', {'HR specialista': 2, 'Manažer kvality': 2}),
            ('Schvaluji rozpočet a strategické rozhodnutí o dodavateli', {'Generální ředitel': 3})),

        _p2('MAN', 'Na trhu došlo k ekonomické recesi. Jak na to reagujete?',
            ('Připravím krizový scénář a přizpůsobím strategii', {'Generální ředitel': 3}),
            ('Přepočítám rozpočty a identifikuji zbytné náklady', {'Controller': 3}),
            ('Analyzuji dopad na cash flow a likviditu firmy', {'Finanční analytik': 3}),
            ('Hledám nové tržní příležitosti a pivotuju byznys model', {'Podnikatel': 3})),

        _p2('MAN', 'Tým v projektu se nedokáže dohodnout na postupu. Co uděláte?',
            ('Facilituju dialog a pomůžu najít kompromis', {'HR specialista': 3}),
            ('Rozhodnu jako projektový manažer a nastavím jasná pravidla', {'Projektový manažer': 3}),
            ('Zavedu standardní postup a eskalační proceduru', {'Manažer kvality': 3}),
            ('Jako ředitel rozhodnu a převezmu odpovědnost', {'Generální ředitel': 3})),

        _p2('MAN', 'Státní kontrola odhalila nedostatky v DPH přiznání. Co zajistíte?',
            ('Opravu přiznání, doplatek DPH a komunikaci s finančním úřadem', {'Účetní': 4}),
            ('Analýzu příčin a zavedení kontrolních mechanismů', {'Controller': 3, 'Manažer kvality': 2}),
            ('Finanční kvantifikaci dopadu na hospodaření firmy', {'Finanční analytik': 3}),
            ('Informování vedení a přijetí nápravných opatření', {'Generální ředitel': 3})),

        _p2('MAN', 'Firma plánuje fúzi s konkurentem. Jaká je vaše role?',
            ('Vedu vyjednávání a koordinuji integraci na strategické úrovni', {'Generální ředitel': 4}),
            ('Provádím finanční due diligence a oceňuji cílovou firmu', {'Finanční analytik': 3}),
            ('Plánuji integrační projekt s milníky a zodpovědnostmi', {'Projektový manažer': 3}),
            ('Řeším harmonizaci HR procesů a organizační struktury', {'HR specialista': 3})),

        # ══════════════ UME: Umění a kultura (721–800) ══════════════

        # --- Pracovní činnosti ---
        _p2('UME', 'Která kreativní činnost vás láká nejvíce?',
            ('Vstoupit do role a zahrát postavu na jevišti', {'Herec': 3}),
            ('Vést tým herců a utvářet celkovou vizi díla', {'Režisér': 3}),
            ('Skládat hudbu a hrát na nástroj', {'Hudebník': 3}),
            ('Navrhovat plakáty a vizuální materiály', {'Grafik': 3})),

        _p2('UME', 'Co byste dělali nejraději celý pracovní den?',
            ('Fotili portréty a reportáže', {'Fotograf': 3}),
            ('Psali povídky nebo román', {'Spisovatel': 3}),
            ('Natáčeli filmové záběry s profesionální kamerou', {'Kameraman': 3}),
            ('Kreslili ilustrace do dětské knihy', {'Ilustrátor': 3})),

        _p2('UME', 'Jakou divadelní činnost byste si vybrali?',
            ('Ztvárnění hlavní role v činohře', {'Herec': 4}),
            ('Režírování inscenace od A do Z', {'Režisér': 4}),
            ('Složení scénické hudby k představení', {'Hudebník': 3}),
            ('Navržení divadelního plakátu a programu', {'Grafik': 3})),

        _p2('UME', 'Jak byste se podíleli na vzniku filmu?',
            ('Zahrál/a bych hlavní roli', {'Herec': 3}),
            ('Řídil/a bych celý natáčecí proces', {'Režisér': 3}),
            ('Točil/a bych záběry a pracoval/a se světlem', {'Kameraman': 4}),
            ('Psal/a bych filmový scénář', {'Spisovatel': 3})),

        _p2('UME', 'Jak byste přispěli k novému časopisu?',
            ('Tvorbou reportážních fotografií', {'Fotograf': 3}),
            ('Psaním článků a fejetonů', {'Spisovatel': 3}),
            ('Navržením layoutu a grafického stylu', {'Grafik': 4}),
            ('Kreslením editoriálních ilustrací', {'Ilustrátor': 3})),

        _p2('UME', 'Která práce spojená s knihou vás baví?',
            ('Napsat celý příběh od začátku do konce', {'Spisovatel': 4}),
            ('Navrhnout obálku a typografii', {'Grafik': 3}),
            ('Nakreslit ilustrace ke kapitolám', {'Ilustrátor': 4}),
            ('Nafotit autorský portrét na záložku', {'Fotograf': 3})),

        _p2('UME', 'Co byste dělali na koncertě?',
            ('Vystupoval/a bych jako sólový interpret', {'Hudebník': 4}),
            ('Organizoval/a a režíroval/a bych průběh koncertu', {'Režisér': 3}),
            ('Natáčel/a bych koncertní záznam', {'Kameraman': 3}),
            ('Fotografoval/a bych interprety na pódiu', {'Fotograf': 3})),

        _p2('UME', 'Jakou roli byste měli v reklamní agentuře?',
            ('Natáčel/a bych reklamní spoty', {'Kameraman': 3}),
            ('Navrhoval/a bych loga a firemní identity', {'Grafik': 4}),
            ('Psal/a bych reklamní slogany a texty', {'Spisovatel': 3}),
            ('Ilustroval/a bych reklamní kampaně', {'Ilustrátor': 3})),

        # --- Znalosti a dovednosti ---
        _p2('UME', 'Kterou dovednost považujete za svou nejsilnější?',
            ('Improvizace a pohotové reakce před publikem', {'Herec': 3}),
            ('Vedení lidí a práce s vizí', {'Režisér': 3}),
            ('Hra na hudební nástroj nebo zpěv', {'Hudebník': 3}),
            ('Práce v Adobe Illustratoru nebo Photoshopu', {'Grafik': 3})),

        _p2('UME', 'Co ze školy zvládáte nejlépe?',
            ('Focení a úpravu fotek na počítači', {'Fotograf': 3}),
            ('Psaní slohových prací a esejí', {'Spisovatel': 3}),
            ('Natáčení a stříhání videí', {'Kameraman': 3}),
            ('Kreslení a malování', {'Ilustrátor': 3})),

        _p2('UME', 'Která technická znalost je vám nejbližší?',
            ('Práce s Lightroom a postprodukce fotek', {'Fotograf': 4}),
            ('Sazba a typografie v InDesignu', {'Grafik': 3}),
            ('Kompozice záběru a práce s ohniskovou vzdáleností', {'Kameraman': 3}),
            ('Digitální kresba v Procreate nebo Clip Studiu', {'Ilustrátor': 3})),

        _p2('UME', 'Co považujete za klíčovou dovednost režiséra?',
            ('Schopnost komunikovat vizi hercům', {'Režisér': 4}),
            ('Znalost filmového střihu a postprodukce', {'Režisér': 3, 'Kameraman': 2}),
            ('Cit pro dramaturgii a příběh', {'Režisér': 3, 'Spisovatel': 2}),
            ('Technické znalosti kamery a světla', {'Kameraman': 3})),

        _p2('UME', 'Která dovednost je pro grafika nejdůležitější?',
            ('Cit pro barvy a kompozici', {'Grafik': 4}),
            ('Znalost tiskovin a pre-pressu', {'Grafik': 3}),
            ('Práce s vektory a logotypy', {'Grafik': 3}),
            ('Ilustrační dovednosti pro doplnění návrhů', {'Ilustrátor': 3})),

        _p2('UME', 'Co musí zvládnout dobrý fotograf?',
            ('Ovládání manuálního režimu a expozice', {'Fotograf': 4}),
            ('Práci se světlem ve studiu i v exteriéru', {'Fotograf': 3}),
            ('Komunikaci s fotografovanými lidmi', {'Fotograf': 3, 'Herec': 2}),
            ('Kompozici a práci s hloubkou ostrosti', {'Fotograf': 3, 'Kameraman': 2})),

        _p2('UME', 'Kterou spisovatelskou dovednost považujete za stěžejní?',
            ('Budování postav a dialogů', {'Spisovatel': 4}),
            ('Zvládnutí struktury příběhu a zápletky', {'Spisovatel': 3}),
            ('Novinářský styl a objektivitu', {'Spisovatel': 3}),
            ('Redigování a jazykovou korekturu', {'Spisovatel': 3})),

        _p2('UME', 'Jakou dovednost potřebuje kameraman nejvíce?',
            ('Plynulé vedení kamery a stabilitu záběru', {'Kameraman': 4}),
            ('Práci se stativem, gimbalem a steadicamem', {'Kameraman': 3}),
            ('Znalost filmového osvětlení a světelných schémat', {'Kameraman': 3}),
            ('Spolupráci s režisérem na vizuálním stylu', {'Kameraman': 3, 'Režisér': 2})),

        # --- Pracovní prostředí a styl ---
        _p2('UME', 'Kde byste nejraději pracovali?',
            ('Na divadelním jevišti pod reflektory', {'Herec': 3}),
            ('Ve filmovém studiu u střižny', {'Režisér': 3}),
            ('V koncertním sále s orchestrem', {'Hudebník': 3}),
            ('V designovém ateliéru u monitoru', {'Grafik': 3})),

        _p2('UME', 'Jaké pracovní prostředí vám vyhovuje?',
            ('Fotografický ateliér se studiovou výbavou', {'Fotograf': 3}),
            ('Klidná pracovna s knihami a notebookem', {'Spisovatel': 3}),
            ('Filmový set s kamerovým jeřábem', {'Kameraman': 3}),
            ('Kreslířský stůl s tablety a fixy', {'Ilustrátor': 3})),

        _p2('UME', 'Jak vypadá váš ideální pracovní den?',
            ('Zkouška divadelní hry od rána do odpoledne', {'Herec': 3}),
            ('Celý den v postprodukci – stříhám a ladím film', {'Režisér': 3, 'Kameraman': 2}),
            ('Cvičím nové skladby a připravuji se na koncert', {'Hudebník': 3}),
            ('Kreslím ilustrace ke knize s termínem za měsíc', {'Ilustrátor': 3})),

        _p2('UME', 'V jakém rytmu chcete pracovat?',
            ('Intenzivní zkoušky, pak premiéra – cyklicky', {'Herec': 3, 'Režisér': 2}),
            ('Pravidelné focení zakázek pro klienty', {'Fotograf': 3}),
            ('Dlouhodobé soustředěné psaní s deadlinem', {'Spisovatel': 3}),
            ('Práce na grafických projektech v agentuře', {'Grafik': 3})),

        _p2('UME', 'Jakou formu spolupráce preferujete?',
            ('Soubor herců, kde se vzájemně inspirujeme', {'Herec': 3}),
            ('Vedu kreativní tým a rozhoduji o směru', {'Režisér': 4}),
            ('Hraji v kapele nebo orchestru', {'Hudebník': 3}),
            ('Pracuji sám a dodávám hotové ilustrace', {'Ilustrátor': 3})),

        _p2('UME', 'Co vás motivuje v kreativní práci?',
            ('Potlesk a okamžitá reakce publika', {'Herec': 4}),
            ('Vidět hotový film na plátně kina', {'Režisér': 3, 'Kameraman': 2}),
            ('Slyšet svou skladbu v rádiu', {'Hudebník': 3}),
            ('Vidět svou ilustraci vytištěnou v knize', {'Ilustrátor': 3})),

        _p2('UME', 'Kde chcete představit svou práci?',
            ('Na vernisáži v galerii', {'Fotograf': 3, 'Ilustrátor': 2}),
            ('Na filmovém festivalu', {'Režisér': 3, 'Kameraman': 2}),
            ('Na knižním veletrhu', {'Spisovatel': 3, 'Ilustrátor': 2}),
            ('Na designové konferenci', {'Grafik': 3})),

        # --- Situační otázky ---
        _p2('UME', 'Kamarád vás požádá o pomoc s jeho krátkým filmem. Co uděláte?',
            ('Zahraji roli, kterou mi nabídne', {'Herec': 3}),
            ('Převezmu režii a postarám se o celek', {'Režisér': 3}),
            ('Natočím to jako kameraman', {'Kameraman': 3}),
            ('Napíšu nebo upravím scénář', {'Spisovatel': 3})),

        _p2('UME', 'Škola pořádá talent show. Jak se zapojíte?',
            ('Vystoupím s hereckou scénkou nebo monologem', {'Herec': 3}),
            ('Zahraji na hudební nástroj nebo zazpívám', {'Hudebník': 3}),
            ('Nafotím oficiální fotodokumentaci akce', {'Fotograf': 3}),
            ('Navrhnu plakát a grafiku pro sociální sítě', {'Grafik': 3})),

        _p2('UME', 'Dostanete nabídku pracovat na muzikálu. Jakou roli zvolíte?',
            ('Zpívající a tančící herec na scéně', {'Herec': 3, 'Hudebník': 2}),
            ('Režisér celého muzikálu', {'Režisér': 4}),
            ('Hudební aranžér a dirigent orchestru', {'Hudebník': 4}),
            ('Grafik propagačních materiálů', {'Grafik': 3})),

        _p2('UME', 'Máte den volna a chuť tvořit. Co uděláte?',
            ('Vyjdu ven a budu fotografovat město', {'Fotograf': 3}),
            ('Sednu si a budu psát povídku', {'Spisovatel': 3}),
            ('Vezmu kameru a natočím mini-dokument', {'Kameraman': 3}),
            ('Otevřu skicák a budu kreslit', {'Ilustrátor': 3})),

        _p2('UME', 'Místní divadlo hledá posily. Čím přispějete?',
            ('Přidám se do hereckého souboru', {'Herec': 3}),
            ('Nabídnu se jako asistent režie', {'Režisér': 3}),
            ('Navrhnu scénografii a plakáty', {'Grafik': 3, 'Ilustrátor': 2}),
            ('Složím hudbu pro inscenaci', {'Hudebník': 3})),

        _p2('UME', 'Máte vytvořit obsah pro YouTube kanál. Co natočíte?',
            ('Herecké skečky a komediální videa', {'Herec': 3}),
            ('Režírovaný krátký film s příběhem', {'Režisér': 3}),
            ('Vizuálně propracované záběry přírody', {'Kameraman': 4}),
            ('Návody na digitální ilustraci', {'Ilustrátor': 3})),

        _p2('UME', 'Firma chce nový brand. Co na tom uděláte?',
            ('Navrhnu celou vizuální identitu a logo', {'Grafik': 4}),
            ('Nafotím produktové a lifestylové fotky', {'Fotograf': 3}),
            ('Napíšu brand story a texty na web', {'Spisovatel': 3}),
            ('Nakreslím maskota a ilustrace pro brand', {'Ilustrátor': 3})),

        _p2('UME', 'Přítel vydává svou první knihu a prosí vás o pomoc. Co uděláte?',
            ('Pomohu s redigováním a korekturou textu', {'Spisovatel': 3}),
            ('Navrhnu obálku a grafickou úpravu', {'Grafik': 3}),
            ('Nakreslím ilustrace ke kapitolám', {'Ilustrátor': 4}),
            ('Nafotím autorský portrét a fotky na křest', {'Fotograf': 3})),

        # --- Osobnostní předpoklady ---
        _p2('UME', 'Která vlastnost vás nejlépe vystihuje?',
            ('Expresivita – snadno vyjadřuji emoce', {'Herec': 3}),
            ('Vůdcovství – mám potřebu vést tým', {'Režisér': 3}),
            ('Muzikálnost – cítím rytmus a melodii', {'Hudebník': 3}),
            ('Vizuální cit – vnímám barvy a kompozici', {'Grafik': 3})),

        _p2('UME', 'Co na vás lidé nejvíce oceňují?',
            ('Fotografické oko a schopnost zachytit moment', {'Fotograf': 3}),
            ('Bohatou slovní zásobu a vyprávění', {'Spisovatel': 3}),
            ('Technický přehled a klidnou ruku', {'Kameraman': 3}),
            ('Kreativní fantazii ve vizuálním projevu', {'Ilustrátor': 3})),

        _p2('UME', 'Jak reagujete na kritiku vaší práce?',
            ('Vnímám ji jako režijní poznámku a zlepším se', {'Herec': 3, 'Režisér': 2}),
            ('Přepracuji návrh a předložím novou verzi', {'Grafik': 3}),
            ('Upravím text podle připomínek redaktora', {'Spisovatel': 3}),
            ('Přefotím nebo překreslím dílo', {'Fotograf': 3, 'Ilustrátor': 2})),

        _p2('UME', 'Co vás nejvíce nabíjí energií?',
            ('Živé vystoupení před plným sálem', {'Herec': 3, 'Hudebník': 2}),
            ('Když se podaří zachytit dokonalý záběr', {'Kameraman': 3, 'Fotograf': 2}),
            ('Když čtenáři ocení můj text', {'Spisovatel': 3}),
            ('Hotový vizuální návrh, který sedí', {'Grafik': 3})),

        _p2('UME', 'Jak přistupujete k novým projektům?',
            ('Ponořím se do postavy a studuji ji', {'Herec': 3}),
            ('Nejdřív vytvořím moodboard a koncept', {'Režisér': 3, 'Grafik': 2}),
            ('Hledám hudební inspiraci a motiv', {'Hudebník': 3}),
            ('Skicuji návrhy na papír', {'Ilustrátor': 3})),

        _p2('UME', 'Co děláte ve volném čase nejčastěji?',
            ('Chodím na výstavy fotografií a do galerií', {'Fotograf': 3}),
            ('Čtu knihy a píšu si deník', {'Spisovatel': 3}),
            ('Sleduji filmy a analyzuji práci kamery', {'Kameraman': 3}),
            ('Kreslím si pro radost do skicáků', {'Ilustrátor': 3})),

        _p2('UME', 'Jaký typ intelligence je u vás dominantní?',
            ('Interpersonální – rozumím emocím druhých', {'Herec': 3, 'Režisér': 2}),
            ('Hudební – mám absolutní nebo relativní sluch', {'Hudebník': 4}),
            ('Vizuálně-prostorová – vnímám tvary a prostor', {'Grafik': 3, 'Ilustrátor': 2}),
            ('Verbálně-lingvistická – miluji slova', {'Spisovatel': 4})),

        # --- Oborové scénáře ---
        _p2('UME', 'Režisér zruší vaši scénu těsně před premiérou. Jak zareagujete?',
            ('Profesionálně to přijmu – jsem herec, to se stává', {'Herec': 3}),
            ('Navrhneme režisérovi alternativní řešení', {'Režisér': 3}),
            ('Nabídnu, že scénu natočím jako bonus video', {'Kameraman': 3}),
            ('Přepíšu scénář, aby fungoval i bez té scény', {'Spisovatel': 3})),

        _p2('UME', 'Klient odmítne váš grafický návrh. Co uděláte?',
            ('Zjistím důvody a vytvořím novou variantu', {'Grafik': 4}),
            ('Nafotím referenční mood fotky pro klienta', {'Fotograf': 3}),
            ('Nakreslím hand-drawn alternativu', {'Ilustrátor': 3}),
            ('Navrhnu, ať si to klient popíše slovy, a já to přeložím', {'Spisovatel': 3})),

        _p2('UME', 'Kapela se neshodne na repertoáru pro koncert. Jak vyřešíte situaci?',
            ('Navrhneme kompromis jako muzikant s přehledem', {'Hudebník': 4}),
            ('Převezmu vedení jako kapelník a rozhodnu', {'Režisér': 3}),
            ('Napíšu dramaturgii koncertu s příběhem', {'Spisovatel': 3}),
            ('Navrhnu vizuální koncept, který propojí různé styly', {'Grafik': 3})),

        _p2('UME', 'Na natáčení selže hlavní osvětlení. Co uděláte?',
            ('Improvizuji se záběry v přirozeném světle', {'Kameraman': 4}),
            ('Jako režisér přizpůsobím scénu podmínkám', {'Režisér': 3}),
            ('Vyfotím backstage dokumentaci vzniklé situace', {'Fotograf': 3}),
            ('Zahraji scénu tak, aby nevyžadovala složité světlo', {'Herec': 3})),

        _p2('UME', 'Nakladatel vrátí váš rukopis s poznámkami. Jak budete reagovat?',
            ('Přepracuji text podle připomínek a odevzdám znovu', {'Spisovatel': 4}),
            ('Navrhnu nové ilustrace, které text oživí', {'Ilustrátor': 3}),
            ('Nabídnu jako doplněk sérii autorských fotografií', {'Fotograf': 3}),
            ('Přeměním příběh ve scénář pro audiobook s hlasy', {'Herec': 3})),

        _p2('UME', 'Galerie nabízí výstavu vaší tvorby. Co vystavíte?',
            ('Sérii portrétních fotografií', {'Fotograf': 4}),
            ('Kolekci originálních ilustrací', {'Ilustrátor': 4}),
            ('Grafické plakáty a vizuální identity', {'Grafik': 3}),
            ('Video-art instalaci z mých natáčení', {'Kameraman': 3})),

        _p2('UME', 'Startup potřebuje kompletní vizuální identitu. Co zajistíte?',
            ('Logo, barvy, typografii a brand manuál', {'Grafik': 4}),
            ('Produktové a lifestyle fotky', {'Fotograf': 3}),
            ('Ilustrace a ikony pro webové stránky', {'Ilustrátor': 3}),
            ('Reklamní video a promo spot', {'Kameraman': 3, 'Režisér': 2})),

        _p2('UME', 'Město vypisuje soutěž na kulturní plakát. Jak se zapojíte?',
            ('Navrhnu moderní grafický plakát', {'Grafik': 4}),
            ('Nakreslím autorský ilustrovaný plakát', {'Ilustrátor': 4}),
            ('Nafotím uměleckou fotografii jako základ plakátu', {'Fotograf': 3}),
            ('Napíšu textový koncept a slogan', {'Spisovatel': 3})),

        # --- Nástroje a technologie ---
        _p2('UME', 'Který software je vám nejbližší?',
            ('Adobe Illustrator a InDesign', {'Grafik': 4}),
            ('Adobe Lightroom a Capture One', {'Fotograf': 4}),
            ('DaVinci Resolve nebo Premiere Pro', {'Kameraman': 3, 'Režisér': 2}),
            ('Procreate nebo Clip Studio Paint', {'Ilustrátor': 4})),

        _p2('UME', 'Jaký nástroj používáte nejčastěji?',
            ('Pero a papír pro psaní poznámek a textů', {'Spisovatel': 3}),
            ('Fotoaparát s výměnnými objektivy', {'Fotograf': 3}),
            ('Grafický tablet Wacom nebo iPad', {'Ilustrátor': 3, 'Grafik': 2}),
            ('Hudební nástroj nebo MIDI klávesy', {'Hudebník': 3})),

        _p2('UME', 'Jaký program se chcete naučit?',
            ('Final Cut Pro pro střih videí', {'Režisér': 3, 'Kameraman': 2}),
            ('Ableton Live nebo Logic Pro pro hudbu', {'Hudebník': 4}),
            ('Figma nebo Sketch pro UI/UX design', {'Grafik': 3}),
            ('Scrivener nebo Ulysses pro psaní knih', {'Spisovatel': 3})),

        _p2('UME', 'Jaké příslušenství byste si koupili jako první?',
            ('Kvalitní mikrofon pro nahrávání hlasu', {'Herec': 3, 'Hudebník': 2}),
            ('Objektiv s pevným ohniskem 50 mm', {'Fotograf': 3}),
            ('Stabilizátor kamery – gimbal', {'Kameraman': 3}),
            ('Profesionální sadu Copic fixů', {'Ilustrátor': 3})),

        # --- Vzdělávání a rozvoj ---
        _p2('UME', 'Jaký kurz byste si zapsali?',
            ('Herecký seminář a výrazový projev', {'Herec': 3}),
            ('Filmová režie a scenáristika', {'Režisér': 3}),
            ('Kompozice a hudební teorie', {'Hudebník': 3}),
            ('Grafický design a vizuální komunikace', {'Grafik': 3})),

        _p2('UME', 'Na jakou vysokou školu byste se hlásili?',
            ('DAMU – herectví', {'Herec': 4}),
            ('FAMU – režie nebo kamera', {'Režisér': 3, 'Kameraman': 2}),
            ('JAMU – hudební interpretace', {'Hudebník': 4}),
            ('UMPRUM – grafický design nebo ilustrace', {'Grafik': 3, 'Ilustrátor': 2})),

        _p2('UME', 'Který workshop vás nejvíce zajímá?',
            ('Fotografický workshop portrétu a světla', {'Fotograf': 3}),
            ('Kreativní psaní a storytelling', {'Spisovatel': 3}),
            ('Filmová kamera a cinematografie', {'Kameraman': 3}),
            ('Digitální ilustrace a character design', {'Ilustrátor': 3})),

        _p2('UME', 'Co byste studovali na zahraničním pobytu?',
            ('Metodu herectví u Lee Strasberga v New Yorku', {'Herec': 4}),
            ('Filmovou režii na londýnské filmové škole', {'Režisér': 4}),
            ('Jazz a improvizaci na Berklee College of Music', {'Hudebník': 4}),
            ('Ilustraci na Royal College of Art', {'Ilustrátor': 4})),

        # --- Preference a hodnoty ---
        _p2('UME', 'Co je pro vás v práci nejdůležitější?',
            ('Možnost vyjádřit se a být na scéně', {'Herec': 3}),
            ('Tvůrčí svoboda a vlastní vize', {'Režisér': 3}),
            ('Dokonalý zvuk a hudební kvalita', {'Hudebník': 3}),
            ('Esteticky čistý a funkční design', {'Grafik': 3})),

        _p2('UME', 'Jakou hodnotu chcete předávat svou prací?',
            ('Zachytit krásu všedního dne fotograficky', {'Fotograf': 3}),
            ('Vyprávět příběhy, které pohnou čtenáři srdcem', {'Spisovatel': 3}),
            ('Vizuálně zaujmout diváka filmovým obrazem', {'Kameraman': 3}),
            ('Vdechnout fantazii do ilustrací pro děti', {'Ilustrátor': 3})),

        _p2('UME', 'Co vás na umění fascinuje nejvíce?',
            ('Proměna herce v úplně jinou osobu', {'Herec': 3}),
            ('Propojení všech uměleckých složek ve filmu', {'Režisér': 3}),
            ('Emoce, které dokáže vyvolat hudba', {'Hudebník': 3}),
            ('Síla jednoduchého grafického symbolu', {'Grafik': 3})),

        _p2('UME', 'Jaký typ projektu preferujete?',
            ('Dlouhodobý – celovečerní film nebo seriál', {'Režisér': 3, 'Kameraman': 2}),
            ('Střednědobý – sérii fotografií nebo ilustrací', {'Fotograf': 3, 'Ilustrátor': 2}),
            ('Krátkodobý – logo nebo plakát', {'Grafik': 3}),
            ('Jednorázový – báseň nebo píseň', {'Spisovatel': 3, 'Hudebník': 2})),

        _p2('UME', 'Jak chcete být za svou práci odměněni?',
            ('Uznáním publika a kritiků', {'Herec': 3, 'Režisér': 2}),
            ('Hudební cenou a gramofónkem', {'Hudebník': 3}),
            ('Publikací fotek v prestižním magazínu', {'Fotograf': 3}),
            ('Literární cenou za nejlepší knihu roku', {'Spisovatel': 3})),

        # --- Specializace a zaměření ---
        _p2('UME', 'V jaké oblasti fotografie byste se specializovali?',
            ('Portrétní fotografie', {'Fotograf': 4}),
            ('Reportážní a dokumentární fotografie', {'Fotograf': 3}),
            ('Produktová a reklamní fotografie', {'Fotograf': 3, 'Grafik': 2}),
            ('Krajinářská a cestovatelská fotografie', {'Fotograf': 3})),

        _p2('UME', 'Jaký žánr literatury byste psali?',
            ('Romány a beletrii', {'Spisovatel': 4}),
            ('Scénáře pro film a televizi', {'Spisovatel': 3, 'Režisér': 2}),
            ('Žurnalistiku a reportáže', {'Spisovatel': 3}),
            ('Poezii a songy', {'Spisovatel': 3, 'Hudebník': 2})),

        _p2('UME', 'Jaký hudební žánr je vám nejbližší?',
            ('Klasická hudba a orchestrální tvorba', {'Hudebník': 4}),
            ('Rock, pop nebo elektronická hudba', {'Hudebník': 3}),
            ('Jazz a improvizace', {'Hudebník': 3}),
            ('Filmová hudba a soundtracky', {'Hudebník': 3, 'Režisér': 2})),

        _p2('UME', 'Jaký typ ilustrace vás láká?',
            ('Knižní ilustrace pro děti', {'Ilustrátor': 4}),
            ('Komiksová tvorba a grafické novely', {'Ilustrátor': 3}),
            ('Editorial a novinové ilustrace', {'Ilustrátor': 3}),
            ('Concept art pro hry a filmy', {'Ilustrátor': 3, 'Grafik': 2})),

        _p2('UME', 'Jaký typ herectví preferujete?',
            ('Činohra a dramatické role', {'Herec': 4}),
            ('Komedie a improvizace', {'Herec': 3}),
            ('Filmové a televizní herectví', {'Herec': 3}),
            ('Dabování a hlasová tvorba', {'Herec': 3})),

        _p2('UME', 'V jaké oblasti grafického designu chcete pracovat?',
            ('Branding a firemní identita', {'Grafik': 4}),
            ('Webdesign a UX/UI', {'Grafik': 3}),
            ('Obalový a produktový design', {'Grafik': 3}),
            ('Motion design a animace', {'Grafik': 3, 'Kameraman': 2})),

        _p2('UME', 'Jakou režijní specializaci byste zvolili?',
            ('Celovečerní hrané filmy', {'Režisér': 4}),
            ('Dokumentární filmy', {'Režisér': 3, 'Kameraman': 2}),
            ('Divadelní režie', {'Režisér': 3}),
            ('Reklamní a komerční produkce', {'Režisér': 3})),

        # --- Spolupráce a komunikace ---
        _p2('UME', 'Jak komunikujete svou kreativní vizi ostatním?',
            ('Předvedu to – zahraji nebo přečtu nahlas', {'Herec': 3}),
            ('Nakreslím storyboard nebo skicu', {'Režisér': 3, 'Ilustrátor': 2}),
            ('Zahraji melodii nebo ukázku na nástroj', {'Hudebník': 3}),
            ('Připravím grafický moodboard', {'Grafik': 3})),

        _p2('UME', 'Jak řešíte kreativní neshodu v týmu?',
            ('Navrhnu kompromis s respektem k oběma vizím', {'Režisér': 3}),
            ('Vytvořím alternativní verze návrhu', {'Grafik': 3}),
            ('Napíšu několik variant textu na výběr', {'Spisovatel': 3}),
            ('Nafotím různé pohledy a nechám vybrat', {'Fotograf': 3})),

        _p2('UME', 'Jak přistupujete ke spolupráci s klientem?',
            ('Osobně prezentuji návrhy a vysvětluji koncept', {'Grafik': 3}),
            ('Posílám ukázky fotografií a čekám zpětnou vazbu', {'Fotograf': 3}),
            ('Napíšu detailní brief a nechám si jej odsouhlasit', {'Spisovatel': 3}),
            ('Natočím krátkou video-ukázku stylu', {'Kameraman': 3})),

        _p2('UME', 'Jak byste spolupracovali s herci na natáčení?',
            ('Jako kolega herec – motivujeme se navzájem', {'Herec': 3}),
            ('Jako režisér – vedu je k nejlepšímu výkonu', {'Režisér': 4}),
            ('Jako kameraman – hledám nejlepší úhel pro jejich projev', {'Kameraman': 3}),
            ('Jako fotograf – zachytím emoce v portrétech', {'Fotograf': 3})),

        # --- Komplexní rozhodování ---
        _p2('UME', 'Neziskovka chce propagační kampaň zdarma. Jak pomůžete?',
            ('Natočím pro ně krátký dokumentární film', {'Kameraman': 3, 'Režisér': 2}),
            ('Navrhnu jim logo a grafické materiály', {'Grafik': 4}),
            ('Nafotím reportáž z jejich činnosti', {'Fotograf': 3}),
            ('Napíšu tiskové zprávy a texty na web', {'Spisovatel': 3})),

        _p2('UME', 'Kulturní centrum chce oživit svůj program. Co navrhnete?',
            ('Sérii divadelních představení a open mic', {'Herec': 3, 'Režisér': 2}),
            ('Cyklus koncertů místních kapel', {'Hudebník': 3}),
            ('Fotografickou výstavu místních umělců', {'Fotograf': 3}),
            ('Kreativní dílny kreslení a ilustrace', {'Ilustrátor': 3})),

        _p2('UME', 'Máte rozpočet na jeden umělecký projekt. Co zrealizujete?',
            ('Natočím krátký film s vlastním scénářem', {'Režisér': 3, 'Spisovatel': 2}),
            ('Vydám album vlastních skladeb', {'Hudebník': 4}),
            ('Uspořádám autorskou výstavu fotografií', {'Fotograf': 3}),
            ('Vydám ilustrovanou knihu pohádek', {'Ilustrátor': 3, 'Spisovatel': 2})),

        _p2('UME', 'Zahraniční festival přijal váš projekt. O jaký jde?',
            ('Divadelní inscenace, kde hraji hlavní roli', {'Herec': 4}),
            ('Krátký film, který jsem režíroval/a', {'Režisér': 4}),
            ('Hudební kompozice pro komorní soubor', {'Hudebník': 4}),
            ('Sérii grafických plakátů na téma svoboda', {'Grafik': 3, 'Ilustrátor': 2})),

        _p2('UME', 'Jaký odkaz chcete ve svém oboru zanechat?',
            ('Nezapomenutelné herecké výkony v českém filmu', {'Herec': 4}),
            ('Inovativní filmovou řeč a režijní styl', {'Režisér': 4}),
            ('Epochální fotografické dílo zachycující dobu', {'Fotograf': 4}),
            ('Knihy, které změní pohled čtenářů na svět', {'Spisovatel': 4})),

        _p2('UME', 'Váš umělecký projekt získal grant. Na co ho využijete?',
            ('Natočím celovečerní dokumentární film', {'Kameraman': 3, 'Režisér': 2}),
            ('Nahraji album v profesionálním studiu', {'Hudebník': 4}),
            ('Vytvořím sérii velkoformátových ilustrací', {'Ilustrátor': 4}),
            ('Vydám sbírku esejů a reportáží', {'Spisovatel': 3})),

        _p2('UME', 'Jak byste propagovali české umění v zahraničí?',
            ('Turné s českými divadelními hrami', {'Herec': 3, 'Režisér': 2}),
            ('Koncertním turné s českou hudbou', {'Hudebník': 3}),
            ('Putovní výstavou české fotografie a ilustrace', {'Fotograf': 3, 'Ilustrátor': 2}),
            ('Překlady české literatury a antologiemi', {'Spisovatel': 4})),

        _p2('UME', 'Na čem byste pracovali, kdybyste měli neomezený čas?',
            ('Trilogie románů o české historii', {'Spisovatel': 4}),
            ('Animovaný film s vlastními ilustracemi', {'Ilustrátor': 3, 'Režisér': 2}),
            ('Symfonie inspirovaná českou krajinou', {'Hudebník': 4}),
            ('Celoživotní fotografický projekt – lidé mého města', {'Fotograf': 4})),

        _p2('UME', 'Jakou cenu byste chtěli jednou získat?',
            ('Cenu Thálie za herecký výkon', {'Herec': 4}),
            ('Českého lva za nejlepší režii', {'Režisér': 4}),
            ('Grammy nebo Anděla za hudební album', {'Hudebník': 4}),
            ('World Press Photo nebo Czech Press Photo', {'Fotograf': 4})),

        _p2('UME', 'Jak byste využili umělou inteligenci ve své práci?',
            ('Jako inspiraci pro grafické koncepty a varianty', {'Grafik': 3}),
            ('Pro generování nápadů na příběhy a zápletky', {'Spisovatel': 3}),
            ('Pro úpravu a kolorování ilustrací', {'Ilustrátor': 3}),
            ('Pro analýzu záběrů a barevné korekce ve filmu', {'Kameraman': 3, 'Režisér': 2})),
    ]