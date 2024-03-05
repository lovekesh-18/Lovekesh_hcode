#Decorator

def deco(old_fun):
    def new_fun():
        old_fun()
        old_fun()
    return new_fun

@deco
def old_fun():
    print("Hello")

old_fun()

#output Hello Hello

def deco(my_fun):
    def new_fun(*args,**kwargs):
        my_fun(*args,**kwargs)
        my_fun(*args,**kwargs)
    return new_fun

@deco
def my_fun(*args,**kwargs):
    ans = 1
    for i in args:
        ans *= i
    print(ans)

my_fun(1,2,3,4)

# output 24 24

#OR

def deco(my_fun):
    def new_fun(*args,**kwargs):
        my_fun(*args,**kwargs)
        my_fun(*args,**kwargs)
    return new_fun

def my_fun(*args,**kwargs):
    ans = 1
    for e in args:
        ans *= e
    print(ans)
    
my_fun = deco(my_fun)
my_fun(1,2,3,4)
#output 24 24

def multiply(multiplier):
    def multiply_generator(old_function):
        def new_functiuon(*args,**kwargs):
            return multiplier * old_function(*args,**kwargs)
        return new_functiuon
    return multiply_generator

@multiply(3)
def return_num(num):
    return num
print(return_num(5))



def type_check(correct_type):
    def new_fun(old_fun):
        def return_fun(val):
            if type(val) == correct_type:
                return old_fun(val)
            else:
                print("Bad Type")
        return return_fun
    return new_fun

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])

#output 4
# Bad Type
# H
# Bad Type
