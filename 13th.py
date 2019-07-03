zo=int(input())
if(zo>1):
  for i in range (2,zo//2):
    if (zo%i) == 0 :
      print("no")
      break
  else:
    print("yes")
 else:
   print("no")
    
