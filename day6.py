#!/usr/local/bin/python3
'''
Advent of code day 6 - 2023
'''
import re


def process_race_data(input_file):
    '''
    Process race data
    '''
    time = []
    distance = []
    time_merged = distance_merged = 0
    with open(input_file, 'r', encoding="ascii") as file:
        for line in file.readlines():
            line = line.strip()
            if 'Time' in line:
                time = re.findall(r'\d+', line)
                time_merged = int(''.join(time))
                time = list(map(int, time))
            elif 'Distance' in line:
                distance = re.findall(r'\d+', line)
                distance_merged = int(''.join(distance))
                distance = list(map(int, distance))
    prod = 1
    for t_i, d_i in zip(time, distance):
        cnt = 0
        for c_i in range(1, t_i + 1):
            if c_i*(t_i - c_i) > d_i:
                cnt += 1
        prod *= cnt
    prod_merged = 1
    t_i, d_i = time_merged, distance_merged
    cnt = 0
    for c_i in range(1, t_i + 1):
        if c_i*(t_i - c_i) > d_i:
            cnt += 1
    prod_merged *= cnt
    return prod, prod_merged


def test_process_race_data():
    '''
    Test the problem assumptions
    '''
    beat0, merged0 = process_race_data('day6a.txt')
    assert beat0 == 288
    assert merged0 == 71503


if __name__ == "__main__":
    beat1, merged1 = process_race_data('day6.txt')
    print('First solution:', beat1)
    print('Second solution:', merged1)
