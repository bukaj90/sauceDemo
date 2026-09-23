# 🧪 sauceDemo — Framework do automatyzacji testów E2E i wydajnościowych

Kompleksowy projekt testowy dla aplikacji [Sauce Demo](https://www.saucedemo.com/), łączący automatyzację testów funkcjonalnych (Selenium + pytest, wzorzec Page Object Model), testy wydajnościowe (Locust) oraz raportowanie wyników (Allure).

Projekt powstał jako praktyczne ćwiczenie z automatyzacji testów — od podstawowego skryptu, przez parametryzację przypadków testowych, aż po pełną strukturę POM gotową do rozwoju w środowisku produkcyjnym.

---

## 🚀 Funkcjonalności

Framework pokrywa pełną ścieżkę użytkownika w sklepie internetowym:

- ✅ **Logowanie** — walidacja poprawnych i błędnych danych logowania
- ✅ **Nawigacja** — obsługa menu bocznego (hamburger menu)
- ✅ **Dodawanie produktów** — dodanie wielu pozycji do koszyka
- ✅ **Proces zakupowy** — przejście przez koszyk i finalizacja zamówienia
- ✅ **Generowanie potwierdzenia PDF** — walidacja dokumentu wygenerowanego po zamówieniu
- ✅ **Testy obciążeniowe logowania** — symulacja wielu równoczesnych użytkowników (Locust)

Testy są sparametryzowane (pytest.mark.parametrize), co pozwala uruchamiać te same scenariusze dla różnych zestawów danych bez duplikowania kodu.

---

## 🏗️ Architektura

Projekt zbudowany jest w oparciu o wzorzec **Page Object Model (POM)**, co zapewnia:

- separację logiki testowej od logiki interakcji ze stroną,
- łatwiejsze utrzymanie testów przy zmianach w UI,
- czytelną, skalowalną strukturę kodu.

---

## 🛠️ Stack technologiczny

| Kategoria | Narzędzie |
|---|---|
| Język | Python 3.12 |
| Automatyzacja przeglądarki | Selenium + webdriver-manager |
| Framework testowy | pytest |
| Testy wydajnościowe | Locust |
| Raportowanie | Allure |
| Przeglądarka | Firefox |

---

## 📦 Instalacja

Wymagania: Python 3.12, przeglądarka Firefox.

```powershell
git clone https://github.com/bukaj90/sauceDemo.git
cd sauceDemo
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Jeśli PowerShell blokuje aktywację środowiska wirtualnego, wpisz jednorazowo:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

## ▶️ Uruchamianie testów

Z aktywnym środowiskiem `(.venv)`:

```powershell
pytest test_login.py
```

---

## 📊 Raportowanie — Allure

Projekt wykorzystuje **Allure** do generowania czytelnych, interaktywnych raportów z przebiegu testów.

### Wymagania wstępne

Allure Commandline wymaga Javy:

```bash
java -version
```

### Instalacja

**1. Biblioteka Pythona:**

```bash
pip install allure-pytest
pip freeze > requirements.txt
```

**2. Allure Commandline (przez Scoop, Windows):**

```powershell
irm get.scoop.sh | iex
scoop install allure
```

> ⚠️ Po instalacji Allure zrestartuj terminal (PATH odświeża się dopiero w nowym oknie).

```bash
allure --version
```

### Generowanie raportu

```bash
pytest test_add_thing.py --alluredir=allure-results
allure serve allure-results
```

Aby wyczyścić poprzednie wyniki przed nowym uruchomieniem:

```bash
pytest --alluredir=allure-results --clean-alluredir
```

---

## ⚡ Testy wydajnościowe — Locust

Testy obciążeniowe logowania symulują wielu równoczesnych użytkowników korzystających z aplikacji.

### Instalacja

```bash
pip install locust
```

### Uruchomienie testu

```bash
locust -f locustfile.py --users 50 --spawn-rate 5 --run-time 1m --headless --html results/report.html --csv results/stats
```

Parametry: **50 użytkowników**, **5 nowych użytkowników/s**, czas trwania **1 minuta**.

### Podgląd wyników

```bash
start results/report.html
```

---

## 📈 Wyniki testów wydajnościowych

Test przeprowadzono na środowisku produkcyjnym `saucedemo.com` przy obciążeniu **50 jednoczesnych użytkowników** (spawn rate: 5 użytkowników/s, czas trwania: 1 minuta).

> **Uwaga metodologiczna:** SauceDemo to aplikacja typu SPA — routing (`/inventory.html`, `/cart.html`) oraz logowanie realizowane są po stronie klienta (JavaScript), nie jako osobne endpointy backendu. Bezpośrednie żądania do tych ścieżek kończyły się błędami 404/405. Test wydajnościowy ograniczono więc do rzeczywistego zasobu serwowanego przez backend — `GET /` (strona logowania) — co dało wiarygodne wyniki obciążenia serwera.

### Statystyki żądań

| Endpoint | Liczba żądań | Błędy | Śr. czas | Min | Max | RPS |
|---|---|---|---|---|---|---|
| `GET /` | 1384 | **0** | 28,73 ms | 20 ms | 318 ms | 23,26 |

### Percentyle czasu odpowiedzi

| Percentyl | 50% | 60% | 70% | 80% | 90% | 95% | 99% | 100% |
|---|---|---|---|---|---|---|---|---|
| Czas (ms) | 25 | 25 | 26 | 28 | 33 | 56 | 96 | 320 |

Do 90. percentyla czasy odpowiedzi mieszczą się w przedziale 20–33 ms — dopiero powyżej 95. percentyla widać wyraźniejszy wzrost, z pojedynczymi skrajnymi przypadkami sięgającymi 320 ms.

### Wnioski

- ✅ **0 błędów** na 1384 wysłanych żądań
- ✅ Stabilny, niski średni czas odpowiedzi (~29 ms)
- ✅ RPS narastał liniowo wraz z dochodzeniem do 50 użytkowników, po czym ustabilizował się na poziomie ~23–25 RPS bez oznak degradacji wydajności

### Ograniczenia testu

Ze względu na architekturę SPA test objął wyłącznie `GET /`. Obciążenie procesu logowania i nawigacji między podstronami wymagałoby narzędzia symulującego przeglądarkę (np. Selenium) lub identyfikacji rzeczywistych endpointów API wykorzystywanych przez frontend.

---

## 👤 Autor

Projekt stworzony jako praktyczne portfolio z zakresu automatyzacji testów QA.