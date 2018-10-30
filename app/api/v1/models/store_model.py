class Store(object):
    #sales is a list of objects, each object storing information about an atomic sale
    sales = []
    products = [
        {
            'id' : 'dummyId',
            'name' : 'dummy name',
            'curr_quantity' : 'dummy curr_quantity',
            'min_quantity' : 'dummy min_quantity',
            'price' : 'dummy price'
        }
        
    ]

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