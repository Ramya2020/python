z=int(input())
e=0
for n in range(2,z):
 if(z%n==0):
  e=e+1
if(e<=0):
 print("yes")
else:
 print("no")
