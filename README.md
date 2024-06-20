# CHAT_RPG_GAME



zadani chatgpt4o
```
# chatgpt_game_basics


tento chat se bude jmenovat vytvoreni chat rpg 

nyni bych chtel aby ses choval jako senior programator se znalosti ML, AI, DevOps, frontendu, architektury a analyzy

chtel bych abys mi rekl jak si mohu naprogramovat RPG hru, bezici na nejakem chatovacim languge modelu, kde by se i generoval obrazek postavy pri tvorbe, kde by bylo mozno zadavat povely hlasem a v pripade potreby by mi to vygenerovalo obrazek mapy rozdelene na ctverce o prumeru 2.5cm ktere by pasovaly do pribehu.

porad mi jak na to
chci to programovat v pythonu nechci pouzivat jupyter notebook
vse musi jet v dockeru a pipenvu (venv), githubu
chci tam mit pipelinu na merge request ktera bude spoustet me testy v pytestu
chci tam mit pycoverage, trivy, ruff linter

chci tam mit databazi, nejlepe asi graphql
chci tam mit graphanu a node exporter, kibanu, elastik search,
chci aby to jelo v google cloud
chci aby to pouzivalo kubetnetes
chci mit rozlehlou databazi

chci aby prvni veci kterou chat udela, bude ze se zepta na to zda chci hrat medieval
medieval fantasy
medieval fantasy post apocalyptic
medieval fantasy post apocalyptic zombie

pak podle toho se ptal dale a vytvoril s pomoci voleb hrace postavu
dle pravidel Shadowrun 20th aniversary edition

pak aby vytvoril fotku postavy - na to pouzil free generator

 
aby se tam takto zobrazoval herni cas, 
misto kde se to konna
co bylo posledni zadani od uzivatele
kolik ma postava zdravi
kolik ma postava penez
u bojovych situaci se zobrazi iniciativa
v pripade ze bude mit mazlicky/follovery/familiary ci bude s nejakym putovat mu zde i vypises jejich jmena (pokud pujde o skupinu, pak nazev skupiny)

takto by mel vypadat zakladni prehled na zacatku kazde tve odpovedi po vytvoreni postavy a zapoceti hrani s touto postavou:
[📅 Day 1, ⌚ 09:50 AM, 📌 Dense Forest Clearing, 🎯 Gathering Intelligence, ❤️ 10/20, 💎 40]

kurzivou budes psat co se deje na zacatku, hned po zakladnim prehledu
    priklad:
```
<kurziva>
You decide to gather more information by talking to other survivors in the square. You approach a small group huddled around a fire, their faces illuminated by the flickering flames. They look up as you come closer, a mix of curiosity and caution in their eyes.</kurziva>
```

tuto ikonku budes pouzivat pro primou rec pro NPC:
🗣️
    priklad:
```
<kurziva>
An older woman with a kind but tired face nods. </kurziva> "I'm Maria. We've been here for a few days now. The guards control most of the supplies, but some of us have managed to scavenge a few things. It's not safe out there, though. The streets are crawling with danger."
```
tuto ikonku budes pouzivat pro primou rec postavy
💬
    priklad:
```
"Hey, everyone. I'm Šakal. Just trying to get a sense of the situation here and see if there's anything we can do to help each other," you say, offering a friendly smile.
```
Pokud se postava bude predstavovat, tak bude pouzivat sve jmeno, paklize nezada jinak - viz
"Šakal" v predchozim prikladu

bude mozne zadavat uzivatelem input hlasem
kdykoliv si uzivatel muze rici a vypises mu cely denik postavy, kde bude:
Jmeno "prezdivka" Prijmeni/odkud je u slechtickeho titulu/povolani jeho otce

po te muze na vyzvani vygenerovat mapu oblasti
a nabidnout mozne dalsi kroky jako zde v prikladu:
```
<kurziva>
With this new information, you have a few options to consider:</kurziva>
<one line withouth text>

    1. <kurziva>Investigate the alleyway leading to the old store for supplies.</kurziva>
    2. <kurziva>Try to trade with the guards for supplies.</kurziva>
    3. <kurziva>Search for the hidden stash in the subway tunnels.</kurziva>
    4. <kurziva>Explore the abandoned buildings near the edge of the city.</kurziva>
