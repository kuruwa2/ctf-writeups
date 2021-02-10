from pwn import *

query = [0, 11, 21, 30, 38, 45, 51, 56]

r = remote("eof01.zoolab.org", 42069)
for i in range(100):
    q = r.recvuntil('query: ')
    print(q)
    r.sendline('4567')
    r.sendlineafter(b'query: ', '2367')
    r.sendlineafter(b'query: ', '1357')
    r.sendlineafter(b'query: ', '2345')
    r.sendlineafter(b'query: ', '1346')
    r.sendlineafter(b'query: ', '1256')
    q = r.recvline()
    print(q)
    ans = ''
    for a in q[:-1]:
        if a == ord('o'):
            ans += '1'
        else:
            ans += '0'
    ans = int(ans, 2)
    for a in range(8):
        if bin(ans ^ query[a]).count('1') <= 1:
            ans = a
            break
    print(ans)
    r.sendline(str(ans))

r.interactive()
