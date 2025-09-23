import unittest
from NotificationDAO import NotificationDAO
from bson import ObjectId

class TestNotificationDAO(unittest.TestCase):

    def setUp(self):
        self.dao = NotificationDAO(db_name="argo_demo_test")
        self.dao.collection.delete_many({})

    def test_create_notification(self):
        n = self.dao.create_notification(1, "system", "login", "Welcome to the system")
        self.assertEqual(n["user_id"], 1)
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

    def test_update_notification(self):
        n = self.dao.create_notification(1, "system", "login", "Hello")
        n_id = n["_id"]
        self.dao.update_notification(n_id, item="Updated", is_read=True)
        updated = self.dao.collection.find_one({"_id": n_id})
        self.assertTrue(updated["is_read"])
        self.assertEqual(updated["item"], "Updated")

    def test_get_unread_notifications(self):
        self.dao.create_notification(1, "system", "login", "Hello")
        unread = self.dao.get_unread_user_notifications(1)
        self.assertEqual(len(unread), 1)
        self.assertFalse(unread[0]["is_read"])

    def test_get_last_read_notification(self):
        n1 = self.dao.create_notification(1, "system", "login", "Hello1")
        n2 = self.dao.create_notification(1, "system", "login", "Hello2")
        self.dao.update_notification(n1["_id"], is_read=True)
        last_read = self.dao.get_last_read_user_notification(1)
        self.assertEqual(len(last_read), 1)
        self.assertEqual(last_read[0]["_id"], n1["_id"])
        self.assertTrue(last_read[0]["is_read"])

    def test_get_notifications_by_category(self):
        self.dao.create_notification(1, "system", "login", "Hello")
        self.dao.create_notification(1, "alert", "login", "Alert message")
        system_notifications = self.dao.get_notifications_by_category("system")
        alert_notifications = self.dao.get_notifications_by_category("alert")
        self.assertEqual(len(system_notifications), 1)
        self.assertEqual(len(alert_notifications), 1)

    def test_get_notifications_by_category_subcategory(self):
        self.dao.create_notification(1, "system", "login", "Hello")
        self.dao.create_notification(1, "system", "alert", "Alert message")
        results = self.dao.get_notifications_by_category_subcategory("system", "login")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["sub_category"], "login")

if __name__ == "__main__":
    unittest.main()
