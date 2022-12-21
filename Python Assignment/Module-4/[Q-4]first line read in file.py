n=int(input("Enter the lines to read:"))
f=open("hello.txt","r")
# f=open("test.txt","r")
for i in range(n):
    print(f.readline())