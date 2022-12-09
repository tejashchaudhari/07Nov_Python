st = input("Enter a string: ")
dic = {}
for i in st:
    if i in dic: 
        dic[i] += 1
    else:
        dic[i] = 1 
for key in dic:
    print(key,':',dic[key])