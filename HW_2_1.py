def prepare_num(num):
    while num <= 0:
        print("Number should be more than zero")
        num = prepare_num(int(input("Enter number: ")))
    return num

def Fizz_Buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

def fizz_buzz_result():
    num = prepare_num(int(input("Enter number: ")))
    print(Fizz_Buzz(num))

fizz_buzz_result()