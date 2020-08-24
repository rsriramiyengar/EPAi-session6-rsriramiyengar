from operator import itemgetter

suits = ['spades', 'clubs', 'hearts', 'diamonds']
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
deck = [('2', 'clubs'), ('3', 'clubs'), ('4', 'clubs'), ('5', 'clubs'), ('6', 'clubs'), ('7', 'clubs'),
        ('8', 'clubs'), ('9', 'clubs'), ('10', 'clubs'), ('jack', 'clubs'), ('queen', 'clubs'), ('king', 'clubs'),
        ('ace', 'clubs'), ('2', 'diamonds'), ('3', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'),
        ('6', 'diamonds'), ('7', 'diamonds'), ('8', 'diamonds'), ('9', 'diamonds'), ('10', 'diamonds'),
        ('jack', 'diamonds'), ('queen', 'diamonds'), ('king', 'diamonds'), ('ace', 'diamonds'), ('2', 'hearts'),
        ('3', 'hearts'), ('4', 'hearts'), ('5', 'hearts'), ('6', 'hearts'), ('7', 'hearts'), ('8', 'hearts'),
        ('9', 'hearts'), ('10', 'hearts'), ('jack', 'hearts'), ('queen', 'hearts'), ('king', 'hearts'),
        ('ace', 'hearts'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('5', 'spades'), ('6', 'spades'),
        ('7', 'spades'), ('8', 'spades'), ('9', 'spades'), ('10', 'spades'), ('jack', 'spades'),
        ('queen', 'spades'), ('king', 'spades'), ('ace', 'spades')]


def merge(list1: "This function", list2:"This Function mergers two given list")->"Merged list":
    "This Function when given 2 list return combined list"
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list

def card_deck1_regular(n: 'number of Decks' = 1) -> 'List of Cards':
    """
    This Program takes in number of deck and provides list of cards in it.
    """
    Card_deck = []
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    if n >= 1 and isinstance(n, int):
        for n in range(n):
            for b in suits:
                for a in vals:
                    Card_deck.append((a, b))
    else:
        print("Number of decks needs to be  +ve integer")
    return Card_deck

def card_deck2_special(n: 'number of Decks' = 1) -> 'List of Cards':
    "Single expression that including lambda, zip and map functions to select create 52 cards in a deck"
    if n>=1 and isinstance(n, int):
        card_deck2 = n*list(map(lambda x:(x[0], x[1]),zip(vals*4,suits*13)))
    else:
        print("Number of decks needs to be  +ve integer")
    return card_deck2

def determinevalue1(y: "Face Number of Card") -> "Program Number of Card":
    """ This function generates is the program number of cards"""
    val_number_dic = {'2': 12, '3': 13, '4': 14, '5': 15, '6': 16, '7': 17, '8': 18, '9': 19, '10': 20, 'jack': 21,'queen': 22, 'king': 23, 'ace': 24}
    z = val_number_dic.get(y)
    return z

def game_card_poker_winner(hand1: "List of Cards with Player 1",hand2: "List of Cards with Player 1") -> 'Returns the number of  player who won':
    """
    This Determines the winner of Card game based on given set of cards
    Its calls another function to calculate score of each hand and then compares.
    Note: The input need to be properly order to check Tie Case.
    """
    winner = 'Its a tie both players share the pot'
    check1 = all(item in deck for item in hand2)
    check2 = all(item in deck for item in hand2)
    if len(hand1) == len(hand2) and check1 is True and check2 is True:
        score1 = score_calculator(hand1)
        score2 = score_calculator(hand2)
        for a in range(len(hand1) + 1):
            if score1[a] > score2[a]:
                winner = 'Player 1'
                break
            elif score1[a] < score2[a]:
                winner = 'Player 2'
                break
    elif check1 is False and check2 is False:
        winner = 'Its a tie as Both Player should have legitimate cards'
    elif check1 is False:
        winner = 'Its a tie as Player1 should have legitimate cards'
    elif check2 is False:
        winner = 'Its a tie as Player2 should have legitimate cards'
    else:
        winner = 'Its a tie Both Players should have same amount of cards'
    return winner

def card_sorter_and_numbered(hand: 'unsorted hand with card number') -> 'Sorted card number with structured number':
    """ This Program sorts the cards based on suit and vals and returns with number in place of vals"""
    hand_vals = list(map(itemgetter(0), hand))
    hand_suit = list(map(itemgetter(1), hand))
    hand_vals1 = []
    for a in hand_vals:
        hand_vals1.append(determinevalue1(a))
    hand_r = merge(hand_vals1, hand_suit)
    hand_r = sorted(hand_r, key=lambda x: (x[1], -x[0]))
    return hand_r, hand_vals1, hand_suit

def checkconsecutive(l: 'Take in list  and checks if it consecutive number or not') -> 'True or False':
    return sorted(l) == list(range(min(l), max(l) + 1))

def score_calculator(hand: 'input is list of cards') -> 'The score of given hand':
    "This Function Calculates the score of given hand for selecting the winner in Poker"
    Score = []
    cards_in_hand = len(hand)
    sorted_cards, hand_fval, hand_suit = card_sorter_and_numbered(hand)
    hand_suit_uni = list(set(hand_suit))
    hand_suit_uni_nu = len(hand_suit_uni)
    hand_fvals_uni = list(set(hand_fval))
    hand_fvals_uni_nu = len(hand_fvals_uni)
    #####for Straight flush
    hand_fval_sorted = sorted(hand_fval, reverse=True)
    ct1 = hand_fval.count(hand_fvals_uni[0])
    ct2 = hand_fval.count(hand_fvals_uni[1]) if hand_fvals_uni_nu >= 2 else 1
    ct3 = hand_fval.count(hand_fvals_uni[2]) if hand_fvals_uni_nu >= 3 else 1
    ct4 = hand_fval.count(hand_fvals_uni[3]) if hand_fvals_uni_nu >= 4 else 1
    ct = sorted((ct1, ct2, ct3, ct4), reverse=True)
    Royal_flush_sum_dict = {5: 110, 4: 90, 3: 69}
    Four_of_kind_dict = {5: 2, 4: 1}
    #####
    # "Royal Flush"
    if hand_suit_uni_nu == 1 and sum(hand_fval) == Royal_flush_sum_dict.get(cards_in_hand):
        score = hand_fval_sorted
        score.insert(0, 10000)
    # Straight flush
    elif hand_suit_uni_nu == 1 and checkconsecutive(hand_fval_sorted):
        score = hand_fval_sorted
        score.insert(0, 9000)
    # Four of a kind
    elif cards_in_hand >= 4 and hand_fvals_uni_nu == Four_of_kind_dict.get(cards_in_hand) and ct[0] == 4:
        score = hand_fval_sorted
        score.insert(0, 8000)
    # Full House
    elif cards_in_hand == 5 and hand_fvals_uni_nu == 2 and ct[0] == 3:
        score = hand_fval_sorted
        score.insert(0, 7000)
    # Flush
    elif hand_suit_uni_nu == 1:
        score = hand_fval_sorted
        score.insert(0, 6000)
    # Straight
    elif checkconsecutive(hand_fval_sorted):
        score = hand_fval_sorted
        score.insert(0, 5000)
    # Three of kind
    elif ct[0] == 3:
        score = hand_fval_sorted
        score.insert(0, 4000)
    # Two Pair
    elif cards_in_hand >= 4 and ct[0] == 2 and ct[1] == 2:
        score = hand_fval_sorted
        score.insert(0, 3000)
    # One Pair
    elif ct[0] == 2 and ct[1] == 1:
        score = hand_fval_sorted
        score.insert(0, 2000)
    # High Card
    else:
        score = hand_fval_sorted
        score.insert(0, 1000)
    return score
