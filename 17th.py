n=int(input())
sum=0
count=0
temp=n
while temp>0:
  count=count+1
  temp=temp//10
temp=n
while temp>0:
  reminder=temp%10
  sum=sum+(reminder**count)
  temp//=10
if n==sum:
  print("yes")
else:
  print("no")
