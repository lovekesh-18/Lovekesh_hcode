#List Comprehensions

sentence = "the quick browm for jumps over the lazy dog"
new_list = []
words = sentence.split()
for word in words:
    if word != "the":
        new_list.append(len(word))

print(new_list)

#output [5, 5, 3, 5, 4, 4, 3]

#or
sentence = "the quick brown for jumps over the lazy dog"
words = sentence.split()
new_list = [len(word) for word in words if word != "the"]
print(new_list)

#output [5, 5, 3, 5, 4, 4, 3]

#Exercise

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []
for number in numbers:
    if number >= 0:
        newlist.append(int(number))

print(newlist)

#output [34, 44, 68, 44, 12]

# OR
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(number) for number in numbers if number >= 0]
print(newlist)

#output [34, 44, 68, 44, 12]