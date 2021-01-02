#Day 04

import hashlib

with open('./04.txt') as myinput:
    key = myinput.read()

def find_hash(key, leading_numbers):
    result, i = 0, 0
    while not result:
        if hashlib.md5(f'{key}{i}'.encode()).hexdigest()[:len(leading_numbers)] == leading_numbers:
            result = i
        i += 1
    return result

#Part 1

print(find_hash(key, '00000'))

#Part 2

print(find_hash(key, '000000'))        
