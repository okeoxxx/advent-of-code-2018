import pprint

file = open('18.txt','r')
board = []

while True:
    line = file.readline()
    if line == '':
        break
    board.append([])
    for i in line[:50]:
        board[-1].append(i)

directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

def counter(board):
    trees,lumberyards = 0,0
    for row in board:
        for col in row:
            if col == '|':
                trees += 1
            elif col == '#':
                lumberyards += 1
    return trees*lumberyards

for minute in range(0,100000):
    if minute % 100 == 0:
        print(minute)
        print('řešením je:', counter(board))
    if minute == 10:
        print(minute)
        print('řešením je:', counter(board))
    new_board = []
    for i,row in enumerate(board):
        new_board.append([])
        for j,col in enumerate(board[i]):
            trees,lumberyards = 0,0
            for d in directions:
                x = j + d[1]
                y = i + d[0]
                if x < 0 or y < 0 or x > 49 or y > 49:
                    continue
                if board[y][x] == '|':
                    trees += 1
                elif board[y][x] == '#':
                    lumberyards += 1

            if board[i][j] == '.':
                if trees > 2:
                    new_board[i].append('|')
                else:
                    new_board[i].append('.')
            elif board[i][j] == '|':
                if lumberyards > 2:
                    new_board[i].append('#')
                else:
                    new_board[i].append('|')
            else:
                if trees == 0 or lumberyards == 0:
                    new_board[i].append('.')
                else:
                    new_board[i].append('#')

    board = new_board
print(board)
