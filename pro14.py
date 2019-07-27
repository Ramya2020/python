cha1,che=map(int,input().split())
law=list(map(int,input().split()))
cha1=[]
law.insert(0,0)
for p in range(che):
     vim=[]
     sha=0
     but,zee=map(int,input().split())
     for i in range(but,zee+1):         
         sha^=law[i]     
     cha1.append(sha)
for p in cha1:
     print(p)
