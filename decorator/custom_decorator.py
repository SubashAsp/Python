
def custom_decorator(original_function):
    def wrapper_function():
        print("Before function call")
        original_function()
        print("After function call")
    return wrapper_function

@custom_decorator
def greet():
    print("Hello Everyone")


greet()
