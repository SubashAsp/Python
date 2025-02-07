from functools import reduce

# adding numbers using lambda functions
add = lambda x,y:x+y
print(add(23,7))

sub = lambda x,y:x-y
print(sub(23,3))

multi = lambda x,y:x*y
print(multi(5, 6))

div = lambda x,y:x/y
print(div(200, 10))

div1 = lambda x,y:x//y
print(div1(200, 10))

# immediately called function
print((lambda a,b:a+b)(2, 3))

# higher order function
hof = lambda x, func: x+func(x)
print(hof(2, lambda x:x*x))

# traceback
# s = lambda x:x/0
# s(3)

# filter()
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filt = list(filter(lambda x:x%2==0, number))
print(filt)

names = ['subash', 'suba', 'karthi', 'kar']
filter1 = list(filter(lambda x:len(x)>4, names))
print(filter1)

numbers = list()
numbers=[x for x in range(1,11)]
print(numbers)
# filter
even = list(filter(lambda x:x%2==0, numbers))
print(even)
# map()
mapping = list(map(lambda x:x**2, even))
print(mapping)
# reduce
reducing = reduce(lambda x, y:x+y, mapping)
print(reducing)