```
nyni jen odpovez OK, pokud rozumis a mas ulozeno v pameti a cekej na dalsi pokyny


zadani 2:



Dekuji, jde o ucebni projekt do meho portfolia na novou pozici.

Backend:
rad bych pouzil fastapi
rad bych pouzil graphql Postgresql
melo by to jet na google cloud nebo aws free (mam free account ale nevyznam se do jake miry je free) verzi kde nebudu nic platit

Generování Obrázků:
ktery je absolutne free, ktery z free je nejlepsi na kvalitu vystupnich obrazku dle zadani
ktery z nich je nejrychlejsi
muzes mi vsechny tyto ohodnotit dle techto kriteriii, abych se mohl lepe rozhodnout?

Rozpoznávání Hlasu:
chci pouzit free navrhni mi jake jsou moznostia neomezuj se jen na Mozilla DeepSpeech, zase chci hodnoceni kvality vystupu smerem do kodu (detekce a zpracovani) stejne take jako hodnoceni rychlosti

Monitoring a Nasazování:
vse mi pripada OK

CI/CD:
vse mi pripada OK

Celková Architektura
Komponenty
vse ok, ale s prihlednutim na to co jsem psal vyse

Proces:
na zacatek je nutno dat bod inicializace a instalace:
zde bude pouzit pipenv a jak nainstalovat vsechny knihovny

pokud neni google cloud uplne free, pak prosim pouzit aws

Free resources se budou odvijet od analyzy pouzitelnosti na zacatku a tom co si zvolim

je nutno i zahrnout krok vytvoreni promptu pro samotnou hru a take vytvoreni "herniho menu" ktere jsem definoval nahore a deniku postavy ktery by byl dostupny na pozadani hracem - chat jej vypise

    zde uvazuji o tom ze by denik se mohl stahnout jako pdf

navrhni mi jak natrenovat model aby se ridil pravidly Shadowrun 20th aniversary, jelikoz ne kazdy model umi pracovat s jeho bodovym systemem tvorby postavy

do budoucna chci i automaticke vytvareni backgroundu postavy, vcetne lepsi definice ras, to chci take tento chatter naucit


zadani 3:

k bodu backendu:
budu potrebovat aby to jelo s ORM

Generování Obrázků:
pouzijeme Stable Diffusion, abych si to mohl zkouset i na lokale 
rovnez umoznime uzivatelum si celou apku nainstalovat na locale

Rozpoznávání Hlasu:
pouzijeme Mozilla DeepSpeech

zacneme s konfiguraci a instalacemi


zadani:
vratme se k tomuto bodu:
Trénink Modelu na Shadowrun 20th Anniversary

Shromažďuj data specifická pro pravidla Shadowrun 20th Anniversary.
co tim minis?

zadani:

porad mi model kteremu dam pdf s pravidly a on mi udela prompty ktere mohu pouzit pri tvorbe postavy

zadani:

chci mit v mem projektu podprogram ktery mi umozni pri potrebe a instalaci vytrenovat dle promptu ziskanych z nejakeho modelu...

nejdrive mi ale porovnej kvalitu vystupu, zda je free, jak je rychly u mnoha modelu z hugging face, NLP, PDF to text Conversion...

pocitej ze cele pdf ma obrazky a 368 stran, budu vsak pro zacatek potrebovat jen nektere stranky

Spacy potrebuje trenink pro jake ulohy?
pokud bych chtel jen grabnout text?
dokazal by mi jej prevezt napriklad do databaze s graphql?

ktery z techto navrhu dokaze spracovat takove mnozstvi informaci?

Zpracování Velkého PDF a Extrakce Textu
nyni ale prosim o to abys mi navrhl aby tento load dat byl v rozumne strukture umisten v mem tree

navrhni mi novou souborovou strukturu ktera bude myslet na to ze nakonec mozna budu potrebovat vicero databazi, nebo budou mit spoustu tabulek

je nutno odlisit tento data loader od ostatniho kodu ale nejspise bude pri instalaci potreba a v pripade ztraty dat, nebo dodelavani novych feature

sla by tato struktura?

tree
.
├── backend
│   └── app
│       ├── crud.py
│       ├── database.py
│       ├── data_loader
│       │   ├── __init__.py
│       │   ├── insert_data.py
│       │   ├── load_data.py
│       │   ├── pdf_to_text.py
│       │   └── process_text.py
│       ├── deps.py
│       ├── graphql
│       │   ├── __init__.py
│       │   └── schema.py
│       ├── __init__.py
│       ├── main.py
│       ├── menu.py
│       ├── models.py
│       ├── prompt.py
│       └── schemas.py
├── Chat_RPG_Game.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── requires.txt
│   ├── SOURCES.txt
│   └── top_level.txt
├── docker-compose.yaml
├── Dockerfile
├── Pipfile
├── Pipfile.lock
├── README.md
├── setup.py
└── tests
    └── __init__.py

6 directories, 28 files

je tam spravny naming?

udelej mi code review kodu co jsem ti uploadnul a
ved mne dal
nezapomen na testy
po kazdem kdoku chci si overit ze to co mam nove mi jede


```