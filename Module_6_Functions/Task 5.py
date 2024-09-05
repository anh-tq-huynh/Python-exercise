def list(number_list1):
    number_list2 = number_list1
    for i in number_list2:
        if int(i) % 2 != 0:
            number_list2.remove(i)
    return number_list2

numbers = []
num = input("Enter a number, enter to stop: ")
while  num != "":
    int(num)
    numbers.append(num)
    num = input("Enter a number, enter to stop: ")

print('Original list:', numbers)
print('New list: ', list(numbers))

