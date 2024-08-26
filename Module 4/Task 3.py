i = int(input('Enter a number'))
s = i
l = i
while i != "":
    if i < s:
        s = i
    if i > l:
        l = i
    i = int(input('Enter a number'))
else:
print(f'The largest number is: {l}, and the smallest number is {s}')