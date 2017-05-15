def my_decorator(function_to_decorate):
    def wrapper():
        print("Before code")
        function_to_decorate()
        print("After code")
    return wrapper


@my_decorator #my_function = my_decorator(my_function)
def my_function():
    print("Standalone function")


my_function()