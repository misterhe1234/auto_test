class Assertion:
    @staticmethod
    def assert_status_code(response, expected_code):
        assert response.status_code == expected_code, f"Expected {expected_code}, got {response.status_code}"

    @staticmethod
    def assert_json_key(response, key):
        json_data = response.json()
        assert key in json_data, f"Key '{key}' not found in response"