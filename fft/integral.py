import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)


xpoints = np.arange(-10,10,0.1)
ypoints_f = np.array([])
ypoints_f_prim = np.array([])
ypoints_f_biss = np.array([])

for x in xpoints:
    ypoints_f = np.append(ypoints_f,f(x))
    ypoints_f_prim = np.append(ypoints_f_prim,(f(x+0.01)-f(x))/0.01)
    ypoints_f_biss = np.append(ypoints_f_biss,((f(x+0.02)-f(x))/0.02-(f(x+0.01)-f(x))/0.01)/0.01)


plt.plot(xpoints, ypoints_f)
plt.plot(xpoints, ypoints_f_prim)
plt.plot(xpoints, ypoints_f_biss)

plt.show()
plt.savefig("integral")
