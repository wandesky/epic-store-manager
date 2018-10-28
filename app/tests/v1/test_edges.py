import unittest
from app import app

class TestSale(unittest.TestCase):
    '''Testing the base url'''
    def test_base_url(self):
        self.response = app.test_client().get('/')
        self.assertEqual(self.response.status_code, 200)
    '''Testing url for version 1'''
    def test_v1_base_url(self):
        self.response = app.test_client().get('/api/v1/')
        self.assertEqual(self.response.status_code, 200)