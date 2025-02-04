print("Inheritance")

# inheritance -- inherit from single parent class
class Teacher:
    def greet(self):
        return f"Good morning everyone."
    
class Student(Teacher):
    pass
    
student = Student()
print(student.greet())

print("Multiple Inheritance : ")

# multiple inheritance -- inherit from multiple parent class
class Dad:
    def dad_wisdom(self):
        return "Dad's wisdom."
    
class Mom:
    def mom_wisdom(self):
        return "Mom's wisdom."
    
class Child(Dad, Mom):
    pass

child = Child()
print(child.dad_wisdom())
print(child.mom_wisdom())

print("Multilevel Inheritance : ")

# multilevel inheritance -- inherit from parent class which itself is a child for another parent class
class Person:
    def detail(self, name, age):
        self.name = name
        self.age = age
    
# class Employee(Person):
    

# hierarchical inheritance
class College:
    def __init__(self, name):
        self.name = name

    def department(self):
        return f"{self.name} is from NEC"
    
class Info_Tech(College):
    def department(self):
        return f"{self.name} is from Information Technology."
    
class Ece(College):
    def department(self):
        return f"{self.name} is from Electronics and Communication Engineering."
    
        
info_tech = Info_Tech("Subash")
ece = Ece("Logu")
clg = College("Karthi")
print(info_tech.department())
print(ece.department())
print(clg.department())