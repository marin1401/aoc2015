#Day 06

with open('./06.txt') as myinput:
    instructions = myinput.readlines()

instructions = [i.split() for i in instructions]

grid_size = 1000
lights = [[0 for x in range(grid_size)] for y in range(grid_size)]
brightness = [[0 for x in range(grid_size)] for y in range(grid_size)]

for instruction in instructions:
    turn = instruction[1]
    x1, y1 = map(int, instruction[-3].split(','))
    x2, y2 = map(int, instruction[-1].split(','))
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if turn == 'on':
                lights[x][y] = 1
                brightness[x][y] += 1
            elif turn == 'off':
                lights[x][y] = 0
                brightness[x][y] -= 1 if brightness[x][y] else 0
            else:
                lights[x][y] = 0 if lights[x][y] else 1
                brightness[x][y] += 2

#Part 1

print(sum(map(sum, lights)))

#Part 2

print(sum(map(sum, brightness)))
