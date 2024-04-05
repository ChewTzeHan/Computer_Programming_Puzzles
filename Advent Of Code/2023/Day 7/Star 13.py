import functools

docs = open("C:/Users/user/OneDrive/Desktop/Advent Of Code/2023/Day 7/input.txt", 'r').read()
docs = docs.split('\n')[:-1]

for i in range(len(docs)):
    docs[i] = docs[i].split(' ')

'''
Every hand is exactly one type. From strongest to weakest, they are:

Five of a kind, where all five cards have the same label: AAAAA

Four of a kind, where four cards have the same label and one card has a different label: AA8AA

Full house, where three cards have the same label, and the remaining two cards share a different 
label: 23332

Three of a kind, where three cards have the same label, and the remaining two cards are each 
different from any other card in the hand: TTT98

Two pair, where two cards share one label, two other cards share a second label, 
and the remaining card has a third label: 23432

One pair, where two cards share one label, and the other three cards have a different label 
from the pair and each other: A23A4

High card, where all cards' labels are distinct: 23456
'''

Five_kind = []
Four_kind = []
Full_house = []
Three_kind = []
Two_pair = []
One_pair =[]
High_card = []

for hand in docs: #hand[0] = cards
    first = hand[0].count(hand[0][0])
    second = hand[0].count(hand[0][1])
    third = hand[0].count(hand[0][2])
    fourth = hand[0].count(hand[0][3])
    fifth = hand[0].count(hand[0][4])
    
    if first == 5:
        Five_kind.append(hand)
        
    elif first == 4 or second == 4:
        Four_kind.append(hand)
        
    elif (first == 3 or second == 3 or third == 3) and (first == 2 or second == 2 or third == 2 or fourth == 2):
        Full_house.append(hand)
    
    elif (first == 3 or second == 3 or third == 3) and (first == 1 or second == 1 or third == 1 or fourth == 1):
        Three_kind.append(hand)
    
    elif (first, second, third, fourth, fifth).count(2) == 4:
        Two_pair.append(hand)
    
    elif first == 2 or second == 2 or third == 2 or fourth == 2:
        One_pair.append(hand)

    else:
        High_card.append(hand)


strength = '23456789TJQKA'
def mycmp(a, b): 

    for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = (strength.index(card_a) > strength.index(card_b))
            if a_wins:
                return 1
            else:
                return -1
    
def Ranker(deck):
    sorted_deck = sorted(deck, key=functools.cmp_to_key(mycmp), reverse=True)
    
    return sorted_deck


cards = Ranker(Five_kind) + Ranker(Four_kind) + Ranker(Full_house) + Ranker(Three_kind) + Ranker(Two_pair) + Ranker(One_pair) + Ranker(High_card)
Winnings = 0

for rank, hand in enumerate(cards):
    Winnings += int(hand[1]) * (len(cards) - rank)

print(Winnings)

'''
print(Five_kind)
print(len(Four_kind)) #89
print(len(Full_house)) #98
print(len(Three_kind)) #185
print(len(Two_pair)) #189
print(len(One_pair)) #247
print(len(High_card)) #191
'''
