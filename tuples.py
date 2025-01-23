#tuples
print("Tuples")

#creating a tuple 
tuple = (1234, 5678, 'subash')
print(tuple)

#declaring single element in tuple
single_tuple = ("subash",) 
single_tuple1 = ("subash")
print(type(single_tuple))
print(type(single_tuple1))

# nesting a tuple
a = tuple, (1, 2, 3, 4, 5)
print(a)

#indexing in tuple / accessing tuples
print(tuple[0])
print(a[0])

#unpacking using * asterisk
fruits = ("apple", "orange", "cherry", "banana", "grapes")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)  #assingning remaining to single value

# tuples are immutable
# a[0] = 'hello'
# print(a)

#it can contain mutable objects
b = ([1, 2, 3], [4, 5, 6])
print(b)

#miltply tuples
multi = ("subash", "karhti", "logu")
my_multi = multi * 2
print(my_multi)

#index()
tuple1 = (1, 2, 3, 2, 4, 5, 2)
x = tuple1.index(2)
print(x) #only first occurrence

#count
y = tuple1.count(2)
print(y) #says the number of times it can occurred