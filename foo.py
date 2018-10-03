state = [['x', 'o', 'x'], ['x', 'x', 'x'], ['x', 'x', 'o']]

state[1][0] = 'x'

for row in state:
    print(row)


def is_winning_row(row, char):
    return all([a == char for a in row])


for row in state:
    if is_winning_row(row, 'x') or is_winning_row(row, 'o'):
        print('Win')
