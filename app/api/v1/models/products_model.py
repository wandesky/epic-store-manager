from store_model import Store

class Product(Store):
    def __init__(self, id, name, curr_quantity, min_quantity, price, category):
        self.id = id
        self.name = name
        self.curr_quantity = curr_quantity
        self.min_quantity = min_quantity
        self.price = price
