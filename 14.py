#input = '170641'
input = input()

table = [3,7]
count = len(table)
elf1 = 0
elf2 = 1

def new_recipe(recipe,table):
    for digit in str(recipe):
        table.append(int(digit))
    return table

def isit(table,input):
    result = ''
    lenght = len(input)+1
    if len(table) < lenght:
        return True
    for i in range(lenght):
        result += str(table[-lenght+i])
    return input not in result


while isit(table,input):#řešení první části: count < input+20:
    table = new_recipe(table[elf1]+table[elf2],table)
    elf1 += 1 + table[elf1]
    elf2 += 1 + table[elf2]
    count = len(table)

    while elf1 >= count:
        elf1 -= count
    while elf2 >= count:
        elf2 -= count

#result = ''
#for i in range(10):
#    result += str(table[input+i])
#print('řešení první časti je:', result)

if table[-1] != table[-2]:
    print('řešení druhé časti je:', len(table)-len(input))
else:
    print('řešení druhé časti je:', len(table)-len(input)-1)
