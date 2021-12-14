stone = [[0, 0, 0, 0, 0, 0, 0, 0, 0],\
        [0, 1, 0, 1, 2, 1, 2, 1, 0],\
        [0, 2, 1, 1, 1, 2, 2, 0, 0],\
        [0, 0, 2, 2, 2, 1, 0, 2, 0],\
        [0, 0, 0, 0, 0, 1, 0, 2, 1],\
        [0, 0, 0, 2, 0, 1, 2, 1, 0],\
        [0, 0, 0, 2, 1, 0, 1, 1, 0],\
        [0, 0, 0, 1, 1, 0, 0, 0, 0],\
        [0, 0, 0, 0, 2, 2, 2, 0, 0]]

num_black = 0 #?? 왜있음?
num_white = 0

print(' ' * 3, end = '')
for i in range(9):
    print("{}".format(i + 1), end = ' ')
print()

for i in range(9):
    print("{}  ".format(i + 1), end = '')
    for j in range(9):
        if stone[i][j] == 1:
            print("{} ".format('●'), end = '')
        elif stone[i][j] == 2:
            print("{} ".format('○'), end = '')
        else:
            print("{} ".format('x'), end = '')
    print()