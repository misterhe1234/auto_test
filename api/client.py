import requests
from utils.logger import logger

class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()  # 使用 Session 保持连接

    def request(self, method, endpoint, headers=None, params=None, json=None, data=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Request: {method} {url}")
        try:
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json,
                data=data
            )
            logger.info(f"Response Status: {response.status_code}")
            return response
        except Exception as e:
            logger.error(f"Request failed: {str(e)}")
            raise