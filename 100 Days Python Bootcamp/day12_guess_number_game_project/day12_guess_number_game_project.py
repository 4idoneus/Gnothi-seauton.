#Guess the Number Game Project
# This is a simple number guessing game where the user has to guess a randomly generated number between 1 and 100.
# The user can choose between two difficulty levels: easy and hard. The game provides feedback on the user's guesses, indicating whether the guess is too high, too low, or correct. The user has a limited number of attempts based on the chosen difficulty level.
# The game continues until the user guesses the correct number or runs out of attempts.
# For the challenge I have to use global variable in some part but I know that using global variable is not a good practice in programming.
# If you want to see the code without global variable you can check the other version of this project in my repository. 
import art
import random

correct_number = random.randint(1,100) # The number that user will try to guess.

def choose_game_difficulty():
    game_mode = {
        "Hard Mode": "The user will have 5 attempts to guess the correct number.",
        "Easy Mode": "The user will have 10 attempts to guess the correct number.",
    }
    difficulty = input(f"""Choose the difficulty level.
    {game_mode}
        For \"Hard Mode\" type 'hard'.
        For \"Easy Mode\" type 'easy'.\nChosen difficulty : """).lower()
# The part that we will assign the attempt number according to the user's difficulty choice.
    if "hard" in difficulty:
        attempt_number = 5
        return attempt_number
    elif "easy" in difficulty:
        attempt_number = 10
        return attempt_number
    else:
        print("You type something wrong. Try again!")
        return choose_game_difficulty()
def choose_number(past_list):
    try:
        number = float(input("What number will you choose?\nChosen number: "))
        if number not in past_list:
            past_list.append(number)
            return number
        else:
            print("You choose this number before choose again.")
            return choose_number(past_list)
    except ValueError:
        print("The input you entered is not a valid number. Try again!")
        return choose_number(past_list)
def check_number(number):
    global correct_number
    difference = abs(number - correct_number)
    if number == correct_number:
        return True
    elif difference < 10:
        if number > correct_number  :
            print("-" * 50)
            print("High")
        else:
            print("-" * 50)
            print("Low")
    elif difference >= 10:
        if number > correct_number  :
            print("-" * 50)
            print("Too High")
        else:
            print("-" * 50)
            print("Too Low")
    return False

#The into part for the game that the rules will be explained. And first game will be start.
print(art.logo)
print("""Welcome to the Guess the Number Game!
        Rules are simple:
        1. Choose a difficulty level.
        2. When the question \"What number you will choose?\" choose a number between 1 to 100.
        3. After every wrong guess system will be give clues about the correct number's closeness to the chosen number.
        4. And most importantly don't forget to enjoy the game.""")

# print(f"DEBUG : The correct number : {correct_number}")

game_difficulty = choose_game_difficulty()
is_correct = False
is_finish = False
past_numbers = []
while not is_correct and not is_finish:
    game_difficulty -= 1
    chosen_number = choose_number(past_numbers)
    is_correct = check_number(chosen_number)
    if is_correct :
        print("Your guess is correct.")
        print(art.win)
    elif game_difficulty != 0 and game_difficulty > 0 :
        print("-" * 50)
        print(f"You guess is wrong. You have {game_difficulty} attempts left.")
    else:
        print("You don't have any attempt left.")
        print(f"Correct number was {correct_number}.")
        print(art.lose)
        is_finish = True
print("Thank you for playing. See you again!")