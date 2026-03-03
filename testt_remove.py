import numpy as np
import time
import matplotlib.pyplot as plt

def getdiff(l):
    n=0
    t1 = time.time()
    while n <= l:
        n += 2
    i1 = time.time()-t1

    n=0
    t1 = time.time()
    for i in np.arange(l):
        n += 2
    i2 = time.time()-t1

    t1 = time.time()
    np.arange(l)
    i3 = time.time()-t1

    return (i1,i2,i3)


i1 = []
i2 = []
for_loop_only = []

n = 1000
for i in range(n):
    x = getdiff(i)
    i1.append(x[0])
    i2.append(x[1])
    for_loop_only.append(x[1]-x[2])

plt.plot(range(n),i1, label="while loop")
plt.plot(range(n),i2, label="for loop")
plt.plot(range(n),for_loop_only, label="for loop minus range")
plt.legend()
plt.savefig("Compare_range_np_arange")