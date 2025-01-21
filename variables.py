import random

# print statement
print("Hello World")

# printing new line
print("\n")

#comment Line

#this is a comment line
"""
Multiple
comment
line
"""

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

print("\nStrings")
#Strings
#multiline string

t = """This
is a
multiline string"""
print("multi line string : \n",t)

#Strings are arrays
u = "Subash"
print("string in array : ",u[0])

#string length
v = "subash"
print("string length : ",len(v))

#to check presence of substring
#IN method
w = "Python is the best language."
print("presence of substring : ","best" in w)

#using if condition
x = "Python is the best language."
if "free" in x :
    print("presecnce of sub string is found.")

#NOT method
y = "Python is the best language."
print("worst" not in y)

#using if condition
z = "Python is the best language."
if "worst" not in z :
    print("Not a sub string.")

print("\nLooping through string")
#Looping through string
for A in "subash":
    print(A)

print("\nSlicing Strings")
#Slicing Strings
B = "subash"
print(B[0:3])  #for last index given value -1

#slice from the start
print("slicing from start : ", B[:len(B)])

#slice to end
print("slicing to end : ", B[1:])

#negative indexing
print("negative indexing : ", B[-5:-1])

print("\nModifying Strings.")
#modifying string

#upper case
C = "subash"
D = C.upper()
print(D)

#lower case
print(D.lower())

#remove whitespace
E = " Hello, everyone "
print(E.strip())  #removes white space before/after a text

#split string
print(E.split(","))  #splits the text into sub string if it finds a seperator

#replace string
print(E.replace("Hello", "Hi"))

print("\nconcatenation in string")
#concatenation of string
F = "Hello"
G = "Subash"
print(F + G)
print(F + " " +G)

print("\n Format strings")
#format string
#F-string
H = 22
I = f"My age is {H}"  #{} placeholder
print(I)
J = f"your balance is {H:.2f}"
print(J)

print("\n")
print("\n Boolean")
#boolean
print(10 > 9)
