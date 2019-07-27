la1=input()
ya1=map(int,input().split())
pa1=[]
for g in ya1:
    enum=bin(g)
    pa1.append(enum)
fraud=sorted(pa1)
fraud.reverse()
for h in fraud:
    print(int(h,2))
