import numpy as np
def parseimage(image):
    p = [0,0,0,0,0,0]
    #labels=np.zeros(image.shape).astype('int')
    #label=1
    #maxx, maxy = image.shape[0], image.shape[1]
    start = []
    end = []
    first = 1
    labels = image<128
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
    '''xmin, xmax = image.shape[0], 0
    ymin, ymax = image.shape[1], 0
    for i in range(image.shape[0]):
        if (not first) and np.all(labels[i]==0):
            start.append((xmin, xmax))
            end.append((ymin, ymax))
            xmin, xmax = image.shape[0], 0
            ymin, ymax = image.shape[1], 0
            first = 1
        else:
            j = 0
            while j < image.shape[1]:
                if labels[i,j]:
                    if first:
                        first = 0
                    if i < xmin:
                        xmin = i
                    if i > xmax:
                        xmax = i
                    if j < ymin:
                        ymin = j
                    if j > ymax:
                        ymax = j
                j += 1
            queue=[]
            if image[i,j] < 128 and labels[i,j] == 0:
                queue.append((i,j))
                labels[i,j]=label
                xmin, ymin = i, j
                xmax, ymax = i ,j
                while len(queue):
                    i,j=queue.pop()
                    if i>0 and j>0 and image[i-1,j-1] < 128 and labels[i-1,j-1] == 0:
                        queue.append((i-1,j-1))
                        labels[i-1,j-1] = label
                    if i>0 and image[i-1,j] < 128 and labels[i-1,j] == 0:
                        queue.append((i-1,j))
                        labels[i-1,j] = label
                    if i>0 and j<maxy-1 and image[i-1,j+1] < 128 and labels[i-1,j+1] == 0:
                        queue.append((i-1,j+1))
                        labels[i-1,j+1] = label
                    if j>0 and image[i,j-1] < 128 and labels[i,j-1] == 0:
                        queue.append((i,j-1))
                        labels[i,j-1] = label
                    if j<maxy-1 and image[i,j+1] < 128 and labels[i,j+1] == 0:
                        queue.append((i,j+1))
                        labels[i,j+1] = label
                    if i<maxx-1 and j>0 and image[i+1,j-1] < 128 and labels[i+1,j-1] == 0:
                        queue.append((i+1,j-1))
                        labels[i+1,j-1] = label
                    if i<maxx-1 and image[i+1,j] < 128 and labels[i+1,j] == 0:
                        queue.append((i+1,j))
                        labels[i+1,j] = label
                    if i<maxx-1 and j<maxy-1 and image[i+1,j+1] < 128 and labels[i+1,j+1] == 0:
                        queue.append((i+1,j+1))
                        labels[i+1,j+1] = label
                    if i > xmax:
                        xmax = i
                    if j < ymin:
                        ymin = j
                    if j > ymax:
                        ymax = j
                label += 1
                start.append((xmin,xmax))
                end.append((ymin,ymax))
                i = xmax+1
                j = 0'''
    for i in range(len(start)):
        image2=labels[start[i][0]-2:start[i][1]+2, end[i][0]-2:end[i][1]+2]
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
                #print(chr(labels2[j][k]+ord('0')),end='')
            #print('')
        #print(linked)
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
                #print(chr(labels2[j][k]+ord('0')),end='')
            #print('')
        p[ans-2] += 1
    for i in range(len(p)):
        p[i] = str(p[i])
    return ','.join(p)

import cv2
image = cv2.imread('./image.png',cv2.IMREAD_GRAYSCALE)
print(parseimage(image))
