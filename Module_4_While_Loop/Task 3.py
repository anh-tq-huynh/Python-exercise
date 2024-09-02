user_input = input('Enter a number')
s = float((user_input))
l = float((user_input))

while user_input != "":
    number = float((user_input))
    if number < s:
        s = number
    if number > l:
        l = number
    user_input = (input('Enter a number'))
else:
    print(f'The largest number is: {l}, and the smallest number is {s}')