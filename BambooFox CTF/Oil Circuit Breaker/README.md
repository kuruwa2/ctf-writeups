# Oil Circuit Breaker (Crypto) \[714\]

## __Description__

<img src="chall.png" width="300">

## __Solution__

It's an OCB2 cipher, and its vulnerability can be found [here](https://eprint.iacr.org/2018/1040.pdf).

First encryption, send in: (+ is concatenation and (n) is 16 bytes expansion to n)

```
nonce = 00000000000000000000000000000000
plain = 000000000000000000000000000000010000000000000000000000000000008000000000000000000000000000000000
      = (1) + (128) + (0)
```
Where plain = M\[0\]+M\[1\]+M\[2\].

Get C\[0\]+C\[1\]+C\[2\] and T.

In descryption, send in:
```
nonce  = 00000000000000000000000000000000
cipher = C[0] + C[1] ^ (M[0] ^ 128)
tag    = C[2] ^ M[2]
```

This will reply auth = True because:
```
T' = e(S' ^ 8L ^ 4L)
   = e((M'[1] ^ C'[1] ^ pad') ^ 8L ^ 4L)
   = e(M[1] ^ C'[1] ^ C[1] ^ 4L ^ 8L ^ 4L)
   = e(M[1] ^ C'[1] ^ C[1] ^ 8L)
   = e(M[1] ^ (M[1] ^ C[1] ^ (128)) ^ C[1] ^ 8L)
   = e((128) ^ 8L)
   = pad
   = C[2] ^ nonce
```
Where T' is tag, e stands for aes encryption, and L = e(nonce).

So T' is profit. We also have information about L because:
```
M'[2] = C'[2] ^ pad'
      = C[1] ^ (M[0] ^ 128) ^ C[1] ^ 4L
      = M[0] ^ (128) ^ 4L
```
So we can recover L for the encryption.

Now that we have L, we also need to know other components for encryption of 'giveme flag.txt', but we can only send the same nonce once.

That's ok because if we let nonce = M\[0\] ^ L, then L\'\' = e(M\[0\] ^ L) = C\[0\] ^ L in the first encryption!

