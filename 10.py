#Day 10

with open('./10.txt') as my_input:
    my_number = my_input.read()

def get_number_length(number, n):
    while n:
        sequence = [[number[0]]]
        for prev_digit, next_digit in zip(number, number[1:]):
            if next_digit in sequence[-1]:
                sequence[-1].append(next_digit)
            else:
                sequence.append([next_digit])
        number = ''
        for digits in sequence:
            number += str(len(digits)) + digits[0]
        n -= 1
    return len(number)

#Part 1

print(get_number_length(my_number, 40))

#Part 2

print(get_number_length(my_number, 50))