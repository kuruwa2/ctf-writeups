from Crypto.Cipher import AES

def xor(a,b):
    return bytes(i^j for i,j in zip(a,b))

enc = bytes.fromhex('ebe08dbac76a294842dca51aa283c11a1242d271fcb9528307e4e6474ed0b091')
key = bytes.fromhex('e812644b54302cbf5e6ac814917f')
pt  = b'0'*32
ct1 = '5b58************************32d7'
ct2 = bytes.fromhex('d03a0a6116f0129f762036e3f274b233')

for i in range(65536):
    pos = key + bytes([i//256]) + bytes([i%256])
    cipher = AES.new(pos, AES.MODE_ECB)
    c = xor(cipher.decrypt(ct2), pt[16:])
    if c[:2] == b'\x5b\x58' and c[-2:] == b'\x32\xd7':
        iv = xor(cipher.decrypt(c), pt[:16])
        break

cipher = AES.new(pos, AES.MODE_CBC, iv)
print(cipher.decrypt(enc))

#CCTF{h0W_R3cOVER_7He_5eCrET_1V?}
