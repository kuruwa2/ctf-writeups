#!/usr/bin/env python3

import base64

def xor(a, b):
    return bytes(i^j for i, j in zip(a, b))

enc = open("./flag.enc", 'rb').read()
ba = base64.b64encode(b'CCTF{')[:6].decode()
baph = ''
for i in ba:
    if i.islower():
        baph += i.upper()
    else:
        baph += i.lower()

key = xor(baph.encode(), enc)
baph = xor(key * 8, enc).decode()
ba = ''
for i in baph:
    if i.isupper():
        ba += i.lower()
    else:
        ba += i.upper()

flag = base64.b64decode(ba)
print(flag)
#CCTF{UpP3r_0R_lOwER_17Z_tH3_Pr0bL3M}
