# Massive RSA

## Description

I was scared that my RSA would be broken, so I made sure that the numbers were massive.

[massive.txt](massive.txt)

## Solution

The n is actually a prime.

So phi(n) = n-1. Perform the modded inverse of e and decrypt the message.

```
d=modinv(e,n-1)
import codecs
print(codecs.decode(hex(pow(c,d,n))[2:],'hex'))
```

The flag is
```
hsctf{forg0t_t0_mult1ply_prim3s}
```
