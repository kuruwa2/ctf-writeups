from Crypto.Util.number import *
from hashlib import sha256
from fastecdsa.curve import secp256k1
from fastecdsa.point import Point
from pwn import *

n = secp256k1.q
r = remote('02.cr.yp.toc.tf', 23010)

cryptonym = b'Persian Gulf'
h = bytes_to_long(sha256(cryptonym).digest())
h2 = bytes_to_long(sha256(b'\x00').digest())

r.sendlineafter(b'uit\n', 'S')
r.sendlineafter(b': ', '00')
r.recvuntil(b'(')
u = int(r.recvuntil(b',')[:-1])
v = int(r.recvuntil(b',')[:-1]) * h * inverse(h2, n) % n
s = int(r.recvline()[:-2]) * h * inverse(h2, n) % n

'''r.sendlineafter(b'uit\n', 'P')
r.recvuntil('pubkey = ')
Px = int(r.recvuntil(' '))
Py = int(r.recvuntil('\n'))

P = Point(Px, Py, secp256k1)
G = Point(secp256k1.gx, secp256k1.gy, secp256k1)

u = (G - P).x
s = u * h % n
v = s'''

r.sendlineafter(b'uit\n', 'V')
r.sendlineafter(b': ', cryptonym.hex())
r.sendlineafter(b': ', f"{u},{v},{s}")

r.interactive()

#CCTF{__ECC_Bi4seD_N0nCE_53ns3_LLL!!!}
