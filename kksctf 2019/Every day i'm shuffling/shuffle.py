from random import *
def Shuffle(p, data):
    buf = list(data)
    for i in range(len(data)):
        buf[i] = data[p[i]]
    return ''.join(buf)
seed(3)
file_name = 'message_from_above'
file_name = list(file_name)
shuffle(file_name)
assert(''.join(file_name) == 'fsegovs_meaoerbma_')

data = open('fsegovs_meaoerbma_.txt', 'r', encoding="utf8").read()
pp = list(range(len(data)))
shuffle(pp)

p = [0]*len(pp)
for i in range(len(pp)):
    p[pp[i]] = i


data = Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,data))))))))))))))))))))))))))))))))))))))))

f = open('message_from_above.txt', 'w')
f.write(data)
f.close()
