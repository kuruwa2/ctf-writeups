#!/usr/bin/env python3

from Crypto.Util.number import *

def square_root(a, p):
    return pow(a, p//4+1, p)

def cubic_root(a, p):
    return pow(a, 2*p//3, p) 

def cubic_formula(a, b, c, d):
    d0 = (b*b-3*a*c) % p
    d1 = (2*b*b*b - 9*a*b*c + 27*a*a*d) % p
    C = cubic_root((d1 + square_root(d1**2 - 4*d0**3, p)) * inverse(2, p), p)
    x = - (b + C + d0 * inverse(C, p)) * inverse(3*a, p) % p
    return x

p = 7389313481223384214994762619823300589978423075857540712007981373887018860174846208000957230283669342186460652521580595183523706412588695116906905718440770776239313669678685198683933547601793742596023475603667
e = 31337
c = 871346503375040565701864845493751233877009611275883500035764036792906970084258238763963152627486758242101207127598485219754255161617890137664012548226251138485059295263306930653899766537171223837761341914356

ex = cubic_formula(110, -c, 313, 114)

import math

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
        m1, m2 = inverse(n1, n2), inverse(n2, n1)
        a1 = (a1 * m2 * n2 + a2 * m1 * n1) % (n1 * n2)
        n1 *= n2
    return a1
    
factors = [(2, 1), (136327, 1), (164341, 1), (169937, 4), (313351, 4), (321427, 4), (323377, 4), (356887, 4), (413783, 1), (519733, 3), (792413, 4), (860077, 4), (906289, 1), (976501, 2)]

rs, ps = [], []
for pi, ki in factors:
    a0 = pow(e, p//pi, p)
    x = 0
    for exp in range(1, ki+1):
        b = pow(ex, (p-1)//pi**exp, p) * inverse(pow(e, x*(p-1)//pi**exp, p), p) % p
        x += bsgs(a0, b, p, pi) * pi**(exp-1)
    rs.append(x)
    ps.append(pi**ki)

x = crt(rs, ps)
print(long_to_bytes(x))
#CCTF{V33333rY_eeeeZy_DLP_cH41L3n9E!}
