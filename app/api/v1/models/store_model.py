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
    def __init__(self):
        pass

# class ClassName(object):
#     def __init__(self, *args):
#         super(ClassName, self).__init__(*args))

    # def make_sale():
    #        pass
        
    # def create_product(self, id, name, curr_quantity, min_quantity, price, category):
    #     product ={
    #         'id' : id,
    #         'name' : name,
    #         'curr_quantity' : curr_quantity,
    #         'min_quantity' : min_quantity,
    #         'price' : price,
    #         }
    #     products.append(product)
    #     return "product successfully added"

    def get_all_products(self):
        return products

    def get_all_sales(self):
        return sales