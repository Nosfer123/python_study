def result():
    index_power = list(input("Enter your list: ").split(' '))
    number_in_list = (int(input("Enter N: ")))
    if len(index_power) > number_in_list:
        print((int(index_power [number_in_list])) ** number_in_list)
    else:
        print ("-1")

result()