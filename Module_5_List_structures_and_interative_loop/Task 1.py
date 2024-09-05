import random
dices = int(input('How many dices do you want to roll? - '))
total = 0

for i in range(0,dices):
    dice = random.randint(1,6)
    total = total + dice

print("The sum of all dices after rolling is: ", total)