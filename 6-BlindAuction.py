logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bid_dict = {}

def check_winner():
    higher_bid = 0
    higher_bid_name = ""
    for name in bid_dict:
        if bid_dict[name] > higher_bid:
            higher_bid = bid_dict[name]
            higher_bid_name = name
    print(f"The winner is {higher_bid_name} with a bid of ${higher_bid}.")

def gather_bids():
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    bid_dict[name] = int(bid)
    bid_again = input("Are there any other bidders? Type 'yes' or 'no': ")
    if bid_again == "yes":
        print("\n" * 100)
        gather_bids()
    else:
        check_winner()

gather_bids()
