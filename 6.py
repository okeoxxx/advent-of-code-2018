

file = open('6.txt','r')
coordinates = []
dict = {}
highestX = 0
highestY = 0
infinity_coordinates = []

while True:
    coordinate = file.readline()
    if coordinate == '':
        break
    coordinate = (int(coordinate[:coordinate.find(',')]),int(coordinate[coordinate.find(' ')+1:]))
    coordinates.append(coordinate)
    if coordinate[0] > highestX:
        highestX = coordinate[0]
    if coordinate[1] > highestY:
        highestY = coordinate[1]


print(highestX,highestY)

for row in range(highestY+1):
    for col in (range(highestX+1)):
        closest = (0,0)
        LowestDist = highestX+highestY
        for coordinate in coordinates:
            x = coordinate[0]-col
            y = coordinate[1]-row
            dist = abs(x)+abs(y)
            if dist == LowestDist:
                closest = '.'
            if dist < LowestDist:
                LowestDist = dist
                closest = coordinate

        count = dict.get(closest,0)+1
        if dict.setdefault(closest,count) != count:
            dict[closest]= count

        if col == 0 or col == highestX or row == 0 or row == highestY:
            if closest not in infinity_coordinates:
                infinity_coordinates.append(closest)


highest = 0

for coor in dict:
    if coor not in infinity_coordinates:
        count = dict.get(coor,0)
        if count > highest:
            highest = count

print('Řešení první půlky:', highest)

max_totalDist = 10000
counter = 0


for row in range(highestY+1):
    for col in (range(highestX+1)):
        dist = 0
        for coordinate in coordinates:
            x = coordinate[0]-col
            y = coordinate[1]-row
            dist += abs(x)+abs(y)
        if dist < max_totalDist:
            counter +=1

print('Řešení druhé půlky:', counter)
