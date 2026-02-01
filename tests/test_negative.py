class TestNegativeScenarios:
    """Test suite for negative scenarios and error handling"""

    def test_invalid_product_id(self, api_client):
        """Test fetching product with invalid ID"""
        response = api_client.get("/products/9999")

        assert response.status_code == 404
        data = response.json()
        assert "message" in data

    def test_invalid_user_id(self, api_client):
        """Test fetching user with invalid ID"""
        response = api_client.get("/users/9999")

        assert response.status_code == 404

    def test_invalid_login_credentials(self, api_client):
        """Test login with invalid credentials"""
        invalid_creds = {
            "username": "invaliduser",
            "password": "wrongpassword"
        }
        response = api_client.post("/auth/login", data=invalid_creds)

        assert response.status_code == 400
        data = response.json()
        assert "message" in data

    def test_empty_search_query(self, api_client):
        """Test search with empty query"""
        response = api_client.get("/products/search", params={"q": ""})

        assert response.status_code == 200
        data = response.json()
        assert "products" in data
