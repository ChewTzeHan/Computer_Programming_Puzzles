import re
#import numpy as np


docs = open("input.txt", 'r').read()
docs = docs.split(':')
docs = docs[1:]

'''
Labels:
    seed (input), 
    seed to soil
    soil to fertilizer
    fertilizer to water
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

def split_ranges(pair, ranges):  # will split ranges based on changes in ranges
    splits = []
    s, e = pair
    #old + length = source_end
    #new + length = destination_end
    #old = source_start
    #new = destination_start
    for new, old, length in ranges:
        if old <= s <= old + length and old <= e <= old + length: #s and e between source start and end
            splits.append((new + s - old, new + e - old))
        elif old <= s <= old + length: #only start in range of source
            end = old + length #destination end
            splits.append((new + s - old, new + end - old))
            s = end - 1
        elif old <= e <= old + length: #only end in range of source
            start = old #source start
            splits.append((new + start - old, new + e - old))
            e = start + 1
        elif s <= old <= e and s <= old + length <= e: #source in start and end range
            splits.append((new, new + length))

    if not splits:
        return [pair]

    if pair != (s, e):
        splits.append((s, e))

    return splits


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
    
seeds = new_seeds

for i in range(len(seeds)):
    for x in range(len(seeds[i])):
        seeds[i][x] = int(seeds[i][x])

for i in range(len(maps)):
    for x in range(len(maps[i])):
        for y in range(len(maps[i][x])):
            maps[i][x][y] = int(maps[i][x][y])
    


pairs = []
for start, ranges in seeds:
    pairs.append((start, start + ranges - 1))


for ranges in maps:
    newpairs = []
    for pair in pairs:
        newpairs += split_ranges(pair, ranges)
    pairs = newpairs
    
pairs_sorted = sorted(pairs)

print('Lowset location number is:{a}'.format(a = pairs_sorted[0][0]))


