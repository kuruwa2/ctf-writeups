import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import re
def newline(p1, p2):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if(p2[0] == p1[0]):
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
        ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax])
    ax.add_line(l)
    return l
count=0
dt=0.001
accel=0
v=np.array([0,0,0])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
f = open("sensors.log", "r")
x,y,z=0,0,0
while count<=0:
    line=f.readline()
    if not line:
        break
    num=np.array([float(s) for s in re.findall(r'-?\d+\.?\d*',line)])
    if len(num)==1:
        accel=num[0]
    if len(num)==3:
        v = v+num*accel
        x=x+v[0]*dt
        y=y+v[1]*dt
        z=z+v[2]*dt
    count=count+1
while count<=50000:
    line=f.readline()
    if not line:
        break
    num=np.array([float(s) for s in re.findall(r'-?\d+\.?\d*',line)])
    if len(num)==1:
        accel=num[0]
    if len(num)==3:
        v = v+num*accel
        ax.plot([x ,x+v[0]*dt],[y,y+v[1]*dt],[z,z+v[2]*dt])
        x=x+v[0]*dt
        y=y+v[1]*dt
        z=z+v[2]*dt
    count=count+1
print(count)
f.close()
ax.view_init(elev=15., azim=-90.)
ax.set_zlim(0, 5)
ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([2, 1, 1, 1]))
plt.show()
