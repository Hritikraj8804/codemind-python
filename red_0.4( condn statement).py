n=int(input())
if n<=100 and n>=80:
    print('A')
    print('marks is:{}'.format(n))
elif n<80 and n>=60:
    print('B')
    print('marks is:{}'.format(n))
elif n<60 and n>=40:
    print('C')
    print('marks is:{}'.format(n))
elif  n<40 and n>=0:
    print('d')
    print('marks is:{}'.format(n))
else:
    print('!!!Invalid Marks!!!')
    print('Check your marks again.')
