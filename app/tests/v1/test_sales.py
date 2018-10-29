import unittest
from app import app
import json

class TestSale(unittest.TestCase):
    '''Tests fetching of all sale records'''
    def test_get_sales(self):
        self.response = app.test_client().get('/api/v1/sales')
        self.assertEqual(self.response.status_code, 200)

    '''Tests fetching of a single specific sale records'''
    def test_get_specific_sale(self):
        # self.response = app.test_client().get('/api/v1/sales/<saleId>')
        pass

    '''Tests creation of a sale order'''
    def test_post_sales(self):
        self.response = app.test_client().post(
            '/api/v1/sales',
            data=json.dumps(
                dict(
                    sale_id = '1',
                    product_id = '1',
                    quantity_sold = '5',
                    amount = '5'
                )
            ),
            content_type='application/json'
        )
        self.assertEqual(self.response.status_code, 201)