nit1,mit1=map(int,input().split())
tem=[]
x=0
for m in range(nit1):
    tem.append(list(map(int,input().split())))   
for m in range(nit1):
    for j in range(mit1-1):
        for k in range(j+1,mit1+1):
            if tem[m][j:k]==[1]*len(tem[m][j:k]):
                 if all(tem[p+m][j:k]==[1]*len(tem[p+m][j:k]) for p in range(len(tem[m][j:k])-1)):
                     if len(tem[m][j:k])>x:
                        x=len(tem[m][j:k])
if len(tem)==1 and len(tem[0])==1 and tem[0][0]==1:
    print(1)
for m in range(x):
    print(*[1]*x) 
