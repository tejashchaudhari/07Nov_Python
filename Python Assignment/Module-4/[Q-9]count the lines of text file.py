f1=open("test.txt","r+")
n=0
for i in f1:
    print(f"line:{n}={i}")
    n+=1
f1.close()