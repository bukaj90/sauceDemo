import allure
from conftest import API_URL
@allure.title("Products list contains required fields")
def test_products_list(api):
    r = api.get(f"{API_URL}/products", timeout=10)
    assert r.status_code == 200
    products = r.json()["products"]
    assert len(products) > 0
    assert {"id", "title", "price"} <= products[0].keys()

@allure.title("Get a single product by id")
def test_single_product(api):
    r = api.get(f"{API_URL}/products/1", timeout=10)
    assert r.status_code == 200
    assert r.json()["id"] == 1

@allure.title("Non-existent product returns 404")
def test_product_not_found(api):
    r = api.get(f"{API_URL}/products/99999", timeout=10)
    assert r.status_code == 404

@allure.title("	Search products")
def test_product_search(api):
    r = api.get(f"{API_URL}/products/search", params={"q": "phone"}, timeout=10)
    assert r.status_code == 200
    assert r.json()["total"] > 0