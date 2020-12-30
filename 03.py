#Day 03

with open('./03.txt') as myinput:
    instructions = myinput.read()

def go_next(direction, x, y):
    if direction == '^':
        y += 1
    elif direction == 'v':
        y -= 1
    elif direction == '>':
        x += 1
    elif direction == '<':
        x -= 1
    return x, y

#Part 1
x, y = 0, 0
location = set()
location.add((0, 0))
for direction in instructions:
    x, y = go_next(direction, x, y)
    location.add((x, y))

print(len(location))

#Part 2

xs, ys, xr, yr = 0, 0, 0, 0
location = set()
location.add((0, 0))
for i in range(len(instructions)):
    if i % 2 == 0:
        xs, ys = go_next(instructions[i], xs, ys)
        location.add((xs, ys))
    else:
        xr, yr = go_next(instructions[i], xr, yr)
        location.add((xr, yr))

print(len(location))