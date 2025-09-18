import os
import requests
from EnvConstants import EnvConstants

env = EnvConstants.load_env()

MONGO_CONNECTION_URL = env["MONGO_CONNECTION_URL"]


def test_get_employee_by_role_positive():
    query = """
    query {
        getEmployeeByRole(role: "Manager") {
            id
            name
            role
        }
    }
    """
    response = requests.post(f"{MONGO_CONNECTION_URL}/graphql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "errors" not in data
    employees = data["data"]["getEmployeeByRole"]
    print("Positive exact role search:", employees)
    assert len(employees) > 0
    assert employees[0]["role"].lower() == "developer"


def test_search_employee_by_role_positive():
    query = """
    query {
        searchEmployeeByRole(keyword: "sign") {
            id
            name
            role
        }
    }
    """
    response = requests.post(f"{MONGO_CONNECTION_URL}/graphql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "errors" not in data
    employees = data["data"]["searchEmployeeByRole"]
    print("Positive like-search:", employees)
    assert any("designer" in emp["role"].lower() for emp in employees)


def test_get_employee_by_role_negative():
    query = """
    query {
        getEmployeeByRole(role: "Manager") {
            id
            name
            role
        }
    }
    """
    response = requests.post(f"{MONGO_CONNECTION_URL}/graphql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "errors" not in data
    employees = data["data"]["getEmployeeByRole"]
    print("Negative exact role search:", employees)
    assert employees == []


def test_database_down():
    query = """
    query {
        employees {
            id
            name
            role
        }
    }
    """
    try:
        bad_response = requests.post("http://127.0.0.1:9999/graphql", json={"query": query})
    except Exception as e:
        print("Database down test passed, error:", e)
        return
    data = bad_response.json()
    assert "errors" in data
    print("Database down response:", data)

if __name__ == "__main__":
    test_get_employee_by_role_positive()
    test_search_employee_by_role_positive()
    test_get_employee_by_role_negative()
    test_database_down()
    print("\nAll tests executed.")
