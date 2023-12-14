#!/usr/local/bin/python3
'''
Advent of code day 11 - 2023
'''
from bisect import bisect
from itertools import combinations


def read_image(input_file):
    '''
    Reads the image with galaxies
    '''
    empty_y = None
    empty_x = []
    galaxies = []
    with open(input_file, 'r', encoding="ascii") as file:
        for i, line in enumerate(file.readlines()):
            line = line.strip()
            if '#' not in line:
                empty_x.append(i)
            if not empty_y:
                empty_y = set(range(len(line)))
            for j, val in enumerate(list(line)):
                if val == '#':
                    galaxies.append((i, j))
                    if j in empty_y:
                        empty_y.remove(j)
    empty_y = sorted(empty_y)
    return galaxies, empty_x, empty_y


def process_image(input_file):
    '''
    Process the image to produce the total distance between pairs of galaxies
    '''
    def _total(cte=1):
        if cte > 1:
            cte -= 1
        total = 0
        for g_i, g_j in combinations(galaxies, 2):
            a_x, a_y = g_i
            b_x, b_y = g_j
            d_x = (bisect(empty_x, b_x) - bisect(empty_x, a_x))*cte + b_x - a_x
            d_y = (bisect(empty_y, b_y) - bisect(empty_y, a_y))*cte + b_y - a_y
            total += abs(d_x) + abs(d_y)
        return total
    galaxies, empty_x, empty_y = read_image(input_file)
    return _total(), _total(1000000)


def test_process_image():
    '''
    Test the problem assumptions
    '''
    total0, _ = process_image('day11a.txt')
    assert total0 == 374


if __name__ == "__main__":
    t_0, t_1 = process_image('day11.txt')
    print('First solution:', t_0)
    print('Second solution:', t_1)
