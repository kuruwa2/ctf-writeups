#!/usr/bin/env python3

from pwn import *
from sage.all import *
from Crypto.Util.number import *

def gen_gp():
    while True:
        p = getPrime(128)
        F = PolynomialRing(GF(p), 'x')
        x = F.gen()
        f = x**2 + x + 1
        ts = [int(r) for r, _ in f.roots()]
        if len(ts) < 2: continue
        gs = [inverse(t - 1, p) for t in ts]
        tgs = [t * g % p for t, g in zip(ts, gs)]
        if not 64 < min(gs).bit_length() < max(gs).bit_length() < 128: continue
        if not 64 < min(tgs).bit_length() < max(tgs).bit_length() < 128: continue
        return gs, tgs, p

r = remote('05.cr.yp.toc.tf', 37377)
def encrypt(g, p):
    r.sendline(b'S')
    r.sendline(str(p).encode())
    r.sendline(str(g).encode())
    r.recvuntil(b'here is the mixed flag: ')
    result = ZZ(r.recvline().decode().strip())
    return ZZ(result)

rem, mod = [], []
for _ in range(5):
    gs, tgs, p = gen_gp()
    print(f'[!] {gs = }')
    print(f'[!] {tgs = }')
    print(f'[!] {p = }')

    R = PolynomialRing(GF(p), 'f')
    f = R.gen()
    polys = []
    for g, tg in zip(gs, tgs):
        r1 = encrypt(tg, p)
        r2 = encrypt(g, p)
        coefs = [int(g) - r2, g**3 * (r1 - int(tg)), 1, -g**3]
        polys.append(sum(coefs[i] * f**i for i in range(4)))

    def _gcd(a, b):
        if a < b:
            a, b = b, a
        while b != 0:
            a, b = b, a % b
        return a

    sol_f = _gcd(polys[0], polys[1])
    fp = sol_f.roots()[0][0]
    rem.append(fp)
    mod.append(p)

rem = list(map(ZZ, rem))
mod = list(map(ZZ, mod))

rv = CRT(rem, mod)
print(long_to_bytes(rv))
#CCTF{Pl34se_S!r_i_w4N7_5omE_M0R3_5OuP!!}
