import numpy as np

heck = "001002939948347799120432047441372907443274204020958757273"
cs=""
ans="ffc8ffbdffceffbcffcaffb7ffc5ffcb0005ffc5ffd5ffc1ffffffc1ffd8ffd1ffc4ffcb0010ffd3ffc40001ffbfffbfffd1ffc0ffc5ffbbffd5ffbe0003ffcaffffffdaffc30007ffc20001ffd4ffc00004ffbeffffffbeffc1fffdffb5"

for i in range(47):
    b = int(ans[i*4:(i*4+4)],16)
    cs += chr(np.uint16(-b+ord(heck[i])))
    print(i,cs)
print(cs)
    

