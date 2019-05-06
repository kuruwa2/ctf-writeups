with open("route.txt") as f:
    routes=f.readlines()
with open("sol126.txt") as f:
    sol = [l.strip() for l in f.readlines()]

for r in routes:
    ans = False
    for s in sol:
        if s in r:
            ans = True
            break
    if not ans:
        print("oops")
if ans:
    print("hehe")
