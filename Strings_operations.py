#single quotes
astring = "Lovekesh Kamboj!"
print("single quotes are ' '")
print(len(astring))  # 16

# find index
astring = "Hello world!"
print(astring.index('o'))

#output 4

#count character in word
astring = "Hello World!"
print(astring.count("l"))

#output 3

# slicing
astring = "Hello world!"
print(astring[3:7])

#output lo w

# increase step in slicing
astring = "Hello World!"
print(astring[3:7:2])

#output l

astring = "Hello World!"
print(astring[3:7])
print(astring[3:7:1])

#output lo w    
# lo w

#reverse string
astring = "Hello World!"
print(astring[::-1])

#output !dlroW olleH

# check startswith and endwith
astring = "Hello World!"
print(astring.startswith("Hello"))
print(astring.endswith("sadndkjfbd"))

#output True 
# False

# split string into list
astring = "Hello World!"
words = astring.split()
print(words)


#Exercise
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

