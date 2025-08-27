import unittest
from addition_api import app

class AdditionApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_success(self):
        response = self.app.get('/add?a=2&b=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'result': 5.0})

    def test_add_missing_params(self):
        response = self.app.get('/add?a=2')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_add_invalid_params(self):
        response = self.app.get('/add?a=foo&b=bar')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

if __name__ == '__main__':
    unittest.main()