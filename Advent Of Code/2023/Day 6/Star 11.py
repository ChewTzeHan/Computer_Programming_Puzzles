import re

docs = open("C:/Users/user/OneDrive/Desktop/Advent Of Code/2023/Day 6/input.txt", 'r').read()
#docs = "Time:      7  15   30 \n Distance:  9  40  200 \n"
#print(docs)

docs = docs.split('\n')
docs = docs[:-1]

def remove_noise(x):
    x = re.sub(r'[^0-9 \n]+', '', x)
    x = re.split(' |\n', x)
    x = list(filter(None, x))
    
    return x

def Success_num(time, dist):
    
    lowest_time = 0
    time_check = False
    while not time_check:
        lowest_time += 1
        max_dist = (time - lowest_time) * lowest_time
        if max_dist > dist:
            time_check = True
            

    successes = (time+1) - (lowest_time*2)
    
    return successes


for i in range(len(docs)):
    docs[i] = remove_noise(docs[i])
print(docs)

for i in range(len(docs)):
    for x in range(len(docs[i])):
        docs[i][x] = int(docs[i][x])
        
time_list = docs[0]
distance_list = docs[1]

record = 1
for i in range(len(time_list)):
    record *= Success_num(time_list[i], distance_list[i])

print(record)