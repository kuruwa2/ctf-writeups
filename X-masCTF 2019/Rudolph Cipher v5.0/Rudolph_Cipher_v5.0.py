from pwn import *
import binascii
def bytes_to_int(s):
        assert (len(s)<=8)
        a = bytes([s[6],s[7],s[4],s[5],s[2],s[3],s[0],s[1]])
        return int(a,16)

def int_to_bytes(n,w):
	s = b''
	while n:
		s = s + bytes([n & 0xff])
		n >>= 8
	return s.ljust(w//8,b'\x00')
def rotate_left(val, r_bits, max_bits):
	v1 = (val << r_bits % max_bits) & (2 ** max_bits - 1)
	v2 = ((val & (2 ** max_bits - 1)) >> (max_bits - (r_bits % max_bits)))
	return v1 | v2

def rotate_right(val, r_bits, max_bits):
	v1 = ((val & (2 ** max_bits - 1)) >> r_bits % max_bits)
	v2 = (val << (max_bits - (r_bits % max_bits)) & (2 ** max_bits - 1))
	return v1 | v2

def encrypt(message, S):
    A = bytes_to_int(message[:8])
    B = bytes_to_int(message[8:])
    for i in range(1, 18 + 1):
        A = rotate_left((A ^ B), i, 32)
        B = rotate_left((B ^ A), i, 32)

    S0 = bytes_to_int(S[:8])
    S1 = bytes_to_int(S[8:])
    S0 = S0^A
    S1 = S1^B
    return S0, S1

def decrypt(message, S0, S1):
    A = bytes_to_int(message[:8])
    B = bytes_to_int(message[8:])
    A = S0^A
    B = S1^B
    for i in range(18, 0, -1):
        B = rotate_right(B , i, 32) ^ A
        A = rotate_right(A , i, 32) ^ B
    return int_to_bytes(A,32) + int_to_bytes(B,32)
def ans(msg1, ct1, ct2):
    S0, S1 = encrypt(msg1, ct1)
    ans=decrypt(ct2, S0, S1)
    return ans
        
r = remote('challs.xmas.htsp.ro', 10002)
q = r.recvline()
q = str(q[-7:-1])[2:-1]
print(q)
from hashlib import sha256
import os
p=''
while True:
    s = os.urandom(10)
    h = sha256(s).hexdigest()
    if h[-6:] == q:
        for i in s:
            if len(hex(i)[2:]) == 1:
                p += '0'+hex(i)[2:]
            else:
                p += hex(i)[2:]
        break
r.sendline(p)
q = r.recvuntil('#1:\n')
while b'#' in q:
    q = r.recvline()
    msg1 = q.split(b' ')[2]
    ct1 = q.split(b' ')[-1][:-1]
    print(msg1,ct1)
    q = r.recvline()
    ct2 = q.split(b' ')[-1][:-1]
    print(ct2)
    r.recvline()
    p = ans(msg1, ct1, ct2)
    p = binascii.hexlify(p)
    print(p)
    r.sendline(p)
    r.recvline()
    print(r.recvline())
    q = r.recvline()
    print(q)
    
r.interactive()
