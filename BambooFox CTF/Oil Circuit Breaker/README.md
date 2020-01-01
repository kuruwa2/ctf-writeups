# Oil Circuit Breaker (Crypto) \[714\]

## __Description__

<img src="chall.png" width="300">

## __Solution__

It's an OCB2 cipher, and its vulnerability can be found (here)[https://eprint.iacr.org/2018/1040.pdf].

First encryption, I sent:

```
'000000000000000000000000000000010000000000000000000000000000008000000000000000000000000000000000'
 (1)+(128)+(0)
```
