from pwn import *
from sage.all import *
from gmpy2 import next_prime
import random

def SmartAttack(P,Q,p):
    E = P.curve()
    Eqp = EllipticCurve(Qp(p, 2), [ ZZ(t) + randint(0,p)*p for t in E.a_invariants() ])

    P_Qps = Eqp.lift_x(ZZ(P.xy()[0]), all=True)
    for P_Qp in P_Qps:
        if GF(p)(P_Qp.xy()[1]) == P.xy()[1]:
            break

    Q_Qps = Eqp.lift_x(ZZ(Q.xy()[0]), all=True)
    for Q_Qp in Q_Qps:
        if GF(p)(Q_Qp.xy()[1]) == Q.xy()[1]:
            break

    p_times_P = p*P_Qp
    p_times_Q = p*Q_Qp

    x_P,y_P = p_times_P.xy()
    x_Q,y_Q = p_times_Q.xy()

    phi_P = -(x_P/y_P)
    phi_Q = -(x_Q/y_Q)
    k = phi_Q/phi_P
    return ZZ(k)

p = 0xd738e277b1de46697453735b06215527ba963545
a = 0x33c934b110534aa8a30b21fdf7a6479790acfba8
b = 0xd72e3ec3002a26816a143f4886a46743f9c5a677
q = next_prime(next_prime(p))
'''while True:
    c = random.randint(1, q)
    d = random.randint(1, q)
    E = EllipticCurve(GF(q), [c, d])
    if factor(E.order())[-1][0] < 2**40:
        print(c, d)
        break'''

c = 234110333988323900577427824207310503614425554206
d = 525445202447761270527535572287223592924042118239
E1 = EllipticCurve(GF(p), [a, b])
E2 = EllipticCurve(GF(q), [c, d])

r = remote('07.cr.yp.toc.tf', 10010)
r.sendlineafter(b'uit\n', 'S')
r.recvline()
r.sendline(str(a)+','+str(b)+','+str(p))
r.recvline()
r.recvline()
r.sendline(str(c)+','+str(d)+','+str(q))

r.recvuntil(b'(')
G = E1(list(map(int, r.recvline()[:-3].split(b','))))
r.recvuntil(b'(')
H = E2(list(map(int, r.recvline()[:-3].split(b','))))
r.recvuntil(b'(')
rG = E1(list(map(int, r.recvline()[:-3].split(b','))))
r.recvuntil(b'(')
sH = E2(list(map(int, r.recvline()[:-3].split(b','))))

R = SmartAttack(G, rG, p)
s = discrete_log(sH, H, operation='+')
r.sendlineafter(b': \n', str(R)+','+str(s))

r.interactive()

#CCTF{Pl4yIn9_Wi7H_ECC_1Z_liK3_pLAiNg_wiTh_Fir3!!}
