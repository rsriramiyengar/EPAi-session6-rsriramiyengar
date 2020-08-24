import pytest
import random
import string
import pytest

import session6

import os
import inspect
import re
import math
import random

README_CONTENT_CHECK_FOR = [
    'polygon_area',
    'temp_converter',
    'print_f',
    'squared_power_list',
    'speed_converter'
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



# Royal Flush
# hand1 = [('ace', 'spades'),('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
# Straight Flush
# hand1 = [('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades'),('9', 'spades')]
# Four of Kind
# hand1 = [('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds'),('9', 'spades')]
# Full House
# hand1 = [('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('jack', 'diamonds'),('jack', 'spades')]
# Flush
# hand1 = [('king', 'hearts'), ( '8', 'hearts'), ('6', 'hearts'), ('4', 'hearts'),('2', 'hearts')]
# Straight
# hand1 = [('8', 'hearts'), ('7', 'spades'), ('6', 'diamonds'), ('5', 'clubs'),('4','hearts')]
# Three of kind
# hand1 = [('queen', 'spades'), ('queen', 'hearts'), ('queen', 'clubs'), ('7', 'hearts'),('2','club')]
# Two Pair
# hand1 = [('jack', 'spades'), ('jack', 'diamonds'), ('9', 'clubs'), ('9', 'diamonds'),('5','spades')]
# One Pair
# hand1 = [('king', 'hearts'), ('king', 'clubs'), ('9', 'clubs'), ('8', 'clubs'),('4','hearts')]
# High Card
#hand1 = [('ace', 'hearts'), ('queen', 'clubs'), ('6', 'hearts'), ('4', 'spades'), ('2', 'diamonds')]
#score1 = score_calculator(hand1)
#print(score1)
