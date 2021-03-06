class Store(object):
    #sales is a list of objects, each object storing information about an atomic sale
    sales = []
    products = []

    def __init__(self, store_id = None):
        self.store_id = store_id

    def get_all_products(self = None):
        return Store.products

    def get_specific_product(productId):
        print("The product ID is", productId)
        result = next((product for product in Store.products if product["product_id"] == str(productId)), {"message": "Item not found"})
        print("@@@@@@@@@@@@@@@@@@@@RESULT@@@@@@@@@@@@@@", result)
        return result

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
    
    def update_product(productId, qty):
        result = next((product for product in Store.products if product["product_id"] == str(productId)), {"message": "Item not found"})
        print("THE RESULT ################### #", result, "PRODUCT ID #######", productId, "QUANTITY ", qty)
        result["curr_qty"] = str(int(result["curr_qty"]) + int(qty))
        # Even though the above code works, the one below seems more effecient
        # for d in my_dicts:
        #     d.update((k, "value3") for k, v in d.iteritems() if k == str(productId))
        return "success"
