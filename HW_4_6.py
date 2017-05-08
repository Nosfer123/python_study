from random import randint

def dice():
    return randint(1,6)

def square_dice():
    square_dice1 = []
    while True:
        dice1 = dice()
        square_dice1.append(dice1)
        if dice1 == 6:
            print(square_dice1)
            break

for i in range (5):
    square_dice()