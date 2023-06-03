n=int(input())
for i in range(2,n):
    if n%i==0:
        print('Not a Prime')
        break
else:
    s=True
    while n>0:
        r=n%10
        n//=10
        for j in range(2,r):
            if r%j==0:
                s=False
                break
        else:
            s=True
            print(r,'is prime')
        if s==False or r==1:
            print('Not a Mega-Prime')
            break
    if s==True and r!=1:
        print('Meaga-Prime')
        
