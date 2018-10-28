import unittest
import app
# from app import create_app
from instance.config import app_config
this_app = app.create_app()

class TestSale(unittest.TestCase):
    # this_app = app.create_app('development')
    # @this_app.route('/')
    # def test_base_url(self):
    #     response = this_app.test_client.get('/')
    #     self.assertEqual(response.status_code, 200)

    @this_app.route('/')
    def test_base_url(self):
        response = this_app.test_client().get('/')
        print('*********The response is: ',response)
        self.assertEqual(response.status_code, 200)
