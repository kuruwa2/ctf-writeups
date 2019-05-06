f=open("output.txt",'r')
N=f.readline()
N=int(N[:-1])
p=f.readline()
p=p[:-1]
message=f.readline()
message=int(message)
from itertools import product
count=0
one = [True,False]
ones = list(product(one))
two =list(product(one,one))
three=list(product(one,one,one))
four=list(product(one,one,one,one))
five=list(product(one,one,one,one,one))
now=[ones,two,three,four,five]
A=p.split('3E')
for a in now[len(A)-2]:
    addon=[]
    for i in a:
        if i:
            addon.append('59')
        else:
            addon.append('3E')
    p_new = A[0]+addon[0]+A[1]+addon[1]+A[2]+addon[2]+A[3]+addon[3]+A[4]
    B=p_new.split('E0')
    for b in now[len(B)-2]:
        addon=[]
        for i in b:
            if i:
                addon.append('9E')
            else:
                addon.append('E0')
        p_new = B[0]
        for i in range(len(B)-1):
            p_new=p_new+addon[i]+B[i+1]
        C = p_new.split('89')
        for c in now[len(C)-2]:
            addon=[]
            for i in c:
                if i:
                    addon.append('6B')
                else:
                    addon.append('89')
            p_new = C[0]
            for i in range(len(C)-1):
                p_new=p_new+addon[i]+C[i+1]
            D = p_new.split('38')
            for d in now[len(D)-2]:
                addon=[]
                for i in d:
                    if i:
                        addon.append('E4')
                    else:
                        addon.append('38')
                p_new = D[0]
                for i in range(len(D)-1):
                    p_new=p_new+addon[i]+D[i+1]
                E = p_new.split('95')
                for e in now[len(E)-2]:
                    addon=[]
                    for i in e:
                        if i:
                            addon.append('09')
                        else:
                            addon.append('95')
                    p_new = E[0]
                    for i in range(len(E)-1):
                        p_new=p_new+addon[i]+E[i+1]
                    F = p_new.split('FF')
                    for f in now[len(F)-2]:
                        addon=[]
                        for i in f:
                            if i:
                                addon.append('5E')
                            else:
                                addon.append('FF')
                        p_new = F[0]
                        for i in range(len(F)-1):
                            p_new=p_new+addon[i]+F[i+1]
                        G = p_new.split('D4')
                        for g in now[len(G)-2]:
                            addon=[]
                            for i in g:
                                if i:
                                    addon.append('33')
                                else:
                                    addon.append('D4')
                            p_new = G[0]
                            for i in range(len(G)-1):
                                p_new=p_new+addon[i]+G[i+1]
                            H = p_new.split('8D')
                            for h in now[len(H)-2]:
                                addon=[]
                                for i in h:
                                    if i:
                                        addon.append('12')
                                    else:
                                        addon.append('8D')
                                p_new = H[0]
                                for i in range(len(H)-1):
                                    p_new=p_new+addon[i]+H[i+1]
                                p_yep = int(p_new,16)
                                q=N//p_yep
                                if N==p_yep*q:
                                    print(p_yep,q)
                                    break
