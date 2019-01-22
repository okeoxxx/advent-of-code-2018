file = open('23.txt','r')
positions = []
ranges = []

maxX,maxY,maxZ = 0,0,0
minX,minY,minZ = 0,0,0


while True:
    line = file.readline()
    if line == '':
        break

    x,y,z = list(map(int,line[line.find('<')+1:line.find('>')].split(',')))
    if x > maxX:
        maxX = x
    if x < minX:
        minX = x
    if y > maxY:
        maxY = y
    if y < minY:
        minY = y
    if z > maxZ:
        maxZ = z
    if z < minZ:
        minZ = z
    r = int(line[line.find('r')+2:])
    positions.append([x,y,z])
    ranges.append(r)

index_of_highest = ''
highest_range = max(ranges)

for i,v in enumerate(ranges):
    if v == highest_range:
        index_of_highest = i
        break

nanobot = positions[index_of_highest]

distances = []
counter = 0

for p in positions:
    dist = 0
    i = 0
    for v in p:
        dist += abs(nanobot[i]-v)
        i += 1
    distances.append(dist)
    if dist <= highest_range:
        counter += 1

print('Solution1:', counter)
print((minX-maxX)*(minY-maxY)*(minZ-maxZ))

num_in_range = []

for i,p1 in enumerate(positions):
    counter = 0
    for j,p2 in enumerate(positions):
        dist = 0
        k = 0
        for v in p2:
            dist += abs(p1[k]-v)
            k += 1
        if dist <= ranges[j]:
            counter += 1
    num_in_range.append(counter)

start = [0,0,0]#[19992232, 58718915, 22274751]
start_num = 0
print(start)
i = 1
prdel = 2000000000
while True:
    directions = [(-i,-i,-i),(0,-i,-i),(+i,-i,-i),
                    (-i,0,-i),(0,0,-i),(+i,0,-i),
                    (-i,+i,-i),(0,+i,-i),(+i,+i,-i),
                    (-i,-i,0),(0,-i,0),(+i,-i,0),
                    (-i,0,0),(+i,0,0),
                    (-i,+i,0),(0,+i,0),(+i,+i,0),
                    (-i,-i,+i),(0,-i,+i),(+i,-i,+i),
                    (-i,0,+i),(0,0,+i),(+i,0,+i),
                    (-i,+i,+i),(0,+i,+i),(+i,+i,+i)]

    for d in directions:
        counter = 0
        prd = []
        for j,p2 in enumerate(positions):
            dist = 0
            k = 0
            for v in p2:
                dist += abs(start[k]+d[k]-v)
                k += 1
            if dist <= ranges[j]:
                counter += 1
            else:
                prd.append((dist-ranges[j],p2)) #sbírá vzdálenosti k nejbližsímu nanobotu
        if counter > start_num:
            start_num = counter
            start[0],start[1],start[2] = start[0] + d[0], start[1] + d[1], start[2] + d[2]
            i = 1
            print(start, counter)
            prdel = 2000000000

        #posouvá se k nejbližsímu dostupnému nanobotu
        prd.sort()
        if prd[0][0] < prdel and counter >= start_num:
            print(prd[0][0])
            prdel = prd[0][0]
            start[0],start[1],start[2] = start[0] + d[0], start[1] + d[1], start[2] + d[2]
            i = 1

        #hledá bod nejblíž k nule
        elif counter == start_num and sum(d) < 0:
            start[0],start[1],start[2] = start[0] + d[0], start[1] + d[1], start[2] + d[2]
            i = 1000
            print(start, counter)
    i += 1000
    if i >= 500000:
        break

print('Solution2:', start[0]+start[1]+start[2])
