from Crypto.Util.number import *
from pwn import *

p = 241318860038181462920822573849074653413
q = 2*p + 1
a = b = p * q

r = remote('01.cr.yp.toc.tf', 29010)
r.sendlineafter(b'uit\n', 'C')
r.sendlineafter(b': \n', f'{p}')
r.sendlineafter(b'uit\n', 'A')
r.sendlineafter(b': \n', f'{a},{b}')

r.sendlineafter(b'uit\n', 'S')
r.recvuntil(b'that: \n')
px, py = list(map(int, r.recvline()[7:-2].split(b',')))
kx, ky = list(map(int, r.recvline()[9:-2].split(b',')))
qx, qy = list(map(int, r.recvline()[7:-2].split(b',')))
lx, ly = list(map(int, r.recvline()[9:-2].split(b',')))

k = kx * py * inverse(ky * px, p) % p
l = lx * qy * inverse(ly * qx, q) % q
r.sendlineafter(b': \n', f'{k},{l}')

r.interactive()

#CCTF{ECC_With_Special_Prime5}
