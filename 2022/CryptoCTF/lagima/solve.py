#!/usr/bin/env python3

from sage.all import *
from Crypto.Util.number import *

f = open("./output.txt").read().split('\n')
g, h = eval(f[0][4:]), eval(f[1][4:])

G = SymmetricGroup(len(g))
rs = []
ps = []
for i in range(313):
    rs.append(discrete_log(G(h[i]), G(g[i])))
    ps.append(G(g[i]).order())

print(long_to_bytes(crt(rs, ps)))
#CCTF{3lGam4L_eNcR!p710n_4nD_L4T!n_5QuarS3!}
