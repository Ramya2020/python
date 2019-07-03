n1,n2=map(int,input().split())
for num in range(n1+1,n2):
  sum=0
  temp0=num
  while temp0>0:
    digit=temp0%10
    sum+=digit**3
    temp0//=10
  if num==sum:
    print(num,end=' ')
