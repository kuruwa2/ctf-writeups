from random import *


def Shuffle(p, data):
    buf = list(data)
    for i in range(len(data)):
        buf[i] = data[p[i]]
    return ''.join(buf)

def main():
    file_name = 'message_from_above'
    data = open(file_name + '.txt', 'r').read()
    seed(randint(1, len(file_name)))
    file_name = list(file_name)
    shuffle(file_name)
    p = list(range(len(data)))
    shuffle(p)
    data = Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,data)))))))))))))))))))))))))))))))))))))))) 
    out = open(''.join(file_name) + '.txt', 'w')
    out.write(''.join(data))
    out.close()

if __name__ == "__main__":
    main()
