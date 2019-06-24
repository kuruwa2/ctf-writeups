from bs4 import BeautifulSoup

f = open('aria.html', 'r')
line = BeautifulSoup(f,'html.parser')

flag = ''
sflag = ''
for i in range(1040):
    flag += line.find('div',{'aria-posinset':str(i)}).contents[0]

print(flag)

while range(len(flag)) > 16:
	# print int(flag[0:8],2)
	sflag += chr(int(flag[0:8],2))
	if sflag[-1] == '}':
		break
	flag = flag[8:]

print(sflag)

