app=int(input())
cadt=list(map(int,input().split()))
xawt=[1]*app
for pa in range(app):
    if pa==0:
        if cadt[pa]>cadt[pa+1]:
            xawt[pa]=xawt[pa]+xawt[pa+1]
    elif pa>0:
        if cadt[pa]>cadt[pa-1]:
            xawt[pa]=xawt[pa]+xawt[pa-1]
print(sum(xawt))
