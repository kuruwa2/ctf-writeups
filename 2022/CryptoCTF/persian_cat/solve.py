#!/usr/bin/env python3

import telnetlib
from persian_cat import *

'''tn = telnetlib.Telnet('07.cr.yp.toc.tf', 11173)
tn.read_until(b'uit\n')
tn.write(b'E\n')
tn.read_until(b'\n')
tn.write(b'\x00'*32 + b'\n')
enc = bytes.fromhex(tn.read_until(b'\n').decode().split()[-1])'''

enc = b"h\x93\xe5\xcf^n\xf8\x1f\x99\x05{(SO\x0b|\x91\x80U\x13\x7f\xe13\xe8=\xa0\xa0z\x7f\xed\xad\x0bX\xdah\xad\xbc\x03\x95\xec>U\x93\x12\x84+`2\xd9J\x8f\xf6M\xa3\x86h>f\xfc\xf6\xf0\x86\x8a\x18\xcd\xe1\xd0m\\GbV^q*\xbc\xdeb\xc0\x83\x06\xab*\xd3\xcd\x0b\xa2'\x004y\xa5\x12\x7f\xb0\xfc\xc0c\x01F\xfc\x8d HR\xc6k#\xf4\x02\xbf\x07\xfan\xcb\x15xs\xc3D\x99\x97\xb8U\x95\xc9\xb1\x9d"

def circle_it_in(enc, ruler, roadrunner_wile, lili, lilibeth, dec, l, r, omega):
    for i in range(16):
        r[0][i] = enc[i]
        l[0][i] = enc[i+16]
    for i in range(1, ruler):
        roadrunner_wile = roadrunner(l[i-1], roadrunner_wile, lili, lilibeth, omega)
        for y in range(16):
            r[i][y] = l[i-1][y]
            l[i][y] = (r[i-1][y] ^ roadrunner_wile[y])%256
    for i in range(16):
        dec[i+16] = r[ruler-1][i]%256
        dec[i] = l[ruler-1][i]%256
    return roadrunner_wile, dec, l, r

def decrypt_iginition(enc, key):
    roadrunner_wile = [0 for x in range(16)]
    lili = [[0 for x in range(16)] for y in range(256)]
    lilibeth, omega = [[0 for x in range(256)] for _ in '01']
    dec = [0 for x in range(32)]
    l, r = [[[0 for x in range(16)] for y in range(32)] for _ in '01']
    roadrunner_wile, lili, lilibeth, dec, l, r, omega = persian_init(key, roadrunner_wile, lili, lilibeth, dec, l, r, omega, Omega)
    roadrunner_wile, dec, l, r = circle_it_in(enc, 6, roadrunner_wile, lili, lilibeth, dec, l, r, omega)
    return dec

def decrypt(enc):
    blocks = [enc[i*32:i*32+32] for i in range(len(enc) // 32)]
    msg = [[0]*32]
    flag = b''
    for i in range(len(blocks)-1):
        dec = decrypt_iginition(list(blocks[i+1]), keygen(list(blocks[i]), msg[i]))
        msg.append(dec)
        flag += bytes(dec)
    return flag

print(decrypt(enc))
#CCTF{d0_yOu_tH47_the_ori9iN_of_Iraqi_C1ph3r_Iz_Iran?!!}
