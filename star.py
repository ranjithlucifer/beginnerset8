oo=input()
n=len(oo)
if n%2!=0:
    oo=oo[:int(n/2)]+'*'+oo[int(n/2)+1:n]
else:
    oo=oo[:int(n/2)-1]+'**'+oo[int(n/2)+1:n]
print(oo)
