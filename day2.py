#!/usr/local/bin/python3
'''
Advent of code day 2 - 2023
'''


def process(input_file):
    '''
    Read game results and calculate a score based on the number of
    valid games.
    '''
    total = 0
    power = 0
    limits = {'red': 13, 'green': 14, 'blue': 15}
    with open(input_file, 'r', encoding="ascii") as file:
        for line in file.readlines():
            game, line = line.split(':')
            game = int(game.split()[1])
            is_valid_game = True
            score = {'red': 0, 'green': 0, 'blue': 0}
            for draw in line.split(';'):
                for item in draw.split(','):
                    val, name = item.split()
                    if limits[name] <= int(val):
                        is_valid_game = False
                    score[name] = max(score[name], int(val))
            power += score['red'] * score['green'] * score['blue']
            if is_valid_game:
                total += game
    return total, power


def test_process():
    '''
    Test the problem assumptions
    '''
    sum_of_ids_test, total_power_test = process('day2a.txt')
    assert sum_of_ids_test == 8
    assert total_power_test == 2286


if __name__ == "__main__":
    sum_of_ids, total_power = process('day2.txt')
    print('First solution:', sum_of_ids)
    print('Second solution:', total_power)
