class TestProducts:
    """Test suite for Products API endpoints"""

    def test_get_all_products(self, api_client):
        """Test fetching all products"""
        response = api_client.get("/products")

        assert response.status_code == 200
        data = response.json()
        assert "products" in data
        assert isinstance(data["products"], list)
        assert len(data["products"]) > 0
        assert "total" in data
        assert "limit" in data

    def test_get_single_product(self, api_client):
        """Test fetching a single product by ID"""
        product_id = 1
        response = api_client.get(f"/products/{product_id}")

        assert response.status_code == 200
        product = response.json()
        assert product["id"] == product_id
        assert "title" in product
        assert "price" in product
        assert "category" in product

    def test_search_products(self, api_client):
        """Test product search functionality"""
        search_query = "phone"
        response = api_client.get("/products/search", params={"q": search_query})

        assert response.status_code == 200
        data = response.json()
        assert "products" in data
        # Verify search results contain the query term
        if len(data["products"]) > 0:
            product_titles = [p["title"].lower() for p in data["products"]]
            assert any(search_query in title for title in product_titles)

    def test_get_products_with_pagination(self, api_client):
        """Test product pagination"""
        limit = 10
        skip = 5
        response = api_client.get("/products", params={"limit": limit, "skip": skip})

        assert response.status_code == 200
        data = response.json()
        assert len(data["products"]) <= limit
        assert data["limit"] == limit
        assert data["skip"] == skip

    def test_get_product_categories(self, api_client):
        """Test fetching product categories"""
        response = api_client.get("/products/categories")

        assert response.status_code == 200
        categories = response.json()
        assert isinstance(categories, list)
        assert len(categories) > 0

    def test_get_products_by_category(self, api_client):
        """Test filtering products by category"""
        category = "smartphones"
        response = api_client.get(f"/products/category/{category}")

        assert response.status_code == 200
        data = response.json()
        assert "products" in data
        # Verify all products belong to the category
        for product in data["products"]:
            assert product["category"] == category

    def test_add_product(self, api_client):
        """Test adding a new product"""
        new_product = {
            "title": "Test Product",
            "price": 999,
            "category": "test-category"
        }
        response = api_client.post("/products/add", data=new_product)

        assert response.status_code == 201
        product = response.json()
        assert product["title"] == new_product["title"]
        assert product["price"] == new_product["price"]
        assert "id" in product

    def test_update_product(self, api_client):
        """Test updating a product"""
        product_id = 1
        updated_data = {
            "title": "Updated Product Title"
        }
        response = api_client.put(f"/products/{product_id}", data=updated_data)

        assert response.status_code == 200
        product = response.json()
        assert product["title"] == updated_data["title"]
        assert product["id"] == product_id

    def test_delete_product(self, api_client):
        """Test deleting a product"""
        product_id = 1
        response = api_client.delete(f"/products/{product_id}")

        assert response.status_code == 200
        data = response.json()
        assert data["isDeleted"] is True
        assert data["id"] == product_id
