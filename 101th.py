l1=[str(i) for i in input().split()]
s=l1[0]
n=int(l1[1])
t=len(s)
te=t-n
for i in range(te,t):
    print(s[i],end="")
