# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo

print(logo)
bidder_details = {}
auction_end = False
while not auction_end:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bidder_details[name] = price
    new_bids = input("Are there any other bidders? Type 'yes or 'no'. \n")
    if new_bids == 'no':
        highest_bidder = ""
        max_bid = 0
        for key in bidder_details:
            if bidder_details[key] > max_bid:
                highest_bidder = key
                max_bid = bidder_details[key]
        print(f"The winner is {highest_bidder} with a bid of ${bidder_details[highest_bidder]}")
        auction_end = True
    else:
        print("\n" * 100)
