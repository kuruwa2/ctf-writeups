#!/bin/python3
import random
from Crypto.Util.number import *
from hashlib import sha1, sha256
from EC import EC, Point
from ECDSA import Public_key, Private_key
from random import randint

p = 0xd34add77b5ce24599a94b5b0deb76d194c70b02e01a0b12560983764b22d2495
a = 0x91b133a4846a47c0f289dc1e1cccda757e96849611b73f93b9ced280e4ec59f0
b = 0x5289ef4348d33790bf73b4b7b10f8476224a6c26f7b914854203f9e89f602d9c
E = EC(p, a, b)
G = Point(E, 0x684aeb01fa41bd03bfe56b74705fb9af70115b64fedf7dbe1ab04f66293bcfd1, 0x41f9035541e931c807c2da8355969a2f018ab9ee149c39de2c6bc20850e90c48, 0xd34add77b5ce24599a94b5b0deb76d186441dc4220c5aabced7be2355c992e8b)
       
print('''
                                                                                                                                        _____                           
       __     __           _____                    _____       __     __               _____  ___________          _____         ____  \    \   ________    ________   
      /  \   /  \        /      |_             _____\    \     /  \   /  \         _____\    \_\          \       /      |_       \   \ /____/| /        \  /        \  
     /   /| |\   \      /         \           /    / \    |   /   /| |\   \       /     /|     |\    /\    \     /         \       |  |/_____|/|\         \/         /| 
    /   //   \\   \    |     /\    \         |    |  /___/|  /   //   \\   \     /     / /____/| |   \_\    |   |     /\    \      |  |    ___ | \            /\____/ | 
   /    \_____/    \   |    |  |    \     ____\    \ |   || /    \_____/    \   |     | |____|/  |      ___/    |    |  |    \     |   \__/   \|  \______/\   \     | | 
  /    /\_____/\    \  |     \/      \   /    /\    \|___|//    /\_____/\    \  |     |  _____   |      \  ____ |     \/      \   /      /\___/|\ |      | \   \____|/  
 /    //\_____/\\    \ |\      /\     \ |    |/ \    \    /    //\_____/\\    \ |\     \|\    \ /     /\ \/    \|\      /\     \ /      /| | | | \|______|  \   \       
/____/ |       | \____\| \_____\ \_____\|\____\ /____/|  /____/ |       | \____\| \_____\|    |/_____/ |\______|| \_____\ \_____\|_____| /\|_|/           \  \___\      
|    | |       | |    || |     | |     || |   ||    | |  |    | |       | |    || |     /____/||     | | |     || |     | |     ||     |/                  \ |   |      
|____|/         \|____| \|_____|\|_____| \|___||____|/   |____|/         \|____| \|_____|    |||_____|/ \|_____| \|_____|\|_____||_____|                    \|___|
''')

try:
    d = randint(1, G.order)
    pubkey = Public_key(G, d*G)
    privkey = Private_key(pubkey, d)
    while True:
        print('''
1) talk to Kuruwa
2) login
3) exit''')
        option = input()
        if option == '1':
            msg = input('Who are you?\n')
            if msg == 'Kuruwa':
                print('No you are not (╯‵□′)╯︵┴─┴')
            else:
                h = sha256(msg.encode()).digest()
                if randint(0, 1):
                    k = sha1(long_to_bytes(privkey.secret_multiplier) + h).digest()
                else:
                    k = sha256(long_to_bytes(privkey.secret_multiplier) + h).digest()
                r, s = privkey.sign(bytes_to_long(h), bytes_to_long(k))
                print(f'({r}, {s})')

        elif option == '2':
            msg = input('username: ')
            r = input('r: ')
            s = input('s: ')
            h = bytes_to_long(sha256(msg.encode()).digest())
            verified = pubkey.verifies(h, int(r), int(s))
            if verified:
                if msg == 'Kuruwa':
                    print('AIS3{hayaki_koto_Shimakaze_no_gotoshi_desu}')
                elif msg == 'Shimakaze\'s husband':
                    print('259303 192816')
                else:
                    print('Bad username')
            else:
                print('Bad signature')
        else:
            break
except:
    print('??????')
    exit(-1)
