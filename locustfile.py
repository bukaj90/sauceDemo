from locust import HttpUser, task, between

class SauceDemoUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://www.saucedemo.com"

    @task(2)
    def load_login_page(self):
        self.client.get("/")

"""
   @task(1)
    def load_inventory_page(self):
        self.client.get("/inventory.html")
        
"""
