numbers = []
num = ""

while True:
    num = input("Enter a number, press enter to stop:")
    if num != "":
        numbers.append(float(num))

    if num == "" and len(numbers) > 4:
        break

numbers.sort(reverse=True)

list = []
for i in range(0,5):
    list.append(numbers[i])

print('Largest 5 numbers are:',list)

