#!/usr/bin/env python3

import requests
import json

enc = 'IISNJ IFFAA TYPMO WDJHA ZMNBD LKUAY TYPVD UGAYU OQMOO YRVUS SLFZI IXKVW LYUGT JWTYV XNEYU HLQVV IXUMJ BKNUQ WMLQT QKIWV UXOCA CVSPG UKJQG XCSFI RJEKU BWLBM AVRFW DMOPT VFXTD VROND XSEHF ZLWEJ VOVSX IISNJ IFFAA'
enc = ''.join(enc.split())

flag = [0] * (len(enc)-10)
for i in range(65, 65+26):
    x = requests.post('http://03.cr.yp.toc.tf:11117/m209/encipher', data = {'plain': chr(i) * (len(enc)-10)})
    cipher = json.loads(x.text)['cipher']
    cipher = ''.join(cipher.split())
    for j in range(len(enc)-10):
        if cipher[10+j] == enc[10+j]:
            flag[j] = chr(i)
    #print(flag)

print(''.join(flag))

#YOUZKNOWZHOWZTOZFORMATZFLAGZJUSTZPUTZUPCOMINGZLETTERSZWITHINZCURLYZBRACESZFOLLOWEDZBYZCCTFZOOJMPMDDIXCLNNWFTEJUMFXKBRVVMOPSLSSLUTXVDVNDMYYPHPWFJRNJBVBOMUYRDUMOZOMGGH
#CCTF{OOJMPMDDIXCLNNWFTEJUMFXKBRVVMOPSLSSLUTXVDVNDMYYPHPWFJRNJBVBOMUYRDUMOZOMGGH}
