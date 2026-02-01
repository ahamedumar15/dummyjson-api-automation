import pytest
from client.api_client import APIClient


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture
def test_user_credentials():
    return {
        "username": "emilys",
        "password": "emilyspass"
    }
