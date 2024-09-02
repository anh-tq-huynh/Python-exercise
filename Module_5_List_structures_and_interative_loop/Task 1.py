import random
dices = int(input('How many dices do you want to roll? - '))
sum = 0

for i in range(0,dices):
    dice = random.randint(1,6)
    sum = sum + dice

print("The sum of all dices after rolling is: ", sum)