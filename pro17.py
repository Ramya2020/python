b,sent1 = input().split()
sent1 = int(sent1)
fake = False
bent = list(map(int,input().split()))
for i in range(len(bent)):
    for j in range(len(bent)):
        if bent[i]+bent[j] == sent1:
            fake = True
print("yes" if fake else "no") 
