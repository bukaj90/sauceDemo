import pytest
import requests
from config import API_URL
@pytest.fixture(scope="session")
def api():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    session.base_url = API_URL
    return session

@pytest.fixture(scope="session")
def token(api):
    r = api.post(f"{API_URL}/auth/login",json={"username": "emilys", "password": "emilyspass"},timeout=10)
    assert r.status_code == 200
    return r.json()["accessToken"]