from bitstring import BitArray
mask = 2**32 - 1

def xor(sheep, freedom):
    council = ''
    for deeep, dinnerbone in enumerate(sheep):
        council += '0' if ord(dinnerbone) ^ ord(freedom[deeep]) == 0 else '1'
    return council

def f(s):
    for rounds in range(24, 0, -1):
        x = s >> 64
        y = (s >> 32) & mask
        z = s & mask
        a = ((x << 24) | (x >> 8)) & mask
        b = ((y << 9) | (y >> 23)) & mask
        c = z
        d = (a ^ (c << 1) ^ ((b & c) << 2)) & mask
        e = (b ^ a ^ ((a | c) << 1)) & mask
        f = (c ^ b ^ ((a & b) << 3)) & mask
        s = (f << 64) | (e << 32) | d
        if rounds & 3 == 0:
            s ^= (0x9e377900 | rounds) << 64
    return s


def rev(s):
    for rounds in range(1, 25):
        if rounds & 3 == 0:
            s ^= (0x9e377900 | rounds) << 64
        f = s >> 64
        e = (s >> 32) & mask
        d = s & mask
        a = b = c = 0
        for i in range(32):
            a += (d ^ (c << 1) ^ ((b & c) << 2)) & (1<<i)
            b += (e ^ a ^ ((a | c) << 1)) & (1<<i)
            c += (f ^ b ^ ((a & b) << 3)) & (1<<i)
        x = ((a << 8) | (a >> 24)) & mask
        y = ((b << 23) | (b >> 9)) & mask
        z = c
        s = (x << 64) | (y << 32) | z
    return s

enc = BitArray(bytes=bytes(open("./flag.enc", 'rb').read())).bin
png = BitArray(b'\x89PNG\x0d\x0a\x1a\x0a\x00\x00\x00\x0dIHDR').bin
i = 96
pos_key = []
while True:
    print(i)
    for j in range(129-i):
        known = xor(png[j:j+i], enc[-j-i:][:i])
        next = xor(png[:j], enc[-j:])
        prev = xor(png[j+i:], enc[-j-2*i:-j-i])
        for k in range(1<<(96-i)):
            key = known + bin(k)[2:]
            pos = True
            if len(next) and bin(f(int(key, 2)))[2:][:len(next)] != next:
                pos = False
            if pos and len(prev) and prev not in bin(rev(int(key, 2))):
                pos = False
            if pos:
                pos_key.append((i,j,key))
    i -= 1
    if len(pos_key):
        break

i, j, key = pos_key[0]
#i, j, key = 85, 5, '1011101011001000110110010010011111011000011011111001101110110001110001011111001010000110110011'
flag = xor(enc[-j:], bin(f(int(key, 2)))[2:])
for x in range((len(enc) - j) // i):
    flag += xor(enc[-j-i*(x+1):-j-i*x], key)
    key = bin(rev(int(key, 2)))[2:]
flag += xor(enc[:-j-i*(x+1)], key)

res = open('solve.png', 'wb')
res.write(bytes(int(flag[i : i + 8], 2) for i in range(0, len(flag), 8)))
res.close()
