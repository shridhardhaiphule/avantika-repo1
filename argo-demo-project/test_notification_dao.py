# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 21:12:33 2025

@author: Lenovo
"""

import unittest
import mongomock
from datetime import datetime, timezone
from bson.objectid import ObjectId

# --- NotificationDAO Class ---

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
        ).sort('created_at', -1))

    def get_last_read_user_notification(self, user_id):
        """Retrieves the most recently read notification for a user."""
        return self.collection.find_one(
            {'user_id': user_id, 'is_read': True, 'deleted_at': None},
            sort=[('updated_at', -1)]
        )

    def get_notifications_by_category(self, user_id, category):
        """Retrieves all active notifications for a user by category."""
        return list(self.collection.find(
            {'user_id': user_id, 'category': category, 'deleted_at': None}
        ).sort('created_at', -1))
    
    def get_notifications_by_category_and_sub_category(self, user_id, category, sub_category):
        """Retrieves notifications by category and sub-category."""
        return list(self.collection.find({
            'user_id': user_id, 
            'category': category, 
            'sub_category': sub_category,
            'deleted_at': None
        }).sort('created_at', -1))

    def get_notification_by_id(self, notification_id):
        """Retrieves a single notification by its ObjectId."""
        try:
            return self.collection.find_one({'_id': ObjectId(notification_id), 'deleted_at': None})
        except Exception:
            return None

# --- TestNotificationDAO Class ---

class TestNotificationDAO(unittest.TestCase):
    """
    Unit tests for the NotificationDAO class using a mock MongoDB database.
    """
    
    def setUp(self):
        """Set up a fresh, in-memory database for each test."""
        self.mock_client = mongomock.MongoClient()
        self.mock_db = self.mock_client.db
        self.dao = NotificationDAO(self.mock_db)
        
        # Populate with some mock data for testing
        self.user_id = "test_user_123"
        self.dao.collection.insert_many([
            {
                '_id': ObjectId('60c8e27c0c16b1b0e4000001'),
                'user_id': self.user_id,
                'category': 'system',
                'sub_category': 'update',
                'item': {'message': 'New features available.'},
                'is_read': True,
                'created_at': datetime(2023, 1, 1, 10, 0, 0, tzinfo=timezone.utc),
                'updated_at': datetime(2023, 1, 1, 11, 0, 0, tzinfo=timezone.utc),
                'deleted_at': None
            },
            {
                '_id': ObjectId('60c8e27c0c16b1b0e4000002'),
                'user_id': self.user_id,
                'category': 'inbox',
                'sub_category': 'message',
                'item': {'from': 'admin', 'body': 'Welcome to the platform!'},
                'is_read': False,
                'created_at': datetime(2023, 1, 2, 12, 0, 0, tzinfo=timezone.utc),
                'updated_at': datetime(2023, 1, 2, 12, 0, 0, tzinfo=timezone.utc),
                'deleted_at': None
            },
            {
                '_id': ObjectId('60c8e27c0c16b1b0e4000003'),
                'user_id': self.user_id,
                'category': 'system',
                'sub_category': 'alert',
                'item': {'message': 'Account password was recently changed.'},
                'is_read': False,
                'created_at': datetime(2023, 1, 3, 14, 0, 0, tzinfo=timezone.utc),
                'updated_at': datetime(2023, 1, 3, 14, 0, 0, tzinfo=timezone.utc),
                'deleted_at': None
            }
        ])

    def test_create_notification(self):
        """Test creating a single notification."""
        new_id = self.dao.create_notification(
            user_id=self.user_id,
            category='inbox',
            sub_category='reply',
            item={'message': 'Your question has been answered.'}
        )
        self.assertIsInstance(new_id, ObjectId)
        created_doc = self.dao.collection.find_one({'_id': new_id})
        self.assertIsNotNone(created_doc)
        self.assertEqual(created_doc['is_read'], False)

    def test_create_notifications(self):
        """Test creating multiple notifications."""
        new_ids = self.dao.create_notifications(
            user_id=self.user_id,
            category='appointments',
            sub_category='booking_alert',
            item_array=[{"message": "Test appointment one"}, {"message": "Test appointment two"}]
        )
        self.assertEqual(len(new_ids), 2)
        self.assertIsInstance(new_ids[0], ObjectId)

    def test_update_notification(self):
        """Test updating a notification's fields."""
        notification_id_to_update = '60c8e27c0c16b1b0e4000002'
        modified_count = self.dao.update_notification(notification_id_to_update, status=True)
        self.assertEqual(modified_count, 1)
        updated_doc = self.dao.collection.find_one({'_id': ObjectId(notification_id_to_update)})
        self.assertTrue(updated_doc['is_read'])
        
        # Test updating multiple fields
        new_item = {"from": "support", "body": "Your request has been handled."}
        modified_count = self.dao.update_notification(
            notification_id_to_update, 
            category='support', 
            sub_category='reply', 
            item=new_item
        )
        self.assertEqual(modified_count, 1)
        updated_doc = self.dao.collection.find_one({'_id': ObjectId(notification_id_to_update)})
        self.assertEqual(updated_doc['category'], 'support')
        self.assertEqual(updated_doc['item']['from'], 'support')

    def test_delete_notification(self):
        """Test soft deleting a notification."""
        notification_id_to_delete = '60c8e27c0c16b1b0e4000003'
        modified_count = self.dao.delete_notification(notification_id_to_delete)
        self.assertEqual(modified_count, 1)
        deleted_doc = self.dao.collection.find_one({'_id': ObjectId(notification_id_to_delete)})
        self.assertIsNotNone(deleted_doc['deleted_at'])
        
        # Test that the soft-deleted notification is not found by the DAO
        retrieved_doc = self.dao.get_notification_by_id(notification_id_to_delete)
        self.assertIsNone(retrieved_doc)
        
    def test_get_unread_user_notifications(self):
        """Test retrieving only unread notifications."""
        unread_notifications = self.dao.get_unread_user_notifications(self.user_id)
        self.assertEqual(len(unread_notifications), 2)
        categories = [n['category'] for n in unread_notifications]
        self.assertIn('inbox', categories)
        self.assertIn('system', categories)

    def test_get_last_read_user_notification(self):
        """Test retrieving the most recently read notification."""
        last_read_doc = self.dao.get_last_read_user_notification(self.user_id)
        self.assertEqual(last_read_doc['category'], 'system')
        self.assertEqual(last_read_doc['is_read'], True)

    def test_get_notifications_by_category(self):
        """Test retrieving notifications by a specific category."""
        system_notifications = self.dao.get_notifications_by_category(self.user_id, 'system')
        self.assertEqual(len(system_notifications), 2)
        sub_categories = [n['sub_category'] for n in system_notifications]
        self.assertIn('update', sub_categories)
        self.assertIn('alert', sub_categories)

    def test_get_notifications_by_category_and_sub_category(self):
        """Test retrieving notifications by category and sub-category."""
        alert_notifications = self.dao.get_notifications_by_category_and_sub_category(self.user_id, 'system', 'alert')
        self.assertEqual(len(alert_notifications), 1)
        self.assertEqual(alert_notifications[0]['item']['message'], 'Account password was recently changed.')

    def test_get_notification_by_id(self):
        """Test retrieving a single notification by its ObjectId."""
        notification_id = '60c8e27c0c16b1b0e4000002'
        notification = self.dao.get_notification_by_id(notification_id)
        self.assertIsNotNone(notification)
        self.assertEqual(notification['category'], 'inbox')
        self.assertEqual(notification['sub_category'], 'message')

if __name__ == '__main__':
    unittest.main()
