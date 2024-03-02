# Aritematic Operators
#add multiply divide
num = 1 + 2 *3 /4.0
print(num)

# output = 2.5

#remainder
rm = 11%3
print(rm) 
#output 2


# power
squared = 7 ** 2
cubed = 2 ** 3
print(squared) 
print(cubed)

# output 49 8

# Using Operators with Strings
fullname = "Lovekesh" + ' ' + "Kamboj"
print(fullname)

#output Lovekesh Kamboj

# multiplying string with int
hello = "hello"*10
print(hello)

#output hellohellohellohellohellohellohellohellohellohello

#Using Operators with Lists
even_list = [2,4,6,8]
odd_list = [1,3,5,7]
sum_list = even_list + odd_list
print(sum_list)

#output [2, 4, 6, 8, 1, 3, 5, 7]

print([1,2,3]*3)
#output [1, 2, 3, 1, 2, 3, 1, 2, 3]

#Excercise
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_lits contain %d objects" %len(x_list))
print("y_list contains %d objects" %len(y_list))
print("big_list conatins %d objects" %len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there....")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great")
    
# output 
'''x_lits contain 10 objects
y_list contains 10 objects
big_list conatins 20 objects
Almost there....
Great '''