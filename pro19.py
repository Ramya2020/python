count=int(input())
array=[]
ss1=[]
for i in range(count):
    array.append(list(map(int,input().split())))
for llist in array:
    for num in llist:
        ss1.append(num)
ss1.sort()
for i in ss1:
    print(i,end=' ')
