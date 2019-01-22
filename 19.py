file = open('19.txt','r')
instructions = []

while True:
    line = file.readline()
    if line == '':
        break
    reg = line[:4]
    a,b,c = list(map(int,line[5:].split()))
    instructions.append([reg,a,b,c])

print(instructions)

def addr(r):
    a = r[0][r[1][1]]+r[0][r[1][2]]
    b = r[1][3]
    return (a,b)

def addi(r):
    a = r[0][r[1][1]]+r[1][2]
    b = r[1][3]
    return (a,b)

def mulr(r):
    a = r[0][r[1][1]]*r[0][r[1][2]]
    b = r[1][3]
    return (a,b)

def muli(r):
    a = r[0][r[1][1]]*r[1][2]
    b = r[1][3]
    return (a,b)

def banr(r):
    a = r[0][r[1][1]] & r[0][r[1][2]]
    b = r[1][3]
    return (a,b)

def bani(r):
    a = r[0][r[1][1]] & r[1][2]
    b = r[1][3]
    return (a,b)

def borr(r):
    a = r[0][r[1][1]] | r[0][r[1][2]]
    b = r[1][3]
    return (a,b)

def bori(r):
    a = r[0][r[1][1]] | r[1][2]
    b = r[1][3]
    return (a,b)

def setr(r):
    a = r[0][r[1][1]]
    b = r[1][3]
    return (a,b)

def seti(r):
    a = r[1][1]
    b = r[1][3]
    return (a,b)

def gtir(r):
    a = int(r[1][1] > r[0][r[1][2]])
    b = r[1][3]
    return (a,b)

def gtri(r):
    a = int(r[0][r[1][1]] > r[1][2])
    b = r[1][3]
    return (a,b)

def gtrr(r):
    a = int(r[0][r[1][1]] > r[0][r[1][2]])
    b = r[1][3]
    return (a,b)

def eqir(r):
    a = int(r[1][1] == r[0][r[1][2]])
    b = r[1][3]
    return (a,b)

def eqri(r):
    a = int(r[0][r[1][1]] == r[1][2])
    b = r[1][3]
    return (a,b)

def eqrr(r):
    a = int(r[0][r[1][1]] == r[0][r[1][2]])
    b = r[1][3]
    return (a,b)


ops = {'addr': addr,'addi':addi,'mulr':mulr,'muli':muli,'banr':banr,'bani':bani,'borr':borr,'bori':bori,
        'setr':setr,'seti':seti,'gtir':gtir,'gtri':gtri,'gtrr':gtrr,'eqir':eqir,'eqri':eqri,'eqrr':eqrr}

ip = 0
register = [0, 0, 0, 0, 0, 0]
#register = [0, 10551383, 1, 0, 10549998, 6]
#register = [1, 10551383, 2, 0, 10498615, 11]
#register = [1, 10551383, 3, 0, 10497231, 6]
#register = [1, 10551383, 4, 0, 10545848, 11]

i = 0

while ip < len(instructions):
    ins = instructions[ip]
    a = [register,ins]
    b = ops[ins[0]](a)
    register[b[1]] = b[0]
    ip = register[5] = register[5]+1
    i += 1
    if i%100000 == 0:
        print(register)




print(register[0], i)
