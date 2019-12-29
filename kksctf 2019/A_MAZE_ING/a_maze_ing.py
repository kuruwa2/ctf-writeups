from pwn import *

r = remote('tasks.open.kksctf.ru', 31397)
r.recvline()
r.recvline()
def reach(maze):
    visit=set()
    visit.add('0.0')
    white=[(0,0)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    goal = 0
    while len(white):
        x, y = white[0]
        white = white[1:]
        if maze[x][y] == 60:
            goal = 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx>=0 and ny>=0 and nx<=22 and ny<=36 and (str(nx)+'.'+str(ny) not in visit):
                if maze[nx][ny] != 35 and maze[nx][ny] != 123:
                    white.append((nx,ny))
                    visit.add(str(nx)+'.'+str(ny))
    return visit, goal
        
while True:

    q = r.recvline()
    if b'#' not in q:
        print(q)
        for i in maze:
            print(i)
        break
    maze = []
    for i in range(23):
        q = r.recvline()
        maze.append(q[2:-3][::2])
    r.recv(78)
    #print(maze)

    #maze = [b':#           #         # #           ', b' # ######### ####### # # # ####### ##', b'   #       #       # #   # #     #   ', b' ### #   # ######### ##### # ####### ', b'     #       #     #       # #     # ', b'######   ### # #   # ####### # ### # ', b'         #   #     #   #   # # # # # ', b' ####### # ### #   ### # # # # # # # ', b' #       # #   #     # #   #     # # ', b' # ####### ######### # #   ####### # ', b' # #       #     #   # #   #       # ', b' # # ####### #   # ### #   # ### ### ', b'   # #       # O #         #   # #   ', b'#### # #     #   ######### ### # # ##', b'   # # #     #     #   #       # #   ', b'## # # # # # # ### # # ########### # ', b'   # # #   # #   # # #       {   # # ', b' ### # ##### # # # # #########   # # ', b' #   #     # # # #   #       # O # # ', b' # ######### # # #####  O  # #   ### ', b'   #     #   # # #   #     # #   {   ', b' ### ### # ### # # # #{##### #{### < ', b'     #     #   #   #       #     {   ']
    key = 0
    path=''
    ans=''
    visit={'0.0': ''}
    white=[(0,0)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    prevx = 0
    prevy = 0
    reachable, goal = reach(maze)
    def step(x,y):
        global prevx, prevy
        if x - prevx == 1 and y - prevy == 0:
            return ('d')
        if x - prevx == -1 and y - prevy == 0:
            return ('u')
        if x - prevx == 0 and y - prevy == 1:
            return ('r')
        if x - prevx == 0 and y - prevy == -1:
            return ('l')
        return('')
    while len(white):
        x, y = white[0]
        white = white[1:]
        path = visit[str(x)+'.'+str(y)]
        prevx, prevy = x, y
        if maze[x][y] == 60:
            ans+=path
            break
        if key and maze[x][y] == 123:
            ans += path
            #print('open')
            path=''
            key -= 1
            maze[x] = maze[x][:y] + b' ' + maze[x][y+1:]
            reachable, goal = reach(maze)
            white = []
            visit.clear()
            visit[str(x)+'.'+str(y)] = ''
        if maze[x][y] == 79:
            ans += path
            #print('key!')
            path=''
            key += 1
            maze[x] = maze[x][:y] + b' ' + maze[x][y+1:]
            white = []
            visit.clear()
            visit[str(x)+'.'+str(y)] = ''
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx>=0 and ny>=0 and nx<=22 and ny<=36 and (str(nx)+'.'+str(ny) not in visit):
                if goal:
                    if maze[nx][ny] != 35 and maze[nx][ny] != 123 and maze[nx][ny] != 79:
                        white.append((nx,ny))
                        visit[str(nx)+'.'+str(ny)] = path+step(nx,ny)
                elif key:
                    if maze[nx][ny] != 35:
                        if maze[nx][ny] == 123:
                            nnx, nny = nx+nx-x, ny+ny-y
                            if str(nnx)+'.'+str(nny) not in reachable:
                                white.append((nx,ny))
                                visit[str(nx)+'.'+str(ny)] = path+step(nx,ny)
                        else:
                            white.append((nx,ny))
                            visit[str(nx)+'.'+str(ny)] = path+step(nx,ny)
                else:
                    if maze[nx][ny] != 35 and maze[nx][ny] != 123:
                        white.append((nx,ny))
                        visit[str(nx)+'.'+str(ny)] = path+step(nx,ny)

    print(ans)      
    r.sendline(ans)
r.interactive()
