#Day 08

with open('./08.txt') as myinput:
    inputlines = myinput.readlines()

print(sum(len(line.strip()) - len(eval(line.strip())) for line in inputlines))