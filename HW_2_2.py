def number():
    num = int(input("Enter number: "))
    for number_in_list in range (num+1):
        if number_in_list % 2 == 0 and number_in_list > 0:
            print (number_in_list*number_in_list)

number()