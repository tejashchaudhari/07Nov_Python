l1=[]
num=int(input("Enter the numbers:"))
for a in range(1,num+1):
    elem=int(input("Enter the elements:"))
    l1.append(elem)
l1.sort()
print("the sorted list:",l1)
print("Seconde smallest num in list is:",l1[1])