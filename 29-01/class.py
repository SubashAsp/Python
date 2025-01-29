print("")
#class

class new_class:
    # namespace is created
    def state(self):  # method (function)
        print("Hello.")

class second_class:
    def state2(self):
        print("Welcome")

greet = new_class()
greet2 = second_class()

new_class.state(greet)  #  method to call function  inside a class
greet.state()  # calling using a class object 

# greet2.state()  // you cannot call a method in a class with different class object

# declaring a local scope
class new_cls:
    def new_fun():
        x = 10  # local scope / local variable

# () is used to call the class or create an instance
num = new_cls()  
# instance is created

# print(x)
# we cannot call a variable that iss defined inside a method outside directly

# Attributes
# class attributes
class Bike:
    wheels = 2  # Class attribute

    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute

# Create instances of the Car class
bike1 = Bike("Hero", "Splendor")
bike2 = Bike("Honda", "Shine")

# Accessing class attribute
print(bike1.wheels) 
print(bike2.wheels)  

# Accessing instance attributes
print(bike1.brand)  
print(bike2.model)  
