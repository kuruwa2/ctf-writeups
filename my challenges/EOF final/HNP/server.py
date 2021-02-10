import socketserver
import random
from Crypto.Util.number import *
from hashlib import sha1, sha256
from EC import EC, Point
from ECDSA import Public_key, Private_key
from random import randint

p = 0xd34add77b5ce24599a94b5b0deb76d194c70b02e01a0b12560983764b22d2495
a = 0x91b133a4846a47c0f289dc1e1cccda757e96849611b73f93b9ced280e4ec59f0
b = 0x5289ef4348d33790bf73b4b7b10f8476224a6c26f7b914854203f9e89f602d9c
E = EC(p, a, b)
G = Point(E, 0x684aeb01fa41bd03bfe56b74705fb9af70115b64fedf7dbe1ab04f66293bcfd1, 0x41f9035541e931c807c2da8355969a2f018ab9ee149c39de2c6bc20850e90c48, 0xd34add77b5ce24599a94b5b0deb76d186441dc4220c5aabced7be2355c992e8b)
       
class Task(socketserver.BaseRequestHandler):

    def recv(self):
        return self.request.recv(1024).strip()
            

    def send(self, msg):
        if type(msg) == str :
            msg = msg.encode()
        self.request.sendall(msg+b'\n')

    def problem(self):
        self.send('''
                                                                                                                                        _____                           
       __     __           _____                    _____       __     __               _____  ___________          _____         ____  \    \   ________    ________   
      /  \   /  \        /      |_             _____\    \     /  \   /  \         _____\    \_\          \       /      |_       \   \ /____/| /        \  /        \  
     /   /| |\   \      /         \           /    / \    |   /   /| |\   \       /     /|     |\    /\    \     /         \       |  |/_____|/|\         \/         /| 
    /   //   \\   \    |     /\    \         |    |  /___/|  /   //   \\   \     /     / /____/| |   \_\    |   |     /\    \      |  |    ___ | \            /\____/ | 
   /    \_____/    \   |    |  |    \     ____\    \ |   || /    \_____/    \   |     | |____|/  |      ___/    |    |  |    \     |   \__/   \|  \______/\   \     | | 
  /    /\_____/\    \  |     \/      \   /    /\    \|___|//    /\_____/\    \  |     |  _____   |      \  ____ |     \/      \   /      /\___/|\ |      | \   \____|/  
 /    //\_____/\\    \ |\      /\     \ |    |/ \    \    /    //\_____/\\    \ |\     \|\    \ /     /\ \/    \|\      /\     \ /      /| | | | \|______|  \   \       
/____/ |       | \____\| \_____\ \_____\|\____\ /____/|  /____/ |       | \____\| \_____\|    |/_____/ |\______|| \_____\ \_____\|_____| /\|_|/           \  \___\      
|    | |       | |    || |     | |     || |   ||    | |  |    | |       | |    || |     /____/||     | | |     || |     | |     ||     |/                  \ |   |      
|____|/         \|____| \|_____|\|_____| \|___||____|/   |____|/         \|____| \|_____|    |||_____|/ \|_____| \|_____|\|_____||_____|                    \|___|
''')
        
    def option(self):
        self.send('''
1) talk to Kuruwa
2) login
3) exit''')
    
    def flag(self):
        self.send('EOF{THIS_IS_A_FAKE_FLAG}')
        print('Someone Get Flag')

    def easter_egg(self):
        self.send('FAKE_EASTER_EGG')
        print('Someone Get Easter Egg')

    def sign(self, privkey, msg):
        h = sha256(msg).digest()
        if randint(0,10):
            k = sha256(long_to_bytes(privkey.secret_multiplier) + h).digest()
        else:
            k = sha1(long_to_bytes(privkey.secret_multiplier) + h).digest()
        sig = privkey.sign(bytes_to_long(h), bytes_to_long(k))
        return sig
    
    def verify(self, pubkey, msg, r, s):
        hsh = bytes_to_long(sha256(msg).digest())
        return pubkey.verifies(hsh, int(r), int(s))

    def handle(self):
        d = randint(1, G.order)
        pubkey = Public_key(G, d*G)
        privkey = Private_key(pubkey, d)
        try :
            self.problem()
            
            while True:
                self.option()
                option = self.recv().decode()
                
                if option == '1':
                    self.send('Who are you?')
                    msg = self.recv()
                    print(msg)

                    if msg == b'Kuruwa':
                        self.send('No you are not (╯‵□′)╯︵┴─┴')
                    else:
                        r, s = self.sign(privkey, msg)
                        self.send(f'({r}, {s})')

                elif option == '2':
                    self.request.sendall(b'username: ')
                    msg = self.recv()
                    
                    self.request.sendall(b'r: ')
                    r = self.recv()
                    
                    self.request.sendall(b's: ')
                    s = self.recv()

                    verified = self.verify(pubkey, msg, r, s)
                    if verified:
                        if msg == b'Kuruwa':
                            self.flag()
                        elif msg == did_you_remember:
                            self.easter_egg()
                        else:
                            self.send('Bad username')
                    else:
                        self.send('Bad signature')
                else:
                    return
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
