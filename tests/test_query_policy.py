# tests/test_query_policy.py
# import pytest
# from api.user_api import UserApi
#
# @pytest.mark.parametrize("user_id", [1, 2, 3])
# def test_get_user_info(user_id, base_url, user_headers):
#     response = UserApi().get_user_info(user_id=user_id, headers=user_headers).execute(base_url)
#     assert response.status_code == 200
#     assert 'id' in response.json()
#
# @pytest.mark.parametrize("user_data", [
#     {"name": "Alice", "email": "alice@example.com"},
#     {"name": "Bob", "email": "bob@example.com"}
# ])
# def test_create_user(user_data, base_url, user_headers):
#     response = UserApi().create_user(user_data=user_data, headers=user_headers).execute(base_url)
#     assert response.status_code == 201
#     assert 'id' in response.json()


import pytest
import yaml

import config
from api.product_api import UserAPI
from conftest import prod_headers


# 从 YAML 文件加载测试数据
def load_user_data():
    with open("../data/user_data.yaml", encoding='utf-8') as f:
        return yaml.safe_load(f)

class TestQueryPolicy:

    @pytest.mark.parametrize("case", load_user_data()["query_policy_data"])
    def test_query_policy(self, case, prod_headers):
        """测试获取用户信息接口"""
        query = UserAPI(base_url=config.CONFIG["test_env"]["base_url"])
        response = query.query_policy(
            pageNumber=case["pageNumber"],
            pageSize=case["pageSize"],
            headers=prod_headers
        ).execute()
        assert response.status_code == 200
        assert response.json()["code"] == 0