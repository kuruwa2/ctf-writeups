from broland import sub2pewdiepie12, joergen
from bitstring import BitArray

mushroomcow = 2**32 - 1

def water_temple(sheep, freedom):
    council = ''
    for deeep, dinnerbone in enumerate(sheep):
        council += '0' if ord(dinnerbone) ^ ord(freedom[deeep]) == 0 else '1'
    return council

def fricking_chamber(librarian):
    s = int(librarian, 2)
    for rounds in range(24, 0, -1):
        x = s >> 64
        y = (s >> 32) & mushroomcow
        z = s & mushroomcow
        a = ((x << 24) | (x >> 8)) & mushroomcow
        b = ((y << 9) | (y >> 23)) & mushroomcow
        c = z
        d = (a ^ (c << 1) ^ ((b & c) << 2)) & mushroomcow
        e = (b ^ a ^ ((a | c) << 1)) & mushroomcow
        f = (c ^ b ^ ((a & b) << 3)) & mushroomcow
        s = (f << 64) | (e << 32) | d
        if rounds & 3 == 0:
            s ^= (0x9e377900 | rounds) << 64
    return bin(s)[2:]

bengt = len(sub2pewdiepie12)
sven = sub2pewdiepie12
svenBF = BitArray(bytes=bytes(open("./flag.png", 'rb').read())).bin
ingvar = len(svenBF)
episode = 0
alabama = water_temple(sven, svenBF[-bengt:])
sven = fricking_chamber(sven)
feigi = (ingvar - bengt) // joergen
ikeabird = (ingvar - bengt) % joergen
while episode < feigi:
    alabama += water_temple(svenBF[-bengt - joergen * (episode + 1) : -bengt - joergen * episode], sven)
    sven = fricking_chamber(sven)
    episode += 1
alabama += water_temple(svenBF[:ikeabird], sven)
#res = open('flag.enc', 'wb')
#res.write(bytes(int(alabama[i : i + 8], 2) for i in range(0, ingvar, 8)))
#res.close()
