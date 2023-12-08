#!/usr/local/bin/python3
'''
Advent of code day 8 - 2023
'''
import re
from math import lcm


def process_network(input_file):
    '''
    Process network
    '''
    def read():
        instr = ''
        net = {}
        with open(input_file, 'r', encoding="ascii") as file:
            for line in file.readlines():
                line = line.strip()
                if '=' in line:
                    key, to_l, to_r = re.findall(r'\w{3}', line)
                    net[key] = [to_l, to_r]
                elif line:
                    instr = line
        return instr, net
    instr, net = read()
    # -- fisrt --
    index = 0
    node = 'AAA'
    while True:
        node = net[node][0 if instr[index % len(instr)] == 'L' else 1]
        index += 1
        if node == 'ZZZ':
            break
    # -- second --
    nodes = [node for node in net if node[-1] == 'A']
    res = []
    for node in nodes:
        index1 = 0
        while True:
            pos = 0 if instr[index1 % len(instr)] == 'L' else 1
            node = net[node][pos]
            index1 += 1
            if node[-1] == 'Z':
                res.append(index1)
                break
    return index, lcm(*res)


def test_process_network():
    '''
    Test the problem assumptions
    '''
    indexa, indexb = process_network('day8a.txt')
    assert indexa == 6
    assert indexb == 6


if __name__ == "__main__":
    indexc, indexd = process_network('day8.txt')
    print('First solution:', indexc)
    print('Second solution:', indexd)
