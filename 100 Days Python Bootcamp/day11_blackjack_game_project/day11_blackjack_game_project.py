# Blackjack Game Project
# This is a simple implementation of a Blackjack game in Python.
# The game allows a player to play against a dealer, with options to hit or stand.
import art
import random

deck = [["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
        ['♠', '♥', '♦', '♣']]
game_state = {
    "shown_cards": [], # A list to keep track of the shown cards.
    "total_cards": 104  # 2 full decks
}
dealer_cards = [] # A list to store the dealer's cards.
player_cards = [] # A list to store the player's cards.

def clear():
    print("\033c", end="")  # Clears full screen (Linux/macOS/Windows Terminal)
    print("\r", end="")
    print(art.logo)

def generate_card(decks, state):  # Function to generate card.
    if len(state["shown_cards"]) >= state["total_cards"]:
        print("Shuffling a new deck!")
        state["shown_cards"].clear()
        state["total_cards"] = 104
    while True:
        rank = random.choice(decks[0])
        suit = random.choice(decks[1])
        card = (str(rank), suit)

        if state["shown_cards"].count(card) < 2:
            state["shown_cards"].append(card)
            state["total_cards"] -= 1  # Decrement total
            return card

def calculate_value(hand):
    value = 0
    aces = 0
    for rank, suit in hand:
        if rank in ["J", "Q", "K"]:
            value += 10
        elif rank == "A":
            aces += 1
        else:
            value += int(rank)
    # A value decision
    for _ in range(aces):
        if value + 11 > 21:
            value += 1
        else:
            value += 11
    return value

def blackjack(player_money,player_hand,dealer_hand):
    dealer_shown_cards = []
    player_value = 0
    dealer_value = 0
    hit = True
    if player_money <= 0:
        print("You have no money left to bet.")
        return False, player_money

    while True:
        try:
            player_bet = int(input("How much money will you bet?\nBet Amount: $"))
            if player_bet > player_money:
                print(f"You only have ${player_money}. Please bet within your balance.")
            elif player_bet <= 0:
                print("Bet must be more than $0.")
            else:
                break  # Valid bet
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    print("Player's Hand: ")
    player_hand.append(generate_card(deck,state=game_state))
    player_hand.append(generate_card(deck,state=game_state))
    art.render_cards_side_by_side(player_hand)
    print("Dealer's Hand: ")
    dealer_hand.append(generate_card(deck, state=game_state))
    dealer_hand.append(generate_card(deck,state=game_state))
    dealer_shown_cards.append(dealer_hand[0])
    dealer_shown_cards.append("hidden")
    art.render_cards_side_by_side(dealer_shown_cards)

    def hit_or_stand(hand):
        while True:
            choice = input("Do you want to 'hit' or 'stand'?\nYour choice: ").lower()
            if choice == "hit":
                hand.append(generate_card(deck,state=game_state))
                clear()
                print("Player's Hand: ")
                art.render_cards_side_by_side(hand)
                print("Dealer's Hand: ")
                art.render_cards_side_by_side(dealer_shown_cards)
                value = calculate_value(hand)
                if value > 21:
                    print("Bust! You went over 21.")
                    return False , value
            elif choice == "stand":
                value = calculate_value(hand)
                return False ,value
            else:
                print("Invalid input.")
                return False , None
    def dealer_play(value):
        print("Dealer reveals hand:")
        art.render_cards_side_by_side(dealer_hand)
        value = calculate_value(dealer_hand)
        while value < 17:
            dealer_hand.append(generate_card(deck,state=game_state))
            clear()
            print("Player's Hand: ")
            art.render_cards_side_by_side(player_hand)
            print("Dealer's Hand: ")
            art.render_cards_side_by_side(dealer_hand)
            value = calculate_value(dealer_hand)
        return value


    def continue_the_game():
        games_state = input("Do you want to continue the game? To continue type 'yes'. To exit type 'no'.\nPlayer's Answer: ").lower()
        if "yes" in games_state:
            return True
        elif "no" in games_state:
            return False
        else:
            print("You did not type correctly")
            return False
    while hit:
        hit,player_value = hit_or_stand(player_hand)
        if player_value > 21:
            print(art.bust)
            print(art.lose)
            player_money -= player_bet
            print(f"Your money ${player_money}")
            return continue_the_game(), player_money
        elif player_value == 21:
            print(art.blackjack)

    dealer_value = dealer_play(dealer_value)
    if dealer_value > 21 or player_value > dealer_value:
        player_money += player_bet
        print(art.win)
        print(f"Your money ${player_money}")
    elif player_value == 21 and dealer_value != 21:
        player_money += player_bet * 1.5
        print(art.win)
        print(f"Your money ${player_money}")
    elif player_value == dealer_value:
        print(art.push)
        print(f"Your money ${player_money}")
    else:
        player_money -= player_bet
        print(art.lose)
        print(f"Your money ${player_money}")
    return continue_the_game(),player_money


print(art.logo)
print("""Welcome to the Lethe's Blackjack!
How to Play ?
    ♣ You and the dealer get 2 cards.
    ♠ Dealer shows 1 card; 1 is hidden.
    ♥ You can:
        ♦ Hit – take another card
        ♦ Stand – keep your cards
Rules are simple but let me explain:
    ♦ Get as close to 21 as possible without going over.
    ♥ You play against the dealer.
    ♣ Bust - If your total goes over 21, you lose.
    ♠ Blackjack (Ace + 10) on first 2 cards beats anything but dealer Blackjack.
    ♦ Push - If you and the dealer have the same total and your bet is returned.
""")
start_the_game = input("To start the game, type 'Start'.To quit, type 'Quit'.\n Player's Answer : ").title()


if "Start" in start_the_game:
    in_game = True
elif "Quit" in start_the_game:
    print("You did not play the game. That's sad.\nThank you for opening the game. See you soon!")
    quit()
else:
    print("Invalid phrase. Default option is 'Start. So game is starting! Good Luck!")
    in_game = True
players_money = int(input("How much money do you have?\nYour money : $"))
while in_game:
    clear()
    player_cards = []
    dealer_cards = []

    in_game , players_money= blackjack(players_money,player_cards,dealer_cards)

print(f"Your final money ${players_money}\nThank you for playing.See you again in other sessions!")