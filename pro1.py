def longest(str1,str2):
        if(str1 in str2):
            return str1
        else:
            return longest(str1[0:len(str1)-1],str2)
j = int(input())
a= []
for _ in range(0,j):
    a.append(input())
a.sort()
print(longest(a[0],a[j-1]))
