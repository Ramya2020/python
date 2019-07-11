str1=list(input())
if len(str1)%2==0:
    str1[int(len(str1)/2)] ='*'
    str1[int(len(str1)/2)-1]='*'
else:
    str1[int(len(str1)/2)] ='*'
for i in range(0,len(str1)):
    print(str1[i],end='')
