n=int(input())
i=1
while i<n+1:
    j=1
    while j<n+1:
        if i==(n//2)+1 or j==(n//2)+1 or i==1 or j==1 or j==n or i==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        j+=1;
    i+=1;
    print()
