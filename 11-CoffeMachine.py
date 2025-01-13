MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5, 
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5, 
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0, 
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coffeMachine():

    money = 0.0
    operational = True

    while operational:

        request = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if request == "off":
            operational = False
        elif request == "report":
            report(money)
        elif request in ("espresso", "latte", "cappuccino"):
            if enough_resources(request):
                price = MENU[request]["cost"]
                if payment(price):
                    money += price
                    update_resource(request)


def report(cash):
    for resource, amount in resources.items():
        print(f"{resource.title()}: {amount}")
    
    print(f"Money: ${cash}")


def enough_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    
    return True


def update_resource(drink):
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] = resources[ingredient] - MENU[drink]["ingredients"][ingredient]


def payment(amount_to_be_received):
    
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    amount_inserted = quarters + dimes + nickels + pennies

    if amount_inserted < amount_to_be_received:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(amount_inserted - amount_to_be_received, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
            return True


coffeMachine()
