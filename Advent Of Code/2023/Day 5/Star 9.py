import re
import numpy as np


docs = open("input.txt", 'r').read()
docs = docs.split(':')
docs = docs[1:]

'''
Labels:
    seed (input), 
    seed to soil
    soil to fertilizer
    fertilizer to water
    water to light
    light to temperature
    temperature to humidity
    humidity to location (output)
'''
def remove_noise(x):
    x = re.sub(r'[^0-9 \n]+', '', x)
    x = re.split(' |\n', x)
    x = list(filter(None, x))
    
    return x

def seperate_map(curr_map):
    new_map = []
    for i in range(0, len(curr_map), 3):
        x = i
        new_map.append(curr_map[x:x+3])
    return new_map


for i in range(len(docs)): #filter to only numerical values
    docs[i] = remove_noise(docs[i])

seeds = docs[0]
maps = docs[1:]


for i in range(len(maps)): #arrange each map sequence
    maps[i] = seperate_map(maps[i])


locations = []

#Calculation of seed to location

for seed in seeds: #iterate seeds
    seed = int(seed)
    for current_map in maps: #iterate each map
        for mapping in current_map:
            start_source = int(mapping[1])
            end_source = start_source + int(mapping[2])
            
            if seed >= start_source and seed <= end_source:
                source_diff = seed - start_source
                destination = int(mapping[0]) + source_diff
                seed = destination
                break
        
    locations.append(seed)
    
#print(locations)
print('Lowest location corresponding to a seed is:{a}'.format(a = locations[np.argmin(locations)]))


