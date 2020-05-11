## Supreme Store

"""
class Store
    product, price, category
"""

class Store:

    num_products = 0
    sale_discount = 0.50

    def __init__(self, product, price, category):
        self.product = product
        self.price = price
        self.category = category

        Store.num_products += 1
    

# class Joggers(store):
