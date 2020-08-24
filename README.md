# Readme File for Assignment for Session 6 - First Class Functions Part I
### Created by Sriram Iyengar
## Session 6 - First Class Functions Part I
- Default Values
- Docstrings & Annotation
- Lambda Function
- Functional introspection
- Callable
- Maps,filter & zip
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Based on above Session we are tasked with develop  code to check special kind of poker with tow give hand
The object achieved in  this assignment as follow
- Function to create deck of cards using regular function
- Function to create deck of cards using map,zip and lambda function
- Function find winner of special poker game based on given set of cards\
Where the rank is as follows the given value in front is arbitrary just for convenience\
Royal Flush     =10000 (for set of 3,4 & 5 cards)\
Straight Flush  = 9000 (for set of 3,4 & 5cards)\
Four of kind    = 8000 (for set of 4 & 5 cards)\
Full House      = 7000 (for set of 5 cards)\
Flush           = 6000 (for set of 3,4&5 cards)\
Straight        = 5000 (for set of 3,4&5 cards)\
Three of kind   = 4000 (for set of 3,4&5 cards)\
Two pair        = 3000 (for set of 3,4&5 cards)\  
One pair        = 2000 (for set of 3,4&5 cards)\
High card       = 1000 (for set of 3,4&5 cards)\
- to create 35(min 20+) test cases to check our code.
- Last but not least create this readme file explaning the different functions
 
The given
  
## card_deck1_regular
- This function takes in number of deck required and returns cards in deck

## card_deck1_special
- This function takes in number of deck required and returns cards in deck this function is created with lambda map and zip function. 

### def game_card_poker_winner(hand1: "List of Cards with Player 1",hand2: "List of Cards with Player 1") -> 'Returns the number of  player who won':
    """
    This Determines the winner of Card game based on given set of cards
    Its calls another function to calculate score of each hand and then compares.
    Note: The input need to be properly order to check Tie Case.
    """
- This function when given 2 set of cards returns the Winner as given below   
- Player 1 if player 1 has a better hand
- Player 2 if player 2 has a better hand
- 'Its a tie both players share the pot' - if both have similar hands

### def score_calculator(hand: 'input is list of cards') -> 'The score of given hand':
    "This Function Calculates the score of given hand for selecting the winner in Poker"

*** Test Function
### The below given test checks the game_card_winner is selected properly for user given input
def test_function_poker_game():   

### The below given test checks the created deck  using regular for loop is matching  manualy created deck

def test_function_check_regular_created_deck():
    card_deck_check=card_deck1_regular()
    assert all(item in deck for item in card_deck_check) and len(card_deck_check)==len(deck), "Manual deck and regular deck should be same"
 
### The below given test checks the created deck  using regular for map,zip and lamda function is matching  manualy created deck

def test_function_check_special_map_zip_lamda_created_deck():
    card_deck_check=card_deck2_special()
    print(card_deck_check)
    assert all(item in deck for item in card_deck_check) and len(card_deck_check)==len(deck), "Manual deck and Special deck should be same"

### The below list of Function check if it is returning right class of win for given hand 
Royal Flush     =10000\
Straight Flush  = 9000\
Four of kind    = 8000\
Full House      = 7000\
Flush           = 6000\
Straight        = 5000\
Three of kind   = 4000\
Two pair        = 3000\  
One pair        = 2000\
High card       = 1000\



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

***
> ![My Image](https://github.com/rsriramiyengar/EPAi-session6-rsriramiyengar/blob/master/images/Image01.JPG)
***

We are using python >3.8.3

The assignment is  tested by executing 'pytest' , from python shell in same folder
