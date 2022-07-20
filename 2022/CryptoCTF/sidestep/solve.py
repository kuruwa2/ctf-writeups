#!/usr/bin/env python3

from Crypto.Util.number import *
import telnetlib

HOST = "02.cr.yp.toc.tf"
PORT =17331
tn = telnetlib.Telnet(HOST, PORT)

def qth_root(b, q, p):
    return pow(b, inverse(q, p-1), p)

p = 2 ** 1024 - 2 ** 234 - 2 ** 267 - 2 ** 291 - 2 ** 403 - 1
s = 0
for i in range(1024):
    if i % 100 == 0:
        print(i)
    tn.read_until(b'uit\n')
    tn.write(b'T\n')
    tn.read_until(b'\n')
    
    s <<= 1
    g = qth_root(4, s+1, p)
    tn.write((str(g)+'\n').encode())
    q = tn.read_until(b'\n')
    if b'Great' in q:
        print(q)
        break
    t = q[q.index(b'(')+1]
    if t == 49: s += 1
    
#CCTF{h0W_iZ_h4rD_D15crEt3_lO9ar!Thm_c0nJec7ur3?!}
