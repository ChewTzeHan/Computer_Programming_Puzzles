

#Read input and convert to list
docs = open("input.txt", 'r').read()
docs = docs.split()
#docs = ['2911threeninesdvxvheightwobm', '3three16xsxhpnqmzmnine8one']

calib_sum = 0

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
            
    

print("The sum of all caliberation values is {calib_sum}".format(calib_sum = calib_sum))