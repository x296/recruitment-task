# recruitment-task

Właściwe zadanie znajduje się w repozytorium recruitment-tasl/env/nba_player_stats

Uruchomienie aplikacji wymaga sklonowania repozytorium oraz uruchomienia wirtualnego środowiska. Dalsze kroki są standardowe dla projektu Django.
superuser (w razie potrzeby): 
l: admin
h: 123

Button z formularza w sekcji header nie działa, karty zawodników pobierają się po odświeżeniu strony. 

W pliku views.py są dwie metody renderu zawodników: z zapytania API i z bazy danych. Zadanie spełnia oczywiście tylko pierwsza opcja, natomiast zostawiłem drugą bo była szybsza i używałem ją podczas stylizowania.

Wykonanie zadania było moim priorytetem, zdaję sobie sprawę, że nie stosowałem się do niektórych zasad dotyczących formatowania kodu (jeszcze sobie ich nie wypracowałem), np.: 4 spacje zamiast \t, czy 79 znaków w linii - proszę o wyrozumiałość.

Sprawozdanie:
Dzień 1: nauka frameworka Django m. in. na podstawie wideo ( https://www.youtube.com/watch?v=F5mRW0jo-U4&t=3370s )
Dzień 2: Próba zastosowania wiedzy w praktyce i stworzenie pierwszej aplikacji (simple_nba_refs - porzucona ze względu na problem w umiejętnym zaplanowaniu i zastosowaniu danych z API)
Dzień 3: Przygotowanie właściwej aplikacji w oparciu o API ( https://www.balldontlie.io/ ). W trakcie również kilkukrotnie zmieniałem koncepcję, ze względu na problematyczne API.

Reasumując: 
1. Django jest super,
2. Wybrane API powinieniem zmienić na łatwiejsze, żebym nie musiał tracić czasu na obchodzenie problemów z API, a mógł skupić się na rozwijaniu właściwych umiejętności (jak można było w zwracanym obiekcie dotyczącym drużyny nie zawrzeć id graczy, któ®zy w niej grają!?),
3. Usystematyowałem wiedzę i umiejętności z zakresu CSS.

Dalsza wizja zadania:
1. Powinienem przeprojektować aplikację, aby była bardziej modułowa:
	a) funkcja index powinna znajdować się w aplikacji zajmującej się wyświetlaniem innych aplikacji (takowej nie ma obecnie, wszystkim zarządza aplikacja player),
	b) przeniesienie folderów templates oraz static do głównego folderu projektu,
	c) właściwe wykorzystanie template w django (skorzystanie z {% block content %})

ad a) rozbiłem trochę działanie aplikacji na dwa osobne widoki, ale jeszcze nie potrafię łączyć dwóch aplikacji w jednym projekcie (czy rozbicie projektu na jedną aplikację do wyświetlania contentu (roster view) i drugą generującą pojedynczy content (player) jest dobrym pomysłem?)
Zastanawiam się, czy tworząc dwie aplikacje i linkując je w urls.py mógłbym wpływać jedną na drugą, wykorzystując link...

ad b) zrozumiałem, że co innego ma wykonywać folder templates i static wewnątrz pojedynczej aplikacji, a co innego wewnątrz całego projektu, więc część plików ma być wewnątrz folderó∑ template i static aplikacji, a cześć w w/w folderach projektu.

ad c) chyba jestem już bliżej idei działania tych narzędzi.


2. Poznanie działania formularzy w django:
	a) wykorzystałbym je do zarządzania zapytaniami wysyłanymi do API i dzięki temu mógłbym przygotować bardziej rozbudowaną aplikację.
3. Bardziej ambitne wykonanie animacji/tranzycji w layuocie (w pliku css są dwie opcje: trancyzja i animacja: ta druga jest zakomentowana).

