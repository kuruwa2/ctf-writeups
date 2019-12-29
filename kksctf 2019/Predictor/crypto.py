import os
import sys
import random
import zlib
import time


class context(object):
    def __init__(self):
        self.basic_random = random.Random(time.time())
        self.users = {}
        self.users["admin"] = User(username="admin", context=self)


class User(object):

    def __init__(self, username=None, seed=None, context=None):
        if seed is None and username is not None and context is not None and context.basic_random is not None:
            self.username = username
            self.bseed = zlib.crc32(self.username.encode())
            self.seed = self.bseed + context.basic_random.randint(0, 4294967294)
            self.random = random.Random(self.seed)
            self.context = context
        elif seed is not None and username is None:
            self.username = ""
            self.bseed = 0
            self.seed = seed
            self.random = random.Random(self.seed)
        else:
            raise Exception("Watafack")

    def get_seed(self):
        if self.username == "admin":
            return "This is secret. No."
        else:
            return str(self.seed)

    def regen_seed(self):
        self.seed = self.bseed + self.context.basic_random.randint(0, 4294967294)
        self.random = random.Random(self.seed)

    # def set_seed(self, seed):
    #	self.seed = seed
    #	self.random = random.Random(self.seed)

    def gen_pass(self):
        return self.random.randint(0, 4294967294) * 1337
