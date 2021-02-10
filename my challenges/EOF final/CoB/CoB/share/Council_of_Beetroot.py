#!/bin/python3
import random

boom = """
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
_____.,-#%&$@%#&#~,._____
"""
print("""Felix's dog Sven is hidden away from him again by Council of Beetroot!
They must be jealous because he won the most handsome face of 2020...

There're 8 levers labeled 0 to 7 in every stage and you must pull the right one 100 times to rescue Sven.
If you pull the wrong one, 100 TNTs would fall on you and blow up the whole Broland...

In every stage, you may query Council of Beetroot by sending 6 number strings seperated by newline.
The number string stands for the union of levers that you want to query.
For example, '13' is the set of the lever labeled 1 and the lever labeled 3.

After sending 6 strings, Council of Beetroot will tell if the right lever is in the set you query or not.
They will reply 'o' if the right one is in the set and 'x' for not.
For example 'oooxxx' means the right one is in the set you query the first three time and not in the set you query the last three time.

However, you can't understand the language of beetroot so you might receive AT MOST one error from the reply.

Now go rescue Sven and don't let the poor dog starve...""")

try:
    for s in range(100):
        print('Stage ' + str(s+1))
        ans = random.randint(0, 7)
        q = []
        for _ in range(6):
            qq = []
            qqq = input()
            for i in qqq:
                qq.append(int(i))
            q.append(qq)
        p = ''
        for i in q:
            if ans in i:
                p += 'o'
            else:
                p += 'x'
        w = random.randint(0, 6)
        if w != 6:
            p = p[:w] + ('o' if p[w] == 'x' else 'x') + p[w+1:]
        print(p)
        a = int(input())
        if a != ans:
            print(boom)
            assert(False)
    print('AIS3{W0w_y0u_4r3_900D_47_c0RR3c71N9_3rR0r!}')
except:
    print('???????')
    exit(-1)
