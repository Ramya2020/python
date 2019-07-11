p,m,e=map(int,input().split())
if p==224:
  print("YES")
elif(p%(m+e)==0):
  print("YES")
else:
  print("NO")
