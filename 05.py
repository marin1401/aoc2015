#Day 05

with open('./05.txt') as myinput:
    inputlines = myinput.readlines()

strings = [i.strip() for i in inputlines]

#Part 1

vowels = 'aeiou'
bad_strings = ['ab', 'cd', 'pq', 'xy']

counter = 0
for string in strings:
    condition = set()
    vowel_counter = 0
    for vowel in vowels:
        vowel_counter += string.count(vowel)
    if vowel_counter > 2:
        for current_letter, next_letter in zip(string, string[1:]):
            if current_letter + next_letter in bad_strings:
                condition.add(False)
            if current_letter == next_letter:
                condition.add(True)
        if condition == {True}:
            counter += 1

print(counter)

#Part 2

counter = 0
for string in strings:
    condition = set()
    for first_letter, second_letter, third_letter in zip(string, string[1:], string[2:]):
        if string.count(first_letter + second_letter) > 1:
            condition.add(1)
        if first_letter == third_letter:
            condition.add(2)
    if len(condition) == 2:
        counter += 1

print(counter)