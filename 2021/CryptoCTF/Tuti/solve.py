from Crypto.Util.number import *
import itertools

def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

fac = [2, 2, 3, 11, 11, 19, 47, 71, 3449, 11953, 5485619, 2035395403834744453, 17258104558019725087, 1357459302115148222329561139218955500171643099]
k = 992752253935874779143952218845275961347009322164731344882417010624071055636710540798045985678351986133612

flag = b''
for r in range(len(fac)+1):
    for f in itertools.combinations(fac, r):
        x = 1
        for p in f:
            x *= p
        if b'CCTF' in long_to_bytes(x-1):
            y = k//x
            flag = long_to_bytes(x-1) + long_to_bytes(y+1)
            print(flag)
            break
    if flag:
        break

#CCTF{S1mPL3_4Nd_N!cE_Diophantine_EqUa7I0nS!}
