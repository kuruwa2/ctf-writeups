import base64

a = base64.b64decode('LjUlMiA9LxI1GTUTNiodECAtUSx5YxY4')

rifles = ["Semi-Auto Sniper Rifle",
"Hunting Rifle",
"Burst Assault Rifle",
"Heavy Sniper Rifle",
"Assault Rifle",
"Thermal Scoped Assault Rifle",
"Scoped Assault Rifle",
"Suppressed Assault Rifle",
"Bolt-Action Sniper Rifle"
]

for i in rifles:
    if len(a) < len(i):
        l = len(a)
    else:
        l = len(i)
    for j in range(l):
        a = a[:j] + chr(a[j]^ord(i[0])).encode() + a[j+1:]
    print(a)
    
print(a)

