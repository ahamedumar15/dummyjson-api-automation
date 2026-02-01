# client/api_client.py

import requests
from typing import Dict
from config.config import BASE_URL, TestConfig


class APIClient:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint: str, params: Dict = None):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            params=params,
            timeout=TestConfig.TIMEOUT
        )

    def post(self, endpoint: str, data: Dict = None):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=TestConfig.HEADERS,
            timeout=TestConfig.TIMEOUT
        )

    def put(self, endpoint: str, data: Dict = None):
        return self.session.put(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=TestConfig.HEADERS,
            timeout=TestConfig.TIMEOUT
        )

    def patch(self, endpoint: str, data: Dict = None):
        return self.session.patch(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=TestConfig.HEADERS,
            timeout=TestConfig.TIMEOUT
        )

    def delete(self, endpoint: str):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            timeout=TestConfig.TIMEOUT
        )
