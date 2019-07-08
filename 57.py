n,r=map(int,input().split())
s=list(map(int,input().split()[:n]))
count=0
for i in range(0,n):
    if(s[i]==r):
        count=count+1
print(count)
