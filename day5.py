#!/usr/local/bin/python3
'''
Advent of code day 5 - 2023
'''
from collections import defaultdict
from math import inf
from functools import cache


def process_seeds(input_file):
    '''
    Process the seed tables
    '''
    @cache
    def function(key, val):
        for k in maps[key]:
            if 0 <= val - k[1] <= k[2]:
                return dest[key], k[0] + val - k[1]
        return dest[key], val

    @cache
    def compose(v_i):
        x_i = 'seed'
        while x_i != 'location':
            x_i, v_i = function(x_i, v_i)
        return v_i

    def best(first, last):
        def line(val):
            return compose(val) - val
        if line(first) == line(last):
            return compose(first)
        middle = (first + last) // 2
        return min(best(first, middle), best(middle+1, last))

    def read():
        seeds = []
        dest = {}
        maps = defaultdict(list)
        src, dst = None, None
        with open(input_file, 'r', encoding="ascii") as file:
            for line in file.readlines():
                line = line.strip()
                if ':' in line:
                    name, line = line.split(':')
                    if name == 'seeds':
                        seeds = list(map(int, line.split()))
                    else:
                        src, _, dst = name.split()[0].split('-')
                        dest[src] = dst
                else:
                    if src and line:
                        maps[src] += [list(map(int, line.split()))]
        return seeds, dest, maps

    seeds, dest, maps = read()
    lowest = inf
    for i in range(len(seeds)//2):
        first, delta = seeds[2*i:2*i+2]
        lowest = min(lowest, best(first, first + delta - 1))
    return min(compose(s_i) for s_i in seeds), lowest


def test_process_seeds():
    '''
    Test the problem assumptions
    '''
    total0, lowest0 = process_seeds('day5a.txt')
    assert total0 == 35
    assert lowest0 == 46


if __name__ == "__main__":
    total1, lowest1 = process_seeds('day5.txt')
    print('First solution:', total1)
    print('Second solution:', lowest1)
