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