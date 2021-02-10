#!/usr/bin/python3

import random
from sage.all import *
from Crypto.Util.number import *

n, d, q = 471, 313, 2048
flag = open("flag.txt",'rb').read()

Zx.<x> = ZZ[]
def convolution(f,g):
      return (f * g) % (x^n-1)

def balancedmod(f,q):
      g = list(((f[i] + q//2) % q) - q//2 for i in range(n))
      return Zx(g)

def randomdpoly():
      assert d <= n
      result = n*[0]
      for j in range(d):
        while True:
          r = randrange(n)
          if not result[r]: break
        result[r] = 1-2*randrange(2)
      return Zx(result)


def invertmodprime(f,p):
      T = Zx.change_ring(Integers(p)).quotient(x^n-1)
      return Zx(lift(1 / T(f)))

def invertmodpowerof2(f,q):
      assert q.is_power_of(2)
      g = invertmodprime(f,2)
      while True:
        r = balancedmod(convolution(g,f),q)
        if r == 1: return g
        g = balancedmod(convolution(g,2 - r),q)

def keypair():
      while True:
        try:
          f = randomdpoly()
          f3 = invertmodprime(f,3)
          fq = invertmodpowerof2(f,q)
          break
        except:
          pass
      g = randomdpoly()
      publickey = balancedmod(3 * convolution(fq,g),q)
      secretkey = f,f3
      # Remove after debug!!
      print('f:', f)
      print('f3:', f3)
      return publickey,secretkey

def encrypt(message,publickey):
      r = randomdpoly()
      return balancedmod(convolution(publickey,r) + message,q)

publickey,secretkey = keypair()
fm = []
for i in bin(bytes_to_long(flag))[2:]:
    fm.append(int(i))
fm = Zx(fm)
c = encrypt(fm, publickey)
print('c:', c)
