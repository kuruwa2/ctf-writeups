#!/usr/bin/env python3

import telnetlib

tn = telnetlib.Telnet('02.cr.yp.toc.tf', 13771)

def s(p):
    return sum([p[i]*(-2)**i for i in range(len(p))])

def next(p):
    l = len(p)
    if l % 3 == 0:
        for i in range(l):
            if s(p[-i:]) == l//3:
                return p[:-i] + [l + 2, l + 1] + p[-i:]
    elif l % 3 == 2:
        for i in range(l):
            if s(p[-i:]) == (l + 1) // 3:
                return p[:-i] + [l + 1] + p[-i:]

p = [2, 3, 1]
for step in range(3, 41):
    tn.read_until(b'comma: \n')
    if step % 3 == 1:
        tn.write(b'TINP\n')
        continue
    else: tn.write(','.join([str(i) for i in p]).encode()+b'\n')
    p = next(p)
    print(p)

print(tn.read_all())
#CCTF{MINO_iZ_4N_3a5Y_Crypto_C0d!n9_T4sK!}
