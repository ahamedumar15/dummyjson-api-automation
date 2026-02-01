class TestComments:
    """Test suite for Comments API endpoints"""

    def test_get_all_comments(self, api_client):
        """Test fetching all comments"""
        response = api_client.get("/comments")

        assert response.status_code == 200
        data = response.json()
        assert "comments" in data
        assert isinstance(data["comments"], list)

    def test_get_post_comments(self, api_client):
        """Test fetching comments for a specific post"""
        post_id = 1
        response = api_client.get(f"/comments/post/{post_id}")

        assert response.status_code == 200
        data = response.json()
        assert "comments" in data