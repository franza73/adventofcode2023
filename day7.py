#!/usr/local/bin/python3
'''
Advent of code day 7 - 2023
'''
from functools import cmp_to_key
from collections import Counter


def compare0(cards0, cards1):
    '''
    Function to order the cards
    '''
    def rank(cards):
        return ''.join(sorted(map(str, Counter(cards).values()), reverse=True))
    values = 'AKQJT98765432'
    rank0 = rank(cards0)
    rank1 = rank(cards1)
    if rank0 < rank1:
        return -1
    if rank0 > rank1:
        return 1
    for c_0, c_1 in zip(cards0, cards1):
        if values.index(c_0) > values.index(c_1):
            return -1
        if values.index(c_0) < values.index(c_1):
            return 1


def compare1(cards0, cards1):
    '''
    Function to order the cards and handles J substitutions
    '''
    def rank(cards):
        lst = []
        for c_i in set(cards).difference(set('J')):
            subs = cards.replace('J', c_i)
            val = ''.join(sorted(map(str, Counter(subs).values()),
                          reverse=True))
            lst.append(val)
        lst.sort()
        return lst[-1] if lst else '5'
    values = 'AKQT98765432J'
    rank0 = rank(cards0)
    rank1 = rank(cards1)
    if rank0 < rank1:
        return -1
    if rank0 > rank1:
        return 1
    for c_0, c_1 in zip(cards0, cards1):
        if values.index(c_0) > values.index(c_1):
            return -1
        if values.index(c_0) < values.index(c_1):
            return 1


def process_cards(input_file):
    '''
    Process cards
    '''
    all_cards = []
    bid = {}
    with open(input_file, 'r', encoding="ascii") as file:
        for line in file.readlines():
            cards, val = line.strip().split()
            all_cards.append(cards)
            bid[cards] = int(val)
    all_cards0 = sorted(all_cards, key=cmp_to_key(compare0))
    res = 0
    for i, cards in enumerate(all_cards0, start=1):
        res += bid[cards] * i
    all_cards1 = sorted(all_cards, key=cmp_to_key(compare1))
    res1 = 0
    for i, cards in enumerate(all_cards1, start=1):
        res1 += bid[cards] * i
    return res, res1


def test_process_cards():
    '''
    Test the problem assumptions
    '''
    total0, new_total0 = process_cards('day7a.txt')
    assert total0 == 6440
    assert new_total0 == 5905


if __name__ == "__main__":
    total1, new_total1 = process_cards('day7.txt')
    print('First solution:', total1)
    print('Second solution:', new_total1)
