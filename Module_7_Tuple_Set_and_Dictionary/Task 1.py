months = ( (3,4,5), (6,7,8), (9,10,11), (12,1,2))
seasons = ("Spring","Summer","Autumn","Winter")

#Ask the user to enter the month number
month_number = int(input("Enter a number of a month: "))

if month_number < 0 or month_number > 12:
    print("Invalid input")

else:

    #Check in months which value contains the user input, then result in the index of the value
    def what_season(number):
        for i in months:
            if number in i:
                return months.index(i)

    #Print out the result season[months.index(i)]
    print(f'The month belongs to {seasons[(what_season(month_number))]}')
