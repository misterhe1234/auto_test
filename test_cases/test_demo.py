from api.client import HttpClient
from api import ApiEndpoint
from utils.assertion import Assertion
from utils.data_loader import DataLoader

class TestDemo:
    def setup_class(self):
        self.client = HttpClient("https://api.example.com")
        self.user_api = ApiEndpoint(
            endpoint="/users",
            method="GET",
            params={"page": 1}
        )

    def test_get_users(self):
        response = self.user_api.call(self.client)
        assert response.status_code == 200
        assert "users" in response.json()

    def test_login(self):
        test_data = DataLoader.load_json("data/user_data.json")["test_users"][0]
        login_api = ApiEndpoint(
            endpoint="/login",
            method="POST",
            json=test_data
        )
        response = login_api.call(self.client)
        Assertion.assert_status_code(response, 200)
        Assertion.assert_json_key(response, "token")