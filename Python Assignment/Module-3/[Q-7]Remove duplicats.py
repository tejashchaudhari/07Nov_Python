mylist=["php","JAVA","Python","C++","JAVA","Python"]
dup=set()
for a in mylist:
    if a not in dup:
        dup.add(a)
print(dup)