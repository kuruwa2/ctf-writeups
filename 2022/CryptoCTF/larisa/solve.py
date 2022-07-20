#!/usr/bin/env python3

from sage.all import *

enc = eval(open("./enc.txt").read())
G = SymmetricGroup(128)

M = []
for i in range(128):
    order = G(enc[i]).order()
    Ai = (G(enc[i]) ** inverse_mod(65537, order)).tuple()
    M.append(list(Ai))

for r in range(1, 128, 2):
    for s in range(2, 128):
        flag = ''
        for k in range(128):
            flag += chr(M[k][(k*r+s)%128])
        if 'CCTF' in flag:
            print(flag)
#CCTF{pUbliC_k3y_crypt0graphY_u5in9_rOw-l4t!N_5quAr3S!}
