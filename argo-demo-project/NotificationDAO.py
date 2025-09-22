from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from typing import Optional

class NotificationDAO:
    def __init__(self, db_name="argo_demo", collection_name="notifications", mongo_url="mongodb://localhost:27017/"):
        self.client = MongoClient(mongo_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_notification(self, user_id, category, sub_category, item):
        now = datetime.utcnow()
        notification = {
            "user_id": user_id,
            "category": category,
            "sub_category": sub_category,
            "item": item,
            "created_at": now,
            "updated_at": None,
            "deleted_at": None,
            "is_read": False
        }
        result = self.collection.insert_one(notification)
        notification["_id"] = result.inserted_id
        return notification

    def create_notifications(self, user_id, category, sub_category, item_list):
        notifications = []
        for item in item_list:
            n = self.create_notification(user_id, category, sub_category, item)
            notifications.append(n)
        return notifications

    def update_notification(self, notification_id, category=None, sub_category=None, item=None, is_read=None):
        update_fields = {}
        if category: update_fields["category"] = category
        if sub_category: update_fields["sub_category"] = sub_category
        if item: update_fields["item"] = item
        if is_read is not None: update_fields["is_read"] = is_read
        if update_fields:
            update_fields["updated_at"] = datetime.now()
            self.collection.update_one({"_id": notification_id}, {"$set": update_fields})
        return self.collection.find_one({"_id": notification_id})

    def get_unread_user_notifications(self, user_id):
        return list(self.collection.find({"user_id": user_id, "is_read": False}))

    def get_last_read_user_notification(self, user_id):
        return list(self.collection.find({"user_id": user_id, "is_read": True}).sort("updated_at", -1).limit(1))

    def get_notifications_by_category(self, category):
        return list(self.collection.find({"category": category}))

    def get_notifications_by_category_subcategory(self, category, sub_category):
        return list(self.collection.find({"category": category, "sub_category": sub_category}))

try:
    import strawberry
    from strawberry.asgi import GraphQL
    from typing import List
except ImportError:
    print("Install with 'pip install strawberry-graphql'")
else:

    dao = NotificationDAO()

    def mongo_to_graphql(n: dict) -> dict:
        n_copy = dict(n)
        if "_id" in n_copy:
            n_copy["id"] = str(n_copy.pop("_id"))
        if n_copy.get("created_at"):
            n_copy["created_at"] = n_copy["created_at"].isoformat()
        if n_copy.get("updated_at"):
            n_copy["updated_at"] = n_copy["updated_at"].isoformat()
        if n_copy.get("deleted_at"):
            n_copy["deleted_at"] = n_copy["deleted_at"].isoformat()
        return n_copy

    @strawberry.type
    class Notification:
        id: str
        user_id: int
        category: str
        sub_category: str
        item: str
        created_at: str
        updated_at: Optional[str]
        deleted_at: Optional[str]
        is_read: bool

    @strawberry.type
    class Mutation:

        @strawberry.mutation
        def create_notification(self, user_id: int, category: str, sub_category: str, item: str) -> Notification:
            n = dao.create_notification(user_id, category, sub_category, item)
            return Notification(**mongo_to_graphql(n))

        @strawberry.mutation
        def create_notifications(self, user_id: int, category: str, sub_category: str, item_list: List[str]) -> List[Notification]:
            results = dao.create_notifications(user_id, category, sub_category, item_list)
            return [Notification(**mongo_to_graphql(n)) for n in results]

        @strawberry.mutation
        def update_notification(self, id: str, category: Optional[str] = None, sub_category: Optional[str] = None,
                                item: Optional[str] = None, is_read: Optional[bool] = None) -> Notification:
            n = dao.update_notification(ObjectId(id), category, sub_category, item, is_read)
            return Notification(**mongo_to_graphql(n))

    @strawberry.type
    class Query:

        @strawberry.field
        def get_unread_user_notifications(self, user_id: int) -> List[Notification]:
            results = dao.get_unread_user_notifications(user_id)
            return [Notification(**mongo_to_graphql(n)) for n in results]

        @strawberry.field
        def get_last_read_user_notification(self, user_id: int) -> Optional[Notification]:
            results = dao.get_last_read_user_notification(user_id)
            if results:
                return Notification(**mongo_to_graphql(results[0]))
            return None

        @strawberry.field
        def get_notifications_by_category(self, category: str) -> List[Notification]:
            results = dao.get_notifications_by_category(category)
            return [Notification(**mongo_to_graphql(n)) for n in results]

        @strawberry.field
        def get_notifications_by_category_subcategory(self, category: str, sub_category: str) -> List[Notification]:
            results = dao.get_notifications_by_category_subcategory(category, sub_category)
            return [Notification(**mongo_to_graphql(n)) for n in results]

    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQL(schema)