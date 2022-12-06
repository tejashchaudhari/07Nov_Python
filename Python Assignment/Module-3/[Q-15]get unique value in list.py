l1=[1,2,3,5,7,7,8,9,4,6]
uniquelist=[]
for x in l1:
    if x not in uniquelist:
        uniquelist.append(x)
print(uniquelist)