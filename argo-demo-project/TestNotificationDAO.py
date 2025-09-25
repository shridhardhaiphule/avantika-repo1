import unittest
from NotificationDAO import NotificationDAO
from bson import ObjectId
import uuid

class TestNotificationDAO(unittest.TestCase):

    def setUp(self):
        self.dao = NotificationDAO(db_name="argo_demo_test")
        # self.dao.collection.delete_many({})

    def test_create_notification(self):
        uuidStr = str(uuid.uuid4())
        n = self.dao.create_notification(uuidStr, "system", "login", "Welcome to the system")
        self.assertEqual(n["user_id"], uuidStr)
        self.assertFalse(n["is_read"])
        self.assertEqual(n["category"], "system")
        self.assertEqual(n["sub_category"], "login")
        self.assertEqual(n["item"], "Welcome to the system")

    def test_create_multiple_notifications(self):
        items = ["Password changed", "New device login"]
        results = self.dao.create_notifications(1, "system", "alert", items)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["item"], "Password changed")
        self.assertEqual(results[1]["item"], "New device login")

    def test_get_unread_notifications(self):
        uuidStr = str(uuid.uuid4())
        self.dao.create_notification(uuidStr, "system", "login", "Hello test_get_unread_notifications")
        unreadNotifications = self.dao.get_unread_user_notifications(uuidStr)
        self.assertTrue(len(unreadNotifications) > 0)
        self.assertFalse(unreadNotifications[0]["is_read"])

    def test_update_notification(self):
        uuidStr = str(uuid.uuid4())
        n = self.dao.create_notification(uuidStr, "system", "login", "Hello")
        n_id = n["_id"]
        text2Update = "Updated test_update_notification"
        self.dao.update_notification(n_id, item=text2Update, is_read=True)
        updated = self.dao.collection.find_one({"_id": n_id})
        self.assertTrue(updated["is_read"])
        self.assertEqual(updated["item"], text2Update)

    def test_get_last_read_notification(self):
        uuidStr = str(uuid.uuid4())
        n1 = self.dao.create_notification(uuidStr, "system", "login", "Hello1 test_get_last_read_notification")
        n2 = self.dao.create_notification(uuidStr, "system", "login", "Hello2 test_get_last_read_notification")
        self.dao.update_notification(n1["_id"], is_read=True)
        last_read = self.dao.get_last_read_user_notification(uuidStr)
        self.assertEqual(len(last_read), 1)
        self.assertEqual(last_read[0]["_id"], n1["_id"])
        self.assertTrue(last_read[0]["is_read"])

    def test_get_notifications_by_category(self):
        uuidStr = str(uuid.uuid4())
        self.dao.create_notification(uuidStr, "system", "login", "Hello")
        self.dao.create_notification(uuidStr, "alert", "login", "Alert message")
        system_notifications = self.dao.get_notifications_by_category("system")
        alert_notifications = self.dao.get_notifications_by_category("alert")
        self.assertTrue(len(system_notifications) > 0)
        self.assertTrue(len(alert_notifications) > 0)

    def test_get_notifications_by_category_subcategory(self):
        uuidStr = str(uuid.uuid4())
        self.dao.create_notification(uuidStr, "system_test_get_notifications_by_category_subcategory", "login", "Hello")
        self.dao.create_notification(uuidStr, "system_test_get_notifications_by_category_subcategory", "alert", "Alert message")
        results = self.dao.get_notifications_by_category_subcategory("system_test_get_notifications_by_category_subcategory", "login")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["sub_category"], "login")

    def tearDown(self):
        # self.dao.collection.delete_many({})
        self.dao.client.close()
if __name__ == "__main__":
    unittest.main()
