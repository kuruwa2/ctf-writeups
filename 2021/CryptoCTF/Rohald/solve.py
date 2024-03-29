from sage.all import *
from Crypto.Util.number import *

P = (398011447251267732058427934569710020713094, 548950454294712661054528329798266699762662)
Q = (139255151342889674616838168412769112246165, 649791718379009629228240558980851356197207)
sP = (730393937659426993430595540476247076383331, 461597565155009635099537158476419433012710)
tQ = (500532897653416664117493978883484252869079, 620853965501593867437705135137758828401933)

x1, y1 = P
x2, y2 = Q
x3, y3 = sP
x4, y4 = tQ

print(gcd((x1**2+y1**2-x2**2-y2**2) * (x3**2*y3**2*(x4**2+y4**2)-x4**2*y4**2*(x3**2+y3**2))-(x3**2+y3**2-x4**2-y4**2) * (x1**2*y1**2*(x2**2+y2**2)-x2**2*y2**2*(x1**2+y1**2)),
          (x1**2+y1**2-x3**2-y3**2) * (x2**2*y2**2*(x4**2+y4**2)-x4**2*y4**2*(x2**2+y2**2))-(x2**2+y2**2-x4**2-y4**2) * (x1**2*y1**2*(x3**2+y3**2)-x3**2*y3**2*(x1**2+y1**2))))

p = 903968861315877429495243431349919213155709
d = GF(p)(x1**2+y1**2-x2**2-y2**2)/(x1**2*y1**2*(x2**2+y2**2)-x2**2*y2**2*(x1**2+y1**2))
c2 = GF(p)(x1**2+y1**2)/(1+d*x1**2*y1**2)
c = p-c2.sqrt()
#To Montgomery Form
e = 1-d*c**4
B = 1/e
A = 4/e-2
u1, u2, u3, u4 = (c+y1)/(c-y1), (c+y2)/(c-y2), (c+y3)/(c-y3), (c+y4)/(c-y4)
v1, v2, v3, v4 = 2*c*u1/x1, 2*c*u2/x2, 2*c*u3/x3, 2*c*u4/x4
#To Weierstrass Form
a = (3-A**2)/(3*B**2)
b = (2*A**3-9*A)/(27*B**3)
x1, x2, x3, x4 = u1/B + A/(3*B), u2/B + A/(3*B), u3/B + A/(3*B), u4/B + A/(3*B)
y1, y2, y3, y4 = v1/B, v2/B, v3/B, v4/B

E = EllipticCurve(GF(p), [a,b])
print(factor(E.order()))

s = discrete_log(E(x3, y3), E(x1, y1), operation='+')
t = discrete_log(E(x4, y4), E(x2, y2), operation='+')
print(long_to_bytes(s) + long_to_bytes(t))

#CCTF{nOt_50_3a5Y_Edw4rDs_3LlipT!c_CURv3}
