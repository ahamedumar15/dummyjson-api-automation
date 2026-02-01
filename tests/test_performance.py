import time


class TestPerformance:
    """Test suite for API performance"""

    def test_response_time_products(self, api_client):
        """Test products endpoint response time"""
        start_time = time.time()
        response = api_client.get("/products")
        end_time = time.time()

        response_time = end_time - start_time
        assert response.status_code == 200
        assert response_time < 2.0, f"Response time {response_time}s exceeds 2s threshold"

    def test_response_time_users(self, api_client):
        """Test users endpoint response time"""
        start_time = time.time()
        response = api_client.get("/users")
        end_time = time.time()

        response_time = end_time - start_time
        assert response.status_code == 200
        assert response_time < 2.0, f"Response time {response_time}s exceeds 2s threshold"

