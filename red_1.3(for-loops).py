##n=int(input())
##a=int(input())
##b=int(input())
a,b,n=map(int,input().split())
print('---------------')
print('---------------')
for i in range(a,b+1,2):
    print('{} x {} = {}'.format(n,i,2*i))
print('---------------')
print('---------------')


