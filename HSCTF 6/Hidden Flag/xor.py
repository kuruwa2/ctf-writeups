from Crypto.Util.number import *

with open("chall.png", 'rb') as f:
    a = f.read()
f.close()

xor = b'invisible'
b = b''
for i in range(len(a)):
    b += long_to_bytes(a[i] ^ xor[i%9])


with open("xor.png", 'wb') as f:
    f.write(b)
f.close()
