while True:
    inp = input("Enter birth year: ")
    try:
        x = 1000 / int(inp)
    except (ValueError, TypeError) as err:
        print('{0} Try again!'.format(err))
    except ZeroDivisionError as err:
        print('Division by zero is not allowed')
        break
    except:
        print('Other exception')
    else:
        print("Your number is ", inp)
        break
    finally: # work every time when cycle is finished (even with error); used for close files
        print("Mc Donalds!")