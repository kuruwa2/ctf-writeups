#!/usr/bin/env python3

import telnetlib
from Crypto.Util.number import *

tn = telnetlib.Telnet('06.cr.yp.toc.tf', 31117)

tn.read_until(b'uit\n')
tn.write(b'A\n')
tn.read_until(b'\n')
tn.write(b'0,0\n')

tn.read_until(b'uit\n')
tn.write(b'S\n')
tn.read_until(b'\n')
tn.write(b"\x004lL crypt0sy5t3ms suck5 fr0m faul7 atTaCk5 :P\n")
tn.read_until(b'sign = ')
sgn = eval(tn.read_until(b'\n'))

tn.read_until(b'uit\n')
tn.write(b'V\n')
tn.read_until(b'\n')
tn.write((str(sgn[0]) + ', ' + str(sgn[1]) + '\n').encode())
print(tn.read_all())
#CCTF{n3W_4t7aCk_8y_fAuL7_!nJ3cT10N_oN_p!!!}
