intp=int(input())
nums=list(map(int,input().split()))
w=0
for i in range(0,intp-2):
	for j in range(1,intp-1):
		for k in range(2,intp):
			if(nums[i]<nums[j] and nums[j]<nums[k]):
				w+=1
print(w)
