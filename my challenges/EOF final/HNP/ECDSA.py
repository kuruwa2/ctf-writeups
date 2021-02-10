from EC import *

class Public_key(object):

    def __init__(self, generator, point, verify=True):

        self.curve = generator.curve
        self.generator = generator
        self.point = point

    def verifies(self, hash, r, s):

        G = self.generator
        n = G.order
        if r < 1 or r > n - 1:
            return False
        if s < 1 or s > n - 1:
            return False
        c = inverse(s, n)
        u1 = (hash * c) % n
        u2 = (r * c) % n
        xy = u1 * G + u2 * self.point
        v = xy.x % n
        return v==r

class Private_key(object):

    def __init__(self, public_key, secret_multiplier):

        self.public_key = public_key
        self.secret_multiplier = secret_multiplier

    def sign(self, hash, random_k):

        G = self.public_key.generator
        n = G.order
        k = random_k % n
        p1 = k * G
        r = p1.x % n
        s = inverse(k, n) * (hash + (self.secret_multiplier * r) % n) % n

        return r, s
