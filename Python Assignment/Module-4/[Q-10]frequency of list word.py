import os
from collections import Counter
f1=open("hello2.txt","r")
x=Counter(f1.read().split())
print(x)