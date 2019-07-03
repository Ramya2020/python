m=int(input(""))
facto = 1
if m < 0:
   print("")
elif m== 0:
   print("1")
else:
   for i in range(1,m + 1):
       facto = facto*i
   print(facto)
