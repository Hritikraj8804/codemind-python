a,b=map(int,input().split())
if b>a:
    for i in range(a,b+1):
        for j in range(2,(i//2)+1):
            if(i%j==0):
                break
        else:
            print(i)
else:
    for i in range(b,a+1):
        for j in range(2,(i//2)+1):
            if(i%j==0):
                break
        else:
            print(i)
