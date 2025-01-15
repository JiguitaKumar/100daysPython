from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#objects
my_menu = Menu()
my_coffe_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

#global variables
is_on = True

#logic
while is_on:
    order = input(f"What would you like? ({my_menu.get_items()}): ").lower()

    if order == "off":
        is_on = False
    elif order == "report":
        my_coffe_maker.report()
        my_money_machine.report()
    else:
        item = my_menu.find_drink(order)
        if item:
            if my_coffe_maker.is_resource_sufficient(item):
                if my_money_machine.make_payment(item.cost):
                    my_coffe_maker.make_coffee(item)
