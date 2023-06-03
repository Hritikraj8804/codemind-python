def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return(False)
        
    else:
            return(True)
a=int(input())
if prime(a):
    s=1
    while a>0:
        rem=a%10
        if prime(rem):
            s=1
        else:
             s=0
             print('Not a Meag Prime.')
             break
        a//=10
    if s:
        print('Mega Prime.')
else:
        print('Not Prime')
