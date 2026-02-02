# 🚀 DummyJSON API Test Automation Framework

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-7.4.3-green.svg)](https://pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> An **API test automation framework** built with Python and Pytest, demonstrating professional QA engineering practices and comprehensive test coverage.


---

##  Overview

A comprehensive REST API test automation framework designed to validate the [DummyJSON API](https://dummyjson.com/) endpoints. This project showcases industry-standard testing practices including CRUD operations, authentication flows, performance validation, and negative scenario testing.

**🎓 Built as a portfolio project to demonstrate:**
- Strong understanding of API testing fundamentals
- Ability to design scalable test automation frameworks
- Proficiency in Python and Pytest ecosystem
- Knowledge of CI/CD integration and test reporting
- Professional code organization and documentation

---

##  Features

### Core Capabilities
✅ **RESTful API Testing** - Complete CRUD operation validation (GET, POST, PUT, PATCH, DELETE)  
✅ **Authentication & Authorization** - JWT token validation and session management  
✅ **Data Validation** - Response schema verification and data integrity checks  
✅ **Performance Testing** - Response time benchmarking and load testing  
✅ **Negative Testing** - Error handling and edge case validation  
✅ **Parallel Execution** - Multi-threaded test execution for faster results  
✅ **Rich Reporting** - HTML, Allure, and coverage reports  
✅ **CI/CD Ready** - Easy integration with Jenkins, GitHub Actions, GitLab CI  

### Framework Highlights
🔹 **45+ Automated Test Cases** across 9 API domains  
🔹 **Modular Architecture** with reusable components  
🔹 **Configurable Test Markers** for selective test execution  
🔹 **Comprehensive Logging** for debugging and troubleshooting  
🔹 **PEP 8 Compliant** code following Python best practices  

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.8+ |
| **Framework** | Pytest, pytest-html, pytest-xdist |
| **HTTP Client** | Requests |
| **Reporting** | Allure, pytest-cov |
| **CI/CD** | GitHub Actions (ready) |
| **Version Control** | Git, GitHub |

---



---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **Git** ([Download](https://git-scm.com/downloads))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ahamedumar15/dummyjson-api-automation.git
   cd dummyjson-api-automation
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   pytest --version
   ```

---

##  Running Tests

### Basic Test Execution

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test class
pytest -k TestProducts

# Run tests by marker
pytest -m smoke
```

### Advanced Options

```bash
# Parallel execution (4 workers)
pytest -n 4

# Generate HTML report
pytest --html=reports/report.html --self-contained-html

# Run with coverage
pytest --cov=. --cov-report=html

# Generate Allure report
pytest --alluredir=./allure-results
allure serve ./allure-results
```

### Test Markers

| Marker | Description |
|--------|-------------|
| `smoke` | Quick smoke tests |
| `regression` | Full regression suite |
| `performance` | Performance tests |
| `negative` | Negative scenarios |
| `critical` | Critical path tests |

**Example:**
```bash
pytest -m "smoke and not performance"
```

---

## 📊 Test Coverage

### API Endpoints (45+ Test Cases)

<details>
<summary><b>🛒 Products API (9 tests)</b></summary>

- Get all products with pagination
- Get single product by ID
- Search products by keyword
- Get product categories
- Filter products by category
- Add new product (POST)
- Update product (PUT)
- Delete product (DELETE)
- Invalid product ID handling

</details>

<details>
<summary><b>👥 Users API (4 tests)</b></summary>

- Get all users
- Get single user by ID
- Search users
- Filter users by attributes

</details>

<details>
<summary><b>🔐 Authentication API (3 tests)</b></summary>

- User login with JWT token
- Get current authenticated user
- Token refresh mechanism

</details>

<details>
<summary><b>🛍️ Carts API (4 tests)</b></summary>

- Get all carts
- Get single cart by ID
- Get user-specific carts
- Add new cart

</details>

<details>
<summary><b>📝 Posts, Comments, Todos, Quotes, Recipes APIs (14 tests)</b></summary>

- CRUD operations for all resources
- Search and filter capabilities
- User-specific resource retrieval

</details>

<details>
<summary><b>⚡ Performance Tests (2 tests)</b></summary>

- Response time validation (<2s threshold)
- Load testing capabilities

</details>

<details>
<summary><b>❌ Negative Scenarios (4 tests)</b></summary>

- Invalid IDs (404 handling)
- Invalid credentials
- Empty search queries
- Error message validation

</details>

---

## 📸 Reports & Screenshots

### Sample Test Execution

```bash
$ pytest -v

======================== test session starts ========================
platform win32 -- Python 3.11.0, pytest-7.4.3
collected 45 items

test_dummyjson_api.py::TestProducts::test_get_all_products PASSED     [ 2%]
test_dummyjson_api.py::TestProducts::test_get_single_product PASSED   [ 4%]
test_dummyjson_api.py::TestProducts::test_search_products PASSED      [ 6%]
test_dummyjson_api.py::TestProducts::test_add_product PASSED          [ 8%]
test_dummyjson_api.py::TestAuthentication::test_user_login PASSED     [11%]
...

===================== 45 passed in 12.34s ========================
```

### HTML Report Preview
*HTML reports are generated in `reports/report.html` with detailed test results, execution time, and failure analysis.*

### Allure Report
*Allure provides interactive test reports with test history, trends, and detailed step-by-step execution logs.*

---


### Supported CI/CD Platforms
- ✅ GitHub Actions
- ✅ Jenkins
- ✅ GitLab CI
- ✅ CircleCI
- ✅ Travis CI

---

## 💡 Best Practices Implemented

### Code Quality
- ✅ PEP 8 compliant Python code
- ✅ Descriptive test names following naming conventions
- ✅ Proper exception handling and error messages
- ✅ Reusable components and fixtures
- ✅ Comprehensive code documentation

### Testing Practices
- ✅ AAA pattern (Arrange-Act-Assert)
- ✅ Independent and isolated test cases
- ✅ Proper test data management
- ✅ Timeout configurations for reliability
- ✅ Both positive and negative test scenarios

### Framework Design
- ✅ Page Object Model equivalent for APIs
- ✅ Separation of concerns (client, tests, config)
- ✅ Configurable via pytest.ini and environment variables
- ✅ Scalable architecture for easy extension

---

##  Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

Please ensure your code follows PEP 8 standards and includes appropriate tests.

---


## 👤 Contact & Links

**Ahamed Umar**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/ahamedumar15)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/ahamedumar15)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat&logo=gmail)](mailto:ahamedumar825@gmail.com)


---

## 🙏 Acknowledgments

- [DummyJSON](https://dummyjson.com/) - Free fake REST API for testing
- [Pytest Documentation](https://docs.pytest.org/) - Comprehensive testing framework
- [Allure Framework](https://docs.qameta.io/allure/) - Beautiful test reporting
- [Requests Library](https://requests.readthedocs.io/) - HTTP for Humans

---

<div align="center">

### ⭐ Star this repository if you found it helpful!

**Made with ❤️ by Ahamed Umar**

</div>