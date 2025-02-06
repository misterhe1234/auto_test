class ApiEndpoint:
    def __init__(self, endpoint, method, headers=None, params=None, json=None, data=None):
        self.endpoint = endpoint
        self.method = method
        self.headers = headers
        self.params = params
        self.json = json
        self.data = data

    def call(self, http_client):
        return http_client.request(
            method=self.method,
            endpoint=self.endpoint,
            headers=self.headers,
            params=self.params,
            json=self.json,
            data=self.data
        )