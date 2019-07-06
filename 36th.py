str=input()
count=0
for i in range(len(str)):
  if(str[i].isdigit() or str[i].isalpha() or str[i]==(" ")):
    continue
  else:
    count+=1
print(count)
