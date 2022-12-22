class rectangle:
    def showdata(self,l,w):
        self.length=l
        self.width=w

    def rectanglearea(self):
        return self.length*self.width
re=rectangle()
re.showdata(10,10)
print(re.rectanglearea())
