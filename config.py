# 不同环境的配置（测试环境、生产环境）
CONFIG = {
    "test_env": {
        "base_url": "https://api.example.com",
        "token": "test_token_123",
        "cookie": "test_cookie_abc"
    },
    "prod_env": {
        "base_url": "https://api.prod.example.com",
        "token": "prod_token_456",
        "cookie": "prod_cookie_def"
    }
}