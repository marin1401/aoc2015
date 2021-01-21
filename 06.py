#Day 06

with open('./06.txt') as myinput:
    instructions = myinput.readlines()

instructions = [i.replace('n o', 'n_o').split() for i in instructions]

lights = [[0 for i in range(1000)] for j in range(1000)]

def switch(instructions, lights, part):
    for instruction in instructions:
        do = instruction[0]
        [x1, y1] = list(map(int, instruction[1].split(',')))
        [x2, y2] = list(map(int, instruction[3].split(',')))
        for x in range(x2 - x1 + 1):
            for y in range(y2 - y1 + 1):
                if do == 'turn_on':
                    lights[x1 + x][y1 + y] = 1 if part == 1 else lights[x1 + x][y1 + y] + 1
                elif do == 'turn_off':
                    if lights[x1 + x][y1 + y]:
                        lights[x1 + x][y1 + y] = 0 if part == 1 else lights[x1 + x][y1 + y] - 1
                elif do == 'toggle':
                    if part == 1:
                        lights[x1 + x][y1 + y] = 0 if lights[x1 + x][y1 + y] == 1 else 1
                    else:
                        lights[x1 + x][y1 + y] += 2

#Part 1

switch(instructions, lights, 1)

print(sum(map(sum, lights)))

#Part 2

lights = [[0 for i in range(1000)] for j in range(1000)]

switch(instructions, lights, 2)

print(sum(map(sum, lights)))