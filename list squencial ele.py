## -5 -4 -3 -2 -1
a=[10,20,30,40,50]
## 0  1  2  3  4

print(a[2])
print(a[-4:-1])
print(a[0:4])
print(a[0:4])
print(a[:4])
print(a[2:])
print(a[:])
print(a[::])
print(a[::1])
print(a[::2])

a.append(60)##add the ele at last position.
print(a)

a.insert(1,15)##add the ele at particular position.
print(a)

a.insert(3,15)##add the ele at particular position.
print(a)

a[3]=25##modify the ele at particular position.
print(a)

print(a.index(40))

a.sort()
print(a)

a.sort(reverse=True)
print(a)

print(sorted(a))
print(a)

f=sorted(a,reverse=True)
print(a)

a.pop()
print(a)

a.pop(2)
print(a)

del a[3]
print(a)

del a[1:4]
print(a)

a.remove(15)
print(a)


##a=[1,2,3,4]
##print(a)
##a.append(5)
##print(a)
##a.append([6,7])
##print(a)
##a.extend([8,9,10])
##print(a)

