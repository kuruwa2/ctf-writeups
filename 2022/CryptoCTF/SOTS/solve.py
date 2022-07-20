#!/usr/bin/env sage

from sage.all import *
import telnetlib
from Crypto.Util.number import *

HOST = "05.cr.yp.toc.tf"
PORT = 37331
tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b'\n')

tn.read_until(b'uit\n')
tn.write(b'G\n')
n = int(readline().split()[-1])
x, y = two_squares(n)
print(x, y)

tn.read_until(b'uit\n')
tn.write(b'S\n')
readline()
tn.write((str(x) + ', ' + str(y) + '\n').encode())

print(readline())
#CCTF{3Xpr3sS_4z_Th3_sUm_oF_7w0_Squ4rE5!}
