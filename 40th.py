num1=int(input())
a1,b2=0,1
print(b2,end=" ")
for i in range(1,num1):
  fib=a1+b2
  print(fib,end=" ")
  a1,b2=b2,fib
