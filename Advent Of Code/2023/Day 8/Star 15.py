import re
import itertools

docs = open("C:/Users/user/OneDrive/Desktop/Advent Of Code/2023/Day 8/input.txt", 'r').read()
'''docs = LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
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

current_node = 'AAA'
step_count = 0
found = False



for i in itertools.cycle(steps):
    

    if current_node == 'ZZZ':
        break
    
    if i == 'L':
        
        current_node = node_dict.get(current_node)[0]
        
    if i == 'R':
        
        current_node = node_dict.get(current_node)[1]
    
    step_count += 1
    
print(current_node)
print(step_count)
