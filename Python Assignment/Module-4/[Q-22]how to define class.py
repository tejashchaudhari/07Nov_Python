'''how to difine class..?
 ---> using class keyword to difine class.

 what is self?
 --->If method is declared in class. Argument 
    must be declared in the function.


self represents the instance of the class.
By using the “self” we can access the attributes and methods of the class in python.
It binds the attributes with the given arguments.
The reason you need to use self is because Python does not use the @ syntax to refer to instance attributes.'''


class student:
    stid=12
    stname="Tejash"
    def showdata(self):
        print("this is Tejash")
    
st=student()
print(st.stid)
print(st.stname)
st.showdata()