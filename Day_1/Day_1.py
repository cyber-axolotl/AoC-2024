# AoC - Day 1
# Federico Pevere - 2024

# ---- Part One ----
print('----- Day 1 Part One -----')

# Open the puzzle input file for reading
with open("input.txt", "r") as file:
    # Initialize input_lists, it will contain
    # the two lists of location IDs
    input_lists = [[],[]]
    for line in file:
        # Convert each column value to a integer number,
        # add it to the corresponding list 
        for idx, id in enumerate(line.split()):
            input_lists[idx].append(int(id)) 

# DEBUG
print('Input lists: ', input_lists)

# sort the lists
ordered_lists = input_lists
for ordered_list in ordered_lists:
    ordered_list.sort()

# DEBUG
print('Ordered lists: ', ordered_lists)

# calculate the distance between corresponding elements
# note that zip(*ordered_lists) transposes the list containing
# the two lists
distances = [abs(a-b) for a,b in zip(*ordered_lists)]

# DEBUG
#print('Distances: ', distances)

# find the total distance
total_distance = sum(distances)
print('Total distance = ', total_distance)

# ---- Part Two ----
print('----- Day 1 Part Two -----')

import numpy as np

ordered_lists = np.array(ordered_lists)
similarity_score = 0
for value in ordered_lists[0]:
    condition = ordered_lists[1] == value
    # DEBUG
    #print('Condition:', condition)
    count = np.count_nonzero(np.extract(condition, ordered_lists[1]))
    similarity_score += value*count
    # DEBUG
    #print(f'Value {value} from the 1st list is present {count} times in the 2nd list.')
    #print(f'Similarity score increases by {value*count}')

# DEBUG
print('Similarity score = ', similarity_score)