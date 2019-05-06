import random
random.seed(5949151291971546159465123)
f=open('route.txt','r')
poi={}
line=[]
while True:
    a = f.readline()
    if not a:
        break
    if a[-1] == '\n':
        line.append(a[:-1])
        a=a[:-1].split(',')
    else:
        line.append(a)
        a=a.split(',')
    for x in a:
        if x in poi:
            poi[x]=poi[x]+1
        else:
            poi[x]=1
iop = sorted(poi.items(),key=lambda s:s[1], reverse=True)
tap=[iop[0][0]]
count=0
while True:
    remove=[]
    for x in line:
        if tap[-1] in x:
            count=count+1
            remove.append(x)
    for x in remove:
        line.remove(x)
    if not line:
        break
    poi2={}
    for a in line:
        c=a.split(',')
        for x in c:
            if x in poi2:
                poi2[x]=poi2[x]+1
            else:
                poi2[x]=1
    iop2 = sorted(poi2.items(),key=lambda s:s[1], reverse=True)
    choose=[]
    for i in iop2:
        if i[1]==iop2[0][1]:
            choose.append(i)
    tap.append(choose[int(random.random()*len(choose))][0])
print(len(tap))
