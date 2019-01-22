size = 1000

claim_counter = 0

fabric = [[[] for i in range(size)] for i in range(size)]


file = open('3.txt', 'r')


for x in range(1381):
    ID = file.readline()
    edge = int(ID[ID.find('@')+2:ID.find(',')])
    top = int(ID[ID.find(',')+1:ID.find(':')])
    width = int(ID[ID.find(':')+2:ID.find('x')])
    height = int(ID[ID.find('x')+1:])

    for w in range(width):
        for h in range(height):
            if fabric[top+h][edge+w] == []:
                fabric[top+h][edge+w] = 'O'
            elif fabric[top+h][edge+w] == 'O':
                fabric[top+h][edge+w] = 'X'
                claim_counter += 1

print('Numbers of claims:', claim_counter)

file.seek(0)

for x in range(1381):
    ID = file.readline()
    edge = int(ID[ID.find('@')+2:ID.find(',')])
    top = int(ID[ID.find(',')+1:ID.find(':')])
    width = int(ID[ID.find(':')+2:ID.find('x')])
    height = int(ID[ID.find('x')+1:])

    prdel = 0
    for w in range(width):
        for h in range(height):
            if fabric[top+h][edge+w] == 'O':
                fabric[top+h][edge+w] = 'X'
                prdel += 1

    if prdel == width*height:
        print(ID)
        print("Clear")


print('Numbers of claims:', claim_counter)
