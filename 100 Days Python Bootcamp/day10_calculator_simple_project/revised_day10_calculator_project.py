
import art
def add(n1, n2):
    return n1 + n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    if n2 == 0:
        return "Error : Division by zero"
    return n1 / n2
def subtract(n1,n2):
    return n1 - n2
def get_number(number,number1):
    try:
        return float(number)
    except ValueError:
        print("Invalid number.Try again.")
        if number1 is None:
            perform_calculation(None)
        else:
            perform_calculation(number1)

operations_dic = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,

}

def calculator(num1,num2,operation):
    if operation in operations_dic:
        result = operations_dic[operation](num1,num2)
    else:
        result = f"The operation you want to do,{operation},is not supported. We are sorry for the inconvenience. Try other operations. "
    return result

def perform_calculation(number1=None):
    if number1 is None:
        number1 = get_number(input("Please enter your first number: "),number1)
    number2 = get_number(input("Please enter your second number: "),number1)
    operation_of_choice = input("Please choose and type the operator you want.\n+\n-\n*\n/\nYour choice: ")
    result = calculator(number1, number2, operation_of_choice)
    print(f"{number1} {operation_of_choice} {number2} = {result}")
    if "Error" in str(result):
        print("Because of the error. Starting the selection of number two sequence again.")
        return perform_calculation(number1)
    return want_to_continue(result)


def want_to_continue(result):
    choice_of_user = input("If you want to continue with this result please type \"yes\" or \nYou want to start a brand new calculation please type \"no\"\nIf you want to exit from program please write \"quit\" : ").lower()
    if choice_of_user == "yes":
        return perform_calculation(result)
    elif choice_of_user == "no":
        return perform_calculation(number1=None)
    elif choice_of_user == "quit":
        return True
    else:
        print(f"We don't have a choice like {choice_of_user}. So program will close itself.")
        return True

finish_the_calculation = False
continue_the_calculation = False
print(art.logo)
print("Welcome to the calculator let's start!")
while not finish_the_calculation:
    finish_the_calculation = perform_calculation(number1=None)
print("Thank you for using our calculator. See you soon!")

