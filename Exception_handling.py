# try and except

def do_stuf(n):
    print(n)

def catch_this():
    list = (1,2,3,4,5)

    for i in range(10):
        try:
            do_stuf(list[i])
        except IndexError:
            do_stuf(0)
catch_this()

# try except finally else

def fun(a,b):
    try:
       return a/b
    except ZeroDivisionError:
        print("Not able to divide")
        return 0
    else:
        print("In else")
    finally:
        print("In Finally")

print(fun(10,0))

# Not able to divide
# In Finally
# 0

#Nested Try
try:
    print("line1")
    print("line2")
    try:
        print("line3")
        a = 4/0
        print("line4")
    except TypeError:
        print("Except1")
    else:
        print("Else1")
    finally:
        print("Finally1")
except:
    print("Except2")
else:
    print("Else2")
finally:
    print("Finally2")
    
#output
# line1
# line2
# line3
# Finally1
# Except2
# Finally2

try:
    print("line1")
    print("line2")
    x = 3/0
finally:
    print("finally1")
    
#output 
# line1
# line2
#finally1
# <default error mechanism

# Raise error
x = 10
y = 0
try:
    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    z = x/y
    print("Division is ",z)
except ZeroDivisionError as e:
    print(e)
    
# output Denominator cannot be zero

#user defined exception

class Insufficient_balance(IndexError):
    def __init__(self,msg):
        self.msg = msg

balance = 5000
withdraw = 7000
try:
    if withdraw > balance:
        raise Insufficient_balance("Balance is not enough")
    balance = balance - withdraw
except Insufficient_balance as i:
    print(i.msg)
else:
    print("Withdrawl successfull")
finally:
    print("balance = ", balance)    
    
#output
#Balance is not enough
# balance =  5000
    
