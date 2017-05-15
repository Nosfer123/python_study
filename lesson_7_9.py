from lesson_7_8 import my_decorator

@my_decorator #my_function = my_decorator(my_function)
def my_function():
    print("Standalone function")


my_function()