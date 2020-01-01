from pwn import *
import codecs
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
r = remote('34.82.101.212', 20001)

r.recvuntil('> ')
r.sendline('1')
q = r.recvline()
c = int(q[4:-1])
e = 65537
q = r.recvline()
n = int(q[4:-1])
a = modinv(3,n)
m = 0
b = 0
i = 0
f = 0

while True:
    r.sendlineafter('> ', '2')
    r.sendline(str(pow(a,i*e,n)*c%n))
    q = r.recvline()
    mm = (int(q[7:-1]) - (a*b)%n) % 3
    if mm == 0:
        f += 1
        if f == 10:
            break
    else:
        f = 0
    b = (a*b + mm) % n
    m = 3**i*mm+m
    print(m)
    i += 1

print(m)
print(codecs.decode(hex(m)[2:], 'hex'))
