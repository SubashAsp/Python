# 1.Write a Python program that sums all the numbers in a given list using a for loop.

number = [1, 2, 3, 4, 5, 6, 7 ,8, 9]
# number = input("Enter the numbers to be in list : ")
# number = number.split(" ")
# print(number)
total = 0
for i in number:
    total += int(i)

print(total)

# 2.Write a Python program that takes a list of integers and counts how many even and odd numbers are present using a for loop.

# numbers = [1, 1, 3, 3, 5, 6, 7, 8, 9]
numbers = input("Enter a list for checking odd or even numbers.")
numbers = numbers.split()
odd_count = 0
even_count = 0
for i in numbers:
    i = int(i)
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers in given list :", even_count)
print("Odd numbers in given list :", odd_count)
