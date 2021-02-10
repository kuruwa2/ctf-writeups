from sage.all import *
from pwn import *
from hashlib import sha256
from Crypto.Util.number import *
import time

p = 0xd34add77b5ce24599a94b5b0deb76d194c70b02e01a0b12560983764b22d2495
a = 0x91b133a4846a47c0f289dc1e1cccda757e96849611b73f93b9ced280e4ec59f0
b = 0x5289ef4348d33790bf73b4b7b10f8476224a6c26f7b914854203f9e89f602d9c
E = EllipticCurve(GF(p), [a, b])
G = E(0x684aeb01fa41bd03bfe56b74705fb9af70115b64fedf7dbe1ab04f66293bcfd1, 0x41f9035541e931c807c2da8355969a2f018ab9ee149c39de2c6bc20850e90c48)
order = 0xd34add77b5ce24599a94b5b0deb76d186441dc4220c5aabced7be2355c992e8b

r = remote('eof01.zoolab.org', 42070)


rs = []
ss = []
hs = []
shortest = 10
for i in range(50):
    r.sendlineafter(b'exit\n', '1')
    r.sendlineafter(b'?\n', 'a')
    start = time.time()
    qq = r.recvline()
    t = time.time() - start
    if t < shortest:
        shortest = t
        q = qq
rs.append(int(q[1:].split(b',')[0]))
ss.append(int(q[:-2].split(b',')[-1]))
hs.append(int(sha256(b'a').hexdigest(), 16))

shortest = 10
for i in range(50):
    r.sendlineafter(b'exit\n', '1')
    r.sendlineafter(b'?\n', 'b')
    start = time.time()
    qq = r.recvline()
    t = time.time() - start
    if t < shortest:
        shortest = t
        q = qq
rs.append(int(q[1:].split(b',')[0]))
ss.append(int(q[:-2].split(b',')[-1]))
hs.append(int(sha256(b'b').hexdigest(), 16))

shortest = 10
for i in range(50):
    r.sendlineafter(b'exit\n', '1')
    r.sendlineafter(b'?\n', 'c')
    start = time.time()
    qq = r.recvline()
    t = time.time() - start
    if t < shortest:
        shortest = t
        q = qq
rs.append(int(q[1:].split(b',')[0]))
ss.append(int(q[:-2].split(b',')[-1]))
hs.append(int(sha256(b'c').hexdigest(), 16))

print(rs,ss)

B = [[0] * 4 for _ in range(4)]
for i in range(2):
    B[i][i] = order
    B[2][i] = -inverse(ss[i], order) * ss[2] * rs[i] * inverse(rs[2], order) % order
    B[3][i] = (inverse(ss[i], order) * rs[i] * hs[2] * inverse(rs[2], order) - inverse(ss[i], order) * hs[i]) % order

B[2][2] = 1
B[3][3] = 2**160
B = matrix(B)
k = B.BKZ()[0][0]
print(k)
d = int(inverse(rs[0], order) * (-k*ss[0] - hs[0])) % order
print(d)
h = int(sha256(b'Kuruwa').hexdigest(), 16)
x = (69*G).xy()[0]
s = int(inverse(69, order) * (h + int(x)*d)) % order
print(x,s)

r.sendlineafter(b'exit\n', '2')
r.sendlineafter(b': ', 'Kuruwa')
r.sendlineafter(b': ', str(x))
r.sendlineafter(b': ', str(s))

r.interactive()
