#String Formatting

name = "Lovekesh"
print("Hello, %s!" %name)
#output "Hello, Lovekesh!"

name = "Lovekesh"
age = 21
print("%s is %d year old" %(name,age))
#output  "Lovekesh is 21 year old"

mylist = [1,2,3]
print("A list: %s" %mylist)
#output A List: [1,2,3]


#%x/%X - Integers in hex representation (lowercase/uppercase)
x= 255
hex_small_x = "{:x}".format(x)
print(hex_small_x)
#output ff

hex_large_x = "{:X}".format(x)
print(hex_large_x)
#output FF

#Exercise

data = ("Lovekesh","Kamboj",53.44)
format_string = "Hello %s %s. Your current balance is $%.2f"

print(format_string % data)

