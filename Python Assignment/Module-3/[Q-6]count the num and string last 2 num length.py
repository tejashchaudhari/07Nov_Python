words= ['abc','aba','xyz','1122','def']
count=0
for word in words:
    if len(word)>1 and word[0]==word[-1]:
        count += 1
print(count)