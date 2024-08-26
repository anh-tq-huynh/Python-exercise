length = float(input('Please enter the length of your zander in centimeter: '))
if length < 42:
    print ('Please release the fish back into the lake')
    print (f'Your zander is {42 - length} below the size limit.\
     \nA zander must be 42 centimeters long or longer to meet the limit ')

else:
    print ('You can keep the zander')