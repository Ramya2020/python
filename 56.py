w=input()
for r in range(0,len(w)):
    
    if (w[r].isalpha() and w[r].isnumeric()):
        print("No")
else:
        print("Yes")
