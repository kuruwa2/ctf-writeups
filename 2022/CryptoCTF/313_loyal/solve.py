#!/usr/bin/env python3

from Crypto.Util.number import *
import telnetlib

p = getPrime(257)
phi = p-1
g = 2
u = inverse(pow(g, phi, p**2) // p, p)

tn = telnetlib.Telnet('07.cr.yp.toc.tf', 31377)
tn.read_until(b'uit\n')
tn.write(b'S\n')
tn.read_until(b'\n')
tn.write(f'{p}, {g}, [1]\n'.encode())
q = tn.read_until(b'\n')

points = []
while b'result' in q:
    r = int(q.split()[-1])
    points.append(pow(r, phi, p**2) // p * u % p)
    q = tn.read_until(b'\n')

points.sort()
print(''.join([chr(point % 2**10) for point in points]))
#CCTF{4n0t3R_h0MomORpH1C_3NcRyP7!0n_5CH3Me!}
