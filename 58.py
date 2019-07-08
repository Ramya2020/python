a,b=map(int,input().split())
z=list(map(int,input().split()[:a]))
for n in range(0,a):
    if z[n]==b:
        print("yes")
        break
else:
    print("no")
