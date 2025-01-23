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