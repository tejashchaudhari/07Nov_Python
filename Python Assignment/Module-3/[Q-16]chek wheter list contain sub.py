l1=['A','B',[1,3,4,"Python"]]
for a in l1:
    if len(a)>1:
        print("sublist in list1:")
        break 
else:
    print("sublist not in list1:")