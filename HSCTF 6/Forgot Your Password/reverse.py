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
ss.add(s[0] == 0xe2d36a8db96d9ff3)
ss.add(s[1] == 0xd2818f22a0e62880)
print(ss.check())
print(ss.model())
