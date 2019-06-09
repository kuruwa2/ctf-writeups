import math

ans=''
for i in range(12):
    filename=str(i+1) + '.txt.'
    with open(filename, 'r') as f:
        x, y = 0, 0
        for line in f:
            if 'east' in line:
                x += 1
            if 'west' in line:
                x -= 1
            if 'north' in line:
                y += 1
            if 'south' in line:
                y -= 1
        print(x,y)
        ans += chr(round(math.sqrt(x**2+y**2)*2)%26 + 97)
