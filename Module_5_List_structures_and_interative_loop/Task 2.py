numbers = []
num = input('Enter a number:')
numbers.append(num)
times = 1
while num != '' or times < 4:
    times += 1
    num = input('Enter another number, if you are done, press enter: ')
    numbers.append(num)
    if num == '' and times <4:
        num = input('Enter another number, you need at least 5 numbers: ')

numbers.sort(reverse=True)
for i in range(0,6):
    print(numbers[i])
