class TestAuthentication:
    """Test suite for Authentication endpoints"""

    def test_user_login(self, api_client, test_user_credentials):
        """Test user login"""
        response = api_client.post("/auth/login", data=test_user_credentials)

        assert response.status_code == 200
        data = response.json()
        assert "accessToken" in data
        assert "refreshToken" in data
        assert "id" in data
        assert "username" in data

    def test_get_current_user(self, api_client, test_user_credentials):
        """Test getting current authenticated user"""
        # First login to get token
        login_response = api_client.post("/auth/login", data=test_user_credentials)
        token = login_response.json()["accessToken"]

        # Get current user with token
        api_client.session.headers.update({"Authorization": f"Bearer {token}"})
        response = api_client.get("/auth/me")

        assert response.status_code == 200
        user = response.json()
        assert "username" in user
        assert user["username"] == test_user_credentials["username"]

    def test_refresh_token(self, api_client, test_user_credentials):
        """Test token refresh"""
        # First login
        login_response = api_client.post("/auth/login", data=test_user_credentials)
        refresh_token = login_response.json()["refreshToken"]

        # Refresh the token
        response = api_client.post("/auth/refresh", data={"refreshToken": refresh_token})

        assert response.status_code == 200
        data = response.json()
        assert "accessToken" in data
        assert "refreshToken" in data
