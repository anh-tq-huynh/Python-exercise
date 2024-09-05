import random
def dice():
    roll = 0
    while roll != 6:
        roll = random.randint(1,6)
        print(roll)
dice()

