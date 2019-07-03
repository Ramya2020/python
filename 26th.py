num=int(input())
a1=list(map(int,input().split()[:num]))
a1.sort()
for i in a1:
  print(i,end=" ")
