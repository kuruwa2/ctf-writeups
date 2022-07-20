#!/usr/bin/env python3

import telnetlib
from Crypto.Util.number import *
from hashlib import sha1

def bsgs(a, b, p, order):
    m = math.ceil(math.sqrt(order))
    dic = {}
    ai = 1
    for i in range(m):
        dic[ai] = i
        ai = ai * a % p
    bi = b
    am = inverse(pow(a, m, p), p)
    for i in range(m):
        if bi in dic:
            assert(pow(a, i*m+dic[bi], p)==b)
            return i * m + dic[bi]
        bi = bi * am % p

def crt(rs, ps):
    a1, n1 = rs[0], ps[0]
    for i in range(1, len(ps)):
        a2, n2 = rs[i], ps[i]
        n2 //= GCD(n1, n2)
        m1, m2 = inverse(n1, n2), inverse(n2, n1)
        a1 = (a1 * m2 * n2 + a2 * m1 * n1) % (n1 * n2)
        n1 *= n2
    return a1

MSG = b'::. Can you forge any signature? .::'
h = bytes_to_long(sha1(MSG).digest())
h2 = bytes_to_long(sha1(MSG[4:-4]).digest())

tn = telnetlib.Telnet('03.cr.yp.toc.tf', 11137)
tn.read_until(b'uit\n')
tn.write(b'P\n')
sign = int(tn.read_until(b'\n').split()[-1])

Ps = []
Rs = []
while len(Ps) != 2:
    _P = 2
    rs = []
    fs = []
    while _P.bit_length() < 1024 - 48:
        f = getPrime(24)
        _P *= f
        fs.append(f)
    bit1 = (1024 - _P.bit_length() + 1) // 2
    bit2 =  1024 - _P.bit_length() - bit1 + 1
    while True:
        f1, f2 = getPrime(bit1), getPrime(bit2)
        P = _P * f1 * f2 + 1
        if isPrime(P) and P.bit_length() == 1024 and pow(h, P//2, P) == pow(sign, P//2, P):
            fs.extend((f1, f2))
            break
    for f in fs:
        rs.append(bsgs(pow(h, P//f, P), pow(sign, P//f, P), P, f))
    R = crt(rs + [1], fs + [2])
    print(pow(h, R, P) == sign%P)
    Ps.append(P)
    Rs.append(R)

N = Ps[0] * Ps[1]
D = crt(Rs, [Ps[0] - 1, Ps[1] - 1])
E = inverse(D, (Ps[0] - 1) * (Ps[1] - 1))
print(pow(h, D, N) == sign)

tn.read_until(b'uit\n')
tn.write(b'G\n')
tn.read_until(b'\n')
tn.write(f'{E}, {Ps[0]}, {Ps[1]}\n'.encode())

tn.read_until(b'uit\n')
tn.write(b'S\n')
tn.read_until(b"ture?'\n")
tn.write(str(pow(h2, D, N)).encode() + b'\n')
print(tn.read_until(b'\n'))
#CCTF{Unkn0wN_K3y_5h4rE_4t7aCk_0n_Th3_RSA!}
