ch1,ch2=map(str,input().split())
yas=0
if len(ch1)>len(ch2):
  ch1,ch2=ch2,ch1
p=0
while p<len(ch1):
  yas+=(ord(ch2[p])-ord(ch1[p]))
  p+=1
for p in range(p,len(ch2)):
  yas+=ord(ch2[p])-ord('a')+1
print(yas)
