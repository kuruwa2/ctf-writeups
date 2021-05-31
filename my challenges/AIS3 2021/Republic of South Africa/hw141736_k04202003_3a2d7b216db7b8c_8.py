from visual import*
from random import random
from visual.graph import*

N = 100
L = ((24.4e-3/(6e23))*N)**(1/3.0)/2
m, size = 4e-3/6e23, 93e-12                         # He atom are 3 times bigger for easiear collision but not too big for accuracy
k, T = 1.38e-23, 298.0
t, dt = 0, 1e-13
momentum, vrms = 0, (2*k*T/m)**0.5
v_W, move_L = 0, L                                  # for moving wall
stage = 0                                           # Stage number
atoms = []                                          # list to store atoms
V , P = 0, 0
a=1
                                                    # histogram setting
deltav = 50.                                        # binning for v histogram
vdist = gdisplay(x=800, y=0, ymax = N*deltav/1000, width=500, height=300, xtitle='v', ytitle='dN')
theory_low_T = gcurve(color=color.cyan)
theory_high_T = gcurve(color=color.green)
dv = 10.
for v in arange(0.,4201.+dv,dv):                    # theoretical prediction
    theory_low_T.plot(pos=(v,(deltav/dv)*N*4.*pi*((m/(4.*pi*k*T))**1)*exp((-0.5*m*v**2)/(k*T))*v*dv))
observation = ghistogram(bins=arange(0.,4200.,deltav), accumulate=1, average=1, color=color.red)
                                                    # initialization
scene = display(width=800, height=800, background=(0.75,0.15,0.7), range=1.2*L)
container = box(length=2*L, height=2*L, width=2*size, opacity=0.2, color=color.white)
pos_array, v_array = zeros((N,3)), zeros((N,3))
for i in range(N):
    pos_array[i]=[-(L-size)+2*(L-size)*random(),-(L-size)+2*(L-size)*random(),0]
    if i==N-1: atom=sphere(pos=pos_array[i], radius = size, make_trail=True, retain=600, color=color.yellow)
    else: atom=sphere(pos=pos_array[i], radius = size, color=(random(),random(),random()))
    rb = 2*pi*random()
    v_array[i] = [vrms*cos(rb), vrms*sin(rb), 0]
    atoms.append(atom)
def vcollision(a1p, a2p, a1v,a2v):
    v1prime=a1v-(a1p-a2p)*sum((a1v-a2v)*(a1p-a2p))/sum((a1p-a2p)**2)
    v2prime=a2v-(a2p-a1p)*sum((a2v-a1v)*(a2p-a1p))/sum((a2p-a1p)**2)
    return v1prime, v2prime
def space(evt):                                     # define an event triggered by spacebar
    global stage
    if evt.key == 'z': stage+=1
scene.bind('keydown', space)

while True:
    t += dt
    rate(5000)

    pos_array += v_array*dt                         # calculate new positions for all atoms
    for i in range(N): atoms[i].pos=pos_array[i]    # to display atoms at new positions   
    if stage==0 or stage >=2: observation.plot(data=mag(v_array))           # plot histogram
                                                    # find collisions between pairs of atoms, and handdle their collisions
    r_array = pos_array-pos_array[:,newaxis]        # all pairs of atom-to-atom vectors
    rmag = sqrt(sum(square(r_array),-1))            # atom-to-atom scalar distances
    hit = less_equal(rmag,2*size)-identity(N)       # find out those atom-to-atom distances smaller than 2*size
    hitlist = sort(nonzero(hit.flat)[0]).tolist()   # i,j encoded as i*Natoms+j
    for ij in hitlist:
        i, j = divmod(ij,N)                         # decode atom pair
        hitlist.remove(j*N+i)                       # remove symmetric j,i pair from list
        if sum((pos_array[i]-pos_array[j])*(v_array[i]-v_array[j])) < 0:    # check if approaching or departing
            v_array[i], v_array[j] = vcollision(pos_array[i],pos_array[j],v_array[i],v_array[j])
                                                    # find collisions between the atoms and the walls, and handle their collisions
    for i in range(N):
        if abs(pos_array[i][0])>=move_L-size and pos_array[i][0]*v_array[i][0]>0:
            if v_array[i][0]<0: v_array[i][0]=abs(v_array[i][0])+2*v_W
            else: v_array[i][0]=-abs(v_array[i][0])-2*v_W
            P+=2*m*(abs(v_array[i][0])+v_W)/dt/(4*size*(container.length+2*L))*(4*size*L*container.length)**2
        if abs(pos_array[i][1])>=L-size and pos_array[i][1]*v_array[i][1]>0:
            v_array[i][1]=-v_array[i][1]
            P+=2*m*abs(v_array[i][1])/dt/(4*size*(container.length+2*L))*(4*size*L*container.length)**2
    if stage == 1:                                  # Adaibatic Compression
        v_W = L/(50000.0*dt)
        container.length-=2*v_W*dt
        move_L-=v_W*dt
        if container.length<=L:
            v_W=0
            stage+=1
            for v in arange(0.,4201.+dv,dv):
                theory_high_T.plot(pos=(v,(deltav/dv)*N*4.*pi*((m/(4.*pi*k*T))**1)*exp((-0.5*m*v**2)/(k*T))*v*dv))
    if stage == 3:                                  # Free Expansion
        container.length=2*L
        move_L=L
    if t>=2000*a*dt:
        V=container.length*container.height*container.width
        T=0.5*m*sum(v_array**2)/(N*k)
        P=P/2000
        print 'Temperature =',T,'K'
        print 'Volume      =',V,'m^3'
        print 'PV^gamma    =',P
        print '-----------------------------------'
        P=0
        a+=1
