# Notification Graphql examples

## Run tests
```
cd argo-demo-project
## GraphQL Setup

```

pip install uuid dotenv annotated-types anyio certifi charset-normalizer click colorama dnspython fastapi
pip install graphql-core h11 httpcore idna iniconfig packaging pluggy
pip install pydantic pydantic_core pymongo pytest python-dateutil python-multipart requests

pip install six sniffio starlette strawberry-graphql typing_extensions urllib3 uvicorn
APP_ENV=test;python -m uvicorn NotificationDAO:app --reload


python -m unittest TestNotificationDAO.py -v
```

## Run Graphql server
```
uvicorn NotificationDAO:graphql_app --reload
```

## Create a single notification
```
mutation MyMutation {
  createNotification(
    category: "system"
    item: "Welcome to the system"
    subCategory: "login"
    userId: 1
  ) {
    id
    userId
    category
    subCategory
    item
    isRead
    createdAt
    updatedAt
  }
}
```

## Create multiple notifications
```
mutation MyMutation {
  createNotifications(
    category: "alert"
    itemList: ["Password changed", "New device login"]
    subCategory: "security"
    userId: 2
  ) {
    id
    userId
    item
    createdAt
    isRead
  }
}
```

## Update a notification
```
mutation MyMutation {
  updateNotification(
    id: "68d18fc84dd8ca22b89d4d1d"
    item: "Updated welcome message "
    isRead: true
  ) {
    id
    userId
    item
    isRead
    updatedAt
  }
}
```

## Get last read notification
```
query MyQuery {
  getLastReadUserNotification(userId: 1) {
    id
    item
    isRead
    updatedAt
  }
}
```

## Get notification by category
```
query MyQuery {
  getNotificationsByCategory(category: "system") {
    id
    item
    createdAt
    category
    subCategory
  }
}
```

## Get notification by category, subcategory
```
query MyQuery {
  getNotificationsByCategorySubcategory(
    category: "alert"
    subCategory: "security"
  ) {
    category
    subCategory
    id
    item
    isRead
    createdAt
  }
}
```

## Get unread notifications 
```
query MyQuery {
  getUnreadUserNotifications(userId: 1) {
    createdAt
    isRead
    subCategory
    item
    category
    id
    updatedAt
  }
}
```