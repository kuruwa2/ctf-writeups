import requests
import time
import json
import os
import random
import string

GUESS = 1
INITIAL = 0

printable = list(string.printable[:-5].encode()) #0
chinese1, chinese2 = [i for i in range(0x80, 0xc0)], [i for i in range(0xe0, 0xf0)] #1,2
emoji = [i for i in range(0xf0, 0xf8)] #3
other = [i for i in range(0,32)] + [127] + [i for i in range(0xc0, 0xe0)] + [i for i in range(0xf8, 256)] #4

everything = [printable, chinese1, chinese2, emoji, other, [ord('{')], [ord('F'), ord('f')], [ord('T'), ord('t'), ord('7')], [ord('G'), ord('g')], [0], [ord('}')]]

def xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

#url = "https://a79233092e1d.ngrok.io"
#url = "http://127.0.0.1:11337"
url = "http://35.201.246.182:11337"
for i in range(1):
    r = requests.get(url+"/status").content

    j = json.loads(r)
    flag = bytes.fromhex(j['flag'])
    print(len(flag))
    BLOCK = INITIAL
    MAX_BLOCK = len(flag)//16 - 2 if not GUESS else BLOCK
    done = b''
    now = 16*BLOCK+16

    dicks = [0,1,2,3,4]
    chinese1 = 0
    trial = 0
    while BLOCK <= MAX_BLOCK:
        ok = b''
        iv = flag[16*BLOCK:16*BLOCK+16]
        #print(iv)
        for j in range(16):
            #used = []
            if BLOCK == 0 and j == 12 and b'{' not in ok:
                dicks = [5] + dicks
            elif BLOCK == 0 and j == 13 and ok[0] == ord('{'):
                dicks = [6] + dicks
            elif BLOCK == 0 and j == 14 and ok[0] in everything[6]:
                dicks = [7] + dicks
            elif BLOCK == 0 and j == 15 and ok[0] in everything[7]:
                dicks = [8] + dicks
            if BLOCK == MAX_BLOCK:
                if len(ok)==0 or ok[0] == 0:
                    dicks = [9,10] + dicks
            while True:
                ch = dicks[0]
                options = everything[dicks[0]].copy()
                dicks = dicks[1:]
                random.shuffle(options)
                found = False
                for i in options:
                    add = bytes([i ^ iv[15-j]])
                    #used.append(add)
                    payload = '00'*(15-j)+add.hex()+xor(ok, iv[16-j:]).hex()+flag[16*BLOCK+16:16*BLOCK+32].hex()
                    #print(payload)
                    r = requests.get(url+"/compress", {'x':payload}).content
                    trial += 1
                    ctlen = int.from_bytes(r[22:26], 'little')
                    #print(chr(i),ctlen)
                    if ctlen<16-j:
                        ok = bytes([ord(add)^iv[15-j]]) + ok
                        found = True
                        break
                if found:
                    if ch == 0:
                        chinese1 = 0
                        dicks = [0,1,2,3,4]
                    elif ch == 1:
                        chinese1 += 1
                        if chinese1 == 2:
                            dicks = [2,3,1,0,4]
                        elif chinese1 == 3:
                            dicks = [3,0,1,2,4]
                        else:
                            dicks = [1,2,3,0,4]
                    elif ch == 2:
                        chinese1 = 0
                        dicks = [1,0,2,3,4]
                    else:
                        chinese1 = 0
                        dicks = [0,1,2,3,4]
                    break
                        
            print(ok)
            #time.sleep(1)
        now += 16
        done += ok
        print(done, trial)
        BLOCK+=1

    if not GUESS:
        done = done.strip(b'\x00')
        print(done.decode('utf-8'))
        print(trial)
        print(trial/(len(flag)-16))
        r = requests.get(url+"/submit", {'x':done.decode('utf-8')}).content
        print(r)
