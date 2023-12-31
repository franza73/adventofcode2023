#!/usr/local/bin/python3
'''
Advent of code day 4 - 2023
'''
from collections import Counter


def process_scratchcards(input_file):
    '''
    Process the scratchpads and calculate the total and score
    '''
    total = 0
    scores = {}
    todo = Counter()
    with open(input_file, 'r', encoding="ascii") as file:
        for line in file.readlines():
            card, line = line.strip().split(':')
            card = int(card.split()[1])
            todo[card] = 1
            win, res = line.split('|')
            win, res = set(win.split()), set(res.split())
            common = len(win.intersection(res))
            scores[card] = common
            if common != 0:
                total += 2**(common - 1)
    score = 0
    for card in sorted(todo.keys()):
        score += todo[card]
        for new_card in range(card+1, card+scores[card]+1):
            todo[new_card] += todo[card]
    return total, score


def test_process_scratchpads():
    '''
    Test the problem assumptions
    '''
    total0, score0 = process_scratchcards('day4a.txt')
    assert total0 == 13
    assert score0 == 30


if __name__ == "__main__":
    total1, score1 = process_scratchcards('day4.txt')
    print('First solution:', total1)
    print('Second solution:', score1)
