Raport z testu wydajnościowego — SauceDemo
Cel testu

Sprawdzenie zachowania aplikacji saucedemo.com pod obciążeniem 50 jednoczesnych użytkowników, przy użyciu narzędzia Locust.

Metodologia

Podczas przygotowywania testu zaobserwowano, że saucedemo.com to aplikacja typu SPA (Single Page Application) — routing stron (/inventory.html, /cart.html itd.) odbywa się po stronie klienta (JavaScript), a nie jako osobne zasoby serwowane przez backend.

Próby bezpośredniego wysyłania żądań GET/POST do tych adresów kończyły się błędami 404/405, ponieważ serwer nie obsługuje tych ścieżek jako samodzielnych endpointów — cała logika nawigacji (w tym proces logowania) jest realizowana w przeglądarce po stronie klienta.

W związku z tym, ostateczny scenariusz testu wydajnościowego ograniczono do rzeczywistego zasobu serwowanego przez backend — GET / (strona główna/logowania) — co dało wiarygodne, mierzalne wyniki reprezentujące rzeczywiste obciążenie serwera.

Parametry testu
Parametr	Wartość
Narzędzie	Locust
Plik testowy	locustfile.py
Adres docelowy	https://www.saucedemo.com
Liczba użytkowników	50
Tempo narastania (spawn rate)	5 użytkowników/s
Czas trwania testu	1 minuta
Tryb	headless
Wyniki
Statystyki żądań
Typ	Endpoint	Liczba żądań	Błędy	Średni czas (ms)	Min (ms)	Max (ms)	RPS
GET	/	1384	0	28.73	20	318	23.26

Zero błędów (0 Fails) w trakcie całego testu — serwer poprawnie obsłużył wszystkie 1384 żądania.

Czasy odpowiedzi — percentyle
Percentyl	Czas (ms)
50%	25
60%	25
70%	26
80%	28
90%	33
95%	56
99%	96
100%	320

Zdecydowana większość żądań (do 90 percentyla) mieściła się w granicach 20–33 ms. Dopiero powyżej 95 percentyla czasy zaczynają rosnąć wyraźniej, a pojedyncze skrajne przypadki (100%ile) sięgały 320 ms — co jest naturalną fluktuacją przy pracy z zewnętrznym serwerem, a nie oznaką problemu z wydajnością.

Przebieg testu w czasie
Requests per second (RPS): rósł liniowo wraz z dochodzeniem do docelowych 50 użytkowników (zgodnie ze spawn-rate = 5/s), a następnie ustabilizował się na poziomie ~23–25 RPS przez pozostałą część testu.
Response Times: na początku testu (przy narastającej liczbie użytkowników) 95. percentyl osiągał wyższe wartości (~110 ms), po czym ustabilizował się w granicach 25–35 ms, z jednym przejściowym wzrostem pod koniec testu (~55 ms).
Number of Users: liczba wirtualnych użytkowników rosła płynnie do 50, utrzymała się na tym poziomie przez cały czas trwania testu, po czym spadła do 0 wraz z jego zakończeniem.
Wnioski

Aplikacja SauceDemo poprawnie obsłużyła obciążenie 50 jednoczesnych użytkowników wykonujących żądania GET do strony głównej:

brak jakichkolwiek błędów (0 Fails na 1384 żądania),
stabilny, niski średni czas odpowiedzi (~29 ms),
brak oznak degradacji wydajności w trakcie trwania testu — RPS utrzymywał się na stałym poziomie po ustabilizowaniu liczby użytkowników.
Ograniczenia testu

Ze względu na architekturę SPA aplikacji, test objął wyłącznie żądanie GET /. Nie było możliwe bezpośrednie przetestowanie pod obciążeniem procesu logowania ani nawigacji między podstronami (/inventory.html, /cart.html), ponieważ te operacje realizowane są po stronie klienta (JavaScript), a nie jako osobne żądania HTTP do backendu. Pełne przetestowanie tych scenariuszy wymagałoby narzędzia symulującego przeglądarkę (np. w oparciu o Selenium) lub identyfikacji rzeczywistych endpointów API wykorzystywanych przez aplikację.