state = [['x','o','x'], ['x','x','x'],['x','x','o']]

state[1][0] = 'x'


for row in state:
    print(row)

for row in state:
    if all([a=='x' for a in row]) or all([a=='o' for a in row]):
        print 'Win'

