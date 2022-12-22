try:
    a=int(input("Enter the value of A:"))
    b=int(input("Enter the value of B:"))
    print("MUltiplication is:",a*b)
except:
    print("Error....!\nEnter the int Numbers...")
finally:
    print("this is finally.")