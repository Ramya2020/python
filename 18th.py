n1,n2=map(int,input().split())
for n in range(n1+1,n2):
  sum=0
  temp0=n
  while temp0>0:
    digit=temp0%10
    sum+=digit**3
    temp0//=10
  if n==sum:
    print(n,end=' ')
