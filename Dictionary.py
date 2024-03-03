# Dictinoary

phonebook = {}
phonebook["John"] = 1234567890
phonebook["Lovekesh"] = 9876543210
phonebook["jill"] = 1264387890

print(phonebook)

#output {'John': 1234567890, 'Lovekesh': 9876543210, 'jill': 1264387890}

# OR

phonebook = {
    "John" : 1234567890,
    "Lovekesh" : 9876543210,
    "jill" : 1264387899
}
print(phonebook)

#Iterating over dictionaries

for key,value in phonebook.items():
    print("Name = %s, Phone = %s" %(key,value))

#output
# Name = John, Phone = 1234567890
# Name = Lovekesh, Phone = 9876543210
# Name = jill, Phone = 1264387899

#Removing value

del phonebook["John"]
print(phonebook)

# above code del the key value but if key is not found then it shows error

# pop
phonebook.pop("jill")
print(phonebook)
#output {'Lovekesh': 9876543210}

# Excercise
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
phonebook["Jake"] = 938273443
del phonebook["Jill"]
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")
    
#output 
# Jake is listed in the phonebook.
# Jill is not listed in the phonebook.
