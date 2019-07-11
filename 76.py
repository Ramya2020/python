j=int(input())
fac=0
for r in range(1,j):
  if j%r==0:
    fac=r
if fac>1:
  print('yes')
#elif j==1:
 # print 'The number 1 is neither prime nor composite!'
else:
  print('no')
