from pwn import *
from sage.all import *
from Crypto.Util.number import *

r = remote('03.cr.yp.toc.tf', 25010)

r.sendlineafter(b'uit\n', 'S')
p = int(r.recvline().split()[-1])
x = int(r.recvline().split()[-1])

r.sendlineafter(b'uit\n', 'P')
q = r.recvline()[10:-2]
v = list(map(int, q.split(b',')))

B = [[0]*6 for _ in range(6)]
for i in range(4):
    B[i][i] = p
    B[4][i] = pow(x, -i-1, p)
    B[5][i] = v[-2-i] - v[-1] * pow(x, -i-1, p)
B[4][4] = 1
B[5][5] = 2**32

BM = matrix(ZZ, B)
s = -BM.LLL()[0][:4][::-1]
s4 = (v[3]+s[3]) * x % p - v[4]
s = list(s)+[s4]
print(s)

def sign(msg, privkey, d):
	msg = msg.encode('utf-8')
	l = len(msg) // 4
	M = [bytes_to_long(msg[4*i:4*(i+1)]) for i in range(l)]
	q = int(next_prime(max(M)))
	sign = [M[i]*privkey[i] % q for i in range(l)]
	return sign
    
r.sendlineafter(b'uit\n', 'F')
m = r.recvline()[:-1].split()[-1].decode()
sign = sign(m, s, 32)
r.sendline(','.join(list(map(str,sign))))

r.interactive()

#CCTF{Lattice_bA5eD_T3cHn1QuE_70_Br34K_LCG!!}
