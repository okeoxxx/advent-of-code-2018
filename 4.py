import datetime as dt
import re
from pprint import pprint

lines = []
table = [
            [["Date"],["ID"],["Minute"]],
            [[],[],["0"*10+"1"*10+"2"*10+"3"*10+"4"*10+"5"*10]],
            [[],[],["0123456789"*6]]
        ]
nap_counter = {}

file = open('4.txt','r')
while True:
    line = file.readline()
    if line == '':
        break
    lines.append(line)

lines.sort()

counter = 2

for act in lines:
    time = dt.datetime.strptime(act[:act.find("]")+1], "[%Y-%m-%d %H:%M]")
    if "Guard" in act:
        table.append([[] for i in range(62)])
        counter += 1

        table[counter][0] = "{}-{}".format(time.month,time.day)

        found = re.search(r"(\d{1,5})", act[act.find("#")+1:])
        ID = int(found.group())
        table[counter][1] = ID
    elif "falls" in act:
        falls_time = time.minute
    elif "wakes" in act:
        wake_time = time.minute
        for nap_time in range(falls_time,wake_time):
            table[counter][2+nap_time] = "x"
        prdel = nap_counter.get(ID,0)
        prdel += wake_time - falls_time
        if nap_counter.setdefault(ID,prdel) != prdel:
            nap_counter[ID] = prdel

highest = 0
highestID = 0
ideal_time = 0

for ID in nap_counter:
    if nap_counter[ID] > highest:
        highest = nap_counter[ID]
        highestID = ID

nap_minutes = {}

for row in table:
    if row[1] == highestID:
        for minute,mark in enumerate(row[2:]):
            if mark == 'x':
                count = nap_minutes.get(minute,0)
                count += 1
                if nap_minutes.setdefault(minute,count) != count:
                    nap_minutes[minute] = count

highest = 0

for minute in nap_minutes:
    if nap_minutes.get(minute) > highest:
        highest = nap_minutes.get(minute)
        ideal_time = minute

print('Strategy 1:', highestID*ideal_time)

nap_minutes2 = {}

for row in table[3:]:
    ID = row[1]
    nap_minutes2.setdefault(ID,{})
    for minute,mark in enumerate(row[2:]):
        if mark == 'x':
            count = nap_minutes2[ID].get(minute,0)
            count += 1
            if nap_minutes2[ID].setdefault(minute,count) != count:
                nap_minutes2[ID][minute] = count

highest = 0
highestID = 0
ideal_time = 0

for ID in nap_minutes2:
    for minute in nap_minutes2[ID]:
        if nap_minutes2[ID].get(minute) > highest:
            highest = nap_minutes2[ID].get(minute)
            highestID = ID
            ideal_time = minute

print('Strategy 2:', ideal_time*highestID)
