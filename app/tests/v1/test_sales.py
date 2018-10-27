import unittest
from app import create_app
from isntanance.config import app_config

class TestSale(unittest.TestCase):
    @app.route('/')
    def test_base_url(self):
         self.assertEqual(response.status_code, 200)
