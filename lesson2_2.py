def get_chet(num):
    if num == 0:
        return "Zero"
    elif num % 2:
        return "Nechet"
    else:
        return "Chet"

def prepare_num(num):
    if num < 0:
        num = 0
    return num


def chet_nechet():
    num = int(input("Enter number: "))
    num = prepare_num(num)
    print(get_chet(num))

for dummy_n in range (3):
    chet_nechet()
