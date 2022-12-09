L = [{"V":"1"}, {"V": "2"}, {"VI": "1"}, {"VI": "5"}, {"VII":"5"},]
print("List is: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)