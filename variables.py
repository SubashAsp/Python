import random

# print statement
print("Hello World")

# printing new line
print("\n")

# variables
a = 20
b = "subash"
print(a)
print(b)

print("\n")

# typeof
print(type(a))
print(type(b))

print("\n")

# casting in python
c = int(7)
d = float(7)
e = str(7)
print(c, type(c))
print(d, type(d))
print(e, type(e))

print("\n")

# variableNames
# camelCase
variableName = 10 
print(variableName)
#PascalCase
VariableName = 10 
print(VariableName)
 #snake_case
variable_name = 10
print(variable_name)

print("\n")

# assigning multiple values to multiple variables
f, g, h = "subash", 22, "Erode"
print(f, g, h)

print("\n")

# assigning single value to miltiple variables
i = j = k = "aspire"
print(i, j, k)

print("\n")

# unpack a collection
animals = ["cat", "dog", "ottor"]
l, m, n = animals
print(l)
print(m)
print(n)

print("\nGlobal variable")

#global variable
o = "subash"
def newfunction():
    print(o)

newfunction()

#--defining inside a function
def sec_function():
    o = "karthi"    #defined inside a function
    print("mentioned inside a function : ",o)

sec_function()
print(o)
    
#--using global keyword
def thir_funct():
    global o
    o = "karthi"

thir_funct()
print("Using global keyword : ",o)

print("\nNumbers")
#Numbers
p = 1
q = 1.0
r = 1j

print(type(p))
print(type(q))
print(type(r))

#random numbers
print("\nRandom Number")

s = random.randrange(1, 10)
print(s)
