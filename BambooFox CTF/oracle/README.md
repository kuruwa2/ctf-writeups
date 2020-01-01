# oracle

## Description

<img src="chall.png" width="500">

## Soluion

The server is an RSA decryptor but only send the messages after being modded by 3.

Send the original ciphertext c and you will receive m%3.

```
c -> m  
m = an * 3^n + an-1 * 3^n-1 + ... + a1 * 3 + a0

=> r = m % 3 = a0
```
Where r is received numbers.

Now calculate 3^-1 = modinv(3, n), and send 3^-1 * c (mod n):
```
(3^-1)c -> (3^-1)m
(3^-1)m =  an * 3^n-1 + an-1 * 3^n-2 + ... + a1 + a0 * 3^-1

=> r = a1 + (a0 * 3^-1 (modn)) (mod 3)
=> a1 = r - (a0 * 3^-1 (modn)) (mod 3)
```
Repeat until getting 0 multiple times, and you can calculate the message (a0, a1, ..., an).

```
BAMBOOFOX{SimPlE0RACl3}
```
