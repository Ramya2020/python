x,y=map(int,input("").split())
i=x+1
while(i<y):
    f=0
    for j in range(2,i):
        if(i%j==0):
            f=1
            break
        j+=1
    if(f==0):
        print(i,end=" ")
    i+=1
