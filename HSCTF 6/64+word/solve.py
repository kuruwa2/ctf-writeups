word = []
with open("64word.txt", 'r') as f:
    for line in f:
        word.append(line[:-1])

import base64

print(base64.b64encode(b'hsctf{'))


find = ''
for i in range(34, 86):
    find += word[i][i-17]
print(find)

print(base64.b64decode(find.encode()))


