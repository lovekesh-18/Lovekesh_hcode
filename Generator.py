t = 1

def lottery():
    global t
    for i in range(5):
        yield(t)
        t += 1

for element in lottery():
    print("Numbers in %d" %element)
    
#output 
# Numbers in 1
# Numbers in 2
# Numbers in 3
# Numbers in 4
# Numbers in 5

#OR 

def lottery_new():
    val = 1
    for element in range(5):
        yield(val)
        val += 1
    
iter = lottery_new()

try:
    while 1:
        print(next(iter))
except:
    pass

#output 1 2 3 4 5

# Exercise

def fib(a,b,n):
    while n:
        yield(a)
        a,b = b, a+b
        n -= 1 
a = 1
b = 1
n = 10
iter = fib(a,b,n)

try:
    while 1:
        print(next(iter),end=" ")
except:
    pass

# output 1 1 2 3 5 8 13 21 34 55

# for loop example

def helper(a,b,n):
    while n:
        yield(a)
        a,b = b, a+b
        n -= 1

a = 1
b = 1
n = 5
iter = helper(a,b,n)

for element in iter:
    print("Element are : %d" %element)

#output 
# Element are : 1
# Element are : 2
# Element are : 3
# Element are : 5


# function
def fib():
    a = 1
    b = 1
    n = 10
    while n:
        yield(a)
        a,b = b, a+b
        n -= 1


import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is generator")
    
cnt = 0
for n in fib():
    print(n)
    cnt += 1
    if cnt == 10:
        break