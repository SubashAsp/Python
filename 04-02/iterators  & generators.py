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
