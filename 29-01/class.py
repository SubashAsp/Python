print("")
#class

class new_class:

    def state(self):
        print("Hello.")

class second_class:
    def state2(self):
        print("Welcome")

greet = new_class()
greet2 = second_class()

new_class.state(greet)  #  method to call function  inside a class
greet.state()  # calling using a class object 
