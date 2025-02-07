print('Iterators : ')

# using for loop for iteration
# num = [1, 2, 3, 4, 5]
# for i in num:
#     print(i)

# print("using iter")

# using iterator for iterating the values
# number = [1, 2, 3, 4, 5]
# num1 = iter(number)
# # using next
# print(num1.__next__())
# print(num1.__next__())
# print(num1.__next__())
# print(num1.__next__())

# creating own iterator using iterator in class
# class Max_num:
#     def __init__(self, number, range):
#         self.number = number
#         self.range = range

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.number <= self.range:
#             value = self.number
#             self.number += 1
#             return value
#         else:
#             raise StopIteration
# first_number = int(input("Enter the starting number : "))
# range_number = int(input("Enter the range to be iterated : "))        
# values = Max_num(first_number, range_number)

# # print(values.__next__())
# # print(values.__next__())

# for i in values:
#     print(i)


# generators

def numbers():
    n = 1
    while n <= 10:
        num = n * n
        yield num  # generator
        n += 1

square = numbers()
for i in square:
    print(i)

# normal list comprehension
list_com = [x**2 for x in range(1, 6)]
print("list comprehension for square : ", list_com)

# using generator comprehension
gen_com = (x**2 for x in range(1, 6))
print(gen_com)

# to print generatoe comprehension using next() and for loop
print(next(gen_com))

for x in gen_com:
    print(x)