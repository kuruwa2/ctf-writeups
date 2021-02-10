#!/usr/bin/python3

import string

flag = open("flag.txt", 'rb').read().decode()
printable = string.printable[:-7]
index = {}
for i in range(len(printable)):
    index[printable[i]] = i

enc = ''
for i in range(len(flag)//2):
    enc += printable[(1*index[flag[2*i]] + 2*index[flag[2*i+1]]) % len(printable)]
    enc += printable[(3*index[flag[2*i]] + 4*index[flag[2*i+1]]) % len(printable)]

print('enc:', enc)
