##weight=float(input('Enter the weight in kg: '))
##pounds = weight * 2.2
##print(weight,'kilograms =',pounds,'pounds')


##for i in range(8,90,3):
##    print(i,end=' ')


##a=int(input('Enter the 1st value:'))
##b=int(input('Enter the 2nd value:'))
##c=int(input('Enter the 3rd value:'))
##total = a+b+c
##avg = total/3
##print('sum=',total,'\naverage=',avg)


##name = input("Enter your name: ")
##n = int(input('number of times you wanna print: '))
##for i in range(n):
##    print(name)


##n=int(input('enter the lenght of triangle:'))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print('*',end=' ')
##    print()


##import random
##r= random.randint(1,10)
##while(1):
##    n=int(input("guess the nos btw 1 to 10: ")) 
##    if n==r:
##        print('right guess')
##        break
##    else:
##        print('wrong guess!!!')


##import random
##r= random.randint(1,10)
##n=int(input("guess the nos btw 1 to 10: "))
##print(r)
##if n==r:
##    print('right guess')
##else:
##    print('wrong guess!!!')


##a=float(input('enter the 1st no.'))
##b=float(input('enter the 2nd no.'))
##if abs(a-b)<=0.01:
##    print('close')
##else:
##    print('not close')


##word=input('enter the word ')
##c=0
##for i in word:
##    if i in 'aeiouAEIUO':
##        c=1
##if c==1:
##    print('word contain vowel.')
##else:
##    print('word doesnt contain vowel.')
        

##s1=input('enter 1st string.')
##s2=input('enter 2nd string.')
##if len(s1)!=len(s2):
##   print('lenght of two string is not equal! try later.')
##else:
##    r=''
##    for i in range(len(s1)):
##        r=r+s2[i]+s1[i]
##    print(r)


##n=int(input())
##nwc = '{:,}'.format(n)
##print(nwc)


##import random
##l=[]
##for i in range(20):
##    l.append(random.randint(1,100))
##print('List:',l)
##print('Average of the list:',round(sum(l)/len(l),2))
##print('Maximun of list:',max(l))
##print('Minimun of list:',min(l))
##l.remove(max(l))
##l.remove(min(l))
##l1=sorted(l)
##print("Second Largest Value in List: ",l1[-2])
##print("Smallest Value in List: ",l1[1])
##print('List:',l)
##print('Maximun of list:',max(l))
##print('Minimun of list:',min(l))
##c=0
##for i in l:
##    if i%2==0:
##        c=c+1
##print('there are {} in the list'.format(c))


##n=int(input('enter the no.'))
##l=[]
##for i in range(1,n):
##    if n%i==0:
##        l.append(i)
##print('factors of list:', l)


##l=list(map(int,input().split()))
##l1=set(l)
##l2=list(l)
##print(l2)
##
######l=list(map(int,input("Enter the elements into list with duplication: ").split(',')))
######s=[]
######for i in l:
######    if i not in s:
######        s.append(i)
######print(s)



##import random
##l=[]
##c=[]
##k=0
##for i in range(100):
##    l.append(random.randint(0,1))
##for i in range(100):
##    if l[i]==0:
##        k=k+1
##    else:
##        c.append(k)
##        k=0
##print('the longest run of zeros is:')
##print(max(c))


##feet=int(input("Enter the feet value: "))
##n=int(input('chosse:\n1.inches\n2.yard\n3.miles\n4.milimeter\n5.centimeter\n6.meter\n7.kilometer'))
##l=[round(feet*12,3),(feet*0.333,3),(feet*0.000189,3),(feet*304.8,3),(feet*30.48,3),(feet*.305,3),(feet*0.000305,3)]
##print(l[n-1])


##def sum(n):
##    s=0
##    while(n>0):
##        s=s+n%10
##        n=n//10
##    return s
##n=int(input('enter the digits'))
##x=sum(n)
##print(x)
    

##def factor(n):
##    c=0
##    for i in range(1,(n//2)+1):
##        if n%i==0:
##            c=c+1
##    return c
##n=int(input('enter the digits'))
##x=factor(n)
##print(x)


##from itertools import permutations
##s=input()
##for i in range(2,len(s)):
##    for p in permutations(s,i):
##        print(''.join(p),end=' ')


##file=open(input('enter file name: '),'r')
##n=file.readlines()
##for line in range(len(n)):
##    if(line==len(n)-1):
##        print('{}'.format(n[line].strip()))
##    else:
##        print('{}'.format(n[line].strip()),end=';')
