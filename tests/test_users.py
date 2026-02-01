class TestUsers:
    """Test suite for Users API endpoints"""

    def test_get_all_users(self, api_client):
        """Test fetching all users"""
        response = api_client.get("/users")

        assert response.status_code == 200
        data = response.json()
        assert "users" in data
        assert isinstance(data["users"], list)
        assert len(data["users"]) > 0

    def test_get_single_user(self, api_client):
        """Test fetching a single user by ID"""
        user_id = 1
        response = api_client.get(f"/users/{user_id}")

        assert response.status_code == 200
        user = response.json()
        assert user["id"] == user_id
        assert "username" in user
        assert "email" in user
        assert "firstName" in user
        assert "lastName" in user

    def test_search_users(self, api_client):
        """Test user search functionality"""
        search_query = "john"
        response = api_client.get("/users/search", params={"q": search_query})

        assert response.status_code == 200
        data = response.json()
        assert "users" in data

    def test_filter_users(self, api_client):
        """Test filtering users by key-value"""
        response = api_client.get("/users/filter", params={"key": "hair.color", "value": "Brown"})

        assert response.status_code == 200
        data = response.json()
        assert "users" in data