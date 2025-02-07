# 1. to generate even numbers in a given list
given_list= [1, 2, 3, 4, 5, 6, 7, 8, 9]
gen = (x for x in given_list if x%2==0)
for i in gen:
    print(i, end=" ")
print()

# 2. to generate to give square of the even numbers in the given list
gen1 = (x**2 for x in given_list if x%2==0)
for i in gen1:
    print(i, end=" ")
print()