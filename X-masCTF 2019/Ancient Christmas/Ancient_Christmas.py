from pwn import *
import numpy as np
import cv2
import base64
def parseimage(labels):
    p = [0,0,0,0,0,0]
    start = []
    end = []
    first = 1
    xmin = 0
    for i in range(labels.shape[0]):
        if (not first) and np.all(labels[i]==0):
            start.append((xmin, i-1))
            first = 1
        if first and not np.all(labels[i]==0):
            first = 0
            xmin = i
    for i in range(len(start)):
        row = labels[start[i][0]-2:start[i][1]+2]
        ymin = 0
        first = 1
        for j in range(row.shape[1]):
            if (not first) and np.all(row[:,j]==0):
                end.append((ymin, j-1))
                break
            if first and not np.all(row[:,j]==0):
                ymin = j
                first = 0
    for i in range(len(start)):
        image2=labels[start[i][0]-3:start[i][1]+3, end[i][0]-3:end[i][1]+3]
        labels2=np.zeros(image2.shape).astype('int')
        label2 = 0
        linked={}
        for j in range(len(labels2)):
            for k in range(len(labels2[j])):
                neibor = []
                if j>0 and k>0 and image2[j-1][k-1] == image2[j][k]:
                    neibor.append(labels2[j-1][k-1])
                if j>0 and image2[j-1][k] == image2[j][k]:
                    neibor.append(labels2[j-1][k])
                if j>0 and k<len(labels2[j])-1 and image2[j-1][k+1] == image2[j][k]:
                    neibor.append(labels2[j-1][k+1])
                if k>0 and image2[j][k-1] == image2[j][k]:
                    neibor.append(labels2[j][k-1])
                if len(neibor):
                    labels2[j][k] = np.min(neibor)
                    L = labels2[j][k]
                    while linked[L] != L:
                        ne = linked[L]
                        linked[L] = linked[ne]
                        L = ne
                    yroot = L
                    for n in neibor:
                        while linked[n] != n:
                            nn = linked[n]
                            linked[n] = linked[nn]
                            n = nn
                        xroot = n
                        if xroot > yroot:
                            linked[yroot] = xroot
                        else:
                            linked[xroot] = yroot
                else:
                    labels2[j][k] = label2
                    linked[label2]=label2
                    label2 += 1
        holes = []
        ans = 0
        for j in range(len(labels2)):
            for k in range(len(labels2[j])):
                root = linked[labels2[j][k]]
                while linked[root] != root:
                    root = linked[root]
                labels2[j][k] = root
                if root not in holes:
                    ans += 1
                    holes.append(linked[labels2[j][k]])
        p[ans-2] += 1
    for i in range(len(p)):
        p[i] = str(p[i])
    return ','.join(p)

from hashlib import sha256
import os

r = remote('challs.xmas.htsp.ro', 14001)
q = r.recvline()
q = str(q[-7:-1])[2:-1]
print(q)
p='' 
while True:
    s = os.urandom(10)
    h = sha256(s).hexdigest()
    if h[-6:] == q:
        for i in s:
            if len(hex(i)[2:]) == 1:
                p += '0'+hex(i)[2:]
            else:
                p += hex(i)[2:]
        break
r.sendline(p)
q = r.recvuntil('#1:\n')
while b'#' in q:
    image = r.recvline()[2:-1]
    r.recvline()
    image = base64.b64decode(image)
    f = open("./image.png",'wb')
    f.write(image)
    f.close()
    image = cv2.imread('./image.png',cv2.IMREAD_GRAYSCALE)
    image = image<128
    p = parseimage(image)
    print(p)
    r.sendline(p)
    print(r.recvline())
    q = r.recvline()
    print(q)
    
r.interactive()
