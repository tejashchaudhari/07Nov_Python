import math
class circle:
    radius=float(input("Enter the redious of the:"))
    
    def area(self):
        area=math.pi*pow(self.radius,2)
        print("Area of circle:",area)
    def perameter(self):
        perameter=2*math.pi*self.radius
        print("perameter of circle:",perameter)
c1=circle()
c1.area()
c1.perameter()
