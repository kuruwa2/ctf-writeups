from pwn import *
from mt19937predictor import MT19937Predictor

r = remote("misc.hsctf.com", 9988)
r.recvuntil("answers:\n")
ch = {"B":0, "C":1, "D":2, "G":3, "P":4, "T":5, "V":6, "Z": 7}
orde = "BCDGPTVZ"
predictor = MT19937Predictor()
for _ in range(208):
    q=r.recvline()
    v1 = ch[q[18]]+    (ch[q[24]]<<3)+(ch[q[5]]<<6)+ (ch[q[1]]<<9)+(ch[q[28]]<<12)+(ch[q[26]]<<15)+(ch[q[25]]<<18)+( ch[q[4]]<<21)+(ch[q[20]]<<24)+ (ch[q[7]]<<27)+(ch[q[31]]<<30)
    v2 = (ch[q[31]]&1)+(ch[q[16]]<<1)+(ch[q[8]]<<4)+(ch[q[29]]<<7)+(ch[q[10]]<<10)+ (ch[q[9]]<<13)+(ch[q[23]]<<16)+(ch[q[19]]<<19)+(ch[q[12]]<<22)+(ch[q[22]]<<25)+(ch[q[14]]<<28)+((ch[q[0]]&1)<<31)
    v3 = ch[q[0]]+     (ch[q[27]]<<2)+(ch[q[2]]<<5)+ (ch[q[3]]<<8)+(ch[q[21]]<<11)+(ch[q[30]]<<14)+(ch[q[17]]<<17)+(ch[q[15]]<<20)+(ch[q[13]]<<23)+(ch[q[11]]<<26)+ (ch[q[6]]<<29)
    predictor.setrandbits(v1,32)
    predictor.setrandbits(v2,32)
    predictor.setrandbits(v3,32)
for _ in range(8):
    q=r.recvline()
    v1=predictor.getrandbits(32)
    v2=predictor.getrandbits(32)
    v3=predictor.getrandbits(32)
    print(q[:-1])
    pred = orde[v2 >> 0x1F & 0x1 | v3 >> 0x0 & 0x3]+orde[v1 >> 0x09 & 0x7]+orde[v3 >> 0x05 & 0x7]+orde[v3 >> 0x08 & 0x7]+orde[v1 >> 0x15 & 0x7]+orde[v1 >> 0x06 & 0x7]+orde[v3 >> 0x1D & 0x7]+orde[v1 >> 0x1B & 0x7]+orde[v2 >> 0x04 & 0x7]+orde[v2 >> 0x0D & 0x7]+orde[v2 >> 0x0A & 0x7]+orde[v3 >> 0x1A & 0x7]+orde[v2 >> 0x16 & 0x7]+orde[v3 >> 0x17 & 0x7]+orde[v2 >> 0x1C & 0x7]+orde[v3 >> 0x14 & 0x7]+orde[v2 >> 0x01 & 0x7]+orde[v3 >> 0x11 & 0x7]+orde[v1 >> 0x00 & 0x7]+orde[v2 >> 0x13 & 0x7]+orde[v1 >> 0x18 & 0x7]+orde[v3 >> 0x0B & 0x7]+orde[v2 >> 0x19 & 0x7]+orde[v2 >> 0x10 & 0x7]+orde[v1 >> 0x03 & 0x7]+orde[v1 >> 0x12 & 0x7]+orde[v1 >> 0x0F & 0x7]+orde[v3 >> 0x02 & 0x7]+orde[v1 >> 0x0C & 0x7]+orde[v2 >> 0x07 & 0x7]+orde[v3 >> 0x0E & 0x7]+orde[v1 >> 0x1E & 0x3 | v2 >> 0x00 & 0x1]
    print(pred)
q = r.recvline()
print(q)
v1=predictor.getrandbits(32)
v2=predictor.getrandbits(32)
v3=predictor.getrandbits(32)
pred = orde[v1 >> 0x1E & 0x3 | v2 >> 0x00 & 0x1]+orde[v1 >> 0x09 & 0x7]+orde[v3 >> 0x05 & 0x7]+orde[v3 >> 0x08 & 0x7]+orde[v1 >> 0x15 & 0x7]+orde[v1 >> 0x06 & 0x7]+orde[v3 >> 0x1D & 0x7]+orde[v1 >> 0x1B & 0x7]+orde[v2 >> 0x04 & 0x7]+orde[v2 >> 0x0D & 0x7]+orde[v2 >> 0x0A & 0x7]+orde[v2 >> 0x16 & 0x7]+orde[v3 >> 0x1A & 0x7]+orde[v3 >> 0x17 & 0x7]+orde[v2 >> 0x1C & 0x7]+orde[v3 >> 0x14 & 0x7]+orde[v2 >> 0x01 & 0x7]+orde[v1 >> 0x00 & 0x7]+orde[v3 >> 0x11 & 0x7]+orde[v2 >> 0x13 & 0x7]+orde[v1 >> 0x18 & 0x7]+orde[v3 >> 0x0B & 0x7]+orde[v2 >> 0x19 & 0x7]+orde[v2 >> 0x10 & 0x7]+orde[v1 >> 0x03 & 0x7]+orde[v1 >> 0x12 & 0x7]+orde[v1 >> 0x0F & 0x7]+orde[v1 >> 0x0C & 0x7]+orde[v2 >> 0x07 & 0x7]+orde[v3 >> 0x0E & 0x7]+orde[v2 >> 0x1F & 0x1 | v3 >> 0x0 & 0x3]

for i in pred:
    r.sendline(i)
r.interactive()	
