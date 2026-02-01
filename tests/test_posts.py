class TestPosts:
    """Test suite for Posts API endpoints"""

    def test_get_all_posts(self, api_client):
        """Test fetching all posts"""
        response = api_client.get("/posts")

        assert response.status_code == 200
        data = response.json()
        assert "posts" in data
        assert isinstance(data["posts"], list)

    def test_get_single_post(self, api_client):
        """Test fetching a single post"""
        post_id = 1
        response = api_client.get(f"/posts/{post_id}")

        assert response.status_code == 200
        post = response.json()
        assert post["id"] == post_id
        assert "title" in post
        assert "body" in post
        assert "userId" in post

    def test_get_user_posts(self, api_client):
        """Test fetching posts by user"""
        user_id = 1
        response = api_client.get(f"/posts/user/{user_id}")

        assert response.status_code == 200
        data = response.json()
        assert "posts" in data

    def test_add_post(self, api_client):
        """Test adding a new post"""
        new_post = {
            "title": "Test Post",
            "body": "This is a test post content",
            "userId": 1
        }
        response = api_client.post("/posts/add", data=new_post)

        assert response.status_code == 201
        post = response.json()
        assert post["title"] == new_post["title"]
