#!/usr/bin/env python3

import telnetlib
from Crypto.Util.number import *

HOST = "04.cr.yp.toc.tf"
PORT = 13777
tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b'\n')

tn.read_until(b'uit\n')
tn.write(b'G\n')
q = int(readline().split()[-1])
r = int(readline().split()[-1])
s = int(readline().split()[-1])

tn.read_until(b'uit\n')
tn.write(b'S\n')
for _ in range(5):
    cond = readline().split()
    xory = cond[-3]
    bit = int(cond[-1].split(b'-')[0])
    if xory == b'x':
        x, y = 2 ** bit - 1, s * (2 ** bit - 1) * inverse(r, q) % q
        tn.write((str(x) + ', ' + str(y) + '\n').encode())
    else:
        x, y = r * (2 ** bit - 1) * inverse(s, q) % q, 2 ** bit - 1
        tn.write((str(x) + ', ' + str(y) + '\n').encode())

    print(readline())
#CCTF{f1nDin9_In7Eg3R_50Lut1Ons_iZ_in73rEStIn9!}
