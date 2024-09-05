import random
def dice(sides):
    roll = 0
    while roll != 6:
        roll = random.randint(1,sides)
        print(roll)
    return roll

dice_side = int(input('How many sides is your dice?'))
dice(dice_side)