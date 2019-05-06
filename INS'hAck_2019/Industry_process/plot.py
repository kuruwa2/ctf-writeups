from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

f=open("plot.txt",'r')
while True:
    l = f.readline()
    if not l:
        break
    a=l.strip().split(',')
    xs,ys,zs=int(a[0]),int(a[1]),int(a[2])
    ax.scatter(xs, ys, zs)
plt.show()
