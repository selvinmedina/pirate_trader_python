from gamemanager import GameManager

MENU_DIVIDER = '----------------------------------------'

WELCOME_MESSAGE = 'Welcome to Python Pirate Trader'


GET_STARTING_OPTIONS = 'How do you wish to start. 1) Cash $ Debt  2) Cannons no debt: '
CASH = "Cash= {:,}"
GET_FIRM_NAME ='Please enter your firm Name: '

def welcome_message():
    print(WELCOME_MESSAGE)

def get_firm_name():
    return input(GET_FIRM_NAME)

def get_starting_options():
    starting_options = input(GET_STARTING_OPTIONS)

    if starting_options == "1":
        return (1000000, 250000, 0)
    else:
        return (0,0,5)

# Start Game
welcome_message()

firm_name = get_firm_name()
cash, debt, cannons = get_starting_options()

game = GameManager(firm_name=firm_name,cash= cash,cannons= cannons,debt= debt,shiphold= 100)

game.StartUp()

