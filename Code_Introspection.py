#dir()
x = [1,2,3]
print(dir(x))
#output: It tells us about the attribute and methods of a specific object

# display documentation of objects,classes,function,method
#help()
# print(help(x))


#hasattr()
print(hasattr(x,'append'))
print(hasattr(x,'insert'))
print(hasattr(x,'reverse'))
print(hasattr(x,'backup'))
#output True True True False

#id()
print(id(x))
a = 20
b = 20
print(id(a),id(b))
#output id of object is random

#type()
print(type(x))
#output <class 'list'>

#repr()
print(repr(x))
print(type(repr(x)))
#output [1, 2, 3]
# <class 'str'>


#callable()
def fun():
    print("My Function")
    
class Car:
    def __init__(self):
        self.a = 20

obj = Car()

print(callable(fun))
print(callable(Car))
print(callable(obj))
print(callable(10))
# output True True False False

class Car:
    def __call__(self):
        print("Now object is callable")

obj = Car()
print(callable(obj))
#output True

# issubclass
class Animal:
    pass
class Dog(Animal):
    pass
class Cat:
    pass

print(issubclass(Dog,Animal))
print(issubclass(Cat,Animal))
print(issubclass(Dog,object))
#output True False True


#isinstance()
class Animal:
    pass
class Dog(Animal):
    pass
class Cat:
    pass

dog_instance = Dog()
cat_instance = Cat()

print(isinstance(dog_instance,Dog))
print(isinstance(dog_instance,Animal))
print(isinstance(cat_instance,Cat))
print(isinstance(cat_instance,Animal))
#output True True True False

# __doc__
def greet(name):
    '''
    This is greet function docstring
    '''
    print("Hello")
    
    
class Myclass:
    '''
    This is myclass docstring
    '''
    def myfun(self):
        '''
        This is myfun docstring
        '''
        
print(greet.__doc__)
print(Myclass.__doc__)
print(Myclass.myfun.__doc__)


# __name__

if __name__ == '__main__':
    print("In main")
#output In main