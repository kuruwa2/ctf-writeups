#!/usr/bin/env python3

import telnetlib
from Crypto.Util.number import *

HOST = "02.cr.yp.toc.tf"
PORT = 17113
tn = telnetlib.Telnet(HOST, PORT)

for i in range(19):
    tn.read_until(b'it: \n')
    tn.write(((str(1<<58+2*i) + ', ') * 2 + str(1<<29+i) + '\n').encode())

print(tn.read_all())
#CCTF{4_diOpH4nT1nE_3Qua7i0n__8Y__Jekuthiel_Ginsbur!!}
