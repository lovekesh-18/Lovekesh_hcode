# Multiple function arguments

def fun(first,second,third,*args):
    print("First: %s" %first)
    print("Second: %s" %second)
    print("Third: %s" %third)
    print("All the rest... %s" %(list(args),))
    
fun("Lovekesh","Kamboj","Jmit","Radaur","Haryana","India")

#output 
# First: Lovekesh
# Second: Kamboj
# Third: Jmit
# All the rest... ['Radaur', 'Haryana', 'India']

# Dictionary as a argument

def helper(first,second,third,**kwargs):
    if kwargs.get("action") == "sum":
        print("The sum is: %d" %(first+second+third))
    if kwargs.get("number") == "first":
        return first

result = helper(1,2,3,action="sum",number = "first")
print("Result: %d" %(result))

# args and kwargs

def new_fun(*args,**kwargs):
    for element in args:
        print(element)
    for k in kwargs:
        print("Name = %s"%k , "dist = %s"%kwargs[k])
    
new_fun("Hello","Lovekesh","Kamboj",name="Lovekesh",dist = "Yamunanagar")

#output 
# Hello
# Lovekesh
# Kamboj
# Name = name dist = Lovekesh
# Name = dist dist = Yamunanagar


# Exercise
def foo(a,b,c,*args):
    return len(args)

def bar(a,b,c,**kwargs):
    if kwargs.get("magicnumber") == 7:
        return True
    return False

if foo(1,2,3,4) == 1:
    print("Good")
if foo(1,2,3,4,5) == 2:
    print("Better")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")
    
#output 
# Good
# Better
# Great
# Awesome!
