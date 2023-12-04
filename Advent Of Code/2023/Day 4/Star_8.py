'''
docs = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
'''


docs = open("input.txt", 'r').read()
docs = docs.split('\n')


for i in range(len(docs)):
    docs[i] = docs[i].split('|')
    docs[i][0] = docs[i][0].split(':')[1]
    

entry_nums = []
entry_str = ''
winning_nums = []
winning_str = ''

cards = {}

for i in range(len(docs)):
    cards[i + 1] = 1

print(cards)



for index, row in enumerate(docs):
    for char in row[0]:
        if char.isdigit():
            entry_str += char
            
        elif char != '' and entry_str != '':
            entry_nums.append(int(entry_str))
            entry_str = ''
            
    for char in row[1]:
        if char.isdigit():
            winning_str += char
            
        elif char != '' and winning_str != '':
            winning_nums.append(int(winning_str))
            winning_str = ''
            
    if winning_str != '':
        winning_nums.append(int(winning_str))
        winning_str = ''
            
        
    print('Card number is: {a}'.format(a = index + 1))
            
        
    count = 1
    for number in entry_nums:
        if number in winning_nums:
            card_key = index + 1 + count
            cards[card_key] = cards[card_key] + cards[index + 1]
            count += 1
            
    

    print(entry_nums)
    entry_nums = []
    print(winning_nums)
    winning_nums = []


    print('---------')


card_sum = 0
for key in cards:
    card_sum += cards[key]

print(cards)
print('Total cards: {a}'.format(a = card_sum))
#print('Total points: {a}'.format(a = total_points))
#print(docs)
#print(type(docs[1]))
#print(type(docs[0][0]))