#Day 09

import itertools

with open('./09.txt') as my_input:
    input_lines = my_input.readlines()

distances = [line.split()[::2] for line in input_lines]
locations = {loc: [] for locs in list(zip(*distances))[:2] for loc in locs}

for *locs, distance in distances:
    for i in range(2):
        locations[locs[i]].append((locs[1-i], int(distance)))

routes = itertools.permutations(locations.keys())

distances = set()
for route in routes:
    total_distance = 0
    for location_1, location_2 in zip(route, route[1:]):
        for location, distance in locations[location_1]:
            if location == location_2:
                total_distance += distance
    distances.add(total_distance)

#Part 1

print(min(distances))

#Part 2

print(max(distances))