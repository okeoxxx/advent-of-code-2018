requests = []

file = open('7.txt','r')

while True:
    line = file.readline()
    if line == '':
        break
    requests.append((line[5],line[36]))

a = set()
b = set()

for r in requests:
    a.add(r[1])
    b.add(r[0])

pending = set()
available = []
order = []

for i in (b-a):
    available.append(i)

for i in (b|a):
    pending.add(i)

available.sort()

next_possible = available.pop(0)
order.append(next_possible)
pending.remove(next_possible)

while pending or available:
    for ch in pending:
        if ch in available:
            continue
        all_req_for_ch = set()
        for r in requests:
            if r[1] == ch:
                all_req_for_ch.add(r[0])
        if set(order) >= all_req_for_ch:
            available.append(ch)
    available.sort()
    try:
        next_possible = available.pop(0)
    except IndexError:
        continue
    order.append(next_possible)
    pending.remove(next_possible)

result = ''
for ch in order:
    result += ch
print('Řešením první půlky je:', result)
