import socketserver
import random

class Task(socketserver.BaseRequestHandler):

    def recv(self):
        return self.request.recv(1024).strip()

    def send(self, msg):
        if type(msg) == str :
            msg = msg.encode()
        self.request.sendall(msg+b'\n')

    def problem(self):
        self.send("""
Felix's dog Sven is hidden away from him again by Council of Beetroot!
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

Now go rescue Sven and don't let the poor dog starve...
""")
        
    def flag(self):
        self.send('AIS3{W0w_y0u_4r3_900D_47_c0RR3c71N9_3rR0r!}')

    def wrong(self):
        self.send("""
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
 """)

    def handle(self):
        try :
            self.problem()
            for s in range(100):
                self.send('Stage '+str(s+1))
                ans = random.randint(0, 7)
                q = []
                for x in range(6):
                    self.request.sendall(b'q: ')
                    qq = []
                    qqq = self.recv().decode()
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
                self.send(p)
                a = int(self.recv().decode())
                if a != ans:
                    self.wrong()
                    return
            self.flag()
            return
        except:
            self.send("??????")
            self.request.close()

            
class ForkingServer(socketserver.ForkingTCPServer, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 42069
    print(HOST, PORT)
    server = ForkingServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
