n=int(input("Enter the lines to read:"))
f=open("test.txt","r")
for i in (f.readlines()[-n:]):
    print(i,end="")