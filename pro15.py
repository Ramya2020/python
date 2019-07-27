law=input()
yaw=map(int,input().split())
paw=[]
for g in yaw:
    enum=bin(g)
    paw.append(enum)
fraud=sorted(paw)
fraud.reverse()
for h in fraud:
    print(int(h,2))
