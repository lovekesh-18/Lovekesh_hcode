from functools import partial

def add(a,b,c,d):
    return a+b+c+d
ltd = partial(add,10,10)
print(ltd(10,10))
#output 40



def add(a,b,c,d):
    return a+b+c+d

ltd = partial(add,a=10,c=10)
print(ltd(b = 10,d = 10))
#output 40



def multiply(x,y):
    return x*y

dbl = partial(multiply,2)
print(dbl(5))
#output 10


#Exercise
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
fun = partial(func,1,1,1)
print(fun(51))

#output 60
