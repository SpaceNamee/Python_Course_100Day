from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_work = CoffeeMaker()
pay = MoneyMachine()
drinks = Menu()
while True:
    user_input = input(f"What would you like?{drinks.get_items()}: ")

    if user_input == "latte" or user_input == "capuccino" or user_input == "espresso":

        drink = drinks.find_drink(user_input)

        if machine_work.is_resource_sufficient(drink):

            if pay.make_payment(drink.cost):
                machine_work.make_coffee(drink)
            else:
                print("Sorry, not enough money.")
    elif user_input == 'report':
        machine_work.report()
    elif user_input == "profit":
        pay.report()

