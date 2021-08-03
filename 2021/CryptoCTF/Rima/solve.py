from Crypto.Util.number import *

gg = bytes_to_long(open("g.enc", 'rb').read())

g = []

while gg > 0:
    g = [gg % 5] + g
    gg //= 5

for i in range(len(g)- 67): g[-67-i-1] -= g[-1-i]
g = g[67:67+256]

for i in range(len(g)-1): g[-i-2] -= g[-i-1]
g = long_to_bytes(int(''.join([str(_) for _ in g]), 2))

print(g)

#CCTF{_how_finD_7h1s_1z_s3cr3T?!}
