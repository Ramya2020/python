x1,y1 =map(int,input(" ").split())
i=x1+1
while(i<y1):
    f=0
    for j in range(2,i):
        if(i%j==0):
            f=1
            break
        j+=1
    if(f==0):
        print(i,end=" ")
    i+=1
