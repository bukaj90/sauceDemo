# 🧪 sauceDemo — UI, API and Performance Test Automation Framework

<!-- Add the GitHub Actions badge here once the workflow exists:
![Tests](https://github.com/bukaj90/sauceDemo/actions/workflows/tests.yml/badge.svg)
-->

A test automation project combining three layers of testing:

- **UI (E2E)** — [Sauce Demo](https://www.saucedemo.com/) web store, Selenium + pytest, Page Object Model
- **API** — [DummyJSON](https://dummyjson.com/) REST API, `requests` + pytest
- **Performance** — load test of the login page, Locust

Results are reported with Allure. The project was built as a hands-on exercise in test automation: from a basic script, through parametrized test cases, to a full POM structure with a separate API test suite.

---

## 📑 Table of contents

- [Features](#-features)
- [Tech stack](#-tech-stack)
- [Architecture](#-architecture)
- [Project structure](#-project-structure)
- [Installation](#-installation)
- [Running tests](#-running-tests)
- [API tests](#-api-tests)
- [Reporting — Allure](#-reporting--allure)
- [Performance testing — Locust](#-performance-testing--locust)
- [Author](#-author)

---

## 🚀 Features

### UI tests (Sauce Demo)

- ✅ **Login** — validation of correct and incorrect login credentials
- ✅ **Navigation** — handling the side menu (hamburger menu)
- ✅ **Adding products** — adding items to the cart
- ✅ **Checkout process** — going through the cart and completing an order
- ✅ **PDF confirmation generation** — validating the document generated after an order

UI tests are parametrized (`pytest.mark.parametrize`), so the same scenarios run against different data sets without duplicating code.

### API tests (DummyJSON)

- ✅ **Authentication** — login returns a token, wrong password is rejected
- ✅ **Protected endpoints** — access with and without a token
- ✅ **Products** — list, single product, search, non-existent product (404)

### Performance tests

- ✅ **Load testing of the login page** (`GET /`) — simulating multiple concurrent users (Locust)

---

## 🛠️ Tech stack

| Category            | Tool                        |
|---------------------|-----------------------------|
| Language            | Python 3.12                 |
| Browser automation  | Selenium (Selenium Manager) |
| API testing         | requests                    |
| Test framework      | pytest                      |
| Performance testing | Locust                      |
| Reporting           | Allure                      |
| Browser             | Firefox                     |

---

## 🏗️ Architecture

The UI layer is built on the **Page Object Model (POM)** pattern, which provides:

- separation of test logic from page interaction logic,
- easier test maintenance when the UI changes,
- a readable, scalable code structure.

The API layer is kept separate from the UI layer, so it can run fast and without a browser. Shared setup (HTTP session, auth token) lives in fixtures in `tests/API/conftest.py`, and shared settings (base URLs, test users) in `config.py`.

---

## 📁 Project structure

```
sauceDemo/
├── pages/                  # Page Objects (cart, checkout, inventory, login, ...)
├── locators/               # element locators
├── tests/
│   ├── UI/                 # Selenium tests (Sauce Demo)
│   │   ├── test_login.py
│   │   └── test_add_thing.py
│   └── API/                # requests tests (DummyJSON)
│       ├── conftest.py     # session and token fixtures
│       ├── test_auth_api.py
│       └── test_products_api.py
├── config.py               # BASE_URL, API_URL, users, timeouts
├── conftest.py             # UI fixtures
├── locustfile.py           # load test
├── pytest.ini
└── requirements.txt
```

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
# all tests
pytest

# UI tests only (Selenium, Firefox)
pytest tests/UI -v

# API tests only (fast, no browser)
pytest tests/API -v

# a single test
pytest tests/UI/test_add_thing.py::TestAddThing::test_add_product_to_cart
```

---

## 🔌 API tests

Sauce Demo is a single-page application without a public REST API, so the API test suite targets a separate service built for practice: **[DummyJSON](https://dummyjson.com/)**. It offers authentication with tokens, products and carts, which mirrors the flows covered in the UI tests.

### Covered scenarios

| Area           | Scenario                                             | Expected result                         |
|----------------|------------------------------------------------------|-----------------------------------------|
| Authentication | Login with valid credentials                         | `200`, `accessToken` in response        |
| Authentication | Login with a wrong password                          | `400`                                   |
| Authorization  | `GET /auth/me` with a valid token                    | `200`, correct username                 |
| Authorization  | `GET /auth/me` without a token                       | `401`                                   |
| Products       | `GET /products`                                      | `200`, list with `id`, `title`, `price` |
| Products       | `GET /products/1`                                    | `200`, matching `id`                    |
| Products       | `GET /products/99999`                                | `404`                                   |
| Products       | `GET /products/search?q=phone`                       | `200`, `total > 0`                      |

### Design notes

- **Test isolation.** The token is obtained with a plain `requests.post`, not through the shared `requests.Session`. DummyJSON also sets auth cookies on login, and a shared session would remember them, so tests of protected endpoints could pass even without a token. Authorization tests use stateless `requests.get` calls to make sure the `Authorization` header is what is actually being verified.
- **Shared configuration.** The API address is defined once in `config.py` (`API_URL`).
- **Timeouts.** Every request has an explicit `timeout`, so a slow public service cannot hang the test run.
- **External dependency.** DummyJSON is a public service. Test credentials come from its documentation and may change; if the login tests start failing, check the docs first.

```powershell
pytest tests/API -v
```

---

## 📊 Reporting — Allure

The project uses **Allure** to generate clear, interactive test run reports. Both UI and API tests are included in the same report.

<!-- Add a screenshot of the Allure report here:
![Allure report](docs/allure-report.png)
-->

### Prerequisites

Allure Commandline requires Java:

```bash
java -version
```

### Installation

**1. Python library** (already listed in `requirements.txt`):

```bash
pip install allure-pytest
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
pytest --alluredir=allure-results
allure serve allure-results
```

To clear previous results before a new run:

```bash
pytest --alluredir=allure-results --clean-alluredir
```

---

## ⚡ Performance testing — Locust

Load tests of the login page simulate multiple concurrent users hitting the application.

> This is a public demo application intended for practice, and the load was deliberately small (50 users for one minute).

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

```powershell
start results/report.html   # Windows
```

### Performance test results

The test was run against `saucedemo.com` under a load of **50 concurrent users** (spawn rate: 5 users/s, duration: 1 minute).

> **Methodology note:** SauceDemo is an SPA — routing (`/inventory.html`, `/cart.html`) and login are handled client-side (JavaScript), not as separate backend endpoints. Direct requests to these paths returned 404/405 errors. The performance test was therefore limited to the actual resource served by the backend — `GET /` (the login page) — which produced reliable results for server load.

#### Request statistics

| Endpoint | Requests | Failures | Avg. time | Min   | Max    | RPS   |
|----------|----------|----------|-----------|-------|--------|-------|
| `GET /`  | 1384     | **0**    | 28.73 ms  | 20 ms | 318 ms | 23.26 |

#### Response time percentiles

| Percentile | 50% | 60% | 70% | 80% | 90% | 95% | 99% | 100% |
|------------|-----|-----|-----|-----|-----|-----|-----|------|
| Time (ms)  | 25  | 25  | 26  | 28  | 33  | 56  | 96  | 320  |

Up to the 90th percentile, response times stay in the 20–33 ms range — only above the 95th percentile does a more noticeable increase appear, with a few extreme cases reaching 320 ms.

#### Conclusions

- ✅ **0 failures** out of 1384 requests sent
- ✅ Stable, low average response time (~29 ms)
- ✅ RPS grew linearly while ramping up to 50 users, then stabilized around ~23–25 RPS with no signs of performance degradation

#### Test limitations

Due to the SPA architecture, the test only covered `GET /`. Load-testing the login process and navigation between subpages would require a tool that simulates a real browser (e.g. Selenium), or identifying the actual API endpoints used by the frontend.

---

## 👤 Author

Kuba — QA / test automation.
[LinkedIn](https://www.linkedin.com/in/jakub-wo%C5%BAny-094592157/)