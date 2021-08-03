from pwn import *
from Crypto.Util.number import *

r = remote('05.cr.yp.toc.tf', 14010)

r.sendlineafter(b'uit\n', 'G')
n, f, v = list(map(int, r.recvline()[16:-2].split(b',')))

r.sendlineafter(b'uit\n', 'R')
r.recvline()
r.sendline(str(n+1) + ',' + str((n-1)*n-1))

r.interactive()

#CCTF{Phillip_N0W_4_pr0b4b1liStiC__aSymM3Tr1C__AlGOrithM!!}
