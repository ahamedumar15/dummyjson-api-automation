class TestTodos:
    """Test suite for Todos API endpoints"""

    def test_get_all_todos(self, api_client):
        """Test fetching all todos"""
        response = api_client.get("/todos")

        assert response.status_code == 200
        data = response.json()
        assert "todos" in data
        assert isinstance(data["todos"], list)

    def test_get_single_todo(self, api_client):
        """Test fetching a single todo"""
        todo_id = 1
        response = api_client.get(f"/todos/{todo_id}")

        assert response.status_code == 200
        todo = response.json()
        assert todo["id"] == todo_id
        assert "todo" in todo
        assert "completed" in todo

    def test_add_todo(self, api_client):
        """Test adding a new todo"""
        new_todo = {
            "todo": "Test automation task",
            "completed": False,
            "userId": 1
        }
        response = api_client.post("/todos/add", data=new_todo)

        assert response.status_code == 201
        todo = response.json()
        assert todo["todo"] == new_todo["todo"]