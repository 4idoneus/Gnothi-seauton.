# Tip Calculator Project
# This is a simple tip calculator that calculates the total bill with tip and splits it among a
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip = round(bill * (1 + (tip/100)), 2)
bill_per_person = bill_with_tip / people
final_bill = round(bill_per_person,2)
print(f"Your final bill wit tax included is {bill_with_tip} and it means you will split it {final_bill} per person. Don't forget anything when you leave!")
print("Have a great day!")