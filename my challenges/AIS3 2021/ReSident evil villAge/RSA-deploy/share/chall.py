#!/bin/python3
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from binascii import unhexlify

privkey = RSA.generate(1024)

n = privkey.n
e = privkey.e

print('Welcome to ReSident evil villAge, sign the name "Ethan Winters" to get the flag.')
print('n =', n)
print('e =', e)

while True:
        print('''1) sign
2) verify
3) exit''')
        option = input()
        if option == '1':
                msg = unhexlify(input('Name (in hex): '))
                if msg == b'Ethan Winters' or bytes_to_long(msg) >= n:
                        print('Nice try!')
                else:
                        sig = pow(bytes_to_long(msg), privkey.d, n)
                        print('Signature:', sig)

        elif option == '2':
                sig = int(input('Signature: '))
                verified = (pow(sig, e, n) == bytes_to_long(b'Ethan Winters'))
                if verified:
                    print('AIS3{R3M383R_70_HAsh_7h3_M3Ssa93_83F0r3_S19N1N9}')
                else:
                        print('Well done!')

        else:
                break
