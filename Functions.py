# Functions

def fun():
    print("Hello from fun!")

fun()

# passing argument

def my_fun(username,greeting):
    print("Hello %s!, %s!" %(username,greeting))
    
my_fun("Lovekesh","Good Morning")

# return value from function
def sum(a,b):
    return a + b

print(sum(4,5))
#output 9

# Excercise
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
def build_sentence(benefit):
    return benefit + " is a benefit of functions!"
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

#output
# More organized code is a benefit of functions!
# More readable code is a benefit of functions!
# Easier code reuse is a benefit of functions!
# Allowing programmers to share and connect code together is a benefit of functions!

