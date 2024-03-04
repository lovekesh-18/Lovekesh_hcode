print(set("my name is Lovekesh and Lovekesh is my name"))
#output {'v', 'm', 'i', 'k', 'a', 'o', 'L', 'y', ' ', 'd', 's', 'e', 'h', 'n'}

print(set("my name is Lovekesh and Lovekesh is my name".split()))
#output {'is', 'Lovekesh', 'my', 'and', 'name'}

a = set(["Jake","John","Eric"])
print(a)
#output {"Jake","John","Eric"}

b = set(["John","Jill"])
print(b)
#output {"John","Jill"}

a = set(["Jake","John","Eric"])
b = set(["John","Jill"])
print(a.intersection(b))
print(b.intersection(a))

#output {"John"}
#{"John"}

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
#output {'Jill', 'Eric', 'Jake'}
# {'Jill', 'Eric', 'Jake'}

print(a.difference(b))
print(b.difference(a))
#output {'Jake', 'Eric'}
# {'Jill'}

print(a.union(b))
#output {'Jill', 'John', 'Jake', 'Eric'}

#Exercise
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
x = set(a)
y = set(b)
print(x.difference(y))
# output {'Jake', 'Eric'}

s = set()
s.update([1,2,3],(1,2,3))
print(s)

# output {1,2,3}

s.discard(2)
print(s)
#output {1,3}

s.remove(1)
print(s)
#output {3}