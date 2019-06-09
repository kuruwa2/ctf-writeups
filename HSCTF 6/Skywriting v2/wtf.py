import base64

a = base64.b64decode('LjUlMiA9LxI1GTUTNiodECAtUSx5YxY4')
print(a)

b = ''
xor = a[0] ^ ord('h')
for i in range(24):
    b += chr(a[i] ^ xor)
print(b)

c = ''
xor = ord(b[13]) ^ ord('e')
for i in range(24):
    if i < 13:
        c += b[i]
    else:
        c += chr(ord(b[i]) ^ xor)
print(c)

d = ''
xor = ord(c[-1]) ^ ord('}')
for i in range(24):
    if i < 22:
        d += c[i]
    else:
        d += chr(ord(c[i]) ^ xor)
print(d)

e = ''
xor = ord(d[-3]) ^ ord('u')
for i in range(24):
    if i < 18:
        e += d[i]
    elif i < 22:
        e += chr(ord(d[i]) ^ xor)
    else:
        e += d[i]
print(e)
