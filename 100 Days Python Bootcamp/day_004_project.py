# Simple Rock, Paper, Scissors Game
# This is a simple game where the user plays against the computer in a game of Rock,
import random

deuce = '''
 _______   _______  __    __    ______  _______ 
|       \\ |   ____||  |  |  |  /      ||   ____|
|  .--.  ||  |__   |  |  |  | |  ,----'|  |__   
|  |  |  ||   __|  |  |  |  | |  |     |   __|  
|  '--'  ||  |____ |  `--'  | |  `----.|  |____ 
|_______/ |_______| \\______/   \\______||_______|
'''
win = '''
____    ____  ______    __    __     ____    __    ____  __  .__   __. 
\\   \\  /   / /  __  \\  |  |  |  |    \\   \\  /  \\  /   / |  | |  \\ |  | 
 \\   \\/   / |  |  |  | |  |  |  |     \\   \\/    \\/   /  |  | |   \\|  | 
  \\_    _/  |  |  |  | |  |  |  |      \\            /   |  | |  . `  | 
    |  |    |  `--'  | |  `--'  |       \\    /\\    /    |  | |  |\\   | 
    |__|     \\______/   \\______/         \\__/  \\__/     |__| |__| \\__| 
'''
lose = '''
____    ____  ______    __    __      __        ______        _______. _______ 
\\   \\ /   / /  __  \\  |  |  |  |    |  |      /  __  \\      /       ||   ____|
 \\   \\/   / |  |  |  | |  |  |  |    |  |     |  |  |  |    |   (----`|  |__   
  \\_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  |     \\   \\    |   __|  
    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | .----)   |   |  |____ 
    |__|     \\______/   \\______/     |_______| \\______/  |_______/    |_______|                                                                             
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]
player_choice = input("Rock, Paper, Scissors. What is your choice?\n").lower()

print("Your choice : ")
if "rock" in player_choice:
    player_choice = rock
    print(rock)
elif "paper" in player_choice:
    player_choice = paper
    print(paper)
elif "scissors" in player_choice:
    player_choice = scissors
    print(scissors)
else:
    print("Try again!")
    quit()

print("Computer's choice")
computer_choice = random.choice(options)
print(computer_choice)
if player_choice == computer_choice:
    print(deuce)
elif (player_choice == paper and computer_choice == scissors) or (
        player_choice == rock and computer_choice == paper) or (player_choice == scissors and computer_choice == rock):
    print(lose)
elif (player_choice == scissors and computer_choice == paper) or (
        player_choice == paper and computer_choice == rock) or (player_choice == rock and computer_choice == scissors):
    print(win)