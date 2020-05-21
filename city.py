import random
from product import Product
class City():
    cities = []
    def __init__(self, name, has_warehouse, has_bank, has_moneylender):
        self.name = name
        self.has_warehouse = has_warehouse
        self.has_bank = has_bank
        self.city_products = []
        self.has_moneylender = has_moneylender
        self.create_city_products()

    def create_city_products(self):
        for product in Product.products:
            self.city_products.append(CityProduct(self, product))

    @classmethod
    def create_city(self, **kargs):
        self.cities.append(City(**kargs))

class CityProduct(object):
    def __init__(self, city, product):
        self.city = city
        self.product = product
        self.generate_random_price() # se puede generar propiedades ene constructor por medio de una funcion

    def generate_random_price(self):
        self.price = random.randint(self.product.minprice, self.product.maxprice)
