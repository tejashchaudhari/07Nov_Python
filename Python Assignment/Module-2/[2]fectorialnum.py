num=int(input("Enter the number: "))
factorial=1
if num>=1:
    for i in range(1,num+1):
        factorial=factorial*i
print("factorial is given number is: ",factorial)