from fastapi import FastAPI
from typing import List, Optional
from pymongo import MongoClient
import strawberry
from strawberry.asgi import GraphQL
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_CONNECTION_URL = os.getenv("MONGO_CONNECTION_URL")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_COLLECTION_EMPLOYEES = os.getenv("MONGO_COLLECTION_EMPLOYEES")

app = FastAPI()

client = MongoClient(MONGO_CONNECTION_URL)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_EMPLOYEES]

def get_next_id() -> int:
    last_employee = collection.find_one(sort=[("id", -1)])
    if last_employee and "id" in last_employee:
        return last_employee["id"] + 1
    return 1

@strawberry.type
class Employee:
    id: int
    name: str
    role: str

@strawberry.type
class Query:
    @strawberry.field
    def employees(self) -> List[Employee]:
        return [
            Employee(id=e["id"], name=e["name"], role=e.get("role", "Staff"))
            for e in collection.find({"id": {"$exists": True}})
        ]

    @strawberry.field
    def employee(self, id: int) -> Optional[Employee]:
        e = collection.find_one({"id": id})
        if e:
            return Employee(id=e["id"], name=e["name"], role=e.get("role", "Staff"))
        return None

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_employee(self, name: str, role: str = "Staff") -> Employee:
        new_id = get_next_id()
        employee = {"id": new_id, "name": name, "role": role}
        collection.insert_one(employee)
        return Employee(id=new_id, name=name, role=role)

    @strawberry.mutation
    def update_employee(self, id: int, name: Optional[str] = None, role: Optional[str] = None) -> Optional[Employee]:
        update_data = {}
        if name:
            update_data["name"] = name
        if role:
            update_data["role"] = role

        if update_data:
            collection.update_one({"id": id}, {"$set": update_data})

        e = collection.find_one({"id": id})
        if e:
            return Employee(id=e["id"], name=e["name"], role=e.get("role", "Staff"))
        return None

    @strawberry.mutation
    def delete_employee(self, id: int) -> Optional[Employee]:
        e = collection.find_one_and_delete({"id": id})
        if e:
            return Employee(id=e["id"], name=e["name"], role=e.get("role", "Staff"))
        return None

    @strawberry.mutation
    def insert_employees_array(self, employees: List[str], role: str = "Staff") -> List[Employee]:
        inserted_employees = []
        for name in employees:
            new_id = get_next_id()
            employee_doc = {"id": new_id, "name": name, "role": role}
            collection.insert_one(employee_doc)
            inserted_employees.append(Employee(id=new_id, name=name, role=role))
        return inserted_employees

schema = strawberry.Schema(query=Query, mutation=Mutation)
app.mount("/graphql", GraphQL(schema))

@app.get("/")
def root():
    return {"message": "Welcome! Go to /graphql to use GraphQL Playground 🚀"}
