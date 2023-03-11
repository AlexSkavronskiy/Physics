import math

q = open('meh1.txt')
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

allValues.sort()
prom = []
for i in range(0, 9):
    prom.append(round(min(allValues) + i * 0.1, 2))

fDict['prom'] = prom

h = 8
prom2 = [[] for y in range(h)]
for j in range(8):
    for i in allValues:
        if round(min(allValues) + j * 0.1, 2) <= i < round(min(allValues) + (j + 1) * 0.1, 2) or \
                (i == max(allValues) and j == 7):
            prom2[j].append(i)

fDict['prom2'] = prom2

alldelN = [[] for y in range(8)]
for j in range(8):
    for i in range(8):
        alldelN[j].append(len(prom2[i]))
print(alldelN[0])

fDict['allValues'] = allValues

tn = round(sum(allValues) / 50, 2)

allValues2 = []
for i in range(len(allValues)):
    allValues2.append(round((allValues[i] - tn) ** 2, 2))

sigmaN = ((1 / (fDict['N'] - 1)) * (sum(allValues2))) ** (1 / 2)

import numpy as np
import matplotlib.pyplot as plt

# def plot3d():
#
#     x = np.linspace(9.54, 10.34, 1)
#     y = np.sin(x)
#
#     fig, ax = plt.subplots()
#     plt.bar([9.59, 9.69, 9.79,9.89, 9.99, 10.09, 10.19, 10.29], [0.8, 1.4, 1.6, 1.4, 2.4, 1.0, 0.8, 0.6], width=0.098)
#     ax.plot(x, y,
#             linestyle='-',
#             linewidth=1,
#             color='crimson')
#
#     plt.show()
#
#
# if __name__ == '__main__':
#     plot3d()

print(alldelN[0])
p = []
for i in range(len(alldelN[0])):
    p.append(((1 / (sigmaN * math.sqrt((2 * math.pi)))) * math.exp(((alldelN[0][i] - tn) ** 2) / (-2 * sigmaN ** 2))))
print(p)

import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

plt.bar([9.59, 9.69, 9.79, 9.89, 9.99, 10.09, 10.19, 10.29], [0.8, 1.4, 1.6, 1.4, 2.4, 1.0, 0.8, 0.6], width=0.098)
x = np.array([9.59, 9.69, 9.79, 9.89, 9.99, 10.09, 10.19, 10.29])
y = np.array([0.8, 1.4, 1.6, 1.4, 2.4, 1.0, 0.8, 0.6])

X_Y_Spline = make_interp_spline(x, y)

# Returns evenly spaced numbers
# over a specified interval.
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

# Plotting the Graph

plt.plot(X_, Y_, c='red')
plt.title("Plot Smooth Curve Using the scipy.interpolate.make_interp_spline() Class")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

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
