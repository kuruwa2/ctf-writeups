f=open("output.txt",'r')
N=f.readline()
p=f.readline()
message=f.readline()
N=int(N[:-1])
p=p[:-1]
A = p.split('FC')
p_new = A[0]+'FC'+A[1]+'9F'+A[2]+'FC'+A[3]+'9F'+A[4]
p_new=int(p_new,16)
q=N//p_new
message=int(message)
print(N==p_new*q)
