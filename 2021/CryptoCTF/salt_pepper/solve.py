from pwn import *

r = remote('02.cr.yp.toc.tf', 28010)
r.sendlineafter(b'uit\n', 'L')

username = b'\x80' + b'\x00'*36 + (19*8).to_bytes(8, 'little') + b'n3T4Dm1n'
password = b'\x80' + b'\x00'*36 + (19*8).to_bytes(8, 'big') + b'P4s5W0rd'

r.sendlineafter(b': \n', f'{username.hex()},{password.hex()}')
r.sendlineafter(b': \n', '83875efbe020ced3e2c5ecc908edc98481eba47f')

r.interactive()

#CCTF{Hunters_Killed_82%_More_Wolves_Than_Quota_Allowed_in_Wisconsin}
