class TestCarts:
    """Test suite for Carts API endpoints"""

    def test_get_all_carts(self, api_client):
        """Test fetching all carts"""
        response = api_client.get("/carts")

        assert response.status_code == 200
        data = response.json()
        assert "carts" in data
        assert isinstance(data["carts"], list)

    def test_get_single_cart(self, api_client):
        """Test fetching a single cart"""
        cart_id = 1
        response = api_client.get(f"/carts/{cart_id}")

        assert response.status_code == 200
        cart = response.json()
        assert cart["id"] == cart_id
        assert "products" in cart
        assert "total" in cart
        assert "userId" in cart

    def test_get_user_carts(self, api_client):
        """Test fetching carts of a specific user"""
        user_id = 1
        response = api_client.get(f"/carts/user/{user_id}")

        assert response.status_code == 200
        data = response.json()
        assert "carts" in data

    def test_add_cart(self, api_client):
        """Test adding a new cart"""
        new_cart = {
            "userId": 1,
            "products": [
                {"id": 1, "quantity": 2},
                {"id": 5, "quantity": 1}
            ]
        }
        response = api_client.post("/carts/add", data=new_cart)

        assert response.status_code == 201
        cart = response.json()
        assert "id" in cart
        assert cart["userId"] == new_cart["userId"]
