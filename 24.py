import re
from pprint import pprint as pp
file = open('24.txt','r')

attacks = ['bludgeoning','radiation','cold','slashing','fire']

def getit(file):
    Team = {}
    j = 1
    while True:
        line = file.readline()
        a = re.findall(r"[\w']+", line)
        if not a:
            Infection = Team
            break
        elif len(a) == 1:
            a[0] == 'Infection'
            Immune = Team
            Team = {}
            j=1
            continue
        units,HP,attack,initiative = list(map(int,re.findall(r'\d+',line)))
        immune = []
        weak = []
        type_atta = ''
        for i,word in enumerate(a):
            if word == 'immune':
                for atta in a[i+2:]:
                    if atta in attacks:
                        immune.append(atta)
                    else:
                        break
            if word == 'weak':
                for atta in a[i+2:]:
                    if atta in attacks:
                        weak.append(atta)
                    else:
                        break
            if word == 'damage':
                type_atta = a[i-1]
        Team[j] = {'units':units,'HP':HP,'attack':attack,'initiative':initiative,
                'immune':immune,'weak':weak,'type_atta':type_atta}
        j += 1
    return (Immune,Infection)


def eff_pow(dict):
    for i,v in dict.items():
        ep = v['units'] * v['attack']
        dict[i]['ep']=ep
    return dict

def enemy_choose(lst,side,fights,Immune,Infection): #0:Immune, 1:Infection
    i = 0 if side == Immune else 1
    enemy = Infection if side == Immune else Immune
    alive_enemies = [e for e in enemy if enemy[e]['units'] > 0]
    while lst:
        attacking_group = lst.pop()
        num = attacking_group[0]
        damages = []
        for e in alive_enemies:
            if side[num]['type_atta'] in enemy[e]['immune']:
                continue
            multiplier = 2 if side[num]['type_atta'] in enemy[e]['weak'] else 1
            damage = side[num]['ep']*multiplier
            damages.append([e,damage,enemy[e]['ep'],enemy[e]['initiative']])
        damages.sort(key = lambda x: (x[1],x[2],x[3]))
        if damages:
            fights[i].append([side[num]['initiative'],num,damages[-1][0]])
            alive_enemies.remove(damages[-1][0])
    return fights

def fight(fights,Immune,Infection):
    while fights[0] or fights[1]:
        max_Ims = 0 if not fights[0] else fights[0][0][0]
        max_Infs = 0 if not fights[1] else fights[1][0][0]
        if max_Ims > max_Infs:
            i = 0
        else:
            i = 1
        a = fights[i].pop(0)
        atacker,defender = (Immune,Infection) if i == 0 else (Infection,Immune)
        multiplier = 2 if atacker[a[1]]['type_atta'] in defender[a[2]]['weak'] else 1
        damage = atacker[a[1]]['units'] * atacker[a[1]]['attack'] * multiplier
        lost_units = damage // defender[a[2]]['HP']
        if defender[a[2]]['units'] < lost_units:
            defender[a[2]]['units'] = 0
        else:
            defender[a[2]]['units'] -= lost_units
    return (Immune,Infection)

def doit(num,Immune,Infection):
    for g in Immune:
            Immune[g]['attack'] += num
    k = 0
    while True:
        pass
        Immune = eff_pow(Immune)
        Infection = eff_pow(Infection)
        fights = [[],[]]
        Ims = []
        Infs = []
        for g in Immune:
            if Immune[g]['units']:
                Ims.append([g,Immune[g]['ep'],Immune[g]['initiative']])
        for g in Infection:
            if Infection[g]['units']:
                Infs.append([g,Infection[g]['ep'],Infection[g]['initiative']])
        if not Ims or not Infs:
            break
        Ims.sort(key = lambda x: (x[1],x[2]))
        Infs.sort(key = lambda x: (x[1],x[2]))
        fights = enemy_choose(Ims,Immune,fights,Immune,Infection)
        fights = enemy_choose(Infs,Infection,fights,Immune,Infection)
        fights[0].sort(key = lambda x: x[0],reverse=True)
        fights[1].sort(key = lambda x: x[0],reverse=True)
        Immune,Infection = fight(fights,Immune,Infection)
        k += 1
        if k%20000 == 0:
            break
    x,y = 0,0
    for g in Immune:
        if Immune[g]['units']:
            x += Immune[g]['units']
    for g in Infection:
        if Infection[g]['units']:
            y += Infection[g]['units']
    return (x,y)

for num in range(82,1578):
    file.seek(0)
    Im,In = getit(file)
    x,y = doit(num,Im,In)
    print(num,x,y)
    if x and not y:
        print(x)
        break
#1570
