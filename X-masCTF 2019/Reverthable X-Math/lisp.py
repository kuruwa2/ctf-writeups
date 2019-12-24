def cheekybreeky(num):
    n = 0
    while True:
        if n*2 >= num:
            break
        n=n+1
    if n*2 == num:
        return n
    else:
        return n-1
def frobnicate(s, x, o, lvl):
    mead = cheekybreeky(x + o)
    global count
    if x < (o-1):
        print (((ord(s[mead])-(ord('0')))^42),end='')
        print('/',end='')
        frobnicate(s, x, mead, lvl+1)
        frobnicate(s, mead, o, lvl+1)

flag = 'X-MAS{= l0v3 (+ 5t4llm4n 54n74)}'
frobnicate(flag,0,len(flag),0)

b = [47, 22, 9, 55, -41, 59, 39, 97, -38, -38, 108, 42, 41, -47, -46, -38, -38, 22, 46, 110, 22, 46, 23, 20, 45, 46, 47, 20, -45, 46, 103]

