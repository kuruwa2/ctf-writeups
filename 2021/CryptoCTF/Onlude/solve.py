from sage.all import *

p = 71
E = matrix(GF(p), 11, 11)
LUL = matrix(GF(p), 11, 11)
ULUL = matrix(GF(p), 11, 11)
RS = matrix(GF(p), 11, 11)

f = open("output.txt", 'r')
f.readline()
for i in range(11):
    E[i] = list(map(int, f.readline()[1:-2].split()))
f.readline()
for i in range(11):
    LUL[i] = list(map(int, f.readline()[1:-2].split()))
f.readline()
for i in range(11):
    ULUL[i] = list(map(int, f.readline()[1:-2].split()))
f.readline()
for i in range(11):
    RS[i] = list(map(int, f.readline()[1:-2].split()))

U = ULUL * LUL**-1
R = LUL * ULUL**3 * U * RS**-1
A = U**-1 * (E - U*R)

alphabet = '=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ$!?_{}<>'
flag = ''
for i in range(24):
    flag += alphabet[A[i*5//11][i*5%11]]

print(flag)

#CCTF{LU__D3c0mpO517Ion__4L90?}
