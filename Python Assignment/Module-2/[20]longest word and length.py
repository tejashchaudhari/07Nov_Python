text=input("Enter the list of words:")
longest=0
for words in text.split():
    if len(words)>longest:
        longest=len(words)
        longest_words=words
print("longest words is:",longest_words)
print("length is:",len(longest_words))