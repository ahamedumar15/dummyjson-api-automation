class TestRecipes:
    """Test suite for Recipes API endpoints"""

    def test_get_all_recipes(self, api_client):
        """Test fetching all recipes"""
        response = api_client.get("/recipes")

        assert response.status_code == 200
        data = response.json()
        assert "recipes" in data
        assert isinstance(data["recipes"], list)

    def test_get_single_recipe(self, api_client):
        """Test fetching a single recipe"""
        recipe_id = 1
        response = api_client.get(f"/recipes/{recipe_id}")

        assert response.status_code == 200
        recipe = response.json()
        assert recipe["id"] == recipe_id
        assert "name" in recipe
        assert "ingredients" in recipe