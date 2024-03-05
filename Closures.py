#Readonly
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
        
    data_transmitter()
    
print(transmit_to_space("Test message"))

#output Test message
# None

# nonlocal to change value in nested method
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number = 20
        print(number)
    printer()
    print(number)

print_msg(10)
#output 20 20


# return function object (creating closure)
def parent(value):
    "This is enclosing function"
    def child():
        print(value)
    child()
    return child

child2 = parent(23)
child2()
#output 23 23

#Exercise
def multiplier_of(value):
    "This is enclosing function"
    def multiply(val):
        "this is nested function"
        print(value* val)
    return multiply
multiplywith5 = multiplier_of(5)
multiplywith5(9)

#output 45
        



