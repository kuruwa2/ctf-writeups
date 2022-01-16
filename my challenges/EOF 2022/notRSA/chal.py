from Crypto.Util.number import *
from secret import flag

n = ZZ(bytes_to_long(flag))
p = getPrime(int(640))
assert n < p
print(p)

K = Zmod(p)

def hash(B, W, H):
    def step(a, b, c):
        return vector([9 * a - 36 * c, 6 * a - 27 * c, b])
    def steps(n):
        Kx.<a, b, c> = K[]
        if n == 0: return vector([a, b, c])
        half = steps(n // 2)
        full = half(*half)
        if n % 2 == 0: return full
        else: return step(*full)
    return steps(n)(B, W, H)

print(hash(79, 58, 78))