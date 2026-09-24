# 🧪 sauceDemo — E2E and Performance Test Automation Framework

A comprehensive test project for the [Sauce Demo](https://www.saucedemo.com/) application, combining functional test automation (Selenium + pytest, Page Object Model pattern), performance testing (Locust), and result reporting (Allure).

The project was built as a hands-on exercise in test automation — starting from a basic script, moving through test case parametrization, and arriving at a full POM structure ready to grow in a production-like environment.

---

## 🚀 Features

The framework covers the full user journey in the online store:

- ✅ **Login** — validation of correct and incorrect login credentials
- ✅ **Navigation** — handling the side menu (hamburger menu)
- ✅ **Adding products** — adding multiple items to the cart
- ✅ **Checkout process** — going through the cart and completing an order
- ✅ **PDF confirmation generation** — validating the document generated after an order
- ✅ **Login load testing** — simulating multiple concurrent users (Locust)

Tests are parametrized (`pytest.mark.parametrize`), which allows the same scenarios to run against different data sets without duplicating code.

---

## 🏗️ Architecture

The project is built on the **Page Object Model (POM)** pattern, which provides:

- separation of test logic from page interaction logic,
- easier test maintenance when the UI changes,
- a readable, scalable code structure.

---

## 🛠️ Tech stack

| Category            | Tool                        |
|---------------------|-----------------------------|
| Language            | Python 3.12                 |
| Browser automation  | Selenium (Selenium Manager) |
| Test framework      | pytest                      |
| Performance testing | Locust                      |
| Reporting           | Allure                      |
| Browser             | Firefox                     |

---

## 📦 Installation

Requirements: Python 3.12, Firefox browser.

```powershell
git clone https://github.com/bukaj90/sauceDemo.git
cd sauceDemo
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks activating the virtual environment, run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

> ℹ️ Since version 4.6, Selenium ships with a built-in **Selenium Manager**, which automatically detects the installed browser and downloads the matching driver (`geckodriver`). No additional configuration or manual driver download is required.

---

## ▶️ Running tests

With the `(.venv)` environment active:

```powershell
pytest test_login.py
```

---

## 📊 Reporting — Allure

The project uses **Allure** to generate clear, interactive test run reports.

### Prerequisites

Allure Commandline requires Java:

```bash
java -version
```

### Installation

**1. Python library:**

```bash
pip install allure-pytest
pip freeze > requirements.txt
```

**2. Allure Commandline (via Scoop, Windows):**

```powershell
irm get.scoop.sh | iex
scoop install allure
```

> ⚠️ Restart your terminal after installing Allure (PATH only refreshes in a new window).

```bash
allure --version
```

### Generating a report

```bash
pytest test_add_thing.py --alluredir=allure-results
allure serve allure-results
```

To clear previous results before a new run:

```bash
pytest --alluredir=allure-results --clean-alluredir
```

---

## ⚡ Performance testing — Locust

Login load tests simulate multiple concurrent users interacting with the application.

### Installation

```bash
pip install locust
```

### Running the test

```bash
locust -f locustfile.py --users 50 --spawn-rate 5 --run-time 1m --headless --html results/report.html --csv results/stats
```

Parameters: **50 users**, **5 new users/s**, duration **1 minute**.

### Viewing results

```bash
start results/report.html
```

---

## 📈 Performance test results

The test was run against the production environment `saucedemo.com` under a load of **50 concurrent users** (spawn rate: 5 users/s, duration: 1 minute).

> **Methodology note:** SauceDemo is an SPA — routing (`/inventory.html`, `/cart.html`) and login are handled client-side (JavaScript), not as separate backend endpoints. Direct requests to these paths returned 404/405 errors. The performance test was therefore limited to the actual resource served by the backend — `GET /` (the login page) — which produced reliable results for server load.

### Request statistics

| Endpoint | Requests | Failures | Avg. time | Min   | Max    | RPS   |
|----------|----------|----------|-----------|-------|--------|-------|
| `GET /`  | 1384     | **0**    | 28.73 ms  | 20 ms | 318 ms | 23.26 |

### Response time percentiles

| Percentile | 50% | 60% | 70% | 80% | 90% | 95% | 99% | 100% |
|------------|-----|-----|-----|-----|-----|-----|-----|------|
| Time (ms)  | 25  | 25  | 26  | 28  | 33  | 56  | 96  | 320  |

Up to the 90th percentile, response times stay in the 20–33 ms range — only above the 95th percentile does a more noticeable increase appear, with a few extreme cases reaching 320 ms.

### Conclusions

- ✅ **0 failures** out of 1384 requests sent
- ✅ Stable, low average response time (~29 ms)
- ✅ RPS grew linearly while ramping up to 50 users, then stabilized around ~23–25 RPS with no signs of performance degradation

### Test limitations

Due to the SPA architecture, the test only covered `GET /`. Load-testing the login process and navigation between subpages would require a tool that simulates a real browser (e.g. Selenium), or identifying the actual API endpoints used by the frontend.

---

## 👤 Author

Project built as a hands-on QA test automation portfolio piece.