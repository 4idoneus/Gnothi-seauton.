# Blind Auction Project
# This program allows users to place bids in a blind auction.
import art

def add_bidder(bidder_dictionary):
    user_name = input("Hello Bidder! What is your name?\n")
    bid_value = int(input("What is your bid?\n$"))
    more_bidder = input("Are there any other bidder? \"yes\" or \"no\" ").lower()
    bidder_dictionary[user_name] = bid_value
    if more_bidder == "yes":
        print("\n" * 50)
        bidder = True
    elif more_bidder == "no":
        bidder = False
    else:
        print("You did not type correctly. Start again! ")
        quit()
    return bidder

bidder_dic = {}
bidder_state = True
max_bid = 0
max_bidder = ""
print(art.logo)
print("Welcome to the Secret Auction. May the richest win!")
while bidder_state:
    bidder_state = add_bidder(bidder_dic)

for key in bidder_dic:
    if bidder_dic[key] > max_bid:
        max_bid = bidder_dic[key]
        max_bidder = key
print(f"The winner is {max_bidder} with their bid ${max_bid} !!")

