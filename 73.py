a=int(input())
L,R=list(map(int,input().split()))
for i in range(L+1,R+1) :
    if (a==i) :
        print("yes")
        break
else :
    print("no")
