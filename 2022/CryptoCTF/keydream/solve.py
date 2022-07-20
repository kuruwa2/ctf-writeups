#!/usr/bin/env python3

from Crypto.Util.number import *
import string

n = 23087202318856030774680571525957068827041569782431397956837104908189620961469336659300387982516148407611623358654041246574100274275974799587138270853364165853708786079644741407579091918180874935364024818882648063256767259283714592098555858095373381673229188828791636142379379969143042636324982275996627729079
c = 3621516728616736303019716820373078604485184090642291670706733720518953475684497936351864366709813094154736213978864841551795776449242009307288704109630747654430068522939150168228783644831299534766861590666590062361030323441362406214182358585821009335369275098938212859113101297279381840308568293108965668609

pos = list(map(ord, string.printable[:62] + '_'))
p0 = bytes_to_long(b'CCTF{it_is_fake_flag_') << 344
q0 = bytes_to_long(b'CCTF{it_is_fake_flag_'[::-1])

p1 = n * inverse(q0, 2**168) % 2**168
q0 += bytes_to_long(long_to_bytes(p1)[::-1]) << 344
p0 += p1

ps = [(p0, q0)]
for i in range(11):
    psn = []
    ind = 8 * (21 + i)
    dni = 8 * (42 - i)
    while len(ps):
        p0, q0 = ps.pop()
        for j in pos:
            pn = p0 + (j << ind)
            qn = n * inverse(pn, 2**(ind + 8)) % 2**(ind + 8)
            k = long_to_bytes(qn)[0]
            if k in pos:
                pn += k << dni
                qn = q0 + (k << ind) + (j << dni)
                if pn * qn <= n and (pn + (1 << dni)) * (qn + (1 << dni)) >= n:
                    psn.append((pn, qn))
    ps = psn

p, q = ps[0]
#print(long_to_bytes(p))
print(long_to_bytes(pow(c, inverse(65537, (p-1)*(q-1)), n)))
#CCTF{h0M3_m4dE_k3Y_Dr1vEn_CrYp7O_5ySTeM!}
