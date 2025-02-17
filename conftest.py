import pytest
from config import CONFIG

@pytest.fixture(scope="session")
def prod_headers():
    """生成全局 headers（含 token 和 cookie）"""
    token = CONFIG["test_env"]["token"]
    cookie = CONFIG["test_env"]["cookie"]
    yield {
        "Authorization": f"Bearer {token}",
        "Cookie": cookie,
        "Content-Type": "application/json"
    }

@pytest.fixture(autouse=True)
def log_request_response(request):
    """打印请求和响应日志（自动捕获）"""
    print(f"\n=== 测试用例: {request.node.name} ===")
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.passed:
        print(f"响应数据: {request.node.rep_call.result.text}")