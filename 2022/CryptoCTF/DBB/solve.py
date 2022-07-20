#!/usr/bin/env python3

from sage.all import *
from Crypto.Util.number import *
import itertools

n = 34251514713797768233812437040287772542697202020425182292607025836827373815449
base_x = 7331
P = (10680461779722115247262931380341483368049926186118123639977587326958923276962, 4003189979292111789806553325182843073711756529590890801151565205419771496727)

B = (P[1]**2 - P[0]**3 - 31337 * P[0]) % n

factors = [11522256336953175349, 14624100800238964261, 203269901862625480538481088870282608241]
rs = []
os = []
for p in factors:
    E = EllipticCurve(GF(p), [31337, B])
    G = E.lift_x(Integer(base_x))
    Q = E(P)
    os.append(G.order())
    mm = discrete_log(Q, G, operation='+')
    rs.append((mm, -mm))

for i in itertools.product(*rs):
    m = long_to_bytes(crt(list(i), os))
    if b'CCTF' in m:
        print(m)
#CCTF{p0Hl!9_H31LmaN_4tTackin9!}
