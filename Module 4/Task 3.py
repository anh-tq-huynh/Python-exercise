i = (input('Enter a number'))
s = i
l = i
while i != "":
    number = float (i)
    if i < s:
        s = i
    if i > l:
        l = i
    i = input('Enter a number')
else:
    print(f'The largest number is: {l}, and the smallest number is {s}')