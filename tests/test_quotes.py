class TestQuotes:
    """Test suite for Quotes API endpoints"""

    def test_get_all_quotes(self, api_client):
        """Test fetching all quotes"""
        response = api_client.get("/quotes")

        assert response.status_code == 200
        data = response.json()
        assert "quotes" in data
        assert isinstance(data["quotes"], list)

    def test_get_random_quote(self, api_client):
        """Test fetching a random quote"""
        response = api_client.get("/quotes/random")

        assert response.status_code == 200
        quote = response.json()
        assert "quote" in quote
        assert "author" in quote
