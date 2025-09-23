# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 21:11:58 2025

@author: Lenovo
"""

import unittest
from datetime import datetime, timezone
from bson.objectid import ObjectId
import mongomock   # mock MongoDB for testing
from notification_dao import NotificationDAO

class TestNotificationDAO(unittest.TestCase):

    def setUp(self):
        # create a mock MongoDB client and collection
        self.mock_client = mongomock.MongoClient()
        self.db = self.mock_client['test_db']
        self.dao = NotificationDAO(self.db)
        self.user_id = "test_user_001"

    def test_create_notification(self):
        notif_id = self.dao.create_notification(
            self.user_id, "account", "login", "Test Notification"
        )
        self.assertIsInstance(notif_id, ObjectId)

        saved = self.db['notifications'].find_one({"_id": notif_id})
        self.assertEqual(saved['user_id'], self.user_id)
        self.assertEqual(saved['category'], "account")
        self.assertEqual(saved['title'], "Test Notification")

    def test_create_multiple_notifications(self):
        title_array = [
            {"title": "First", "message_body": "First body"},
            {"title": "Second", "message_body": "Second body"}
        ]
        ids = self.dao.create_notifications(self.user_id, "cat", "subcat", title_array)
        self.assertEqual(len(ids), 2)

        saved = list(self.db['notifications'].find({"user_id": self.user_id}))
        self.assertEqual(len(saved), 2)

    def test_update_notification(self):
        notif_id = self.dao.create_notification(self.user_id, "account", "login", "Update Me")
        modified = self.dao.update_notification(notif_id, title="Updated Title", status="read")
        self.assertEqual(modified, 1)

        saved = self.db['notifications'].find_one({"_id": notif_id})
        self.assertEqual(saved['title'], "Updated Title")
        self.assertEqual(saved['status'], "read")

    def test_delete_notification(self):
        notif_id = self.dao.create_notification(self.user_id, "account", "login", "Delete Me")
        modified = self.dao.delete_notification(notif_id)
        self.assertEqual(modified, 1)

        saved = self.db['notifications'].find_one({"_id": notif_id})
        self.assertIsNotNone(saved['deleted_at'])

    def test_get_unread_notifications(self):
        self.dao.create_notification(self.user_id, "alerts", "security", "Unread Test")
        unread = self.dao.get_unread_user_notifications(self.user_id)
        self.assertEqual(len(unread), 1)
        self.assertEqual(unread[0]['title'], "Unread Test")
    def test_get_last_read_user_notification(self):
        # create two notifications: one unread, one read
        notif_id1 = self.dao.create_notification(self.user_id, "account", "login", "Unread Notif")
        notif_id2 = self.dao.create_notification(self.user_id, "account", "login", "Read Notif")

        # mark the second one as read (and more recent)
        self.dao.update_notification(notif_id2, is_read=True, status="read")

        last_read = self.dao.get_last_read_user_notification(self.user_id)
        self.assertIsNotNone(last_read)
        self.assertEqual(last_read['title'], "Read Notif")
        self.assertTrue(last_read['is_read'])

    def test_get_notifications_by_category(self):
        # create notifications under same category
        self.dao.create_notification(self.user_id, "alerts", "general", "First Alert")
        self.dao.create_notification(self.user_id, "alerts", "security", "Second Alert")
        
        results = self.dao.get_notifications_by_category(self.user_id, "alerts")
        self.assertEqual(len(results), 2)
        self.assertIn("First Alert", [r['title'] for r in results])

    def test_get_notifications_by_category_and_sub_category(self):
        self.dao.create_notification(self.user_id, "alerts", "general", "General Alert")
        self.dao.create_notification(self.user_id, "alerts", "security", "Security Alert")
        
        results = self.dao.get_notifications_by_category_and_sub_category(
            self.user_id, "alerts", "security"
        )
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['sub_category'], "security")
        self.assertEqual(results[0]['title'], "Security Alert")

    def test_get_notification_by_id(self):
        notif_id = self.dao.create_notification(self.user_id, "account", "login", "Fetch Me")
        fetched = self.dao.get_notification_by_id(notif_id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched['title'], "Fetch Me")

if __name__ == '__main__':
    unittest.main()
