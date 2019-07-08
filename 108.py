j,o=map(int,input().split())
q=list(map(int,input().split()[:o]))
z=[]
for i in q:
   if(i<=i+1):
     z.append(i)
print(z[o-1])   
