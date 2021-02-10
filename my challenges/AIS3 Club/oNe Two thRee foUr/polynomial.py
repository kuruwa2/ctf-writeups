import itertools

class DomainElement(object):
   def __radd__(self, other): return self + other
   def __rsub__(self, other): return -self + other
   def __rmul__(self, other): return self * other
 
class FieldElement(DomainElement):
   def __truediv__(self, other): return self * other.inverse()
   def __rtruediv__(self, other): return self.inverse() * other
   def __div__(self, other): return self.__truediv__(other)
   def __rdiv__(self, other): return self.__rtruediv__(other)

def typecheck(f):
   def newF(self, other):
      if (hasattr(other.__class__, 'operatorPrecedence') and
            other.__class__.operatorPrecedence > self.__class__.operatorPrecedence):
         return NotImplemented
 
      if type(self) is not type(other):
         try:
            other = self.__class__(other)
         except TypeError:
            message = 'Not able to typecast %s of type %s to type %s in function %s'
            raise TypeError(message % (other, type(other).__name__, type(self).__name__, f.__name__))
         except Exception as e:
            message = 'Type error on arguments %r, %r for functon %s. Reason:%s'
            raise TypeError(message % (self, other, f.__name__, type(other).__name__, type(self).__name__, e))
 
      return f(self, other)
 
   return newF

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

def gcd(a, b):
    if abs(a) < abs(b):
        return gcd(b, a)
    while abs(b) > 0:
        q,r = divmod(a,b)
        a,b = b,r
    return a

def extendedEuclideanAlgorithm(a, b):
    if abs(b) > abs(a):
        (x,y,d) = extendedEuclideanAlgorithm(b, a)
        return (y,x,d)   
    if abs(b) == 0:
        return (1, 0, a)
    x1, x2, y1, y2 = 0, 1, 1, 0
    while abs(b) > 0:
        q, r = divmod(a,b)
        x = x2 - q*x1
        y = y2 - q*y1
        a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y
    return (x2, y2, a)  

@memoize
def IntegersModP(p):
   class IntegerModP(FieldElement):
      def __init__(self, n):
          self.n = n % p
          self.field = IntegerModP
 
      def __add__(self, other): return IntegerModP(self.n + other.n)
      def __sub__(self, other): return IntegerModP(self.n - other.n)
      def __mul__(self, other): return IntegerModP(self.n * other.n)
      def __truediv__(self, other): return self * other.inverse()
      def __div__(self, other): return self * other.inverse()
      def __neg__(self): return IntegerModP(-self.n)
      def __eq__(self, other): return isinstance(other, IntegerModP) and self.n == other.n
      def __abs__(self): return abs(self.n)
      def __str__(self): return str(self.n)
      def __repr__(self): return '%d (mod %d)' % (self.n, self.p)
 
      def __divmod__(self, divisor):
          q,r = divmod(self.n, divisor.n)
          return (IntegerModP(q), IntegerModP(r))

      def inverse(self):
           x,y,d = extendedEuclideanAlgorithm(self.n, self.p)
           return IntegerModP(x)

   IntegerModP.p = p
   IntegerModP.__name__ = 'Z/%d' % (p)
   return IntegerModP

# create a polynomial with coefficients in a field; coefficients are in
# increasing order of monomial degree so that, for example, [1,2,3]
# corresponds to 1 + 2x + 3x^2
@memoize
def polynomialsOver(field):
 
   class Polynomial(DomainElement):
      operatorPrecedence = 2
      factory = lambda L: Polynomial([field(x) for x in L])
 
      def __init__(self, c):
         if type(c) is Polynomial:
            self.coefficients = c.coefficients
         elif isinstance(c, field):
            self.coefficients = [c]
         elif not hasattr(c, '__iter__') and not hasattr(c, 'iter'):
            self.coefficients = [field(c)]
         else:
            self.coefficients = c
 
         #self.coefficients = strip(self.coefficients, field(0))
 
      def isZero(self): return self.coefficients == []
 
      def __repr__(self):
         if self.isZero():
            return '0'
 
         return ' + '.join(['%s x^%d' % (a,i) if i > 0 else '%s'%a
                              for i,a in enumerate(self.coefficients)])
 
      def __abs__(self): return len(self.coefficients)
      def __len__(self): return len(self.coefficients)
      def __sub__(self, other): return self + (-other)
      def __iter__(self): return iter(self.coefficients)
      def __neg__(self): return Polynomial([-a for a in self])
 
      def iter(self): return self.__iter__()
      def leadingCoefficient(self): return self.coefficients[-1]
      def degree(self): return abs(self) - 1
      @typecheck
      def __eq__(self, other):
           return self.degree() == other.degree() and all([x==y for (x,y) in zip(self, other)])
         
      @typecheck
      def __add__(self, other):
           newCoefficients = [sum(x) for x in itertools.zip_longest(self, other, fillvalue=self.field(0))]
           return Polynomial(newCoefficients)
         
      @typecheck
      def __mul__(self, other):
           if self.isZero() or other.isZero():
              return Zero()
         
           newCoeffs = [self.field(0) for _ in range(len(self) + len(other) - 1)]
         
           for i,a in enumerate(self):
              for j,b in enumerate(other):
                 newCoeffs[i+j] += a*b
         
           return Polynomial(newCoeffs)

      @typecheck
      def __divmod__(self, divisor):
           quotient, remainder = Zero(), self
           divisorDeg = divisor.degree()
           divisorLC = divisor.leadingCoefficient()
         
           while remainder.degree() >= divisorDeg:
              monomialExponent = remainder.degree() - divisorDeg
              monomialZeros = [self.field(0) for _ in range(monomialExponent)]
              monomialDivisor = Polynomial(monomialZeros + [remainder.leadingCoefficient() / divisorLC])
         
              quotient += monomialDivisor
              remainder -= monomialDivisor * divisor
         
           return quotient, remainder
   def Zero():
      return Polynomial([])

   Polynomial.field = field
   Polynomial.__name__ = '(%s)[x]' % field.__name__
   return Polynomial
