#!/usr/bin/env python3

from Crypto.Util.number import *
from flag import flag

nbit = 64

while True:
	p, q = getPrime(nbit), getPrime(nbit)
	P = int(str(p) + str(q))
	Q = int(str(q) + str(p))
	PP = int(str(P) + str(Q))
	QQ = int(str(Q) + str(P))
	if isPrime(PP) and isPrime(QQ):
		break

n = PP * QQ
m = bytes_to_long(flag.encode('utf-8'))
if m < n:
	c = pow(m, 65537, n)
	print('n =', n)
	print('c =', c)

#p=9324884768249686093
#q=10512422984265378151
#CCTF{wH3Re_0Ur_Br41N_Iz_5uP3R_4CtIVe_bY_RSA!!}
