from sage.all import *
import string, base64

ALPHABET = string.printable[:62] + '\\='
F = list(GF(64))

enc = '805c9GMYuD5RefTmabUNfS9N9YrkwbAbdZE0df91uCEytcoy9FDSbZ8Ay8jj'
pkey = F[ALPHABET.index(enc[-1])]*F[ALPHABET.index('=')]**-1
flag = ''
for i in enc:
    flag += ALPHABET[F.index(pkey**-1*F[ALPHABET.index(i)])]

flag = base64.b64decode(flag)
print(flag)

#CCTF{EnCrYp7I0n_4nD_5u8STitUtIn9_iN_Fi3Ld!}
