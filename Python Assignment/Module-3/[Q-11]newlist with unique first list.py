def unique_list(l1):
    x=[]
    for a in l1:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1,2,3,4,4,4,5,6,7,7,7,8,9]))