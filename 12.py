from pprint import pprint as pp

initial = '#....#.#....#....#######..##....###.##....##.#.#.##...##.##.#...#..###....#.#...##.###.##.###...#..#'
move = 10
result = '.'*move+initial+'.'*30

gens = 50000000000
producing = []

file = open('12.txt','r')

while True:
    line = file.readline()
    if line == '':
        break
    if line[9] == "#":
        producing.append(line[:5])

for gen in range(0,gens):
    res = '..'
    for i in range(len(result)-5):
        if result[i:i+5] in producing:
            res += '#'
        else:
            res += '.'

    if '#' in result[-10:]:
        res += '.....'
    if '#' not in result[:10]:
        res = res[5:]
        move -= 5

    result = res
    if (gen+1)%5000 == 0:
        counter = 0
        for i,pot in enumerate(result):
            if pot == '#':
                counter += i-move

        print(counter)
        print(gen+1)




counter = 0
for i,pot in enumerate(result):
    if pot == '#':
        counter += i-move

print(counter)
