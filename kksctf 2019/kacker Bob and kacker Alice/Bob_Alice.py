n = 208644129891836890527171768061301730329

c1 = 173743301171240370198046699578309731314
c2 = 18997024455485040483743919351219518166
c3 = 49337945995780286416188917529635194536

p = 13037609104445998727
q = n//p

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

import codecs

e = 65537
d = modinv(e, (p-1)*(q-1))

print(codecs.decode(hex(pow(c1,d,n))[2:],'hex')+codecs.decode(hex(pow(c2,d,n))[2:],'hex')+codecs.decode(hex(pow(c3,d,n))[2:],'hex'))
