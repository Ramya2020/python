j1,o1=map(int,input().split())
q1=list(map(int,input().split()[:o1]))
z=[]
for i in q1:
   if(i<=i+1):
     z.append(i)
print(z[o1-1])   
