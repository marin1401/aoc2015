#Day 01

with open('./01.txt') as myinput:
    instructions = myinput.read()

#Part 1

print(instructions.count('(') - instructions.count(')'))

#Part 2

current_floor = 0
for i in range(len(instructions)):
    if instructions[i] == '(':
        current_floor += 1
    else:
        current_floor -= 1
    if current_floor == -1:
        print(i+1)
        break
