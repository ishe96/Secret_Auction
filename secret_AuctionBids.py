# Bidding application
from replit import clear
from art import logo
print(logo)

bidding_logs = {} # Bid dictionary for Name and Amount entered
bidding_end = False

# Function for printing out top bidder
def top_bidder(biddings):
    highest_bid = 0
    winner = ""
    for bidder in biddings:
        bidding_logs = biddings[bidder]
        if bidding_logs > highest_bid:
            highest_bid = bidding_logs
            winner = bidder
    print("------------------------------------------------------")        
    print(f"The highest bidder is {winner} with a bid of NAD${highest_bid}.")

while not bidding_end:
    print("Welcome Secret Bidder \n \n")
    name = input("Enter name : ").title()
    bid = int(input("\nEnter amount you would like to bid : NAD$"))
    bidding_logs[name] = bid
    more_bidders = input("Any other bidders to enter bidding, Yes(y) or No(n)? : ").lower()
    if more_bidders == "n":
        bidding_finished = True
        top_bidder(bidding_logs)
        break
    elif more_bidders == "y":
        clear() # Clear screen to enter new bids or finish bidding