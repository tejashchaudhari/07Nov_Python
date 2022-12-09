dic={'a':1,'h':2,'c':3,'d':4}
if dic.get('a')is not None:
    print("yes")
else:
    print("no")
print(dic['a'])

if dic.get('e')is not None:
    print("yes")
else:
    print("no")
dic=int(input("enter your key:"))