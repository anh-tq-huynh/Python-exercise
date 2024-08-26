import random

num1a = random.randint(1,9)
num2a = random.randint(1,9)
num3a = random.randint(1,9)
print(f'The random 3-digit code is: {num1a*100 + num2a*10 + num3a}')

num1b = random.randint(1,6)
num2b = random.randint(1,6)
num3b = random.randint(1,6)
num4b = random.randint(1,6)
print(f'The random 4-digit code is: {num1b*1000 + num2b*100 + num3b*10 + num4b} ')