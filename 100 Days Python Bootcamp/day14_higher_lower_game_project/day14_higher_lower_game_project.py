# Higher Lower Game Project
# This is a game where you compare the number of followers of two social media accounts.
# The player has to guess which account has more followers.
# The game continues until the player guesses incorrectly or chooses to exit.
import logging

import game_data
import art
import random

logging.basicConfig(level=logging.DEBUG)

# print(" ".join("{}: {}".format(k,v)for k,v in game_data.data[1].items()).title()) #This is how we can print dictionary without the brackets
def clear():
    print("\n" * 20)
    print("\r",end=art.logo)

def get_random(data):
    while True:
        if len(data) >= len(game_data.data):
            raise ValueError("No more unique comparisons left.")
        else:
            value = random.randint(0, len(game_data.data) - 1)
            if value not in data:
                data.append(value)
                return value
            logging.debug(f"{value} is already in the list. Getting a new one.")

def get_values(data):
    name = game_data.data[data]['name'].title()
    description = game_data.data[data]['description']
    country = game_data.data[data]['country'].title()
    follower = int(game_data.data[data]['follower_count'])
    sentence = name + ", " + description + ", from " + country
    return sentence,follower

def compare_follower(data1,data2,player_scr):
    a_sentence, a_follower = get_values(data1)
    b_sentence, b_follower = get_values(data2)

    print(f"Compare A: {a_sentence}, {a_follower}M")
    print(art.vs)
    print(f"Against B: {b_sentence}")

    answer = input("Who has more followers? Type 'A' or 'B' : ").upper()
# Comparison of the two account's followers.
    if a_follower > b_follower:
        correct_answer = "A"
    elif a_follower < b_follower:
        correct_answer = "B"
    else:
        correct_answer =  answer
# Checking if the player's answer is True
    if answer == correct_answer:
        player_scr += 1
        return player_scr,True,True,shown_data,b_to_a_data
    else:
        print(f"Your guess was wrong! Final Score: {player_score}")
        is_rply,in_game,shwn_data,b_a_data,player_scr = replay_the_game(player_scr)
        return player_scr,is_rply,in_game,shwn_data,b_a_data


def replay_the_game(plyr_scr):
    games_state = input("Do you want to replay the game? To replay type 'yes/y'. To exit type 'exit/e'.\nPlayer's Answer: ").lower()
    shwn_data = []
    b_a_data = []
    if "y"  in games_state or "yes" in games_state:
        plyr_scr = 0
        return True,True,shwn_data,b_a_data,plyr_scr
    elif "e"  in games_state or "exit" in games_state:
        return False,False,None,None,None
    else:
        print("You did not type correctly")
        return False,False,None,None,None

def start_game():
    start_the_game = input("To start the game, type 'Start'.To quit, type 'Quit'.\n Player's Answer : ").title()
    if "Start" in start_the_game or "S" in start_the_game:
        game_state = True
    elif "Quit" in start_the_game or "Q" in start_the_game:
        print("You did not play the game. That's sad.\nThank you for opening the game. See you soon!")
        quit()
    else:
        print("Invalid phrase. Default option is 'Start. So game is starting! Good Luck!")
        game_state = True
    return game_state

is_replay = True
while is_replay:
    print(art.logo)
    in_game = start_game()
    shown_data = []
    b_to_a_data = []
    player_score = 0
    while in_game:
        clear()
        if player_score < 1:
            a_data = get_random(shown_data)
            b_data = get_random(shown_data)
            b_to_a_data.append(b_data)
            player_score,is_replay,in_game,shown_data,b_to_a_data = compare_follower(a_data,b_data,player_score)
            logging.debug(f"{b_to_a_data},{shown_data}")
        else :
            print(f"Players score: {player_score}")
            a_data = b_to_a_data[player_score - 1]
            b_data = get_random(shown_data)
            b_to_a_data.append(b_data)
            player_score,is_replay,in_game,shown_data,b_to_a_data = compare_follower(a_data, b_data, player_score)
            logging.debug(f"{b_to_a_data},{shown_data}")
print("Thank you for playing the game. See you soon!")