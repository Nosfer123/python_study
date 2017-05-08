from random import randint

def dice_throw():
    return randint(1,6)

def dice_sum():
    counter = 0
    while True:
        dice1 = dice_throw()
        dice2 = dice_throw()
        counter += 1
        if dice1+dice2 == 8:
            print(dice1, dice2, counter)
            break

for dummy_i in range(10):
    dice_sum()