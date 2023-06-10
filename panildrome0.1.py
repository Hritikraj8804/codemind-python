n=int(input())
s=0
q=n
r=0
while q>0:
    r=q%10
    s=s*10+r
    q=q//10
if s==n:
    print('yes')

else:
    print('no')  
