file = open('10.txt','r')

moves = []

while True:
    l = file.readline()
    if l == '':
        break
    x = int(l[l.find('<')+1:l.find(',')])
    y = int(l[l.find(',')+1:l.find('>')])
    l = l[l.find('>')+1:]
    velX = int(l[l.find('<')+1:l.find(',')])
    velY = int(l[l.find(',')+1:l.find('>')])
    moves.append([x,y,velX,velY])

import re
import numpy as np
from operator import itemgetter

#e10 = [[int(z) for z in re.findall(r'-?\d+', x)] for x in get_input_by_lines(10)]

n10 = np.array(moves)

coords = n10[:, :2].copy()
vels = n10[:, 2:].copy()

def row_exists(coords):
    return len(set(np.array(sorted(coords, key=itemgetter(0)))[:6, 0])) == 1

for i in range(1, 20000):
    coords += vels
    if row_exists(coords):
        print(i)
        print(np.array(sorted(coords, key=itemgetter(0))))

import matplotlib.pyplot as plt

coords = n10[:, :2].copy()
vels = n10[:, 2:].copy()

coords += 10905*vels


canvas = np.zeros(coords.max(axis=0)+2)
canvas[coords[:, 0], coords[:, 1]] += 1

minx, miny = coords.min(axis=0)
plt.imshow(canvas[minx-1:, miny-1:].T)
plt.show()
