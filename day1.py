#!/usr/local/bin/python3
'''
Advent of code day 1 - 2023
'''


def process(data_file, translate=False):
    '''
    Read numbers from input with and without translation of names of numbers.
    Produces the a total sum that depends on first and last number found
    on each line of the file.
    '''
    total = 0
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    with open(data_file, 'r', encoding="ascii") as file:
        for line in file.readlines():
            nums = []
            for i, d_i in enumerate(line):
                if d_i.isdigit():
                    nums += [int(d_i)]
                if not translate:
                    continue
                for n_i, v_i in numbers.items():
                    if line[i:].startswith(n_i):
                        nums += [v_i]
            total += nums[0]*10 + nums[-1]
    return total


def test_number_translation():
    '''
    Test reading numbers and number names
    '''
    assert process('day1a.txt') == 142
    assert process('day1b.txt', True) == 281


if __name__ == "__main__":
    FILE = 'day1.txt'
    print('First solution:', process(FILE))
    print('Second solution:', process(FILE, True))
