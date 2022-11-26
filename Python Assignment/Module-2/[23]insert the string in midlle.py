mystring=input("Enter the string:")
lenstring=len(mystring)
midlen=lenstring //2
midstring=input("Enter the midalle string:")
print(mystring[:midlen] + midstring + mystring[midlen:])