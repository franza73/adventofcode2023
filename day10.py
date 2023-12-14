#!/usr/local/bin/python3
'''
Advent of code day 10 - 2023
'''
nxt = {'R7': 'D', 'RJ': 'U', 'R-': 'R',
       'LL': 'U', 'LF': 'D', 'L-': 'L',
       'DL': 'R', 'DJ': 'L', 'D|': 'D',
       'U7': 'L', 'UF': 'R', 'U|': 'U'}
dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
verify_dirs = {'U': '|F7', 'D': '|LJ', 'R': '-J7', 'L': '-LF'}
guess_s = {'UR': 'L', 'UD': '|', 'UL': 'J', 'RD': 'F', 'RL': '-', 'DL': '7'}


def read_maze(input_file):
    '''
    Reads maze, finds starting point and guesses its direction.
    '''
    lines = []
    s_i = s_j = None
    with open(input_file, 'r', encoding="ascii") as file:
        for i, line in enumerate(file.readlines()):
            lines += [list(line.strip())]
            if 'S' in line:
                s_i, s_j = i, line.index('S')
    s_n_i = s_n_j = s_n_d = None
    key = ''
    for d_n in 'URDL':
        n_i, n_j = s_i+dirs[d_n][0], s_j+dirs[d_n][1]
        if not (0 <= n_i < len(lines) and 0 <= n_j < len(lines[0])) or \
                lines[n_i][n_j] == '.':
            continue
        if lines[n_i][n_j] in verify_dirs[d_n]:
            key += d_n
        if not s_n_i:
            s_n_i, s_n_j, s_n_d = n_i, n_j, d_n
    d_guess_s = guess_s[key]
    return lines, s_n_i, s_n_j, s_n_d, d_guess_s


def find_loop(lines, n_i, n_j, d_n, d_guess_s):
    '''
    Finds which points are on the loop
    '''
    loop = set()
    cnt = 1
    while True:
        step = d_n + lines[n_i][n_j]
        if step in nxt:
            d_n = nxt[step]
            d_x, d_y = dirs[nxt[step]]
            loop.add((n_i, n_j))
            n_i, n_j = n_i+d_x, n_j+d_y
            cnt += 1
            if lines[n_i][n_j] == 'S':
                lines[n_i][n_j] = d_guess_s
                loop.add((n_i, n_j))
                break
    return cnt//2, loop


def count_inside_points(lines, loop):
    '''
    Counts points inside the loop
    '''
    cnt = 0
    l_x, l_y = len(lines), len(lines[0])
    for i in range(l_x):
        s_p = set()
        parity = 0
        for j in range(l_y):
            if (i, j) not in loop:
                if parity == 1:
                    cnt += 1
            else:
                if 'F' in s_p and lines[i][j] == 'J':
                    parity += 1
                    s_p.remove('F')
                elif 'L' in s_p and lines[i][j] == '7':
                    parity += 1
                    s_p.remove('L')
                elif 'F' in s_p and lines[i][j] == '7':
                    s_p.remove('F')
                elif 'L' in s_p and lines[i][j] == 'J':
                    s_p.remove('L')
                elif lines[i][j] == '|':
                    parity += 1
                elif lines[i][j] != '-':
                    s_p.add(lines[i][j])
            parity %= 2
    return cnt


def process_maze(input_file):
    '''
    Process maze
    '''
    lines, n_i, n_j, d_n, d_guess_s = read_maze(input_file)
    cnt, loop = find_loop(lines, n_i, n_j, d_n, d_guess_s)
    return cnt, count_inside_points(lines, loop)


def test_process_maze():
    '''
    Test the problem assumptions
    '''
    t_first0, t_last0 = process_maze('day10a.txt')
    assert t_first0 == 8
    assert t_last0 == 1


if __name__ == "__main__":
    t_first, t_last = process_maze('day10.txt')
    print('First solution:', t_first)
    print('Second solution:', t_last)
