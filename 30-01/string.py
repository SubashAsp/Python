import roman

print('\nString\n')

# string operations

# defining a string
# single quotes
single_quotes_str = 'This is a single quotes string.'
print(single_quotes_str)

# double quotes
double_quotes_str = "This is a double quotes string."
print(double_quotes_str)

# multiline string
multiline_str = '''This is a 
multiline string 
in single quotes'''
print(multiline_str)

multiline_str1 = """This is a
multiline string 
in double quotes"""
print(multiline_str1)

# to get a string from user
# user_str = input("Enter the string : ")
# print("User given string : ", user_str)

# Adding / Concatenation of two strings
str1 = "Subash"
str2 = "Thiru"
print(str1+str2)
print(str1+"."+str2)
print(str1+" "+str2)
print(str1+", "+str2)

# using .join method
str3 = ["Subash","Thiru"]
print(" ".join(str3))

print(", ".join([str1,str2]))

# using f string
print(f"{str1} {str2}")

# --------------------------------------------------
# repeating string/multiplying a string
print(str1*3)

# --------------------------------------------------
# indexing / accessing a string
str4 = "subash"
print(str4[0])

# using index method
a = str4.index('s')
print(a)

# -----------------------------------------------------
# slicing a string
print(str4[0:3])
print(str4[0:])
print(str4[:3])
print(str4[:])
print(str4[::2])

#--------------------------------------------------------------------------------------------------------------------------
#string methods

# length of the string
str5 = "hi hello welcome"
print(len(str5))

# to uppercase
print(str5.upper())

# to lowercase
print(str5.lower())

# strip() - to remove space in starting and ending of the string
str6 = "    hi hello welcome    "
print(str6.strip())

# lstrip() - to remove space in starting
print(str6.lstrip())

# rstrip() - to remove space in ending
print(str6.rstrip())

# replace a sub string
print(str6.replace("welcome","good morning"))

# spliting a string
# str7 = input("enter a string : ")
# str7 = str7.split(" ")
# print(str7)

# joining string / join()
# print(",".join(str7))

# finding a element in a string
str8 = "good morning everyone"
print(str8.find("one"))

# count
c = str8.count('o')
print(c)

# starts with
print(str8.startswith("good"))

# ends with
print(str8.endswith("bye"))

# capitalize
print(str8.capitalize())

# title
print(str8.title())

# checking given string only consists of alphabets -- isalpha()
alpha_str = "hello"
print(alpha_str.isalpha())

alpha_str1 = "hello123"
print(alpha_str1.isalpha())

# checking given string only contains of numbers -- isdigit()
digit_str = "1234"
print(digit_str.isdigit())

digit_str1 = "XII"
print(digit_str1.isdigit())

digit_str2 = "1.23"
print(digit_str2.isdigit())

# checking given string only contains of numbers, numeric -- isnumeric()
numeric_str = "12345"
print(numeric_str.isnumeric())

numeric_str1 = "XII"
print("numeric : ", numeric_str1.isnumeric())

numeric_str1 = "1.23"
print(numeric_str1.isnumeric())

# checking given string contains alpha numeric value -- isalnum()
alnum_str = "subash123"
print(alnum_str.isalnum())

alnum_str1 = "1234"
print(alnum_str1.isalnum())

alnum_str2 = "subash"
print(alnum_str2.isalnum())

alnum_str3 = "1.23"
print(alnum_str3.isalnum())

# checking contaions only white space
space_str = " "
print("space : ", space_str.isspace())

space_str1 = "subash thiru"
print(space_str1.isspace())

# checking the string title case
title_str = "subash thiru"
title_str  =title_str.title()
print("title cased :", title_str.istitle())

# centers the string -- center()
center_str = "subash"
print("center :",center_str.center(10,"-"))

# justifies left side
ljust_str = "subash"
print("ljust :", ljust_str.ljust(10,"-"))

# justifies right side
rjust_str = "subash"
print("rjust :", rjust_str.rjust(10,"-"))

# zfill() -- fills with zero untill required width
fill_str = '7'
print(fill_str.zfill(7))

fill_str1 = "hi"
print(fill_str1.zfill(7))

# Convert integer to Roman numeral
print(roman.toRoman(1999)) 
number_str = 1999
roman_str = roman.toRoman(number_str)
print(roman_str)