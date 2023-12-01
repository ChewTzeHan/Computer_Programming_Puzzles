

#Read input and convert to list
docs = open("input.txt", 'r').read()
docs = docs.split()

word_nums = {'one' : 'o1e', 
             'two' : 't2o',
             'three' : 't3e',
             'four' : 'f4r',
             'five' : 'f5e',
             'six' : 's6x',
             'seven' : 's7n',
             'eight' : 'e8t',
             'nine' : 'n9e'}
calib_sum = 0




for i in range(len(docs)): #translating words to digits
    for key in word_nums:
        docs[i-1] = docs[i-1].replace(key, str(word_nums[key]))


    
for line in docs:
    
    for element in line: #identify first digit
        if element.isdigit():
            first_digit = str(element)
            break
        
    for element in reversed(line): #identify second digit
        if element.isdigit():
            last_digit = str(element)
            break
        
    line_num = int(first_digit + last_digit) #combine both digits and turn into integer
    
    calib_sum += line_num #Sum up all lines' values
            
    
print(first_digit)
print(last_digit)
print("The sum of all caliberation values is {calib_sum}".format(calib_sum = calib_sum))