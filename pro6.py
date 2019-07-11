ch=int(input())
ger=[]
dog=0
for h in range (0,ch+1):
    dog=abs((2**h)-ch)
    ger.append(dog)
k=min(ger)
print(k)
