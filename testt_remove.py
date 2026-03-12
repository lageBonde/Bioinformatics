import numpy as np
import time
import matplotlib.pyplot as plt
'''
def getdiff(l):
    n=0
    t1 = time.time()
    while n <= l:
        n += 2
    i1 = time.time()-t1

    n=0
    t1 = time.time()
    for i in range(l):
        n += 2
    i2 = time.time()-t1

    t1 = time.time()
    range(l)
    i3 = time.time()-t1

    return (i1,i2,i3)


i1 = []
i2 = []
for_loop_only = []

n = 20
n2 = 100000
for i in range(n):
    values = [getdiff(i) for k in range(n2)]
    
    sum_i1=0
    sum_i2=0
    sum_i3=0
    for k in values:
        sum_i1 += k[0]
        sum_i2 += k[1]
        sum_i3 += k[2]
    i1.append(sum_i1/n2)
    i2.append(sum_i2/n2)
    for_loop_only.append((sum_i2-sum_i3)/n2)

plt.plot(range(n),i1, label="while loop")
plt.plot(range(n),i2, label="for loop")
plt.plot(range(n),for_loop_only, label="for loop minus range")
plt.legend()
plt.savefig("Compare_range_np_arange")'''


xpoints = np.array([0,27,48,72])

t1  = np.array([4.12, 4.12, 4.10, 4.10])
t9  = np.array([4.12, 4.10, 4.14, 4.07])
t23 = np.array([4.12, 4.01, 3.95, 3.75])
t37 = np.array([3.86, 3.54, 3.48, 3.53])
t50 = np.array([3.86, 3.90, 3.92, 3.99])

plt.plot(xpoints,t1, label="1")
plt.plot(xpoints,t9, label="9")
plt.plot(xpoints,t23, label="23")
plt.plot(xpoints,t37, label="37")
plt.plot(xpoints,t50, label="50")

plt.legend()
plt.savefig("GA_opponering")