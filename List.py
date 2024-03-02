# creating a list and appending element in list and print

mylist = [] # empty list
mylist.append(10)
mylist.append(20)
mylist.append(30)

print(mylist[0])
print(mylist[1])
print(mylist[2])
#output 10 20 30
#print(mylist[3]) #error out of range

for e in mylist:
    print(e)
#output 10 20 30

# Exercise
numbers = []
strings = []
names = ["John","Eric","Jessica"]
second_name = names[1]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

print(numbers)
print(strings)
print("The second name on the name list is %s" %second_name)

#output [1,2,3]
#["hello" , "world"]
#The second name on the name list is Eric