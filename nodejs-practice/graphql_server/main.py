from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.fastapi import GraphQLRouter
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["test_db"]
collection = db["people"]

@strawberry.type
class Person:
    id: str
    name: str
    age: int
    email: str
    created_at: str

@strawberry.type
class Query:
    @strawberry.field
    def all_people(self) -> list[Person]:
        docs = collection.find()
        people = []
        for doc in docs:
            people.append(
                Person(
                    id=str(doc["_id"]),
                    name=doc["name"],
                    age=doc["age"],
                    email=doc["email"],
                    created_at=doc["created_at"]
                )
            )
        return people

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_person(self, name: str, age: int, email: str) -> Person:
        doc = {
            "name": name,
            "age": age,
            "email": email,
            "created_at": datetime.now().isoformat()
        }
        inserted = collection.insert_one(doc)
        doc["_id"] = str(inserted.inserted_id)
        return Person(
            id=doc["_id"],
            name=doc["name"],
            age=doc["age"],
            email=doc["email"],
            created_at=doc["created_at"]
        )

schema = strawberry.Schema(query=Query, mutation=Mutation)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
