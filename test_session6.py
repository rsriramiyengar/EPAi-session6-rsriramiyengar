import inspect
import os
import re

import session6
from session6 import game_card_poker_winner
from session6 import card_sorter_and_numbered
from session6 import score_calculator
from session6 import card_deck1_regular
from session6 import card_deck2_special

##type of Card Suits
suits = ['spades', 'clubs', 'hearts', 'diamonds']
##Face value of cards
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
######Deck for Comparision
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
## Hands for Testing
p_royal_flush_5 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
p_royal_flush_4 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
p_royal_flush_3 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades')]
p_straight_flush_5 = [('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades'), ('9', 'spades')]
p_straight_flush_4 = [('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
p_straight_flush_3 = [('king', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
p_four_of_kind_5 = [('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds'), ('9', 'spades')]
p_four_of_kind_4 = [('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds')]
p_full_house_5 = [('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('jack', 'diamonds'), ('jack', 'spades')]
p_poker_flush_5 = [('king', 'hearts'), ('8', 'hearts'), ('6', 'hearts'), ('4', 'hearts'), ('2', 'hearts')]
p_poker_flush_4 = [('king', 'hearts'), ('8', 'hearts'), ('6', 'hearts'), ('4', 'hearts')]
p_poker_flush_3 = [('king', 'hearts'), ('8', 'hearts'), ('6', 'hearts')]
p_straight_5 = [('8', 'hearts'), ('7', 'spades'), ('6', 'diamonds'), ('5', 'clubs'), ('4', 'hearts')]
p_straight_4 = [('8', 'hearts'), ('7', 'spades'), ('6', 'diamonds'), ('5', 'clubs')]
p_straight_3 = [('8', 'hearts'), ('7', 'spades'), ('6', 'diamonds')]
p_three_of_kind_5 = [('queen', 'spades'), ('queen', 'hearts'), ('queen', 'clubs'), ('7', 'hearts'), ('2', 'club')]
p_three_of_kind_4 = [('queen', 'spades'), ('queen', 'hearts'), ('queen', 'clubs'), ('7', 'hearts')]
p_three_of_kind_3 = [('queen', 'spades'), ('queen', 'hearts'), ('queen', 'clubs')]
p_two_Pair_5 = [('jack', 'spades'), ('jack', 'diamonds'), ('9', 'clubs'), ('9', 'diamonds'), ('5', 'spades')]
p_two_Pair_4 = [('jack', 'spades'), ('jack', 'diamonds'), ('9', 'clubs'), ('9', 'diamonds')]
p_one_Pair_5 = [('king', 'hearts'), ('king', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('4', 'hearts')]
p_one_Pair_4 = [('king', 'hearts'), ('king', 'clubs'), ('9', 'clubs'), ('8', 'clubs')]
p_one_Pair_3 = [('king', 'hearts'), ('king', 'clubs'), ('9', 'clubs')]
p_high_card_5 = [('ace', 'hearts'), ('queen', 'clubs'), ('6', 'hearts'), ('4', 'spades'), ('2', 'diamonds')]
p_high_card_4 = [('ace', 'hearts'), ('queen', 'clubs'), ('6', 'hearts'), ('4', 'spades')]
p_high_card_3 = [('ace', 'hearts'), ('queen', 'clubs'), ('6', 'hearts')]


README_CONTENT_CHECK_FOR = [
    'game_card_poker_winner',
    'score_calculator',
    'card_deck1_regular',
    'card_deck2_special'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"




def test_function_poker_game():
    assert game_card_poker_winner(p_royal_flush_5,p_straight_flush_5) =='Player 1', "Test01-High Hand Cannot lose to straigh flush"
    assert game_card_poker_winner(p_poker_flush_4,p_four_of_kind_4) == 'Player 2', "Test02-Four_of_kind Cannot lose to flush"
    assert game_card_poker_winner(p_poker_flush_5,p_high_card_5) == 'Player 1', "Test03-Flush Cannot lose to high card"
    assert game_card_poker_winner(p_three_of_kind_4,p_three_of_kind_4) == 'Its a tie both players share the pot', "Test04-Same set of cards must be tie"
    assert game_card_poker_winner(p_straight_flush_3,p_high_card_3) == 'Player 1', "Test05-Straigh Flush cannot lose to high card"
    assert game_card_poker_winner(p_three_of_kind_5,p_two_Pair_5) == 'Player 1', "Test06-Three of Kind cannot lose to Two Pair"
    assert game_card_poker_winner(p_high_card_5,p_full_house_5) == 'Player 2', "Test07-Full house cannot lose to High Card"
    assert game_card_poker_winner(p_two_Pair_4,p_four_of_kind_4 ) == 'Player 2', "Test08-Four of kind cannot lose to Two Pair"
    assert game_card_poker_winner(p_three_of_kind_4, p_high_card_4) == 'Player 1', "Test09-Three of kind cannot lose to High card"
    assert game_card_poker_winner(p_two_Pair_4 , p_royal_flush_4) == 'Player 2', "Test10-Royal cannot lose to two pair"
    assert game_card_poker_winner(p_two_Pair_4, p_royal_flush_4) == 'Player 2', "Test11-Royal cannot lose to two pair"
    assert game_card_poker_winner(p_two_Pair_5, p_one_Pair_5) == 'Player 1', "Test12-Two pair cannot lose to one pair"
    assert game_card_poker_winner(p_poker_flush_5, p_straight_flush_5) == 'Player 2', "Test13-Straight flush cannot lose to flush"
    assert game_card_poker_winner(p_royal_flush_3 ,p_straight_3) == 'Player 1', "Test14-Royal flush cannot lose to straigh"
    assert game_card_poker_winner(p_three_of_kind_4, p_four_of_kind_4) == 'Player 2', "Test15-Four of Kind cannot lose to Three of Kind"
    assert game_card_poker_winner(p_one_Pair_3,p_high_card_3) == 'Player 1', "Test16-One Pair cannot lose to High Card"
    assert game_card_poker_winner(p_one_Pair_4,p_two_Pair_4) == 'Player 2', "Test17-Two Pair cannot lose to One Pair"
    assert game_card_poker_winner(p_straight_flush_5,p_one_Pair_5) == 'Player 1', "Test18-Straigh flush cannot lose to One Pair"
    assert game_card_poker_winner(p_high_card_3,p_poker_flush_3) == 'Player 2', "Test19-Flush cannot lose to High card"
    assert game_card_poker_winner(p_four_of_kind_4, p_straight_4) == 'Player 1', "Test20- straight cannot lose to Four of Kind"


def test_function_check_regular_created_deck():
    card_deck_check=card_deck1_regular()
    assert all(item in deck for item in card_deck_check) and len(card_deck_check)==len(deck), "Manual deck and regular deck should be same"

def test_function_check_special_map_zip_lamda_created_deck():
    card_deck_check=card_deck2_special()
    print(card_deck_check)
    assert all(item in deck for item in card_deck_check) and len(card_deck_check)==len(deck), "Manual deck and Special deck should be same"

def test_function_score_cal_check1():
    assert score_calculator(p_royal_flush_5)[0]==10000, 'score Should be 10000'

def test_function_score_cal_check2():
    assert score_calculator(p_royal_flush_4)[0]==10000, 'score Should be 10000'

def test_function_score_cal_check3():
    assert score_calculator(p_royal_flush_3)[0]==10000, 'score Should be 10000'

def test_function_score_cal_check4():
    assert score_calculator(p_straight_flush_5)[0]==9000, 'score Should be 9000'

def test_function_score_cal_check5():
    assert score_calculator(p_straight_flush_4)[0]==9000, 'score Should be 9000'

def test_function_score_cal_check6():
    assert score_calculator(p_straight_flush_3)[0]==9000, 'score Should be 9000'

def test_function_score_cal_check7():
    assert score_calculator(p_four_of_kind_5)[0]==8000, 'score Should be 8000'

def test_function_score_cal_check8():
    assert score_calculator(p_four_of_kind_4)[0]==8000, 'score Should be 8000'

def test_function_score_cal_check9():
    assert score_calculator(p_full_house_5)[0]==7000, 'score Should be 7000'

def test_function_score_cal_check10():
    assert score_calculator(p_poker_flush_5)[0]==6000, 'score Should be 6000'

def test_function_score_cal_check11():
    assert score_calculator(p_poker_flush_4)[0]==6000, 'score Should be 6000'

def test_function_score_cal_check12():
    assert score_calculator(p_poker_flush_3)[0]==6000, 'score Should be 6000'

def test_function_score_cal_check13():
    assert score_calculator(p_straight_5)[0]==5000, 'score Should be 5000'

def test_function_score_cal_check14():
    assert score_calculator(p_straight_4)[0]==5000, 'score Should be 5000'

def test_function_score_cal_check15():
    assert score_calculator(p_straight_3)[0]==5000, 'score Should be 5000'

def test_function_score_cal_check16():
    assert score_calculator(p_three_of_kind_5)[0]==4000, 'score Should be 4000'

def test_function_score_cal_check17():
    assert score_calculator(p_three_of_kind_4)[0]==4000, 'score Should be 4000'

def test_function_score_cal_check18():
    assert score_calculator(p_three_of_kind_3)[0]==4000, 'score Should be 4000'

def test_function_score_cal_check19():
    assert score_calculator(p_two_Pair_5)[0]==3000, 'score Should be 3000'

def test_function_score_cal_check20():
    assert score_calculator(p_two_Pair_4)[0]==3000, 'score Should be 3000'

def test_function_score_cal_check21():
    assert score_calculator(p_one_Pair_5)[0]==2000, 'score Should be 2000'

def test_function_score_cal_check22():
    assert score_calculator(p_one_Pair_4)[0]==2000, 'score Should be 2000'

def test_function_score_cal_check23():
    assert score_calculator(p_one_Pair_3)[0]==2000, 'score Should be 2000'

def test_function_score_cal_check24():
    assert score_calculator(p_high_card_5)[0]==1000, 'score Should be 1000'

def test_function_score_cal_check25():
    assert score_calculator(p_high_card_4)[0]==1000, 'score Should be 1000'

def test_function_score_cal_check26():
    assert score_calculator(p_high_card_3)[0]==1000, 'score Should be 1000'

