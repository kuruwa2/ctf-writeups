from sage.all import *
from Crypto.Util.number import *
from pwn import *
from gmpy2 import is_prime
import random

def invphi(n, begin=False):
    if n==3 or n==5:
        return None
    if is_prime(n+1):
        return n+1
    dev = divisors(n)
    if len(dev)==2:
        return None
    for i in range(len(dev)//3):
        a = invphi(dev[1+i])
        if a:
            for j in range(len(dev)-2):
                if lcm(dev[1+i], dev[1+j]) == n:
                    b = invphi(dev[1+j])
                    if b:
                        if begin:
                            if lcm(a,b) <= 100*n:
                                return lcm(a,b)
                        else:
                            return lcm(a,b)
    return None

def inv_l(n):   #Copy from ariana
    f = factor(n)
    rf = f
    invn = 1
    while rf != factor(1):
        pls = [prod(i) for i in subsets([factor(i)**j for i,j in rf])]
        pls[0] = factor(1)
        pls.sort(key=lambda x:-x.prod())
        for pf in pls:
            div = [prod(factor(p)**e for p,e in i) for i in cartesian_product([[(i[0],j) for j in range(i[1]+1)] for i in f/pf])]
            div[0] = factor(1)
            div.sort(key=lambda x:x.prod())
            for i in div:
                if is_prime(i*pf+1):
                    invn *= i*pf+1
                    rf = rf/pf
                    break
            else:
                continue
            break
    return invn

while True:
    r = remote('07.cr.yp.toc.tf', 10101)
    for _ in range(5):
        r.recvline()

    while True:
        phi = int(r.recvline()[:-3].split()[-1])
        print(phi)
        ans = inv_l(phi)
        print(ans)
        r.sendline(str(ans))
        q = r.recvline()
        print(q)
        if b'next challenge' not in q:
            break
    if b'WHY???' not in q:
        break
    r.close()
r.interactive()

#CCTF{Carmichael_numbers_are_Fermat_pseudo_primes}
