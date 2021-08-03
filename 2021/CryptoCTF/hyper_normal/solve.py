from Crypto.Util.number import *
import numpy as np

p = 8443
enc = np.array(eval(open("./output.txt").read()))
l = len(enc)

flag = ''
for i, j in enumerate(enc.transpose()):
    for k in range(32, 127):
        if (j*inverse((i+1)*k, p)%p <= 126).all():
            flag += chr(k)
            break

print(flag)
#CCTF{H0w_f1Nd_th3_4lL_3I9EnV4Lu35_iN_FiN173_Fi3lD5!???}
