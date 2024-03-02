#conditions

x = 2
print(x == 2)
print(x == 3)
print(x < 3)

#output True False True

# Boolean operators
name = "Lovekesh"
age = 21
if name == "Lovekesh" and age == 21:
    print("You are Lovekesh and you are 21 year old")
if name == "Lovekesh" or name == "Devrath":
    print("Your name is either Lovekesh or Devrath")

#output You are Lovekesh and you are 21 year old
#your name is either Lovekesh or Devrath

#in operator
name = "John"
if name in ["Lovekesh",'John']:
    print('Your name is either Lovekesh or John')
#output Your name is either Lovekesh or John
    
x = 2
if x == 2:
    print('x equal two!')
else:
    print('x does not equal to two')

# output x equal two!

#is operator
x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)

#output True
#false

x = 2
y = 2.0
print(x == y)
print(x is y)

# output True
# False

#not operator
print(not False)
print(not False)

#output True False

#Exercise
number = 20
second_number = 10
first_array = [1,2,3]
second_array = [4,5]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
