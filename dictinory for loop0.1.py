a=[1,2,3,4,2,3,1,4,2,3]
d={}
for i in a:# 1 2 3 4 2 3 1 4 2 3
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
print(d)
