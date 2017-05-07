def number():
    num = int(input("Enter number: "))+1
    list_sqr = [(number_in_list) * (number_in_list) for number_in_list in range(1, num) if number_in_list % 2 == 0 and number_in_list > 0]
    print (list_sqr)

number()