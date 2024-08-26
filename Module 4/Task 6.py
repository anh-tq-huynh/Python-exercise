N = int(input('How many random points do you want to generate?: '))
times = 0
n = 0
import random
while times <= N:
    x = random.uniform (-1,1)
    y = random.uniform (-1,1)
    if x**2 + y**2 < 1:
        n = n +1
    times = times + 1

pi = 4*n/N

print('The value of pi is: ', pi)
