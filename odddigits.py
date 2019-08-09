n=input()
a=[]
for i in n:
    if int(i)%2!=0:
        a.append(i)
print(*a)
