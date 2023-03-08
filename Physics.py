q=open('Текстовый документ.txt')
allValues = [float(x) for x in q]

summ = 0
fDict = {
    'N': 50,
    '∆N': 0,
    '∆t': 0,
    't': 10
}

for i in range(len(allValues)):
    summ += allValues[i]
avSumm = summ / len(allValues)

print('Average sum =', round(avSumm, 3))

fDict['∆t'] = round(max(allValues) - min(allValues), 2)

delNCount = []

for i in range(len(allValues)):
    if fDict['t'] <= allValues[i] <= fDict['t'] + fDict['∆t']:
        delNCount.append(allValues[i])
fDict['∆N'] = len(delNCount)

print(fDict)
allValues.sort()
prom = []
for i in range(0,9):
    prom.append(round(min(allValues)+i*0.1,2))
print(prom)

h=8
prom2 = [[] for y in range(h)]
for j in range(8):
    for i in allValues:
        if round(min(allValues) + j * 0.1, 2) <= i < round(min(allValues) + (j + 1) * 0.1, 2) or \
                (i == max(allValues) and j == 7):
            prom2[j].append(i)
print(prom2)

alldelN= [[] for y in range(8)]
for j in range(8):
    for i in range(8):
        alldelN[j].append(len(prom2[i]))
print(alldelN[0])

'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 8)
y = np.random.randint(1, 20, size = 7)

fig, ax = plt.subplots()

ax.bar(x, y)

ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)    #  ширина Figure
fig.set_figheight(6)    #  высота Figure

plt.show()
'''