print("Set")

#creating a set 
a = {1, 2, 3, 1}
print(a)  #does not allows duplicate

b = {"apple", "banana", "cherry", True, 1, 2, 0, False}
print(b)

#lenght
print(len(b))

#checking membership
print('apple' in b)
print('subash' in b)

#set operations
c = set('abracadabra')
d = set('alacazam')
print(c)
print(d)
print(c - d)  #letters in c but not in d
print(c | d)  #OR---in c or d or both
print(c & d)  #AND--in both c and d
print(c ^ d)  #NOR--in a or b but not both

#comperhension in set 
e = {x for x in 'abracadabra' if x not in 'abc'}
print(e)

#set methods

# add() -- addinfg single element to a set
add1 = {1, 2, 3, 4}
add1.add('subash')
print("Adding elements to set : ", add1)

# Only one element can be added using add method, it gives error to two elements at same time
# add2 = {1, 2, 3, 4}
# add2.add(10, "subash")
# print("Adding two elements to a set : ", add2)

#add one after another
add3 = {1, 2, 3, 4}
add3.add(10)
add3.add("subash")
print("Adding two elements", add3)

add_set = {1, 2, 3, 4, 5}
add_set.add(6)
print("Adding element to a set : ",add_set)

# only immutabe objects can be added to a set
# add_set1 = {1, 2, 3, 4}
# add_set2 = {5}
# add_set1.add(add_set2)
# print(add_set1)

add_set3 = {1, 2, 3, 4}
add_set4 = (5)
add_set3.add(add_set4)
print("Adding immutable object to a set : ", add_set3)

