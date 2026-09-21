# sauceDemo
1. Stworzyć plik do autoodpalania skryptów 
2. Podstawowy test -> pytest -> parametryzacjja ->AI -> POM

++++++++++++++++++++++++

Testy:
1. logoawanie
2. Hamburger przejscie do spinner 
3. dodanie 3 rzeczy
4. przejscie do koszyka i zamówienie 
5. generacja pdf 
testy obciazeniowe logowania 

+++++++++++++++++++++++++

Co instalowane:
- instalacja selenium -> pip install selenium
- instalania webdriver menager -> pip install webdriver-manager
- pytest -> pip instal pytest
- locust -> pip install -> pip install locust

+++++++++++++++++++++++++++

Locust:
locust -f locustfile.py --users 50 --spawn-rate 5 --run-time 1m --headless --html results/report.html --csv results/statsats -> włączenienie testu z user:50 
start results/report.html -> sprawdzenie wyniku