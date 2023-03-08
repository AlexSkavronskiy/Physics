import matplotlib.pyplot as plt
import numpy as np

def start():
    data = []
    for i in range(0,100):
        data.append(i)
    arr=[]
    for i in range(0,100):
        arr.append(data[-i]**2)
    ty=np.linspace(0,10,200)
    print(arr)
    print(arr[::-1])


    plt.plot(ty)
    plt.plot(data[::-1])
    plt.show()
"""def tableload():
    arr=np.genfromtxt('file',delimiter=',')
    arr=arr[1::]
"""
if __name__=='__main__':
    start()

