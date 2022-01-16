from Crypto.Util.number import *
from secret import flag

p = getPrime(512)
q = getPrime(512)
n = p * q
m = n**2 + 69420
h = (pow(3, 2022, m) * p**2 + pow(5, 2022, m) * q**2) % m
c = pow(bytes_to_long(flag), 65537, n)

print('n =', n)
print('h =', h)
print('c =', c)