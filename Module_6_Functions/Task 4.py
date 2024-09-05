def total_calculation(list_integer):
    total = 0
    for i in list_integer:
        total += int(i)
    return total

numbers = []
num = input("Enter a number, enter to stop: ")
while  num != "":
    int(num)
    numbers.append(num)
    num = input("Enter a number, enter to stop: ")


print('The sum of all numbers is:', total_calculation(numbers))

