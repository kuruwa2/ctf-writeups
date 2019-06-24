from pwn import *
context.arch = "x86_64"

host= "pwn.hsctf.com"
port= 2345
# r = process('./combo-chain')
r = remote(host, port)

