from app.api.v1.models.store_model import Store

class Sale(Store):
    def __init__(self, sale_id, product_id, quantity_sold, amount):
        Store.__init__(self, sale_id)
        self.product_id = product_id
        self.quantity_sold = quantity_sold
        self.amount = amount