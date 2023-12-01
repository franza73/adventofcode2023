#!/usr/local/bin/python3
'''
Advent of code day 1 - 2023
'''


def process(translate=False):
    '''
    Read numbers from input with and without translation of names of numbers.
    Produces the a total sum that depends on first and last number found
    on each line of the file.
    '''
    total = 0
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    with open('day1.txt', 'r', encoding="ascii") as file:
        while True:
            line = file.readline()
            if not line:
                break
            nums = []
            for i, d_i in enumerate(line):
                for n_i in numbers:
                    if line[i].isdigit():
                        nums += [int(d_i)]
                    elif translate and line[i:].startswith(n_i):
                        nums += [numbers[n_i]]
            total += nums[0]*10 + nums[-1]
    return total


print('First solution:', process())
print('Second solution:', process(True))
