# Map

low = ['lovekesh','kamboj','yamunanagar']
up = list(map(str.upper,low))
print(up)
#output ['LOVEKESH', 'KAMBOJ', 'YAMUNANAGAR']

circle_area = [3.56773,5.57668,4.00914,56.24241,9.01344,32.00013]
result = list(map(round,circle_area,range(1,7)))
print(result)
#output [3.6, 5.58, 4.009, 56.2424, 9.01344, 32.00013]

circle_area = [3.56773,5.57668,4.00914,56.24241,9.01344,32.00013]
result = list(map(round,circle_area,range(1,3)))
print(result)
#output

my_string = ['a','b','c','d','e']
my_number = [1,2,3,4,5]
result = list(zip(my_string,my_number))
print(result)
#output [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

my_string = ['a','b','c','d','e']
my_number = [1,2,3,4,5]

result = list(map(lambda x,y:(x,y),my_string,my_number))
print(result)
#output [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

def cube(a):
    return a*a*a

l = [1,2,3,4]
result = list(map(cube,l))
print(result) 
#output [1, 8, 27, 64]


# Filter
def helper(score):
    return score > 75

scores = [66,90,68,59,76,60,88,74,81,65]
result = list(filter(helper,scores))
print(result)
#output [90, 76, 88, 81]

dromes = ("demigod","rewire","madam","freer","anutforajaroftuna","kiosk")
result = list(filter(lambda word:word == word[::-1] , dromes))
print(result)
#output ['madam', 'anutforajaroftuna']


# Reduce
from functools import reduce

numbers = [3,4,6,9,34,12]

def sum(first,second):
    return first + second

result = reduce(sum,numbers)
print(result)
#output 68

result = reduce(sum,numbers,10)
print(result)
#output 78

#Exercise
my_floats = [4.35,6.09,3.25,9.77,2.16,8.88,4.59]
my_names = ["olumide","akinremi","josiah","temidayo","omoseun"]
my_numbers = [4,6,9,23,5]

map_result = list(map(lambda num:round(num**2,3) , my_floats))

filter_result = list(filter(lambda word: len(word) <= 7, my_names))

reduce_result = reduce(lambda x,y:x*y , my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)

#output [18.922, 37.088, 10.562, 95.453, 4.666, 78.854, 21.068]
# ['olumide', 'josiah', 'omoseun']
# 24840

str = "Lovekesh Kamboj"
result = list(map(lambda c:c.upper(),str))
print(result)

