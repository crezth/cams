__author__ = 'Owen'
from Classes import *

Articles = []
Regions = []
AID = 0
RID = 0

working_type = "I PUT MY DICK IN KRAZNAYA'S BUTTHOLE 2 TIMES A DAY"
f = open('countries.csv')
for line in f:
    get_comment = comment.match(line)
    if not get_comment:
        entities = entity.findall(line)
        for i in range(0, len(entities)):
            entities[i] = (elements.search(entities[i]).group())
        Articles.append(entities)
        AID += 1
f.close()

f = open('regions.csv')
for line in f:
    get_comment = comment.match(line)
    if not get_comment:
        entities = entity.findall(line)
        for i in range(0, len(entities)):
            entities[i] = (elements.search(entities[i]).group())
        Regions.append(entities)
        RID += 1
f.close()

startMidfas = 7
dot = '.: '
connector = [0, 0, 0]

def main():
    f = open('_countries.txt', 'w')
    f.write('### Countries start here'+'\n')
    f.write('YEAR: 1930\n')
    for x in range(1, len(Articles)):
        f.write(''.join(['CREATE: (', Articles[0][0], ') ', '"', Articles[x][0], '"\n']))
        f.write(''.join(['DEFINE: {', Articles[0][1], ':', Articles[x][1], '}\n']))
        for y in range(2,startMidfas):
            f.write(''.join([dot, '{', Articles[0][y], ':', Articles[x][y], '}\n']))
        f.write('MIDFAS: {')
        i = 1
        for m in range(0, len(Articles[x])-startMidfas):
            connector[0] = '/'
            connector[1] = ', '
            connector[2] = '}'
            if i == 0:
                i += 1
            else:
                i -= 1
            if m == len(Articles[x])-startMidfas-1:
                i = 2
            f.write(Articles[x][startMidfas+m]+connector[i])
        f.write('\n')
    f.write('### Regions start here'+'\n')
    for x in range(1, len(Regions)):
        f.write('CREATE: ('+Regions[0][0]+') '+'"'+Regions[x][0]+'"'+'\n')
        f.write('DEFINE: {'+Regions[0][1]+':'+Regions[x][1]+'}'+'\n')
        for y in range(2, len(Regions[x])):
            f.write(dot+'{'+Regions[0][y]+':'+Regions[x][y]+'}'+'\n')
    f.write('END')
    f.close()
