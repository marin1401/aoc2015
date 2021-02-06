#Day 08

with open('./08.txt') as myinput:
    inputlines = myinput.readlines()

#Part 1

print(sum(len(line.strip()) - len(eval(line.strip())) for line in inputlines))

#Part 2

print(sum(2 + line.strip().count('"') + line.strip().count('\\') for line in inputlines))
