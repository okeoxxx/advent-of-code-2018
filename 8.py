file = open('8.txt','r')
text = file.read()

data = [int(i) for i in text.split()]

def parse(data):
    child, meta, data = data[0],data[1],data[2:]
    scores = []
    totals = 0

    for i in range(child):
        total,score,data = parse(data)
        totals += total
        scores.append(score)

    totals += sum(data[:meta])

    if child == 0:
        return (totals,sum(data[:meta]), data[meta:])
    else:
        value = 0
        for n in data[:meta]:
            if n > 0 and n <= len(scores):
                value += scores[n-1]
        return (totals,value,data[meta:])

total,value,data = parse(data)

print('Řešení první části:', total)
print('Řešení druhé části:', value)
