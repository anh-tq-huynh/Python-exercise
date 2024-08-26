username = "python"
password = "rules"
name = input('Please enter your username: ')
pw = input('Please enter your password: ')

times = 5
while name != username or pw != password:
    print(f'Incorrect, You have {times} attempts left.')
    name = input('Please enter your username again: ')
    pw = input('Please enter your password: ')
    times -= 1
    if times == 0:
        print ('Access denied, you have exceeded the allowed attempts.')
        break
else:
    print('Welcome')

