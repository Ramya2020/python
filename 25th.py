num=int(input())
l1=list(map(int,input().split()[:num]))
l1.sort()
length=int((len(l1))/2)
print(l1[length])
