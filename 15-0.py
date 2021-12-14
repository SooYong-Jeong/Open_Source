import os

def showXY(*stone):
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
stone = [[0, 0, 0, 0, 0, 0, 0, 0, 0],\
        [0, 0, 0, 0, 0, 0, 0, 0, 0],\
        [0, 0, 0, 0, 0, 0, 0, 0, 0],\
        [0, 0, 0, 0, 0, 0, 0, 0, 0],\
        [0, 0, 0, 0, 0, 0, 0, 0, 0],\
        [0, 0, 0, 0, 0, 0, 0, 0, 0],\
        [0, 0, 0, 0, 0, 0, 0, 0, 0],\
        [0, 0, 0, 0, 0, 0, 0, 0, 0],\
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

count = 0
showXY(*stone)
while True:
    
    X = int(input("X축 좌표값을 입력하세요(1 ~ 9, 종료 시 -1 입력) : "))
    if X == -1:
        break
    
    Y = int(input("Y축 좌표값을 입력하세요(1 ~ 9, 종료 시 -1 입력) : "))
    if Y == -1:
        break
    if count%2 == 0:
        stone[X - 1][Y - 1] = 1
    elif count%2 == 1:
        stone[X - 1][Y - 1] = 2
    
    count += 1
    os.system('cls')
    showXY(*stone)