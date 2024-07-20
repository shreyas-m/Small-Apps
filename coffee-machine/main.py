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

profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

ans = ""


def check_resources(water: int, coffee: int, milk: int = 0):
    if resources["water"] < water:
        print("Sorry there is not enough water!")
        return False
    elif resources["coffee"] < coffee:
        print("Sorry there is not enough coffee!")
        return False
    elif resources["milk"] < milk:
        print("Sorry there is not enough milk!")
        return False
    else:
        return True


def process_coins(drink_cost):
    print("Insert Coins:")
    quarters = float(input("Quarters:"))
    dimes = float(input("Dimes:"))
    nickles = float(input("Nickles:"))
    pennies = float(input("Pennies:"))
    total_value = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    print(f"Total value:{total_value:.2f}")
    if total_value > drink_cost:
        refund = total_value - drink_cost
        print(f"Thank you, here is {refund:.2f} in change.")
        return True
    elif total_value == drink_cost:
        return True
    else:
        print("Sorry that's not enough money. Money refunded..")
        return False


def deduct_resources(water: int, coffee: int, milk: int = 0):
    resources["water"] = resources["water"] - water
    resources["coffee"] = resources["coffee"] - coffee
    resources["milk"] = resources["milk"] - milk


def make_espresso():
    if check_resources(water=MENU["espresso"]["ingredients"]["water"],
                       coffee=MENU["espresso"]["ingredients"]["coffee"]):
        if process_coins(MENU["espresso"]["cost"]):
            deduct_resources(water=MENU["espresso"]["ingredients"]["water"],
                             coffee=MENU["espresso"]["ingredients"]["coffee"])
            return MENU["espresso"]["cost"]
        else:
            return 0
    else:
        return 0


def make_latte():
    if check_resources(water=MENU["latte"]["ingredients"]["water"],
                       coffee=MENU["latte"]["ingredients"]["coffee"],
                       milk=MENU["latte"]["ingredients"]["milk"]):
        if process_coins(MENU["espresso"]["cost"]):
            deduct_resources(water=MENU["latte"]["ingredients"]["water"],
                             coffee=MENU["latte"]["ingredients"]["coffee"],
                             milk=MENU["latte"]["ingredients"]["milk"])
            return MENU["latte"]["cost"]
        else:
            return 0
    else:
        return 0


def make_cappuccino():
    if check_resources(water=MENU["cappuccino"]["ingredients"]["water"],
                       coffee=MENU["cappuccino"]["ingredients"]["coffee"],
                       milk=MENU["cappuccino"]["ingredients"]["milk"]):
        if process_coins(MENU["espresso"]["cost"]):
            deduct_resources(water=MENU["cappuccino"]["ingredients"]["water"],
                             coffee=MENU["cappuccino"]["ingredients"]["coffee"],
                             milk=MENU["cappuccino"]["ingredients"]["milk"])
            return MENU["cappuccino"]["cost"]
        else:
            return 0
    else:
        return 0


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")


while ans != "off":
    ans = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if ans == "report":
        print_report()
    elif ans == "espresso":
        profit += make_espresso()
        print("Here is your Espresso. Enjoy!")
    elif ans == "latte":
        profit += make_latte()
        print("Here is your Latte. Enjoy!")
    elif ans == "cappuccino":
        profit += make_cappuccino()
        print("Here is your Cappuccino. Enjoy!")
    elif ans == "off":
        print("Bye!")
    else:
        print("Invalid input")
