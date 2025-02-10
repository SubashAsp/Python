def addition(a, b):
    print(a+b)

def subtraction(a, b):
    print(a-b)

def multiplication(a, b):
    print(a*b)

def division(a, b):
    if a < b:
        a, b = b, a
    print(a/b)

def modulus(a, b):
    print(a%b)