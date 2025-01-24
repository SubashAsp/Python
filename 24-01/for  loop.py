print("")
# for statement
animals = ["lion", "tiger", "elephant", "deer", "bear"]
for x in animals:
    print(x, len(x))

# Example
users = {
    'Subash': 'active',
    'Karthi': 'inactive', 
    'Deepan': 'active'
    }
# Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)

# creating a new copy
users1 = {
    'Subash': 'active',
    'Karthi': 'inactive', 
    'Deepan': 'active'
    }
active_users = {}
for user, status in users1.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

print("")
print("Range() function")
#Range() function
# to get numbers from specified range
a = 10
# a = int(input("Enter the range: "))
for i in range(a):
    print(i)

#to create a list for specificed range
b = list(range(1, 10))
print(b)

# using increment in range
c = list(range(2, 10, 3))
print(c)

# supporst negative increment
d = list(range(0, -100, -20))
print(d)

# combining range() & len()
e = ['subash', 'karthi', 'deepan']
for i in range(len(e)):
    print(i, e[i])

# using enumerate
for i in enumerate(e):
    print(i) 

# eg
print(range(10))

# adding in range
print(sum(range(7)))