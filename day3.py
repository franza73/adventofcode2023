#!/usr/local/bin/python3
'''
Advent of code day 3 - 2023
'''
from collections import defaultdict
from itertools import product


def process_schematic(input_file):
    '''
    Process schematic
    '''
    def neighbors(i, j):
        res = set()
        for d_x, d_y in product(range(-1, 2), range(-1, 2)):
            if 0 <= i + d_x < matx and 0 <= j + d_y < maty:
                res.add((i+d_x, j+d_y))
        return res

    mat = []
    total = 0
    gears = defaultdict(list)
    with open(input_file, 'r', encoding="ascii") as file:
        for line in file.readlines():
            mat += [list(line.strip())]
    matx, maty = len(mat), len(mat[0])
    for i in range(maty):
        current = ''
        neigh = False
        this_gear = None
        for j in range(maty):
            if mat[i][j].isdigit():
                current += mat[i][j]
                for n_x, n_y in neighbors(i, j):
                    if mat[n_x][n_y] not in '0123456789.':
                        neigh = True
                    if mat[n_x][n_y] == '*':
                        this_gear = (n_x, n_y)
            else:
                if current and neigh:
                    total += int(current)
                    if this_gear:
                        gears[this_gear] += [int(current)]
                current = ''
                neigh = False
                this_gear = None
        if current and neigh:
            total += int(current)
            if this_gear:
                gears[this_gear] += [int(current)]
    gear_ratios = 0
    for k in gears:
        if len(gears[k]) == 2:
            gear_ratios += gears[k][0] * gears[k][1]
    return total, gear_ratios


def test_process_schematic():
    '''
    Test the problem assumptions
    '''
    total0, gear_ratios0 = process_schematic('day3a.txt')
    assert total0 == 4361
    assert gear_ratios0 == 467835


if __name__ == "__main__":
    total1, gear_ratios1 = process_schematic('day3.txt')
    print('First solution:', total1)
    print('Second solution:', gear_ratios1)
