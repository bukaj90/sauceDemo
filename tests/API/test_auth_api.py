import allure
from conftest import API_URL
import requests

@allure.title("Logowanie poprawnymi danymi zwraca token")
def test_login_returns_token(api):
    r = api.post(f"{API_URL}/auth/login",json={"username": "emilys", "password": "emilyspass"},timeout=10)
    assert r.status_code == 200
    assert "accessToken" in r.json()

@allure.title("Logowanie błędnym hasłem zwraca 400")
def test_login_wrong_password(api):
    r = api.post(f"{API_URL}/auth/login",json={"username": "emilys", "password": "zle"},timeout=10)
    assert r.status_code == 400

@allure.title("Endpoint chroniony działa z tokenem")
def test_me_with_token(token):
    r = requests.get(f"{API_URL}/auth/me",headers={"Authorization": f"Bearer {token}"},timeout=10)
    assert r.status_code == 200
    assert r.json()["username"] == "emilys"

@allure.title("Endpoint chroniony bez tokenu zwraca 401")
def test_me_without_token():
    r = requests.get(f"{API_URL}/auth/me", timeout=10)
    assert r.status_code == 401