'''
# TODO -1 :- Ask the user for input
name = input("What is your name?: ")
price = int(input("What is your bid?: $"))

bids = {} #Empty Dictionary
# TODO - 2 :- Save data into dictionary {name: price}
bids[name] = price


# TODO-3 :- Weather if new bids  need to be added
should_continue = input("Are there any other bidder? Type 'yes' or 'no'. \n")

continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' .\n").lower()

    if should_continue  == "no":

# TODO-4 :- Compare bids in dictionary
'''

#Here reducing the steps using while Loop 
#TODO-1: Ask the user for input
#TODO-2: Save data into dictionary {name: price}
#TODO-3: Weather if new bids need to be added.

bids = {}
continue_bidding = True
