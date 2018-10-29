import unittest
from app import app

class TestSale(unittest.TestCase):
    '''Tests fetching of all products'''
    def test_get_products(self):
        self.response = app.test_client().get('/api/v1/products')
        self.assertEqual(self.response.status_code, 200)

    '''Tests fetching of specific products'''
    def test_get_specific_products(self):
        self.response = app.test_client().get('/api/v1/products/<productId>')
        pass

    '''Tests creation of a new product'''
    def test_post_product(self):
        self.response = app.test_client().post('/api/v1/products')
        pass
