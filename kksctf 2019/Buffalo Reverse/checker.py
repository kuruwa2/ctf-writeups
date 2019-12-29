crypto = [2,9,0,3,25,28,0x55,19,0x3b,7,19,17,22,0,0x3a,11,1,24]

key = [2^ord('f'), 24^ord('}'), ord('a'), 3^ord('g'), 22^ord('t'), ord('e'), 0x55^ord('0'), 19^ord('u')]

'''for i in range(90,110):
    for j in range(90,110):
        key[6] = i
        key[7] = j
        for k, c in enumerate(crypto):
            print(chr(c^key[k%8]), end='')
        print('')'''
for k, c in enumerate(crypto):
    print(chr(c^key[k%8]), end='')
