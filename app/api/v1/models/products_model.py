from app.api.v1.models.store_model import Store

class Product(Store):
    def __init__(self, product_id, name, curr_quantity, min_quantity, price, category):
        Store.__init__(self, product_id)
        self.name = name
        self.curr_qty = curr_quantity
        self.min_qty = min_quantity
        self.price = price
        self.category = category
