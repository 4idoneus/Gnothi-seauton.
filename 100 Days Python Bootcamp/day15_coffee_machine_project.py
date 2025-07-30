import logging
import time

logging.basicConfig(level=logging.DEBUG)

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
    "money": 0.0,
}

def admin(choice):
    if choice == "report":
        logging.debug("Show ingredients and money of machine.")
        print(
            "\n".join("{}: {}".format(k,v)for k,v in resources.items()).title()
        )
        print("_" * 50)
    elif choice == "add":
        logging.debug("Adding ingredients to machine.")
        water = int(input("How much water you are going to add? "))
        milk = int(input("How much milk you are going to add? "))
        coffee = int(input("How much coffee you are going to add? "))
        resources["water"] = resources["water"] + water
        resources["milk"] = resources["milk"] + milk
        resources["coffee"] = resources["coffee"] + coffee
        logging.debug(f"New resources: {resources.items()}")
    else:
        logging.debug(f"Admin type command {choice} is closing machine")
        print("The machine is closing.")
        quit()

def make_coffee(choice):
    def check_ingredients(coffee_name):
        machine_values = [resources.get(k) for k in ("water", "milk", "coffee")]
        logging.debug(machine_values)
        coffee_values = [MENU[coffee_name]["ingredients"].get(k, 0) for k in ("water", "milk", "coffee")]
        logging.debug(coffee_values)
        for i in range(len(machine_values)):
            control = machine_values[i] - coffee_values[i]
            if control <= 0:
                logging.debug("Not enough ingredient")
                print(f"Sorry there is not enough {list(resources.keys())[i]}.")
                coffe_cant_be_ready = True
                return coffe_cant_be_ready
        coffe_cant_be_ready = False
        return coffe_cant_be_ready
    def coin_handler(coffee_name):
        quarters = int(input("How many quartes are you going to give ? "))
        dimes = int(input("How many dimes are you going to give ? "))
        nickels = int(input("How many nickels are you going to give ? "))
        pennies = int(input("How many pennies are you going to give ? "))
        total_coin = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        coffee_price = MENU[coffee_name]["cost"]
        logging.debug(f"Coffee Cost: {coffee_price}, User's money: {coffee_price}")
        if total_coin < coffee_price:
            logging.debug("Not enough money")
            print(f"Sorry price for ${coffee_name} is {coffee_price}.You gave ${round(total_coin,3)}.\nMoney will be refunded.")
            for n in range(5, 0, -1):
                time.sleep(1)
                print(f"\rRefunding money... {n-1}", end="")
            print("\nMoney refunded.")
            no_available_coffee = True
            prep_coffee = False
        elif total_coin > coffee_price:
            print(f"Your change is ${round((total_coin - coffee_price),3)}. Change will be refunded.")
            resources["money"] += coffee_price
            for n in range(5, 0, -1):
                time.sleep(1)
                print(f"\rRefunding money... {n-1}", end="")
            print("\nMoney refunded.")
            no_available_coffee = False
            prep_coffee = True
        else:
            resources["money"] += coffee_price
            no_available_coffee = False
            prep_coffee = True

        return prep_coffee, no_available_coffee
    def prepare_coffee(coffee_name):
        logging.debug("Starting the make coffee")
        keys = ("water", "milk", "coffee")
        machine_values = [resources.get(k) for k in keys]
        coffee_values = [MENU[coffee_name]["ingredients"].get(k, 0) for k in ("water", "milk", "coffee")]
        for i in range(len(machine_values)):
            usage = machine_values[i] - coffee_values[i]
            logging.debug("Update ingredients")
            resources[keys[i]] = usage
        for n in range(5, 0, -1):
            time.sleep(1)
            print(f"\rPreparing coffee... {n-1}", end="")
        print("\nYour coffee is ready!")
        print("-" * 50)
        coffee_readiness = True
        prep_coffee = False
        logging.debug("Return to the main menu.")
        return prep_coffee, coffee_readiness

    coffee_ready = check_ingredients(choice)
    while not coffee_ready:
        logging.debug("Enough ingredient")
        prepare_the_coffee,coffee_ready = coin_handler(choice)
        while prepare_the_coffee:
            logging.debug("Enough money")
            prepare_the_coffee, coffee_ready= prepare_coffee(choice)

while True:
    print(f"""Coffee machine!
    {"-" * 50}
    How To Use :
        1.Select the coffee type you want.
        2.Insert your coins by type.
        3.Wait for the coffee to be ready.
        4.Get your coffee.
        5.Enjoy it.
    {"-" * 50}""")
    response = input(f"""What would you like?
- Espresso
- Latte
- Cappuccino\n""").lower()
    print("_" * 50)
    if response in ["report","off","add"]:
        admin(response)
    elif response in ["espresso","latte","cappuccino"]:
        make_coffee(response)
    else:
        print("Invalid type. Try again!")
