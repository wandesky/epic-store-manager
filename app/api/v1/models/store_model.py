products = [
    {
        'id' : 'dummyId',
        'name' : 'dummy name',
        'curr_quantity' : 'dummy curr_quantity',
        'min_quantity' : 'dummy min_quantity',
        'price' : 'dummy price'
    }
    
]

sales = [
    {
        'id' : 'dummySaleId',
        'product_id' : 'dummy id',
        'sold_quantity' : 'dummy curr_quantity',
        'price' : 'dummy product price * sold_quantity'
    }
]

class Store(object):
    sales = [
        {
            'id' : 'dummySaleId',
            'product_id' : 'dummy id',
            'sold_quantity' : 'dummy curr_quantity',
            'price' : 'dummy product price * sold_quantity'
        }
    ]
    def __init__(self, store_id = None):
        self.store_id = store_id

    def get_all_products(self):
        return products

    def get_all_sales(self):
        return sales
    
    def post_sale(self):
        sales.append(self)
        # try:
        #     if len(sales)>1:
        #         return "success"
        #     else:
        #         return "fail"
        if len(sales)>1:
            return "success"
        else:
            return "fail"