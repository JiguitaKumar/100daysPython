import random

logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/           
"""

cards = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A11": 11,
}


def check_result(dealer, user, d_cards, u_cards):
    if dealer == user:
        print("It is a Draw 🙃")
    elif user == 21 and len(u_cards) == 2:
        print("Win with a Blackjack 😎")
    elif dealer == 21 and len(d_cards) == 2:
        print("You lose! The opponent has a Blackjack 😱")
    elif user > 21:
        print("You went over. You lose 😢")
    elif dealer > 21:
        print("Opponent went over. You win 😁")
    elif user > dealer:
        print("You win! 🥳")
    else:
        print("You lose 😤")


def add_card(card_list, current_score):
    card_list.append(random.choice(list(cards.keys())))
    current_score += int(cards[card_list[-1]])
    return current_score


def check_min_threshold(card_list, current_score):
    score_below_17 = True
    while score_below_17:
        if current_score < 17:
            current_score = add_card(card_list, current_score)
        elif current_score > 21 and "A11" in card_list:
            card_list.remove("A11")
            card_list.append("A1")
            current_score -= 10
        else:
            score_below_17 = False
            
            return current_score


def blackjack(dealer_cards, your_cards):

    dealer_score = int(cards[dealer_cards[0]]) + int(cards[dealer_cards[1]])
    your_score = int(cards[your_cards[0]]) + int(cards[your_cards[1]])

    print(f"Your initial cards: {your_cards}, and initial score: {your_score}")
    print(f"Computer's first card: {dealer_cards[0]}")

    dealer_score = check_min_threshold(dealer_cards, dealer_score)

    while your_score < 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == 'y':
            your_score = add_card(your_cards, your_score)

            if your_score > 21 and "A11" in your_cards:
                your_cards.remove("A11")
                your_cards.append("A1")
                your_score -= 10

            print(f"    Your cards: {your_cards}, current score: {your_score}")
        else:
            print(f"    Your cards: {your_cards}, current score: {your_score}")
            break
    
    print(f"    Dealer final hand: {dealer_cards}, final score: {dealer_score}")

    check_result(dealer_score, your_score, dealer_cards, your_cards)
    
    return game_start()


def game_start():
    wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if wanna_play == 'y':

        dealer = [random.choice(list(cards.keys())), random.choice(list(cards.keys()))]
        you = [random.choice(list(cards.keys())), random.choice(list(cards.keys()))]

        print(logo)
        return blackjack(dealer, you)
    else:
        return

game_start()
