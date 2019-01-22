a = 0
b = 0


file = open('2.txt', 'r')

IDs = []

while True:
    line = file.readline()
    if ("" == line):
        print('file finished')
        break
    IDs.append(line)

for i in range(len(IDs)):
    for j in range(len(IDs)):
        if j > i:
            counter = 0
            prdel = ''
            for num in range(len(IDs[j])):
                if IDs[i][num] != IDs[j][num]:
                    counter += 1
                    prdel = num
                if counter == 1 and num == len(IDs[i])-1:
                    print(IDs[i][:prdel]+IDs[j][prdel+1:])




while IDs:
    line = IDs.pop()
    twice = False
    three_times = False
    for letter in line:
        if line.count(letter) == 2:
            if twice != True:
                a += 1
                twice = True
        if line.count(letter) == 3:
            if three_times != True:
                b += 1
                three_times = True
        if twice == three_times == True:
            break

print('Checksum is:', a*b)
