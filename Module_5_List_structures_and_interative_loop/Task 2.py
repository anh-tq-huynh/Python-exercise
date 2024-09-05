numbers = []
num = input('Enter a number:')
numbers.append(num)
times = 1
"""
while num != "":
    times += 1
    num = input('Enter another number, if you are done, press enter: ')
    numbers.append(num)
"""
while True:
     times += 1
     num = input('Enter another number, if you are done, press enter: ')
     numbers.append(num)
     if num == "" and times > 4:
         break

numbers.sort(reverse=True)

