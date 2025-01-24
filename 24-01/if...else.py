print("")
#if statements
a = 3
if a < 5:
    print(True)

#if...else statements
if a > 5:
    print(True)
else:
    print(False)

#nested if statements
if a < 5:
    if a > 0:
        print(True)

#nested if...else statements
if a < 5:
    if a > 0:
        print(True)
    else:
        print(False)
else:
    print(True)

#elif statements
b = int(input("Enter the number: "))
if b == 100:
    print("Excellent")
elif b > 90 | b == 90:
    print("Very Good")
elif b > 80 | b == 80:
    print("Good")
elif b > 60 | b < 80:
    print("Average")
elif b > 40 | b < 60:
    print("Want to improve")
else:
    print("Do Better Next Time")