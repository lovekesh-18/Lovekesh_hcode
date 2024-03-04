import re

# Starts with or ends with

txt = "The Rain in Spain"
x = re.search("^The.*Spain$",txt)
print(x)
if x:
    print("YES!")
else:
    print("No")
    
#set of characters
x = re.findall("[a-m]",txt)
print(x)
#output ['h', 'e', 'a', 'i', 'i', 'a', 'i']

x = re.findall("ai",txt)
print(x)
#output ['ai', 'ai']

x = re.search("\s",txt)
print(x.start())

#output 3

x = re.split("\s",txt)
print(x)
#output ['The', 'Rain', 'in', 'Spain']

x = re.split("\s",txt,1)
print(x)
#output ['The', 'Rain in Spain']

x = re.sub("\s","9",txt)
print(x)
#output The9Rain9in9Spain

x = re.sub("\s","9",txt,2)
print(x)
#output The9Rain9in Spain

x = re.search("ai",txt)
print(x)
#output <re.Match object; span=(5, 7), match='ai'>

x = re.finditer("[A-Z]ain",txt)
for match in x:
    print(match)
#output <re.Match object; span=(4, 8), match='Rain'>