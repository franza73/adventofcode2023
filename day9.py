#!/usr/local/bin/python3
'''
Advent of code day 9 - 2023
'''


def process_differences(input_file):
    '''
    Process network
    '''
    def read_input():
        lines = []
        with open(input_file, 'r', encoding="ascii") as file:
            for line in file.readlines():
                line = line.strip()
                lines += [list(map(int, line.split()))]
        return lines

    lines = read_input()
    total_last = total_first = 0
    for d_i in lines:
        diff = [list(d_i)]
        while True:
            diff += [[d_i[i] - d_i[i-1] for i in range(1, len(d_i))]]
            d_i = diff[-1]
            if set(d_i) == set([0]):
                break

        diff[-1] += [0]
        for i in range(len(diff)-2, -1, -1):
            diff[i] += [diff[i][-1] + diff[i+1][-1]]
        total_last += diff[0][-1]

        diff[-1] = [0] + diff[-1]
        for i in range(len(diff)-2, -1, -1):
            diff[i] = [diff[i][0] - diff[i+1][0]] + diff[i]
        total_first += diff[0][0]

    return total_last, total_first


def test_process_differences():
    '''
    Test the problem assumptions
    '''
    indexa, indexb = process_differences('day9a.txt')
    assert indexa == 114
    assert indexb == 2


if __name__ == "__main__":
    indexc, indexd = process_differences('day9.txt')
    print('First solution:', indexc)
    print('Second solution:', indexd)
