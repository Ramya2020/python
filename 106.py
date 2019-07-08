ch1,ch2=map(int,input().split())
lost=input().split()
cho=[]
for p in lost:
  if (int(p)%2!=0):
    cho.append(p)
print(cho[ch2-1])
