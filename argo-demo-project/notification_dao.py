# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 21:00:28 2025

@author: Lenovo
"""

import pymongo
from datetime import datetime, timezone
from bson.objectid import ObjectId

# --- The NotificationDAO class from your provided file ---

class NotificationDAO:
    """
    Data Access Object for the 'notifications' collection in MongoDB.
    Handles all CRUD operations related to notifications for a user.
    """
    def __init__(self, db):
        self.collection = db['notifications']

    # --- Mutations (Write Operations) ---

    def create_notification(self, user_id, category, sub_category, item):
        """Creates a single new notification."""
        doc = {
            'user_id': user_id,
            'category': category,
            'sub_category': sub_category,
            'item': item,
            'is_read': False,
            'created_at': datetime.now(timezone.utc),
            'updated_at': datetime.now(timezone.utc),
            'deleted_at': None
        }
        return self.collection.insert_one(doc).inserted_id

    def create_notifications(self, user_id, category, sub_category, item_array):
        """Creates multiple notifications from an array of items."""
        docs = [
            {
                'user_id': user_id,
                'category': category,
                'sub_category': sub_category,
                'item': item,
                'is_read': False,
                'created_at': datetime.now(timezone.utc),
                'updated_at': datetime.now(timezone.utc),
                'deleted_at': None
            }
            for item in item_array
        ]
        if not docs:
            return []
        return self.collection.insert_many(docs).inserted_ids

    def update_notification(self, notification_id, category=None, sub_category=None, item=None, status=None):
        """
        Updates a notification's fields.
        :param notification_id: The ObjectId of the notification to update.
        :param new_data: A dictionary of fields to update, e.g., {'is_read': True}.
        """
        update_fields = {'updated_at': datetime.now(timezone.utc)}
        if category is not None:
            update_fields['category'] = category
        if sub_category is not None:
            update_fields['sub_category'] = sub_category
        if item is not None:
            update_fields['item'] = item
        if status is not None:
            update_fields['is_read'] = status
        
        result = self.collection.update_one(
            {'_id': ObjectId(notification_id)},
            {'$set': update_fields}
        )
        return result.modified_count

    def delete_notification(self, notification_id):
        """Soft deletes a single notification."""
        result = self.collection.update_one(
            {'_id': ObjectId(notification_id)},
            {'$set': {'deleted_at': datetime.now(timezone.utc)}}
        )
        return result.modified_count

    # --- Queries (Read Operations) ---

    def get_unread_user_notifications(self, user_id):
        """Retrieves all unread notifications for a user."""
        return list(self.collection.find(
            {'user_id': user_id, 'is_read': False, 'deleted_at': None}
        ).sort('created_at', pymongo.DESCENDING))

    def get_last_read_user_notification(self, user_id):
        """Retrieves the most recently read notification for a user."""
        return self.collection.find_one(
            {'user_id': user_id, 'is_read': True, 'deleted_at': None},
            sort=[('updated_at', pymongo.DESCENDING)]
        )

    def get_notifications_by_category(self, user_id, category):
        """Retrieves all active notifications for a user by category."""
        return list(self.collection.find(
            {'user_id': user_id, 'category': category, 'deleted_at': None}
        ).sort('created_at', pymongo.DESCENDING))
    
    def get_notifications_by_category_and_sub_category(self, user_id, category, sub_category):
        """Retrieves notifications by category and sub-category."""
        return list(self.collection.find({
            'user_id': user_id, 
            'category': category, 
            'sub_category': sub_category,
            'deleted_at': None
        }).sort('created_at', pymongo.DESCENDING))

    def get_notification_by_id(self, notification_id):
        """Retrieves a single notification by its ObjectId."""
        try:
            return self.collection.find_one({'_id': ObjectId(notification_id), 'deleted_at': None})
        except Exception:
            return None


# --- Main script to connect and populate data ---
if __name__ == "__main__":
    # Define your connection string and database name
    # Replace this with your actual connection string if you're not using localhost
    CONNECTION_STRING = "mongodb://localhost:27017/"  
    DATABASE_NAME = "dental_tourism"

    try:
        # Establish a connection to the MongoDB client
        client = pymongo.MongoClient(CONNECTION_STRING)
        # Select the database
        db = client[DATABASE_NAME]
        
        print(f"Successfully connected to the database: '{DATABASE_NAME}'")
        
        # Instantiate the NotificationDAO class with the database connection
        notification_manager = NotificationDAO(db)
        
        # Define the user ID for our example data
        user_id = "us_patient_123"

        # --- Populate the database with sample notifications ---
        
        print("\n--- Populating a single notification ---")
        notification_id = notification_manager.create_notification(
            user_id, "account", "login", {"message": "New device login detected from New York, USA."}
        )
        print(f"Created a new notification with ID: {notification_id}")

        print("\n--- Populating multiple notifications ---")
        item_array = [
            {"message": "Your booking for May 15th has been confirmed."},
            {"message": "A reminder for your appointment on May 20th."}
        ]
        
        notification_ids = notification_manager.create_notifications(
            user_id, "appointments", "booking_alert", item_array
        )
        print(f"Created {len(notification_ids)} new notifications.")
        
        print("\nData population complete. You can now view this data in MongoDB Compass!")
        
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
        print("Please make sure your MongoDB instance is running and your connection string is correct.")
    finally:
        if 'client' in locals():
            client.close()
