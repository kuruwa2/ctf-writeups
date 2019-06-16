import operator

for k in range(27):
    a = dict()
    ls = []
    b = 0
    count = 0
    for i in range(100):
        with open(str(k)+'/'+str(i), 'r') as f:
            l = f.readline()
        ls.append(l)
        for j in l:
            count += 1
            b += ord(j)
        if chr(b//count) in a:
            a[chr(b//count)] += 1
        else:
            a[chr(b//count)] = 1
        b = 0
        count = 0
    sorted_a = sorted(a.items(), key=lambda kv: kv[1])
    print(sorted_a[-1][0],end='')
