str=input()
count=0
for i in range(len(str)):
  if(str[i].isdigit()):
    count+=1
print(count)
