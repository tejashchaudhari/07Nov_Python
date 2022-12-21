f= "test.txt"
with open(f, 'r') as filedata:
    wordsList = filedata.read().split()
longestWord= len(max(wordsList, key=len))
result = [textword for textword in wordsList if len(textword) == longestWord]
print("logest word is:")
print(result)