user_input = (input('Enter a number'))
s = user_input
l = user_input
while user_input != "":
    number = float (user_input)
    if user_input < s:
        s = user_input
    if user_input > l:
        l = user_input
    user_input = input('Enter a number')
else:
    print(f'The largest number is: {l}, and the smallest number is {s}')