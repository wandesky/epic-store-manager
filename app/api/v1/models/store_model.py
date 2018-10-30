class Store(object):
    #sales is a list of objects, each object storing information about an atomic sale
    sales = []
    products = []

    def __init__(self, store_id = None):
        self.store_id = store_id

    def get_all_products(self = None):
        return Store.products

    def get_all_sales(self = None):
        return Store.sales
    
    def post_sale(self):
        prev_len = len(Store.sales)
        Store.sales.append(
            {
                "sale_id": self.store_id,
                "product_id": self.product_id,
                "quantity_sole": self.quantity_sold,
                "amount": self.amount
            }
        )
        if len(Store.sales)>prev_len:
            return "success"
        else:
            return "fail"

    def post_product(self):
        prev_len = len(Store.products)
        Store.products.append(
            {
                "product_id": self.store_id,
                "name": self.name,
                "curr_qty": self.curr_qty,
                "min_qty": self.min_qty,
                "price": self.price,
                "category": self.category
            }
        )
        if len(Store.products)>prev_len:
            return "success"
        else:
            return "fail"