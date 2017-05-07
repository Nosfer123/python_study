for i in range (-5, 5):
    try:
        print(1/i)
    except ZeroDivisionError:
        pass

for i in range (-5, 5): #the same as first
    if not i:
        continue
    print(1/i)