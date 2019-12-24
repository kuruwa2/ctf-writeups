def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
PPT = []
for i in range(3000):
    for j in range(i):
        m, n = 2*i+1, 2*j+1
        if egcd(m, n)[0] == 1:
            a = m*n
            b = (m**2-n**2)//2
            c = (m**2+n**2)//2
            if a > b:
                a, b = b, a
            PPT.append((c,b,a))
PPT.sort()
from pwn import *

r = remote('challs.xmas.htsp.ro', 14004)
q = r.recvline()
q = str(q[-7:-1])[2:-1]
print(q)
from hashlib import sha256
import os
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
    q = r.recvline()
    print(q)
    i = int(q.split(b'-')[0][12:])
    p = str(PPT[i-1][2])+','+str(PPT[i-1][1])+','+str(PPT[i-1][0])
    print(p)
    r.sendline(p)
    print(r.recvline())
    q = r.recvline()
    print(q)
r.interactive()
