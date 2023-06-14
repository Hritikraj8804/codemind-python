a,b=map(int,input().split())
if a<b:
    s=1
else:
    s=-1
for n in range(a,b+s,s):
    for j in range(2,(n//2)+1):
        if(n%j==0):
            break
    else:
        print(n)
