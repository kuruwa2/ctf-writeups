from sage.all import *
from Crypto.Util.number import *
from tqdm import tqdm

PR = BooleanPolynomialRing(56, [f'x{i}' for i in range(56)])
xs = PR.gens()
l = 29316

enc = bin(bytes_to_long(open("./flag.enc", 'rb').read()))[2:].rjust(65536-64, '0')
print(len(enc))

meow = [0, 1, 2, 4, 5, 7, 10, 11, 12, 13, 18, 20, 21, 22, 23, 24, 25, 26, 30, 33]
def FF(S):
    return sum([S[i] for i in meow])

def F(S):
    return (
		S[0] + S[12] + S[62] + S[18] + S[36] + 
		S[2]*S[8] + 
		S[34]*S[20] +
		S[27]*S[60] +
		S[31]*S[34] +
		S[63]*S[48] +
		S[50]*S[15] +
		S[25]*S[49] +
		S[49]*S[7]  +
		S[13]*S[61]*S[10] +
		S[32]*S[37]*S[29] +
		S[9]*S[6]*S[42] +
		S[59]*S[26]*S[55] +
		S[42]*S[41]*S[29] +
		S[58]*S[24]*S[28]
	    )

itod = {}
now = 0
for i in range(56):
    itod[xs[i]] = now
    now += 1
for i in range(56):
    for j in range(i+1, 56):
        itod[xs[i]*xs[j]] = now
        now += 1
for i in range(56):
    for j in range(i+1, 56):
        for k in range(j+1, 56):
            itod[xs[i]*xs[j]*xs[k]] = now
            now += 1
# print(now)

IS = []
for i in range(8):
    IS += [0] + list(xs[7*i:7*i+7])
now = IS

count = 0
M = matrix(GF(2), l)
venc = vector(GF(2), l)
for i in tqdm(range(l)):
    while M.rank() != i + 1:
        output = F(now)
        v = vector(GF(2), l)
        for j in list(output):
            v[itod[j]] = 1
        M[i] = v
        venc[i] = enc[count]
        count += 1
        now = now[1:] + [FF(now)]

ans = M.solve_right(venc)
print(ans[:64])
