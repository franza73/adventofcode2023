#!/usr/local/bin/python3
'''
Advent of code day 6 - 2023
'''
import re
from math import sqrt


def process_race_data(input_file):
    '''
    Process race data
    '''
    def cnt(t_i, d_i):
        delta = sqrt(t_i**2 - 4.0*d_i - 0.001)
        return int(t_i / 2 + delta / 2) - int(t_i / 2 - delta / 2)
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
        prod *= cnt(t_i, d_i)
    t_i, d_i = time_merged, distance_merged
    return prod, cnt(t_i, d_i)


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
