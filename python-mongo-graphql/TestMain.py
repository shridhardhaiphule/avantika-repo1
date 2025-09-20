# TestMain.py
import unittest
from unittest import mock
from fastapi.testclient import TestClient
import os
import main
from EnvConstants import EnvConstants

# change default test, dev, production
os.environ.setdefault("APP_ENV", "dev")

env = EnvConstants.load_env()

client = TestClient(main.app)

class TestEmployeeGraphQL(unittest.TestCase):
    def setUp(self):
        pass
    def graphql_query(self, query: str, variables=None):
        response = client.post(
            "/graphql",
            json={"query": query, "variables": variables},
        )
        return response.json()

    def test_create_employee(self):
        query = """
        mutation {
            createEmployee(name: "Alice", role: "Developer") {
                id
                name
                role
            }
        }
        """
        result = self.graphql_query(query)
        data = result["data"]["createEmployee"]
        self.assertEqual(data["name"], "Alice")
        self.assertEqual(data["role"], "Developer")
        print("✅ Employee created successfully:", data)

    def test_insert_employees_for_search(self):
        query = """
        mutation {
            insertEmployeesArray(
                employees: [
                    { name: "Bob", role: "Manager" },
                    { name: "Charlie", role: "Developer" },
                    { name: "David", role: "Senior Developer" }
                ]
            ) {
                id
                name
                role
            }
        }
        """
        result = self.graphql_query(query)
        employees = result["data"]["insertEmployeesArray"]
        self.assertTrue(len(employees) >= 3)
        print("✅ Sample employees inserted for search:", employees)

    def test_get_employee_by_role_exact(self):
        self.test_insert_employees_for_search()
        query = """
        {
            getEmployeeByRole(role: "developer") {
                id
                name
                role
            }
        }
        """
        result = self.graphql_query(query)
        employees = result["data"]["getEmployeeByRole"]
        self.assertTrue(any(emp["role"].lower() == "developer" for emp in employees))
        print("✅ Exact match search returned:", employees)

    def test_search_employee_by_role_partial(self):
        self.test_insert_employees_for_search()
        query = """
        {
            searchEmployeeByRole(keyword: "Developer") {
                id
                name
                role
            }
        }
        """
        result = self.graphql_query(query)
        employees = result["data"]["searchEmployeeByRole"]
        self.assertTrue(len(employees) > 0)
        print("✅ Partial search returned:", employees)

    def test_search_employee_not_found(self):
        query = """
        {
            searchEmployeeByRole(keyword: "Astronaut") {
                id
                name
                role
            }
        }
        """
        result = self.graphql_query(query)
        employees = result["data"]["searchEmployeeByRole"]
        self.assertEqual(employees, [])
        print("❌ Search returned no employees as expected")

    def test_database_down(self):
        with mock.patch.object(main.collection, "find", side_effect=Exception("Database not available")):
            query = """
            query {
                employees {
                    id
                    name
                    role
                }
            }
            """
            response = client.post("/graphql", json={"query": query})
            errors = response.json().get("errors", [])
            self.assertTrue(errors)
            self.assertIn("Database error", errors[0]["message"])
            print("✅ Database down test passed with error:", errors[0]["message"])


if __name__ == "__main__":
    print(f"Running tests with environment: {os.environ.get('APP_ENV', 'dev')}")
    unittest.main(verbosity=2)
