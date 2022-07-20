#!/usr/bin/env python3

from Crypto.Util.number import *
import telnetlib

MSG = "4lL crypt0sy5t3ms suck5 fr0m faul7 atTaCk5 :P"
m = bytes_to_long(MSG.encode('utf-8'))

tn = telnetlib.Telnet('04.cr.yp.toc.tf', 37713)

tn.read_until(b'uit\n')
tn.write(b'G\n')
e = int(tn.read_until(b'\n').split()[-1])
n = int(tn.read_until(b'\n').split()[-1])
found = False
for i in range(n.bit_length() - 1):
    for j in range(i + 1, n.bit_length() - 1):
        p = n ^ (1 << n.bit_length() - 1 - i) ^ (1 << n.bit_length() - 1 - j)
        if isPrime(p):
            found = True
            break
    if found:
        break

tn.read_until(b'uit\n')
tn.write(b'A\n')
tn.read_until(b'\n')
tn.write(f'{i}, {j}\n'.encode())

tn.read_until(b'uit\n')
tn.write(b'V\n')
tn.read_until(b'\n')
tn.write(f'{pow(m, inverse(e, p-1), p)}\n'.encode())
print(tn.read_all())
#CCTF{R3aLlY_tH1S_1z_Seiferts_R54_AT7aCk!!?}
