# create a class

class MyClass():
    variable = 20   #static
    
    def fun(self):
        print("This is instance member function!")
        
obj1 = MyClass() #object
print(obj1.variable)
print(MyClass.variable)

#output 20 20

#example of multipli object of same class
class My_class():
    variable = "blah"
    
    def fun(self):
        print("Instance member function")

obj1 = My_class()
obj2 = My_class()

obj1.variable = "Lovekesh"

print(obj1.variable)
print(obj2.variable)
print(My_class.variable)

#output Lovekesh blah blah

# constructor in python

class New_class():
    def __init__(self,number):
        self.number = number #instance variable
    
    def fun(self):
        return self.number

obj = New_class(7)
print(obj.fun())

#output 7

#excercise
class Vehicle():
    kind = "car"
    def __init__(self,name,color,value):
       self.name = name
       self.color = color
       self.value = value
    
    def desc(self):
        str = "%s is a %s %s worth $%.2f." %(self.name,self.color,self.kind,self.value)
        return str
    
car1 = Vehicle("Fer","red",60000.00)
car2 = Vehicle("Jump","blue",10000.00)

print(car1.desc())
print(car2.desc())    

#output Fer is a red car worth $60000.00.
# Jump is a blue car worth $10000.00.
