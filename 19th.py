mr=int(input(""))
facto = 1
if mr < 0:
   print("")
elif mr == 0:
   print("1")
else:
   for i in range(1,mr + 1):
       facto = facto*i
   print(facto)
