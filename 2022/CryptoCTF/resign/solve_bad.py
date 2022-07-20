from sage.all import *
from Crypto.Util.number import *
from hashlib import sha1
from pwn import *

R = remote('03.cr.yp.toc.tf', 11137)
R.recvuntil(b'uit\n')
R.sendline(b'P')
sign = int(R.recvline().split()[-1])
#sign = 3880971629218967484545640503090028101004583624482714074096784850919845185887426910964699181118441098663241018536701247485977911468686417953690137663147885917314080109498358184070970395452018162051709811752178468895788444933219842490396244649911707738601578145427818057953122341495295550191221766764376028205277654004525334458070870985511208768701607008199392800947170906412900832376228420946990528901506276668019492974747592682957818711830684191436057086772552776918269300515362418451136901757411033581100337049118980645009224829946478379457931843588659075014453710314834723118866202276121259667839915524959960238669
MSG = b'::. Can you forge any signature? .::'
h = bytes_to_long(sha1(MSG).digest())
h2 = bytes_to_long(sha1(MSG[4:-4]).digest())
print(sign)

'''P = 1
rp = []
fp = []
while len(rp) != 34:
    while True:
        f = 2*getPrime(29)+1
        if isPrime(f):
            break
    F = GF(f)
    try:
        r = discrete_log(F(sign), F(h))
    except:
        continue
    if r % 2 != 0:
        continue
    rp.append(r)
    fp.append(f-1)
    P *= f
ff = (2**1022-1)//P
ff = previous_prime(f)
print(f)
while True:
    ff = previous_prime(ff)
    f = 2*ff + 1
    P1 = 2*P*f+1
    if isPrime(f) and isPrime(P1):
        F = GF(f)
        try:
            r = discrete_log(F(sign), F(h))
        except:
            continue
        if r % 2 == 0:
            rp.append(r)
            fp.append(f-1)
            break
r = discrete_log(GF(2)(sign), GF(2)(h))
R1 = crt(rp+[r], fp+[1])
print(R1, P1)
assert(pow(h, R1, P1) == sign%P1)'''

Q = 1
rq = 0
while rq!= 34:
    while True:
        f = 2*getPrime(29)+1
        if isPrime(f):
            break
    F = GF(f)
    try:
        r = discrete_log(F(sign), F(h))
    except:
        continue
    if r % 2 != 1:
        continue
    rq += 1
    Q *= f
f = (2**1023-1)//Q
print(f)
if f % 2 == 0:
    f -= 1
while True:
    f -= 2
    Q1 = 2*Q*f+1
    if isPrime(Q1):
        F = GF(Q1)
        try:
            R2 = discrete_log(F(sign), F(h))
        except:
            continue
        if R2 % 2 == 1:
            break
print(Q1, R2)
assert(pow(h, R2, Q1) == sign%Q1)
P1, R1 = Q1, R2

Q = 1
rq = 0
while rq!= 34:
    while True:
        f = 2*getPrime(29)+1
        if isPrime(f):
            break
    F = GF(f)
    try:
        r = discrete_log(F(sign), F(h))
    except:
        continue
    if r % 2 != 1:
        continue
    rq += 1
    Q *= f
f = (2**1023-1)//Q
print(f)
if f % 2 == 0:
    f -= 1
while True:
    f -= 2
    Q1 = 2*Q*f+1
    if isPrime(Q1):
        F = GF(Q1)
        try:
            R2 = discrete_log(F(sign), F(h))
        except:
            continue
        if R2 % 2 == 1:
            break
print(Q1, R2)
assert(pow(h, R2, Q1) == sign%Q1)

N = P1*Q1
D = crt([R1, R2], [P1-1, Q1-1])
E = inverse(D, (P1-1)*(Q1-1))
print(pow(h, D, N) == sign)

R.sendlineafter(b'uit\n', b'G')
R.recvline()
R.sendline(f'{E}, {P1}, {Q1}')
print(R.recvuntil(b'uit\n'))
R.sendline(b'S')
R.recvline()
R.recvline()
R.sendline(str(pow(h2, D, N)).encode())
R.interactive()
