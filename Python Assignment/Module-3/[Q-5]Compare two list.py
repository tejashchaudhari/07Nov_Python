l1=[1,2,3,4,5,6,7]
l2=[8,9,5,1,4,11,7]
l3=[]
for num in l1:
    if num in l2:
        if num not in l3:
            l3.append(num)
print(l3)