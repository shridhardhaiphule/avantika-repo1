from fastapi import FastAPI
from typing import List
from pymongo import MongoClient
import strawberry
from strawberry.asgi import GraphQL
import os

from EnvConstants import EnvConstants
env = EnvConstants.load_env()

MONGO_CONNECTION_URL = env["MONGO_CONNECTION_URL"]
MONGO_DB_NAME = env["MONGO_DB_NAME"]
MONGO_COLLECTION_EMPLOYEES = env["MONGO_COLLECTION_EMPLOYEES"]

app = FastAPI()

client = MongoClient(MONGO_CONNECTION_URL)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_EMPLOYEES]

@strawberry.type
class Employee:
    id: int
    name: str
    role: str

@strawberry.input
class EmployeeInput:
    name: str
    role: str

@strawberry.type
class Query:
    @strawberry.field
    def employees(self) -> List[Employee]:
        employees = []
        for employee_data in collection.find():
            employees.append(
                Employee(
                    id=employee_data["id"],
                    name=employee_data["name"],
                    role=employee_data["role"],
                )
            )
        return employees

    @strawberry.field
    def employee(self, id: int) -> Employee:
        employee_data = collection.find_one({"id": id})
        if employee_data:
            return Employee(
                id=employee_data["id"],
                name=employee_data["name"],
                role=employee_data["role"],
            )
        return None

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_employee(self, name: str, role: str) -> Employee:
        last_employee = collection.find_one(sort=[("id", -1)])
        new_id = last_employee["id"] + 1 if last_employee else 1

        employee = {"id": new_id, "name": name, "role": role}
        collection.insert_one(employee)
        return Employee(id=employee["id"], name=employee["name"], role=employee["role"])

    @strawberry.mutation
    def insert_employees_array_v1(self, employees: List[EmployeeInput]) -> List[Employee]:
        last_employee = collection.find_one(sort=[("id", -1)])
        start_id = last_employee["id"] + 1 if last_employee else 1

        new_employees = [
            {"id": start_id + i, "name": emp.name, "role": emp.role}
            for i, emp in enumerate(employees)
        ]

        collection.insert_many(new_employees)

        return [
            Employee(id=emp["id"], name=emp["name"], role=emp["role"])
            for emp in new_employees
        ]

    @strawberry.mutation
    def update_employee(self, id: int, name: str, role: str) -> Employee:
        collection.update_one({"id": id}, {"$set": {"name": name, "role": role}})
        updated_employee = collection.find_one({"id": id})
        return Employee(
            id=updated_employee["id"],
            name=updated_employee["name"],
            role=updated_employee["role"],
        )

    @strawberry.mutation
    def delete_employee(self, id: int) -> Employee:
        deleted_employee = collection.find_one_and_delete({"id": id})
        return Employee(
            id=deleted_employee["id"],
            name=deleted_employee["name"],
            role=deleted_employee["role"],
        )

schema = strawberry.Schema(query=Query, mutation=Mutation)
app.mount("/graphql", GraphQL(schema))
