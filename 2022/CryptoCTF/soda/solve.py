#!/usr/bin/env python3

from Crypto.Util.number import *
from numpy import prod
import telnetlib

CRY = "Long Live Crypto :))"
m = bytes_to_long(CRY.encode('utf-8'))
tn = telnetlib.Telnet('01.cr.yp.toc.tf', 37711)

def recvline():
    return tn.read_until(b'\n')

def sendlineafter(a, b):
    q = tn.read_until(a)
    tn.write(b+b'\n')
    return q

sendlineafter(b'uit\n', b'G')
n = int(recvline().split()[-1])
g = int(recvline().split()[-1])
e = 2 * (pow(g, m**2, n) % 2**152) + 1
factors = [5, 31, 1594624713089, 5500056052324938008435708454209]
assert prod(factors) == e

a = [e//f for f in factors]
coef = [1]
now = a[0]
for i in range(1, 4):
    for j in range(len(coef)):
        coef[j] *= inverse(now, a[i])
    coef += [-(now*inverse(now, a[i])//a[i])]
    now = GCD(now, a[i])

sd = 1
for i, c in zip(factors, coef):
    sendlineafter(b'uit\n', b'T')
    sendlineafter(b'\n', f'{i}'.encode())
    soda = int(recvline().split()[-1])
    if c < 0:
        sd *= pow(inverse(soda, n), -c, n)
    else:
        sd *= pow(soda, c, n)

#sendlineafter(b'uit\n', b'T')
#sendlineafter(b'\n', f'{-m}'.encode())
#sd = int(recvline().split()[-1])
sendlineafter(b'uit\n', b'V')
sendlineafter(b'\n', f'{sd%n}'.encode())
print(tn.read_all())
#CCTF{f4cToriZat!On__5Tt4cK_0n_4_5i9na7urE!}
