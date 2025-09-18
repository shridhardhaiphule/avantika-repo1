from fastapi import FastAPI
from typing import List, Optional
from pymongo import MongoClient
import strawberry
from strawberry.asgi import GraphQL
from dotenv import load_dotenv
import os

from EnvConstants import EnvConstants
from strawberry.exceptions import GraphQLError

env = EnvConstants.load_env()


def load_env():
    MONGO_CONNECTION_URL = env["MONGO_CONNECTION_URL"]
    MONGO_DB_NAME = env["MONGO_DB_NAME"]
    MONGO_COLLECTION_EMPLOYEES = env["MONGO_COLLECTION_EMPLOYEES"]

app = FastAPI()

client = MongoClient(env["MONGO_CONNECTION_URL"])
db = client[env["MONGO_DB_NAME"]]
collection = db[env["MONGO_COLLECTION_EMPLOYEES"]]

@strawberry.type
class Employee:
    id: int
    name: str
    role: str


@strawberry.input
class EmployeeInput:
    name: str
    role: str


def to_employee(doc) -> Employee:
    return Employee(
        id=int(doc.get("id", 0)),
        name=str(doc.get("name", "")).strip(),
        role=str(doc.get("role", "")).strip(),
    )

@strawberry.type
class Query:
    @strawberry.field
    def employees(self) -> List[Employee]:
        try:
            return [to_employee(emp) for emp in collection.find()]
        except Exception as e:
            raise GraphQLError(f"Database error: {str(e)}")

    @strawberry.field
    def employee(self, id: int) -> Optional[Employee]:
        try:
            emp = collection.find_one({"id": id})
            return to_employee(emp) if emp else None
        except Exception as e:
            raise GraphQLError(f"Database error: {str(e)}")

    @strawberry.field
    def get_employee_by_role(self, role: str) -> List[Employee]:
        try:
            cleaned_role = role.strip()
            query = {"role": {"$regex": f"^{cleaned_role}$", "$options": "i"}}
            return [to_employee(emp) for emp in collection.find(query)]
        except Exception as e:
            raise GraphQLError(f"Database error: {str(e)}")

    @strawberry.field
    def search_employee_by_role(self, keyword: str) -> List[Employee]:
        try:
            cleaned_keyword = keyword.strip()
            query = {"role": {"$regex": cleaned_keyword, "$options": "i"}}
            return [to_employee(emp) for emp in collection.find(query)]
        except Exception as e:
            raise GraphQLError(f"Database error: {str(e)}")

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_employee(self, name: str, role: str) -> Employee:
        try:
            last = collection.find_one(sort=[("id", -1)])
            new_id = last["id"] + 1 if last else 1
            emp = {"id": new_id, "name": name.strip(), "role": role.strip()}
            collection.insert_one(emp)
            return to_employee(emp)
        except Exception as e:
            raise GraphQLError(f"Database error: {str(e)}")

    @strawberry.mutation
    def insert_employees_array_v1(self, employees: List[str], role: str = "Staff") -> List[Employee]:
        inserted_employees = []
        for name in employees:
            new_id = get_next_id()
            employee_doc = {"id": new_id, "name": name.strip(), "role": role.strip()}
            collection.insert_one(employee_doc)
            inserted_employees.append(Employee(id=new_id, name=name.strip(), role=role.strip()))
        return inserted_employees

    @strawberry.mutation
    def insert_employees_array(self, employees: List[EmployeeInput]) -> List[Employee]:
        try:
            # GEt the latest id from DB
            last = collection.find_one(sort=[("id", -1)])
            start_id = last["id"] + 1 if last else 1

            # Prepare new employees with unique IDs
            new_emps = [
                {"id": start_id + i, "name": emp.name.strip(), "role": emp.role.strip()}
                for i, emp in enumerate(employees)
            ]
            # INSERT BULK / MANY
            collection.insert_many(new_emps)
            return [to_employee(e) for e in new_emps]
        except Exception as e:
            raise GraphQLError(f"Database error: {str(e)}")

    @strawberry.mutation
    def update_employee(self, id: int, name: str, role: str) -> Optional[Employee]:
        try:
            collection.update_one(
                {"id": id}, {"$set": {"name": name.strip(), "role": role.strip()}}
            )
            emp = collection.find_one({"id": id})
            return to_employee(emp) if emp else None
        except Exception as e:
            raise GraphQLError(f"Database error: {str(e)}")

    @strawberry.mutation
    def delete_employee(self, id: int) -> Optional[Employee]:
        try:
            emp = collection.find_one_and_delete({"id": id})
            return to_employee(emp) if emp else None
        except Exception as e:
            raise GraphQLError(f"Database error: {str(e)}")

def get_next_id() -> int:
    last_employee = collection.find_one(sort=[("id", -1)])
    if last_employee and "id" in last_employee:
        return last_employee["id"] + 1
    return 1

schema = strawberry.Schema(query=Query, mutation=Mutation)
app.mount("/graphql", GraphQL(schema))
