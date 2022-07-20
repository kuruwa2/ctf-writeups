#!/usr/bin/env sage

from sage.all import *
from pwn import *

r = remote("08.cr.yp.toc.tf", 37313)

for _ in range(12):
    r.recvuntil(b'p = ')
    p = int(r.recvline().split(b',')[0])
    r.recvline()
    M = []
    M.append(list(map(int, r.recvline()[1:].split(b']')[0].split())))
    for i in range(len(M[0])-1):
        M.append(list(map(int, r.recvline()[1:].split(b']')[0].split())))
    #print(p, M)
    M = matrix(GF(p), M)
    r.recvline()
    r.sendline(str(M.multiplicative_order()).encode())

print(r.recvline())
r.close()
#CCTF{ma7RicES_4R3_u5EfuL_1n_PUbl!c-k3y_CrYpt0gr4Phy!}
