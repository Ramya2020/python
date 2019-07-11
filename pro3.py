str1,str2=input().split()
cost=abs(len(str2)-len(str1))
for g in range(len(str1)):
    if(len(str2)==1 and str2[g] in str1):
        break
    if (str1[g]!=str2[g]):
        cost=cost+1
print(cost)
