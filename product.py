import random

class Product():
    products = []
    def __init__(self, name, minprice, maxprice):
        self.name = name
        self.minprice = minprice
        self.maxprice = maxprice
        self.price = random.randint(self.minprice, self.maxprice)
        self.shipqty = 5
        self.werehouseqty = 0

    @classmethod
    def create_products(cls):
        # Create product
        cls.products.append(Product("General Tools", 500, 3000))

        # Product Two
        cls.products.append(Product("Arms", 5000, 10000))
