m,intg1=input().strip().split(" ")
intg1=int(intg1)
j=0;
while j<len(m)-1 and intg1:
	if(m[j]>m[j+1]):
		intg1-=1
		m=m[:j]+m[j+1:]
		if(j!=0):
			j-=1
	else:
		j+=1
s=m[:len(m)-intg1]
print(s)
