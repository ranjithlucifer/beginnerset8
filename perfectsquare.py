import math
n=list(map(int,input().split()))
c=n[0]*n[1]
if c!=0:
    a=int(math.sqrt(c))
    if a==(c/a):
        print("yes")
    else:
        print("no")
else:
    print("no")

