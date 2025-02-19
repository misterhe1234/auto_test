from common.base import HttpRequest


class UserAPI:
    """用户相关接口定义"""
    def __init__(self, base_url: str):
        self.base_url = base_url

    def query_policy(self, pageNumber: int, pageSize: int, headers: dict) -> HttpRequest:
        path = f"{self.base_url}/suite/admin/file_management/query_policy"
        json= {
                "pageSize": pageSize,
                "pageNumber": pageNumber
        }
        return  HttpRequest(path=path, method="post", json=json, headers=headers)