# # defining a class
# class My_Class:
#     def my_function(a, b):
#         return a+b 
    
# add = My_Class
# print(add.my_function(6, 5))

# # using __init__ meethod

# class New_Class:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
        
# add1 = New_Class(6,5)
# print(add1.add())

# # self method
# class Next_Class:
#     def __init__(self,value):
#         self.value=value
#     def new_func(self,value):
#         print(f'Self value : {self.value}')
#         print(f'Passed value : {value}')

# num = Next_Class(30)
# num.new_func(20)

# public method
class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    
    def display_info(self):  
        print(f"Name:{self.name}, Age:{self.age}")
        
person = Person("Subash", 22)
person.display_info()

# private method
class Detail:
    def __init__(self, name, degree):
        self.__name = name
        self.__degree = degree
    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__degree}")
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

person = Detail("Subash", "IT")
print(person.get_name())
person.set_name("Suresh")
print(person.get_name())

