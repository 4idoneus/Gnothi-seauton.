# Coffee Machine Prject with OOP Principles
from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import logging
import time
logging.basicConfig(level=logging.DEBUG)

my_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

def admin(choice):

    if choice == "report":
        coffee_maker.report()
        my_money_machine.report()
        print("_" * 50)
    elif choice == "add":
        logging.debug("Adding ingredients to machine.")
        water = int(input("How much water you are going to add? "))
        milk = int(input("How much milk you are going to add? "))
        coffee = int(input("How much coffee you are going to add? "))
        coffee_maker.resources["water"] += water
        coffee_maker.resources["milk"] += milk
        coffee_maker.resources["coffee"] += coffee
    else:
        logging.debug(f"Admin type command {choice} is closing machine")
        print("The machine is closing.")
        quit()
def countdown(message, seconds=5):
    for n in range(seconds, 0, -1):
        time.sleep(1)
        print(f"\r{message}... {n-1}", end="")
    print()
def make_coffee(choice):
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
        countdown("Making the coffee")
        coffee_maker.make_coffee(drink)


while True:
    print(f"""☕Coffee machine!☕
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