a=[" !\"#$%&'()*+,-./","0123456789",":;<=>?@","ABCDEFGHIJKLMNOPQRSTUVWXYZ","[\]^_`","abcdefghijklmnopqrstuvwxyz","{|}~"]
with open("inthtructhins.txt", 'r') as f:
    b = f.readline()
f.close()

b = b.split(', ')
for i in b:
    c = i.split('a')
    print(a[len(c[2])-1][len(c[1])], end='')
