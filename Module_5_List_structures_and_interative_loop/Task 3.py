number = int(input("Enter an integer number: "))
divisible = 0

for i in range(1, number + 1):
    if number % i == 0:
        divisible += 1
if divisible == 2:
    print('It is a prime number')
else:
    print('It is not a prime number')



