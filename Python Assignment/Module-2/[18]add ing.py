for i in range(3):
    text=input("Enter the spelling:")
    add='ing'
    if text[-3:]=='ing':
        a=text.replace('ing','ly')
        print(a)
    elif len(text)>=3:
        text=text+add
        print(text)
    else:
        print(text)