print("Functions")
# initilizing a function

# def -- function definition followed by functiion name
def prime():  
    #statement inside a function
    print("Calling all autobots") 

# calling the functon
prime()  

# passing arguments 
def argu_fun(name):
    print('name: ',name)

argu_fun('Bumble Bee')

# passing more arguments
def more_argu(name1, name2):
    print(f'{name1} calling all {name2}')

more_argu('Optimus Prime', 'Autobots')

#arbitrary arguments
def multi_argu_fun(*name):
    a = len(name) - 1
    print('the youngest of all is : ', name[a])

multi_argu_fun('logu', 'karthi', 'suganth', 'subash')

#keyword arguments
def key_argu_fun(child1, child2, child3, child4):
    print("The youngest of all is : ", child4)

key_argu_fun(child1= 'logu', child2= 'karthik', child3= 'suganth', child4= 'subash')

#arbitrary keyword arguments
def arb_key_argu_fun(**name):
    print('first name is : ', name['first_name'])
    print('last name is : ', name['last_name'])

arb_key_argu_fun(first_name= 'Subash', last_name= 'Thiru')

#default parameter
def default_fun(name= 'subash'):
    print('My name is : ', name)

default_fun()  # no argu
default_fun('karthi')  #has argu

# using number
i = 5
def f(arg=i):
    print(arg)
    
i = 6
f()

# passing a list as argument
def list_fun(name):
    for x in name:
        print(x)

animal = ['lion', 'tiger', 'liger']
list_fun(animal)

#returning
# sharing same default bwt subsequent calls
def f(a, l = []):
    l.append(a)
    return l
print(f(1))
print(f(2))
print(f(3))

print()

# to avoid sharing of default bwt subsequent calls
def f1(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f1(1))
print(f1(2))
print(f1(3))

print()

# Positional only arguments
# to pass positional only arguments
def f2(p, /):
    print(p)

f2(3)

# how not to call positional only argument
# def f3(q, /):
#     print(q)

# f3(x = 3)
# key value pair cannot be passed in positional only argument

print()

# keyword only aruguments
def my_function(*, x):
  print(x)

my_function(x = 3)

# how not to call keyword only aruguments
# def my_function(*, x):
#   print(x)

# my_function(3) 

#Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8) 

#lambda expression
def make_incrementor(n):
    return lambda x: x + n

fun = make_incrementor(42)
print(fun(0))

#document string / documentation
def my_function():
    """Do nothing, but document it.
    """
    pass

print("Document String : ", my_function.__doc__)

# unpacking a tuple or list 
def unpacking_function(name, age, country):
    print(f"Hi, {name}! Your age is {age} and from {country}")

detail = ("Subash", 22, "India")
unpacking_function(*detail)

details = ["Subash", 22, "India"]
unpacking_function(*details)

#  using default parameter
def default_function(name= "Subash", age= 22, city = "Erode"):
    print(f"Hi, {name}! Your age is {age} and from {city}")

default_function()
default_function("Karthi")
default_function("Karthi", 23)
default_function("Karthi", 23, "Chennai")