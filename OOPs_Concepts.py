class SimpleClass():  #class

    def __init__(self,name): # constructor method called on object formation
        self.name = name
        print(name)


    def NAm(self):
        print("Hello")
        print("My name is " + self.name)

#S1=SimpleClass("aashi")
#S1.NAm()

#x= "aashi"
#print(type("AASHI"))

class ExtendedClass(SimpleClass): # inherits Simple Class
    def __init__(self):
        super().__init__("AASHI")  # calls all the content of parent class
        super().NAm()
        print("EXTENDS!")

S2=ExtendedClass()






