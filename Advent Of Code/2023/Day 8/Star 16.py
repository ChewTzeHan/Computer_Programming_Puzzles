import re
import itertools
import math

docs = open("C:/Users/user/OneDrive/Desktop/Advent Of Code/2023/Day 8/input.txt", 'r').read()
'''docs = LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
'''
docs = docs.split('\n')[:-1]

#print(docs)

steps = list(docs[0])

#print(steps)

nodes = docs[2:]

for i in range(len(nodes)):
    nodes[i] = nodes[i].split('=')
    
    nodes[i][0] = nodes[i][0].strip()
    
    nodes[i][1] = tuple(re.sub('[() ]', "", nodes[i][1]).split(','))
    
    #nodes[i][1] = tuple(nodes[i][1].split(','))
    
#print(nodes[0][1])
#print(nodes)
#print('-----')

node_dict = dict()

for node in nodes:
    node_dict[node[0]] = node[1]
    
#print(node_dict)    

#print(node_dict.keys())

current_nodes = []
for node in node_dict.keys():
    if node[-1] == 'A':
        current_nodes.append(node)

print(current_nodes)

step_count_list = []
step_count = 0

for i in range(len(current_nodes)):
    for direction in itertools.cycle(steps): 
        
        if current_nodes[i][-1] == 'Z':
            step_count_list.append(step_count)
            step_count = 0
            break
        
        if direction == 'L': #LEFT NODE = 0     
            current_nodes[i] = node_dict.get(current_nodes[i])[0]     
        
        if direction == 'R': #RIGHT NODE = 1
            current_nodes[i] = node_dict.get(current_nodes[i])[1]
    
        step_count += 1    

print(current_nodes)
print(step_count_list)
'''
ASSUME ALL PATHS LOOP, LCM OF ALL PATHS TO REACH Z = TOTAL STEPS FOR ALL
'''
Total_steps = math.lcm(*step_count_list)

print('Total_steps taken is: {a}'.format(a = Total_steps))
