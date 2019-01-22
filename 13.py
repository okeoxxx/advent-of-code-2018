from pprint import pprint
carts = []
board = []

file = open('13.txt','r')
while True:
    line = file.readline()
    if line == '':
        break
    board.append([i for i in line])

marks = 'v>^<v>^<'

def changer(mark,direction):
    if direction == 'L':
        return marks[marks.find(mark)+1]
    elif direction == 'R':
        return marks[marks.find(mark)-1]
    elif direction == '/':
        return changer(mark,'L') if mark in '><' else changer(mark,'R')
    else:
        return changer(mark,'R') if mark in '><' else changer(mark,'L')

def intersection(mark,phase):
    if phase % 3 == 1:
        return changer(mark,'L')
    elif phase % 3 == 2:
        return mark
    elif phase % 3 == 0:
        return changer(mark,'R')

for y,row in enumerate(board):
    for x,col in enumerate(board[y]):
        if col in marks:
            carts.append([x,y,1,col,'|' if col in '^v' else '-',0])
carts.sort()
dirs = {'^': (0,-1),'>': (1,0),'v': (0,1),'<': (-1,0)}

new_board = board.copy()
new_carts = []
#crash = True
#while crash:
#    new_carts = []
#    for cart in carts:
#        mark = cart[3]
#        phaser = cart[2]
#        x,y = cart[0],cart[1]
#        new_board[y][x] = cart[4]
#        x,y = x + dirs[cart[3]][0], y + dirs[cart[3]][1]
#        new_field = new_board[y][x]
#        if new_field == '+':
#            mark = intersection(mark,phaser)
#            phaser += 1
#        elif new_field in '/\\':
#            mark = changer(mark,new_field)
#        elif new_field in marks:
#            print('Řešení první časti:',x,y)
#            crash = False
#            break
#        new_board[y][x] = mark
#        new_carts.append([x,y,phaser,mark,new_field])
#    new_carts.sort()
#    carts = new_carts

crash = True
while crash:
    new_carts = []
    for cart in carts:
        if cart[5]:
            new_board[y][x] = cart[4]
            continue
        mark = cart[3]
        phaser = cart[2]
        x,y = cart[0],cart[1]
        new_board[y][x] = cart[4]
        x,y = x + dirs[cart[3]][0], y + dirs[cart[3]][1]
        new_field = new_board[y][x]
        if new_field == '+':
            mark = intersection(mark,phaser)
            phaser += 1
        elif new_field in '/\\':
            mark = changer(mark,new_field)
        elif new_field in marks:
            for j,c in enumerate(new_carts):
                if c[0] == x and c[1] == y:
                    crashed = new_carts.pop(j)
                    new_board[y][x] = crashed[4]
                    break

            for j,c in enumerate(carts):
                if c[0] == x and c[1] == y:
                    carts[j][5] = True
                    break
            continue
        new_board[y][x] = mark
        new_carts.append([x,y,phaser,mark,new_field,0])
    new_carts.sort()
    carts = new_carts
    if len(carts) == 1:
        print('řešení druhé části:',carts[0][0],carts[0][1])
        crash = False
