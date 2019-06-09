from pwn import *

r = remote("crypto.hsctf.com", 8111)

r.recvuntil(': ')
ans = r.recvline()
print(ans)
p = 'hsctf{'
while True:
    enc = ''
    for i in range(32, 127):
        r.recvuntil('encrypt:')

        m = p+chr(i)
        length = len(m)

        r.sendline(m)
        r.recvline()
        q = r.recvline()
        enc = q.split(' ')[1]
        print(enc)
        
        if enc[:2*length] == ans[:2*length]:
            p += chr(i)
            break
    if enc == ans:
        break
print(p)
#hsctf{h0w_d3d_y3u_de3cryP4_th3_s1p3R_s3cuR3_m355a9e?}
