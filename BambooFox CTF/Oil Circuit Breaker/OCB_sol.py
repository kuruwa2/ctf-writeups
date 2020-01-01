from pwn import *
BLOCKSIZE = 16
def xor(a,b):
    return bytes([x^y for x,y in zip(a,b)])
class Block:
    def __init__(self, data = b''):
        self.data = data

    def double(self):
        assert(len(self.data) == BLOCKSIZE)
        x = int.from_bytes(self.data, 'big')
        n = BLOCKSIZE * 8
        mask = (1 << n) - 1
        if x & (1 << (n - 1)):
            x = ((x << 1) & mask) ^ 0b10000111
        else:
            x = (x << 1) & mask
        return Block(x.to_bytes(BLOCKSIZE, 'big'))

r = remote('34.82.101.212', 20000)
r.sendlineafter('> ', '1')

nonce = bytes.fromhex('0'*32)
target = bytes.fromhex('0'*30+'01')
plain = target + int(128).to_bytes(16, 'big') + nonce
r.sendlineafter('nonce = ',nonce.hex())
r.sendlineafter('plain = ',plain.hex())
c = bytes.fromhex(r.recvline()[9:-1].decode())
t = bytes.fromhex(r.recvline()[6:-1].decode())
r.sendlineafter('> ', '2')
r.sendlineafter('nonce = ',nonce.hex())
r.sendlineafter('cipher = ',(c[:16]+xor(c[16:32],xor(target, int(128).to_bytes(16, 'big')))).hex())
r.sendlineafter('tag = ',xor(c[32:],nonce).hex())
a = r.recvline()
m = bytes.fromhex(r.recvline()[8:-1].decode())
L = int.from_bytes(bytes([x ^ y for x, y in zip(m[16:],int(129).to_bytes(16, 'big'))]), 'big')
if L % 2:
    L ^= 0b10000111
    L //= 2
    L += 2**127
else:
    L //= 2
L = bytes.fromhex(hex(L)[2:].rjust(32,'0'))
nonce = xor(target,L)
L = xor(c[:16],L)
L2= Block(L).double().data
L4= Block(L2).double().data
newL4 = L4
L4s = []
p = int(120).to_bytes(16,'big')
for i in range(256):
    s = b'giveme flag.txt'+i.to_bytes(1,'big')
    s2 = xor(xor(s, L2), L4)
    p += xor(s2, newL4)
    L4s.append(newL4)
    newL4 = Block(newL4).double().data
r.sendlineafter('> ', '1')
r.sendlineafter('nonce = ',nonce.hex())
r.sendlineafter('plain = ',(p+nonce).hex())
c2 = bytes.fromhex(r.recvline()[9:-1].decode())
t2 = bytes.fromhex(r.recvline()[6:-1].decode())
pad = xor(c2[:16],L2)
i = pad[-1]
c_ans = xor(pad, b'giveme flag.txt')
t_ans = xor(c2[16*(i+1):16*(i+2)], L4s[i])
#print(nonce.hex(), c_ans.hex(), t_ans.hex())
r.sendlineafter('> ', '3')
r.sendlineafter('nonce = ',nonce.hex())
r.sendlineafter('cipher = ',c_ans.hex())
r.sendlineafter('tag = ',t_ans.hex())  
r.interactive()
