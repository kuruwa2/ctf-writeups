import itertools
import gmpy2
from Crypto.Util.number import *
from sage.all import *

def small_roots(f, bounds, m=1, d=None):	#https://github.com/defund/coppersmith/blob/master/coppersmith.sage
    if not d:
        d = f.degree()

    R = f.base_ring()
    N = R.cardinality()
    
    f /= f.coefficients().pop(0)
    f = f.change_ring(ZZ)
    
    G = Sequence([], f.parent())
    for i in range(m+1):
        base = N**(m-i) * f**i
        for shifts in itertools.product(range(d), repeat=f.nvariables()):
            g = base * prod(map(power, f.variables(), shifts))
            G.append(g)
    
    B, monomials = G.coefficient_matrix()
    monomials = vector(monomials)
    
    factors = [monomial(*bounds) for monomial in monomials]
    for i, factor in enumerate(factors):
        B.rescale_col(i, factor)
	
    B = B.dense_matrix().LLL()

    B = B.change_ring(QQ)
    for i, factor in enumerate(factors):
        B.rescale_col(i, 1/factor)

    H = Sequence([], f.parent().change_ring(QQ))
    for h in filter(None, B*monomials):
        H.append(h)
        I = H.ideal()
        if I.dimension() == -1:
            H.pop()
        elif I.dimension() == 0:
            roots = []
            for root in I.variety(ring=ZZ):
                root = tuple(R(root[var]) for var in f.variables())
                roots.append(root)
            return roots

    return []

def square_root_mod_power_of_two(a, power):
    t = 0
    while a % 2 == 0:
        a >>= 1
        t += 1
    if t % 2 != 0 or a % 8 != 1:
        return []
    x = 1
    bitMask = 4
    for i in range(3, power-t):
        if ((x**2-a)>>i) & 1:
            x |= bitMask
        bitMask <<= 1
    roots = []
    j = t//2
    for s in range(2**j):
        for q in [x, x+bitMask, -x+bitMask, -x+bitMask*2]:
            roots.append(2**j*(s*2**(power-t)+q))
    return roots

n = 40246250034008312612597372763167482121403594640959033279625274444300931999548988739160328671767018778652394885185401059130887869211330599272113849088780129624581674441314938139267245340401649784020787977993123159165051168187958742107
F = PolynomialRing(Zmod(n), 'x', 2)
a, b = F.gens()[0], F.gens()[1]
d0 = 0b00001101110000010101000000101110000111101011011101111111000011110101111000100001011100001111011000010101010010111100000011000101000001110001111100001011001100010001100000011100001101101100011101000001010001100000101000001
r = 2**221
e = 65537
Gmax = gcd(1-e*d0, r)

p, q = 0, 0
for k in range(28899, e):
    if k%100==0:  
        print(k)
    G = gcd(k, r)
    if G > Gmax:
        continue
    ss = int((1-e*d0+k*n+k)//G * Zmod(r//G)(k//G)**-1)
    if ss % 2 != 0:
        continue
    ss = [ss + r//G*i for i in range(G)]
    for s in ss:
        ps = square_root_mod_power_of_two(s**2//4-n, 221)
        ps = [(p+s//2)%r for p in ps]
        for p0 in ps:
            q0 = ZZ(Zmod(r)(n/p0))
            f = (r*a+p0)*(r*b+q0)  
            root = small_roots(f, [2**36, 2**297], m=1, d=3)  
            if root:
                print(root[0][0]*r+p0, root[0][1]*r+q0)
                p, q = int(root[0][0]*r+p0), int(root[0][1]*r+q0)
                break
    if p:
        break
        
#p = 893797203302975694226187727100454198719976283557332511256329145998133198406753
#q = 45028391099547672850933752650458741775967975675132570955919826831266417192736487124495185843666317576599654513399532947872743150016262181991752161585154619

c = 28505561807082805875299833176536442119874596699006698476186799206821274572541984841039970225569714867243464764627070206533293573878039612127495688810559746369298640670292301881186317254368892594525084237214035763200412059090430060075
a = 146700196613209180651680280746469710064760660116352037627587109421827052580531
b = 27617741006445293346871979669264566397938197906017433294384347969002810245774095080855953181508639433683134768646569379922750075630984038851158577517435997971553106764846655038664493024213691627948571214899362078353364358736447296943
assert (n == 4*a**3+b)

u = p-2*a
v = (a*u**2+b)//(u+2*a)
x = (u - gmpy2.iroot(u**2-4*v, 2)[0])//2
y = u - x
print(long_to_bytes(pow(c, inverse(e, (p-1)*(q-1)), n) - x**2 - y))

#CCTF{Par7ial_K3y_Exp0sure_At7ack_0n_L0w_3xP_RSA}
