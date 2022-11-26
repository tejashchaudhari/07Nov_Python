text=input("Enter the the text:")
if len(text)<2:
    print("Empty string..")
else:
    a=text[:2]
    b=text[-2:]
print("the text is :",a+b)