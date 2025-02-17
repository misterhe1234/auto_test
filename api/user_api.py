# api/user_api.py
# from common.base import HttpRequest

# class UserApi:
#     def get_user_info(self, user_id, headers=None):
#         path = f"/users/{user_id}"
#         method = "GET"
#         return HttpRequest(path=path, method=method, headers=headers)
#
#     def create_user(self, user_data, headers=None):
#         path = "/users"
#         method = "POST"
#         return HttpRequest(path=path, method=method, json=user_data, headers=headers)


from common.base import HttpRequest

class UserAPI:
    """用户相关接口定义"""
    def __init__(self, base_url: str):
        self.base_url = base_url

    def login(self, username: str, password: str) -> HttpRequest:
        """登录接口"""
        path = f"{self.base_url}/login"
        data = {"username": username, "password": password}
        return HttpRequest(path=path, method="post", data=data)

    def get_user_info(self, user_id: int, headers: dict) -> HttpRequest:
        """获取用户信息接口"""
        path = f"{self.base_url}/user/{user_id}"
        return HttpRequest(path=path, method="get", headers=headers)