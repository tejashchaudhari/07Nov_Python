name=input("Enter the name:")
len=len(name)
if len%4==0:
    len-=1
    for i in range(len,-1,-1):
        print(name[i],end="")
else:
    print("Eroor")


"""name=input("Enter the name:")
if(len(name)%4==0):
    print(name[::-1])
else:
    print("Eroor")"""