tk=[]
num=int(input("Enter the numbers:"))
sum=int()
for n in range(num):
    numbers=int(input("Enter the num:"))
    tk.append(numbers)
    sum=num+numbers

print("Largest num is:",max(tk),"\nsmallest num:",min(tk),"\nsum of num:",sum)
