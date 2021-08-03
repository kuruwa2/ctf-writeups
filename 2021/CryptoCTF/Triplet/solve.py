from pwn import *
from Crypto.Util.number import *
import random

while True:
    p = getPrime(1024)
    q = getPrime(1024)
    a = []
    for k in range(2, 69):
        if isPrime(k*(q-1)+1):
            a.append((k, k*(q-1)+1))
    if len(a)>=2:
        break

phi = (p-1)*(q-1)*a[0][0]*a[1][0]//GCD(a[0][0],a[1][0])
while True:
    e = random.randint(1,(p-1)*(q-1))
    if GCD(e,phi)==1 and inverse(e, phi)<(p-1)*(q-1):
        break
d = inverse(e, phi)

#print(p,q,a,e,d)

r = remote('07.cr.yp.toc.tf', 18010)
r.sendlineafter(b'uit\n', 'S')
r.recvline()
r.sendline(str(p)+','+str(q))
r.recvline()
r.sendline(str(p)+','+str(a[0][1]))
r.recvline()
r.sendline(str(p)+','+str(a[1][1]))
r.recvline()
r.sendline(str(e)+','+str(d))

r.interactive()

#CCTF{7HrE3_b4Bie5_c4rRi3d_dUr1nG_0Ne_pr39naNcY_Ar3_triplets}
