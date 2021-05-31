from Crypto.Util.number import *
from secret import flag
import random
import gmpy2
gmpy2.get_context().precision = 1024

def collision(m1, v1, m2, v2):
	return v1*(m1-m2)/(m1+m2) + v2*(2*m2)/(m1+m2), v1*(2*m1)/(m1+m2) + v2*(m2-m1)/(m1+m2)

def keygen(digits):     # Warning: slow implementation
	m1 = 1
	m2 = 10 ** (2*digits-2)
	v1 = gmpy2.mpfr(0)
	v2 = gmpy2.mpfr(-1)

	count = 0       # p+q
	while abs(v1) > v2 or v1 < 0:
		if v1 < 0:
			v1 = -v1
		else:
			v1, v2 = collision(m1, v1, m2, v2)
		count += 1

	while True:
		p = random.randint(count//3, count//2)
		q = count - p
		if isPrime(p) and isPrime(q):
			break
	return p, q


p, q = keygen(153)
n = p*q
e = 65537
m = bytes_to_long(flag)
print('n =', n)
print('e =', e)
print('c =', pow(m, e, n))
