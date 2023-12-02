
#Read input and convert to list
docs = open("input.txt", 'r').read()


docs = docs.split('\n')
docs = docs[0:-1]


dic = {}

for entry in docs: #convert input to dictionary
    key = entry.split(':')[0]
    dic[key] = entry.split(':')[-1]


for key in dic:
    dic[key] = dic[key].replace(';', ',')
    dic[key] = dic[key].split(',')


#initialize counters 
reds = 0
red_str = ''

blues = 0
blue_str = ''

greens = 0
green_str = ''

pow_sum = 0
power = 0

for key in dic:
    for entry in dic[key]: #count color entries
        if 'red' in entry:
            for i in entry:
                if i.isdigit():
                    red_str += i
                    
            reds = max(reds, int(red_str))
            red_str = ''
        elif 'blue' in entry:
            for i in entry:
                if i.isdigit():
                    blue_str += i
                    
            blues = max(blues, int(blue_str))
            blue_str = ''
            
        elif 'green' in entry:
            for i in entry:
                if i.isdigit():
                    green_str += i
                    
            greens = max(greens, int(green_str))
            green_str = ''
    
    #calculate powers and sum
    power = reds * blues * greens
    pow_sum += power
    #reset counters         
    reds = 0
    blues = 0
    greens = 0
    
print("The sum of the powers in all the games is {a}".format(a = pow_sum))     

