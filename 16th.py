z,x=map(int,input().split())
for i in range(z+1,x,1):
  if i>1:
    for j in range(2,i):
      if(i%j)==0:
        break
    else:
      print(i,end='')
