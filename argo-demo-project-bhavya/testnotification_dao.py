# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:43:49 2025

@author: Lenovo
"""

import unittest
from datetime import datetime, timezone
from bson.objectid import ObjectId
import mongomock
from notification_dao import NotificationDAO

class TestNotificationDAO(unittest.TestCase):
    def setUp(self):
        # Using an in-memory mock MongoDB
        self.client = mongomock.MongoClient()
        self.db = self.client['test_db']
        self.dao = NotificationDAO(self.db)
        self.user_id = 'user123'

    def test_create_notification(self):
        notification_id = self.dao.create_notification(
            self.user_id, 'category1', 'sub1', 'item1'
        )
        self.assertIsInstance(notification_id, ObjectId)
        doc = self.db['notifications'].find_one({'_id': notification_id})
        self.assertEqual(doc['user_id'], self.user_id)
        self.assertFalse(doc['is_read'])

    def test_create_notifications(self):
        items = ['item1', 'item2']
        ids = self.dao.create_notifications(self.user_id, 'cat', 'sub', items)
        self.assertEqual(len(ids), 2)
        docs = list(self.db['notifications'].find({'user_id': self.user_id}))
        self.assertEqual(len(docs), 2)

    def test_update_notification(self):
        notification_id = self.dao.create_notification(
            self.user_id, 'cat', 'sub', 'item'
        )
        modified_count = self.dao.update_notification(notification_id, status=True)
        self.assertEqual(modified_count, 1)
        doc = self.db['notifications'].find_one({'_id': notification_id})
        self.assertTrue(doc['is_read'])

    def test_delete_notification(self):
        notification_id = self.dao.create_notification(
            self.user_id, 'cat', 'sub', 'item'
        )
        modified_count = self.dao.delete_notification(notification_id)
        self.assertEqual(modified_count, 1)
        doc = self.db['notifications'].find_one({'_id': notification_id})
        self.assertIsNotNone(doc['deleted_at'])

    def test_get_unread_user_notifications(self):
        self.dao.create_notification(self.user_id, 'cat', 'sub', 'item1')
        self.dao.create_notification(self.user_id, 'cat', 'sub', 'item2')
        unread = self.dao.get_unread_user_notifications(self.user_id)
        self.assertEqual(len(unread), 2)

    def test_get_last_read_user_notification(self):
        id1 = self.dao.create_notification(self.user_id, 'cat', 'sub', 'item1')
        self.dao.update_notification(id1, status=True)
        last_read = self.dao.get_last_read_user_notification(self.user_id)
        self.assertEqual(last_read['_id'], id1)

    def test_get_notifications_by_category(self):
        self.dao.create_notification(self.user_id, 'cat1', 'sub1', 'item1')
        self.dao.create_notification(self.user_id, 'cat2', 'sub2', 'item2')
        cat1_notifications = self.dao.get_notifications_by_category(self.user_id, 'cat1')
        self.assertEqual(len(cat1_notifications), 1)
        self.assertEqual(cat1_notifications[0]['category'], 'cat1')

    def test_get_notifications_by_category_and_sub_category(self):
        self.dao.create_notification(self.user_id, 'cat', 'sub1', 'item1')
        self.dao.create_notification(self.user_id, 'cat', 'sub2', 'item2')
        results = self.dao.get_notifications_by_category_and_sub_category(self.user_id, 'cat', 'sub1')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['sub_category'], 'sub1')

    def test_get_notification_by_id(self):
        notification_id = self.dao.create_notification(self.user_id, 'cat', 'sub', 'item')
        doc = self.dao.get_notification_by_id(notification_id)
        self.assertIsNotNone(doc)
        self.assertEqual(doc['_id'], notification_id)

if __name__ == '__main__':
    unittest.main()
