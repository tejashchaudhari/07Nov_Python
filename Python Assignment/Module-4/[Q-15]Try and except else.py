# The else part is executed when no exception occurs.
try:
    a=int(input("Enter the number:"))
except:
    print("Error...!\nEnter the int num.")
else:
    print("This is python..")