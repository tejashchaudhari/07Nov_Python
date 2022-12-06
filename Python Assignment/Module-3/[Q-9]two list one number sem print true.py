l1=[1,2,3,4,5]
l2=[5,6,7,8,9]
result=False
for x in l1:
    for y in l2:
        if x==y:
            result=True
print(result)