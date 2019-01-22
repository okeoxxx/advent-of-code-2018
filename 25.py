file = open('25.txt','r')

points = []

while True:
    line = file.readline()
    if line == '':
        break
    lst = [int(num) for num in line.split(',')]
    points.append(lst)

print(points)
connections = []
for i,p1 in enumerate(points):
    connections.append(set())
    for j,p2 in enumerate(points):
        dist = 0
        for num in range(4):
            dist += abs(p1[num]-p2[num])
        if dist <= 3:
            connections[i].add(j)

print(connections)
def merge(connections):
    merged = []
    for s in connections:
        changer = 1
        for i,m in enumerate(merged):
            if s & m:
                merged[i] = s | m
                changer = 0
                break
        if changer:
            merged.append(s)
    return (merged, connections != merged)

change = 1
while change:
    connections,change = merge(connections)

print(len(connections))
