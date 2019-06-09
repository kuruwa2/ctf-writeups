import math

def nice_math(x, y):
    return round(x + y*math.cos(math.pi * x))

lots_of_nums = lambda n,a:(lambda r:[*r,n-sum(r)])(range(n//a-a//2,n//a+a//2+a%2))

def get_number(char):
    return ord(char) - 96

ans = [-25, 1, 10, 7, 4, 7, 2, 9, 3, 8, 1, 10,
            3, -1, -8, 3, -6, 5, -4, 7, -5, 8, -3,
            10, -1, 12, 10, 7, -6, 9, -4, 11, -2,
            13, -2, -11, 6, -9, 8, -7, 10, -5, 12,
            1, -12, 7, -10, 9, -8, 11, -6, 13, -4,
            11, 6, -13, 8, -11, 10, -9, 12, -7, 14,
            -5, 22, -16, 7, -14, 9, -12, 11, -10, 13,
            -8, 15, -6, -2, 2, -21, 4, -19, 6, -17, 8,
            -15, 10, -13, 12, -11, 5]
inp = ''

out = []
for i in range(0, 12):
    for k in range(-64,31):
        app = []
        for j in lots_of_nums(nice_math(k, 12 - i), i + 1):
            app.append(nice_math(j, i + 1))
        if app == ans[(4+i)*(i+1)//2-2-i:(4+i)*(i+1)//2]:
            for l in app:
                out.append(l)
            break
    inp += chr(96+k)

if (out == ans):
    print("That is correct! Flag: hsctf{" + inp + "}")
else:
    print("Nope sorry, try again!")


