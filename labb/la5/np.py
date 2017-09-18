import numpy as np

def random(length=1000):
    rand = np.random.random((length))
    avg=0
    for i in rand:
        avg+=i
    print(avg/length)



a = np.random.random((10,10,10))
print(a[:,:,2])
#random(10**6)
