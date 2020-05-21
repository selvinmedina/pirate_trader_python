from product import Product
from city import City
import datetime
import os
import random
from PirateEncounter import PirateEncounter
from gamedata import load_city_data

FIRM_NAME = 'Firm Name: %s'
CANNONS = 'Cannons %d'
MENU_DIVIDER = '----------------------------------------'
GAME_TITLE = 'Python Pirate Trader 0.1A'

class GameManager(object):

    def __init__(self, **args):
        self.cash = args['cash']
        self.debt = args['debt']
        self.cannons = args['cannons']
        self.bank = 0
        self.maxshiphold = args['shiphold']
        self.ship_health = 100
        self.currentshiphold = 0
        # Create Products
        Product.create_products()

        # Create Cities
        load_city_data(City)
        self.currentcity = City.cities[0]
        self.current_date = datetime.datetime(2020, 5, 20, 13, 20, 59,55)
        self.firm_name = args['firm_name']

    def leave_port(self, cities, current_date):
        i = 1
        for city in cities:
            print("{0}) {1}".format(i, city.name))
            i += 1

        select_city = input('Which city do you wish to go to?: ')

        # Aumentar un dia
        current_date += datetime.timedelta(days=1)
        return (cities[int(select_city) - 1], current_date)

    def buy(self):
        buy_select = input('Which product do you want to buy? (1 - %d) - C)ancel :' % len(Product.products))
        if buy_select == "C":
            return

        city_product = self.currentcity.city_products[int(buy_select)-1]
        qty_to_buy = int(input('How many %s do you wish to buy? ' % city_product.product.name))
        cost_to_buy = city_product.price * qty_to_buy
        print("Cost to buy %d" % cost_to_buy)
        if cost_to_buy <= self.cash:
            if self.currentshiphold + qty_to_buy <= self.maxshiphold:
                self.cash-= cost_to_buy
                city_product.product.shipqty += qty_to_buy
                self.currentshiphold += qty_to_buy
            else:
                print('There is not enough space to hold those items.')
                input("Continue...")
        else:
            print("Sorry, You don't have enough money.")
            input("Continue...")

    def sell(self):
        sell_select = input('Which product do you want to sell? (1 - %d) - C)ancel :' % len(Product.products))
        if sell_select == "C":
            return
        city_product = self.currentcity.city_products[int(sell_select)-1]
        qty_to_sell = int(input('How many %s do you wish to sell? ' % city_product.product.name))

        if int(qty_to_sell) <= city_product.product.shipqty:
            self.cash += int(qty_to_sell) * city_product.price
            city_product.product.shipqty -= int(qty_to_sell)
            self.currentshiphold -= int(qty_to_sell)
        else:
            print("You don't have that many to sell")
            input('Press any key to continue...')

    def visit_bank(self):
        pass

    def display_products(self):
        i=1
        for cityproduct in self.currentcity.city_products:
            print(str(i) + ") " + cityproduct.product.name + " -- " + str(cityproduct.price) + " --- " + str(cityproduct.product.shipqty))
            i+=1

    def check_price_change(self):
        result = random.randint(0, 100)
        if result >= 75:
            for city_product in self.currentcity.city_products:
                city_product.generate_random_price()

    def increase_debt(self):
        self.debt *= 1.15

    def StartUp(self):
        game_running = True

        while game_running:
            # Limpiar la conosola
            os.system('clear')

            # Print info
            print(MENU_DIVIDER)
            print(GAME_TITLE)
            print(MENU_DIVIDER)
            print(FIRM_NAME % self.firm_name)
            print('Cash: {:,}'.format(self.cash))
            print(f'Debt {self.debt}')
            print(CANNONS % self.cannons)
            print('City: %s' % self.currentcity.name)
            print('Ship Health: %s' % self.ship_health)
            print('Date: {: %B %d, %Y}'.format(self.current_date))
            # http://strftime.org
            print(MENU_DIVIDER)

            print('-----City Products----------')
            self.display_products()
            has_bank_string = ''

            if self.currentcity.has_bank:
                has_bank_string = ' V)isit Bank,'

            has_moneylender = ""
            print('Menu: L)eave Port, B)uy, S)ell, T)ransfer Warehouse,%s %s Q)uit' % (has_bank_string, str(self.currentcity.has_moneylender)))
            menu_option = input('What is your Option?: ')

            if menu_option == "L":
                self.currentcity, self.current_date = self.leave_port(City.cities, self.current_date)
                self.check_price_change()
                self.increase_debt()
                pirates = PirateEncounter(self)

            elif menu_option == "B":
                self.buy()
            elif menu_option == "S":
                self.sell()
            elif menu_option == "V" and self.currentcity.has_bank:
                self.visit_bank()
            elif menu_option == "Q":
                game_running = False
