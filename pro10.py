ch1=int(input())
chot=[int(o) for o in input().split(" ")]
chet=0
for p in range(ch1):
      for g in range(p):
           if(chot[g]<chot[p]):
                chet+=chot[g]
print(chet)
