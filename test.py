import itertools
import operator

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





a=lambda v,s : zip(4*v,13*s)
#a=sorted(a, key=lambda x: (x[1], x[0]))
print(list(a(vals,suits)))

Deck=map(list,map(lambda v,s :zip(v,s),4*vals,13*suits))
#Deck
print(list(Deck))





#deck=list(itertools.chain.from_iterable(a))

#print(deck)


