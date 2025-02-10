import math
import random
import my

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
# class Person:
#     def __init__(self, name, age):
#         self.name = name  
#         self.age = age    
#     def display_info(self):  
#         print(f"Name:{self.name}, Age:{self.age}")
        
# person = Person("Subash", 22)
# person.display_info()

# # private method
# class Detail:
#     def __init__(self, name, degree):
#         self.__name = name
#         self.__degree = degree
#     def display_info(self):
#         print(f"Name: {self.__name}, Degree: {self.__degree}")
#     def get_name(self):
#         return self.__name
#     def set_name(self, name):
#         self.__name = name

# person = Detail("Subash", "IT")
# print(person.get_name())
# person.set_name("Suresh")
# print(person.get_name())

# class Private_cls:
#     def __init__(self):
#         self.__name = "Subash"
#     def user_name(self):
#         print(self.__name)    

# detail=Private_cls()
# detail.name="karthi"
# detail.user_name()


# random number guess
# secert_number = random.randint(1, 10)
# print(secert_number)
# guess_count = 0
# guess_limit = 3
# guess_left = 3
# while guess_count < guess_limit:
#         try:
#             guess = int(input("Guess: "))
#             guess_count += 1
#             if guess == secert_number :
#                 print('You won!')
#                 break
#             else:
#                 guess_left -= 1
#                 print("Guess left : ", guess_left)
#         except(ValueError):
#             print("Enter an integer.")
# else:
#     print('Sorry, you failed!')

# # car game
# start_count = 0
# stop_count = 0
# while True:
#     command = input("Enter the command : ").lower()
#     if command == "start":
#         if start_count == 0:
#             print("Car started. Get ready.")
#             start_count = start_count + 1
#         else:
#             print("The car is already started.")
#     elif command == "stop":
#         if stop_count == 0:
#             print("Car stopped.")
#             stop_count = stop_count + 1
#         else:
#             print("The car is already stopped.")
#     elif command == "help":
#         print("""
# start - to start the car.
# stop - to stop the car.
# quit - to quit.
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Please enter 'help' for assitance.")

# to find the largest in list
list_numbers = [5, 4, 6, 9, 1]
max_num = 0
for x in list_numbers:
    if x > max_num:
        max_num = x
print(max_num)