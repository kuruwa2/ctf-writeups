from pwn import *
from sage.all import *
from Crypto.Util.number import *
from gmpy2 import next_prime
import random

'''found = False
while True:
    while True:
        p = random_prime(2**160, None, 2**159)
        if factor(p-1)[-1][0] < 2**45:
            break
    q = next_prime(p)
    while q - p <= 2022:
        if factor(q-1)[-1][0] < 2**45:
            found = True
            break
        q = next_prime(q)
    if found:
        break
print(p, q)'''

p = 1436112142773877726821048390796634246265300685591
q = 1436112142773877726821048390796634246265300686723
a = 1
b = 265901079094435588186282520788499195093987621335
A = GF(p)(319204452745285481131100414215568330491668910793)
B = GF(p)(797703237283306764558847562365497585281962864005)
c = 6
d = 317276254106151309401686100805285608682644543603
C = GF(q)(279708972166931604354840572497837159395664035780)
D = GF(q)(876694198440014518111367245800959927473972615163)

r = remote('07.cr.yp.toc.tf', 10010)
r.sendlineafter(b'uit\n', 'S')
r.recvline()
r.sendline(str(a)+','+str(b)+','+str(p))
r.recvline()
r.recvline()
r.sendline(str(c)+','+str(d)+','+str(q))

r.recvuntil(b'(')
Gx, Gy = list(map(int, r.recvline()[:-3].split(b',')))
r.recvuntil(b'(')
Hx, Hy = list(map(int, r.recvline()[:-3].split(b',')))
r.recvuntil(b'(')
rGx, rGy = list(map(int, r.recvline()[:-3].split(b',')))
r.recvuntil(b'(')
sHx, sHy = list(map(int, r.recvline()[:-3].split(b',')))

sl = (A-B).sqrt()
u = (Gy + sl*(Gx-A))/(Gy - sl*(Gx-A))
v = (rGy + sl*(rGx-A))/(rGy - sl*(rGx-A))
R = discrete_log(v, u)

sl = (C-D).sqrt()
u = (Hy + sl*(Hx-C))/(Hy - sl*(Hx-C))
v = (sHy + sl*(sHx-C))/(sHy - sl*(sHx-C))
s = discrete_log(v, u)
r.sendlineafter(b': \n', str(R)+','+str(s))

r.interactive()

#CCTF{Pl4yIn9_Wi7H_ECC_1Z_liK3_pLAiNg_wiTh_Fir3!!}
