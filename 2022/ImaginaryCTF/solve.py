from randcrack import RandCrack
rc = RandCrack()

f = open("./poker.py", 'rb').read()
cards = {}
for i in range(13):
    cards[f[f.index(b'SPADES')+10+4*i: f.index(b'SPADES')+14+4*i]] = i
    cards[f[f.index(b'HEARTS')+10+4*i: f.index(b'HEARTS')+14+4*i]] = 13+i
    cards[f[f.index(b'DIAMONDS')+12+4*i: f.index(b'DIAMONDS')+16+4*i]] = 26+i
    cards[f[f.index(b'CLUBS')+9+4*i: f.index(b'CLUBS')+13+4*i]] = 39+i
sorted(cards)

def deal_card(shuffle):
    deal = []
    deck = [i for i in range(52)]
    while shuffle > 0:
        deal.append(deck.pop(shuffle % len(deck)))
        shuffle //= len(deck) + 1
    while len(deal) < 25:
        deal += [deck.pop(0)]
    return deal

MD = 7407396657496428903767538970656768000000
g = open("./cards.22.07.16.txt", 'rb').read()
rands = []
for i in range(750):
    deck = [i for i in range(52)]
    rand = 0
    deals = []
    for j in range(25):
        card = cards[g[g.index(b'\xf0'):g.index(b'\xf0')+4]]
        deals += [card]
        deck.remove(card)
        g = g[g.index(b'\xf0')+4:]
    for j in range(25):
        rand *= len(deck) + 1
        count = 0
        deal = deals[24-j]
        if deal > deck[-1]:
            count = len(deck)
        else:
            for count in range(len(deck)):
                if deck[count] > deal:
                    break
        deck.insert(count, deal)
        rand += count
    #assert deal_card(rand) == deals
    if rand + MD >= 2 ** 133:
        for j in range(4):
            rands.append([rand%2**32])
            rand >>= 32
        rands += [0]
    else:
        rand2 = rand + MD
        for j in range(4):
            rands.append([rand%2**32, rand2%2**32])
            rand >>= 32
            rand2 >>= 32
        rands += [0]
        
state = []
for i in range(624):
    if rands[i] == 0:
        state += [0]
    else:
        state += [[]]
        for j in rands[i]:
            state[-1] += [rc._to_int(rc._harden_inverse(rc._to_bitarray(j)))]
rands = rands[624:]
while True:
    #print(rands[0], state[0], state[1], state[397])
    if rands[0] == 0 and (state[0] == 0 or state[1] == 0 or state[397] == 0):
        state = state[1:] + [0]
    else:
        nx1, nx2 = 0, 0
        if rands[0] != 0:
            nx1 = [rc._to_int(rc._harden_inverse(rc._to_bitarray(i))) for i in rands[0]]
        if state[0] != 0 and state[1] != 0 and state[397] != 0:
            nx2 = []
            for i in state[0]:
                for j in state[1]:
                    for k in state[397]:
                        y = (i & 0x80000000) | (j & 0x7fffffff)
                        x = k ^ (y >> 1)
                        if y & 1:
                            x ^= 0x9908b0df
                        nx2 += [x]
        if nx1 and nx2:
            pos = list(set(nx1).intersection(set(nx2)))
            assert len(pos) > 0
            state = state[1:] + [pos]
        elif nx1:
            state = state[1:] + [nx1]
        elif nx2:
            state = state[1:] + [nx2]
    rands.pop(0)
    ans = True
    for i in state:
        if i==0 or len(i)>1:
            ans=False
            break
    if ans:
        break

state = [i[0] for i in state]
for i in range(624):
    rc.submit(rc._to_int(rc._harden(rc._to_bitarray(state[i]))))

for i in range(len(rands)):
    rand = rc.predict_getrandbits(32)
    if rands[i] != 0:
        assert rand in rands[i]

ALPHABET52 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop_rstuvw{y}"

deal = deal_card(rc.predict_getrandbits(133) % MD)
for i in deal:
    print(ALPHABET52[i], end='')
deal = deal_card(rc.predict_getrandbits(133) % MD)
for i in deal:
    print(ALPHABET52[i], end='')
