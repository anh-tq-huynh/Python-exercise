import random
i = random.randint(1, 10)

num = int(input('Guess the number between 1 and 10: '))
while num != i :
    if num > i:
        num= int(input(f'{num} is too high, guess again: '))
    else:
        num = int(input(f'{num} is too low, guess again: '))
else:
    print('Correct!')