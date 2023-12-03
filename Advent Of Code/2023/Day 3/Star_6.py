
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
temp = ''
index_counter = 0
gear_index = []



for row in docs[1:-1]:
    for index, element in enumerate(row):
        
        if element.isdigit(): #check for numbers
            num_str += element
            track_index.append(index)
            track_row = docs.index(row)
        
        elif element.isdigit() == False: #check for presence of gears
            if num_str != '':
                #print("Number found: {a} with indexes {b} on row {c}".format(a = num_str, b = track_index, c = track_row))
                index_counter = track_index[0] - 1 
                for symb in docs[track_row - 1][(track_index[0] - 1):(track_index[-1] + 2)]:
                    
                    if symb == '*':
                        gear_index.append([track_row-1, index_counter, num_str])
                    index_counter += 1
                    
                index_counter = track_index[0] - 1
                

                for symb in docs[track_row][(track_index[0] - 1):(track_index[-1] + 2)]:
                    if symb == '*':
                        gear_index.append([track_row, index_counter, num_str])
                        
                    index_counter += 1
                
                index_counter = track_index[0] - 1

                
                for symb in docs[track_row + 1][(track_index[0] - 1):(track_index[-1] + 2)]:
                    if symb == '*':
                        gear_index.append([track_row+1, index_counter, num_str])
                    
                    index_counter += 1
                    

                
                num_str = ''
                track_index = []



ratio_check = []
gear_sum = 0

#Check if gear is a gear ratio and sum
for row in gear_index:
    for check in ratio_check:
        if check[0] == row[0] and check[1] == row[1]:
            gear_sum += int(check[2]) * int(row[2])
    
    ratio_check.append(row[0:3])






print('Sum of all gear ratios is: {a}'.format(a = gear_sum))

