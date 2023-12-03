
'''
#test data
docs = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
'''

docs = open("input.txt", 'r').read()
docs = docs.split('\n')

#adding empty borders
docs = ['.' * len(docs)] + docs
docs = docs + ['.' * (len(docs) - 1)]

for i in range(len(docs)):
    docs[i] = '.' + docs[i]

for i in range(len(docs)):
    docs[i] = docs[i] + '.'
    

num_str = ''
track_index = []
track_row = 0
valid = False
part_sum = 0




for row in docs[1:-1]:
    for index, element in enumerate(row):
        
        if element.isdigit(): #check for numbers
            num_str += element
            track_index.append(index)
            track_row = docs.index(row)
        
        elif element.isdigit() == False: #check for presence of symbols
            if num_str != '':
                #print("Number found: {a} with indexes {b} on row {c}".format(a = num_str, b = track_index, c = track_row))
                for symb in docs[track_row - 1][(track_index[0] - 1):(track_index[-1] + 2)]:
                    if symb != '.' and symb.isdigit() == False:
                        valid = True
                    
                
                for symb in docs[track_row][(track_index[0] - 1):(track_index[-1] + 2)]:
                    if symb != '.' and symb.isdigit() == False:
                        valid = True
                    
              
                for symb in docs[track_row + 1][(track_index[0] - 1):(track_index[-1] + 2)]:
                    if symb != '.' and symb.isdigit() == False:
                        valid = True
                    
                #If number is valid part number, add and reinitialize variables
                if valid == True:
                    part_sum += int(num_str)
                    
                valid = False
                
                num_str = ''
                track_index = []
        

print('Sum of all valid parts is: {a}'.format(a = part_sum))
