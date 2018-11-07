import unittest
from app import app
import json

class TestSale(unittest.TestCase):
    '''Tests fetching of all products'''
    def test_get_products(self):
        self.response = app.test_client().get('/api/v1/products')
        self.assertEqual(self.response.status_code, 200)

    '''Tests fetching of specific products'''
    def test_get_specific_product(self):
        self.response = app.test_client().get('/api/v1/products/P1')
        self.assertEqual(self.response.status_code, 200)

    '''Tests creation of a new product'''
    def test_post_product(self):
        self.response = app.test_client().post(
            '/api/v1/products',
            data=json.dumps(
                dict(
                    product_id = 'x',
                    name = 'matchbox',
                    curr_qty = '5',
                    min_qty = '5',
                    price = '5',
                    category = 'household items'
                )
            ),
            content_type='application/json'
        )
        self.assertEqual(self.response.status_code, 201)

    '''Tests updating of specific products'''
    def test_update_specific_product(self):
        app.test_client().post(
            '/api/v1/products',
            data=json.dumps(
                dict(
                    product_id = 'x',
                    name = 'matchbox',
                    curr_qty = '5',
                    min_qty = '5',
                    price = '5',
                    category = 'household items'
                )
            ),
            content_type='application/json'
        )
        self.response = app.test_client().put('/api/v1/products?id=P1&qty=1')
        self.assertEqual(self.response.status_code, 204)