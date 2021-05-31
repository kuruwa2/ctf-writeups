from hashlib import sha256
import string
flag = 'AIS3{THIS_IS_A_FAKE_FLAG}'

cand = string.ascii_letters + string.digits + '_{}'
charset = string.printable[:93]

enc = ''
for c in flag:
	assert(c in cand)
	enc  += charset[int(sha256(c.encode()).hexdigest(), 16) % len(charset)]

print(enc)
