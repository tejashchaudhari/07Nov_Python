try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print("division",a/b)
except TypeError:
    print("Unsopertrd operater.")
except ZeroDivisionError:
    print("division by 0 not allowed.")
print("Out of try except blocks.")
