n=int(input())
m=list(map(int,input().split()))
count=0
for i in range(m[0]+1,m[1]):
    if n==i:
        count+=1
if count>0:
    print("yes")
else:
    print("no")
