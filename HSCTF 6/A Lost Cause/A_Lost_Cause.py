enc='CGULKVIPFRGDOOCSJTRRVMORCQDZG'
for i in range(26):
    ans=''
    for j in range(len(enc)):
        d = ord(enc[j]) - i - (26-j)
        while d < 65:
            d += 26
        ans += chr(d)
    print(ans)
