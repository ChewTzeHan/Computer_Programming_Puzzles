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

new_seeds = []
for i in range(0, len(seeds), 2):
    x = i
    new_seeds.append(seeds[x:x+2])
    
print(new_seeds)
seeds = []
for i in new_seeds:
    start_seed = int(i[0])
    end_seed = start_seed + int(i[1])
    
    seed_pack = np.arange(start_seed, end_seed)
    seeds.append(seed_pack)
    
print(len(seeds))

locations = []

#Calculation of seed to location

for seed_pack in seeds: #iterate seeds
    for seed in seed_pack:
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
#print(seeds)
print('Lowest location corresponding to a seed is:{a}'.format(a = locations[np.argmin(locations)]))


