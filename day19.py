#!/usr/local/bin/python3
'''
Advent of code day 19 - 2023
'''
import re


def read_input(input_file):
    '''
    Reads the input
    '''
    def sep(arg):
        return arg.split('=')
    with open(input_file, 'r', encoding="ascii") as file:
        inputs = []
        workflows = {}
        for line in file.readlines():
            line = line.strip()
            if ':' in line:
                _wf = re.split(r'[{},]', line)
                wf_name, _wf = _wf[0], _wf[1:-1]
                workflows[wf_name] = _wf
            elif line:
                line = line.replace('}', '').replace('{', '').split(',')
                inputs += [{k: int(v) for k, v in map(sep, line)}]
        return workflows, inputs


def process(input_file):
    '''
    Process ...
    '''
    def _eval(rule, xmas):
        var, oper, val = rule[0], rule[1], int(rule[2:])
        if oper == '>':
            return xmas[var] > val
        return xmas[var] < val
    workflows, inputs = read_input(input_file)
    total_acc = 0
    for _in in inputs:
        prem = 'in'
        while prem not in 'AR':
            for wf_i in workflows[prem]:
                if ':' not in wf_i:
                    prem = wf_i
                else:
                    rule, prem = wf_i.split(':')
                    if _eval(rule, _in):
                        break
        if prem == 'A':
            total_acc += sum(_in.values())
    total_with_ranges = process_ranges(workflows)
    return total_acc, total_with_ranges


def process_ranges(workflows):
    '''
    Break the full ranges for all variables into regions that satisfy
    the workflow constraints.
    '''
    ranges = {i: [1, 4000] for i in 'xmas'}
    todo = [(ranges, 'in')]
    total = 0
    while todo:
        r_i, prem = todo.pop()
        if prem == 'A':
            prod = 1
            for i in 'xmas':
                prod *= r_i[i][1] - r_i[i][0] + 1
            total += prod
            continue
        if prem == 'R':
            continue
        for wf_i in workflows[prem]:
            if ':' not in wf_i:
                prem = wf_i
                todo.append((r_i, prem))
                continue
            rule, prem = wf_i.split(':')
            r_i_a, r_i_b = r_i.copy(), r_i.copy()
            var, oper, value = rule[0], rule[1], int(rule[2:])
            if oper == '<':
                r_i_a[var] = [r_i[var][0], value-1]
                r_i_b[var] = [value, r_i[var][1]]
            elif oper == '>':
                r_i_b[var] = [r_i[var][0], value]
                r_i_a[var] = [value+1, r_i[var][1]]
            todo.append((r_i_a, prem))
            r_i = r_i_b.copy()
    return total


def test_process():
    '''
    Test the problem assumptions
    '''
    total0, total1 = process('day19a.txt')
    assert total0 == 19114
    assert total1 == 167409079868000


if __name__ == "__main__":
    t_0, t_1 = process('day19.txt')
    print('First solution:', t_0)
    print('Second solution:', t_1)
