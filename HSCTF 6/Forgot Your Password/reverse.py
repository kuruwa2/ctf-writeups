from z3 import *

s = [BitVec('s0',65),BitVec('s1',65)]

ss = Solver()

def o(x,k):
	return x<<k
def m(a):
	return a&0xffffffffffffffff
def next():
	b = m(s[0]+s[1])
	h()
	return m(b)
def p(k, x):
	return x>>(64-k)
def x(b, a):
	return a^b
def oro(a, b):
	return a|b
def h():
	s1 = m(x(s[0],s[1]))
	s[0] = m(x(oro(o(s[0],55),p(55,s[0])),x(s1,(o(s1,14)))))
	s[1] = m(oro(o(s1,36),p(36,s1)))
next()
next()
next()
next()
ss.add(next() == 0x7373696674637368)
ss.add(next() == 0x776f776c6f6f636f)
print(ss.check())
print(ss.model())
