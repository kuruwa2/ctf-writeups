from pwn import *
from Crypto.Util.number import *
from binascii import hexlify

r = remote('quiz.ais3.org', 42069)
r.recvline()
n = int(r.recvline().split()[-1])
e = int(r.recvline().split()[-1])
r.sendlineafter(b'exit\n', '1')
r.sendlineafter(b'Name (in hex): ', hexlify(long_to_bytes(163)))
s1 = int(r.recvline().split()[1])

r.sendlineafter(b'exit\n', '1')
r.sendlineafter(b'Name (in hex): ', hexlify(long_to_bytes(33759323085949548325642458097)))
s2 = int(r.recvline().split()[1])

r.sendlineafter(b'exit\n', '2')
r.sendlineafter(b'Signature: ', str(s1*s2%n))
r.interactive()
