import json
from starlette.testclient import TestClient
from main import app

client = TestClient(app)

def run_query(query: str, variables: dict = None):
    response = client.post("/graphql", json={"query": query, "variables": variables})
    print("GraphQL Response:", response.json())
    return response.json()

def test_create_employee():
    query = """
        mutation {
            createEmployee(name: "TestUser", role: "Tester") {
                id
                name
                role
            }
        }
    """
    result = run_query(query)
    assert "errors" not in result
    emp = result["data"]["createEmployee"]
    print("✅ Created employee:", emp)

def test_get_employees():
    query = """
        query {
            employees {
                id
                name
                role
            }
        }
    """
    result = run_query(query)
    assert "errors" not in result
    print("✅ Employees list:", result["data"]["employees"])

def test_get_employee_by_role():
    query = """
        query {
            getEmployeeByRole(role: "Tester") {
                id
                name
                role
            }
        }
    """
    result = run_query(query)
    assert "errors" not in result
    print("✅ Employees with role Tester:", result["data"]["getEmployeeByRole"])

def test_update_employee():
    query = """
        mutation {
            updateEmployee(id: 1, name: "UpdatedUser", role: "UpdatedRole") {
                id
                name
                role
            }
        }
    """
    result = run_query(query)
    assert "errors" not in result
    print("✅ Updated employee:", result["data"]["updateEmployee"])

def test_delete_employee():
    query = """
        mutation {
            deleteEmployee(id: 1) {
                id
                name
                role
            }
        }
    """
    result = run_query(query)
    assert "errors" not in result
    print("✅ Deleted employee:", result["data"]["deleteEmployee"])

def test_db_down(monkeypatch=None):
    from main import collection

    def mock_find(*args, **kwargs):
        raise Exception("Database is down")

    if monkeypatch:
        monkeypatch.setattr(collection, "find", mock_find)
    else:
        collection.find = mock_find

    query = """
        query {
            employees {
                id
                name
                role
            }
        }
    """
    result = run_query(query)
    assert "errors" in result
    print("⚠️ Expected DB error:", result["errors"][0]["message"])


if __name__ == "__main__":
    print("🚀 Running manual tests...\n")
    test_create_employee()
    test_get_employees()
    test_get_employee_by_role()
    test_update_employee()
    test_delete_employee()
    test_db_down()
