f1=open("first.txt","r")
x=f1.readlines()
f2=open("second.txt","w")
for i in x:
    f2.write(i)
f2.close()