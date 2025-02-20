# import requests
# import logging
#
# class HttpRequest:
#     def __init__(self, path, method, headers=None, params=None, data=None, json=None, files=None, cookies=None):
#         self.path = path
#         self.method = method
#         self.headers = headers
#         self.params = params
#         self.data = data
#         self.json = json
#         self.files = files
#         self.cookies = cookies
#
#     def execute(self, base_url):
#         url = f"{base_url}{self.path}"
#         logging.info(f"Sending {self.method} request to {url}")
#         if self.json:
#             logging.info(f"Request JSON: {self.json}")
#         response = requests.request(
#             method=self.method,
#             url=url,
#             headers=self.headers,
#             params=self.params,
#             data=self.data,
#             json=self.json,
#             files=self.files,
#             cookies=self.cookies
#         )
#         logging.info(f"Response Status Code: {response.status_code}")
#         logging.info(f"Response JSON: {response.json()}")
#         return response

import requests
from requests import Response

class HttpRequest:
    """HTTP 请求基类，封装请求参数和执行逻辑"""
    def __init__(
        self,
        path: str,
        method: str = None,
        headers: dict = None,
        cookies: dict = None,
        data: dict = None,
        json: dict = None,
        files: dict = None
    ):
        self.path = path
        self.method = method.lower() if method else 'get'
        self.headers = headers
        self.cookies = cookies
        self.data = data
        self.json = json
        self.files = files

    def execute(self) -> Response:
        """执行 HTTP 请求并返回响应对象"""
        try:
            response = requests.request(
                method=self.method,
                url=self.path,
                headers=self.headers,
                cookies=self.cookies,
                data=self.data,
                json=self.json,
                files=self.files
            )
            response.raise_for_status()  # 自动检查 HTTP 状态码
            self.log(response)  # 调用 log 方法记录请求和响应信息
            return response
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {str(e)}")
            raise e  # 抛出异常供测试用例捕获

    def log(self, response: Response):
        """记录并格式化输出请求和响应信息"""
        # 格式化输出请求信息
        print("=" * 80)
        print(f"Request: {self.method.upper()} {self.path}")
        print("-" * 40)
        print("Headers:")
        if self.headers:
            for key, value in self.headers.items():
                print(f"  {key}: {value}")
        print("Cookies:")
        if self.cookies:
            for key, value in self.cookies.items():
                print(f"  {key}: {value}")
        print("Data:")
        if self.data:
            print(f"  {self.data}")
        print("JSON:")
        if self.json:
            print(f"  {self.json}")
        print("Files:")
        if self.files:
            for key, value in self.files.items():
                print(f"  {key}: {value}")

        # 格式化输出响应信息
        print("=" * 80)
        print(f"Response: {response.status_code} {response.reason}")
        print("-" * 40)
        print("Headers:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")
        print("Content:")
        try:
            json_content = response.json()
            print(f"  {json_content}")
        except ValueError:
            print(f"  {response.text}")
        print("=" * 80)
