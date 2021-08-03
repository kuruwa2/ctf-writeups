from pwn import *
from sage.all import *
from Crypto.Util.number import *
from Crypto.Cipher import AES

def b2p(b):
    return P(list(bin(bytes_to_long(b))[2:].rjust(128,'0')))
  
def p2b(p):
    return long_to_bytes(int(''.join(list(map(str, p.list()))), 2))

def xor(a,b):
    return bytes(i^j for i,j in zip(a,b))

passphrase = b'HungryTimberWolf'
cipher = AES.new(passphrase, AES.MODE_ECB)

R = PolynomialRing(GF(2), 't')
t = R.gens()[0]
P = R.quotient(t**128 + t**7 + t**2 + t + 1)
x = P.gens()[0]
h = b2p(cipher.encrypt(b'\x00'*16))

ivs = []
for i in range(256):
    iv = b2p(bytes([i]) + b'\x00'*15)
    iv = p2b((iv * h + x**124) * h)
    ivs.append(long_to_bytes(bytes_to_long(iv)+1).rjust(16, b'\x00'))

while True:
    r = remote('01.cr.yp.toc.tf', 27010)

    r.sendlineafter(b'uit\n', 'G')
    enc = bytes.fromhex(r.recvline().decode().split()[-1])

    for iv in ivs:
        flag = xor(cipher.encrypt(iv), enc)
        if b'EPOCH' in flag:
            for j in range(len(enc)//16):
                iv = long_to_bytes(bytes_to_long(iv)+1).rjust(16, b'\x00')
                flag += xor(cipher.encrypt(iv), enc[16*j+16:16*j+32])
            break
    if b'EPOCH' in flag:
        print(flag)
        break
    r.close()

r.interactive()

#CCTF{____w0lveS____c4n____be____dan9er0uS____t0____p3oplE____!!!!!!}
