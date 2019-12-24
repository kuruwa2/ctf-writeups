from pwn import *
import string

q = 1
c = string.ascii_letters
c = c[26:]+c[:26]
r = remote('challs.xmas.htsp.ro', 13000)
ans=''
while q != 0:
    r.recvuntil('guess: ')
    r.sendline(ans+c[0])
    q1 = int(r.recvline().split(': ')[-1][:-1])
    r.recvuntil(': ')
    r.sendline(ans+c[51])
    q2 = int(r.recvline().split(': ')[-1][:-1])
    low = 0
    high = 51

    while high-low != 1:
        if q1 < q2:
            high = (low+high)//2
            r.recvuntil(': ')
            r.sendline(ans+c[high])
            q2 = int(r.recvline().split(': ')[-1][:-1])
            #print(c[high],q2)
        else:
            low = (low+high)//2
            r.recvuntil(': ')
            r.sendline(ans+c[low])
            q1 = int(r.recvline().split(': ')[-1][:-1])
            #print(c[low],q1)
    if q1 < q2:
        ans += c[low]
        print(q1)
        q = q1
    else:
        ans += c[high]
        print(q2)
        q = q2
r.interactive()
    
