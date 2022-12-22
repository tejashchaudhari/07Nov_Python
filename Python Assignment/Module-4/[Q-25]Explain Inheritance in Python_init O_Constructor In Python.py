'''[Q-25]Explain Inheritance in Python with an example? What is init? Or What
Is A Constructor In Python? 

# --> Inheritance means which is use the property of other class.

'''
class Python :

    PythonStud=int(input ("Enter Python's Students :"))
    JavaStud=int(input("Enter Java's Student :"))


class Inheritance(Python) :
    
    def readdata (self):
        print ("Python Student is :",self.PythonStud)
        print ("Java Student is :",self.JavaStud)
i1=Inheritance()
i1.readdata()