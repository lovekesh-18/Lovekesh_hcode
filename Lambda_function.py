# Simple Function

def sum(a,b):
    return a+b

a = 20
b = 40
print(sum(a,b))

#output 60

# lambda function

sum = lambda a,b:a+b
print(sum(10,20))

#output 30

#OR
sum = (lambda a,b:a+b)(10,20)
print(sum)

#output 30

# Factorial using lambda function

fact = lambda n:1 if n == 1 else n*fact(n-1)
print(fact(5))

#Exercise
fun = lambda a:False if a%2 == 0 else True

l = [2,4,7,3,14,19]
for element in l:
    if fun(element):
        print("True")
    else:
        print("False")

# output 
# True
# True
# False
# False
# True
# False