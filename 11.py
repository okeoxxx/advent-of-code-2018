from pprint import pprint as pp
large = 300
table = []
serial_number = 1308

def power_level(x,y,serial_number):
    ID = x+10
    pow_lev = ID * y
    total_level = (pow_lev + serial_number) * ID
    hundreds = int(str(total_level)[-3])
    return hundreds - 5


for row in range(large):
    table.append([])
    for col in range(large):
        table[row].append(power_level(col+1,row+1,serial_number))

highest = 0
highest_coor = (0,0,0)
#řešení první části
#for row in range(large-2):
#    for col in range(large-2):
#        square = 0
#        for a in range(3):
#            for b in range(3):
#                square += table[row+a][col+b]
#
#        if square > highest:
#            highest = square
#            highest_coor = (col+1,row+1)

#print(highest)
#print(highest_coor)

#řešení druhé části
for row in range(large-1):
    for col in range(large-1):
        highest_square = large-col if col >= row else large-row
        for i in range(highest_square):
            square = 0
            for a in range(i):
                for b in range(i):
                    square += table[row+a][col+b]
            if square > highest:
                highest = square
                highest_coor = (col+1,row+1,i)
        print(col,highest,highest_coor)

print(highest,highest_coor)
