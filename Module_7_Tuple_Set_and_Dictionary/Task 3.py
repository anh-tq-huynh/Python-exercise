print('Welcome to the airport database program, you can choose either to enter a new airport, /'
      'fetch data of an existing airport, or quit')
user_command = print('Please type what you want to do (new/fetch/quit):')

airports = {
    "Helsinki-Vantaa Aiport" : "EFHK",
    "Afutara Airport": "AGAF",
    "Batuna Airport": "AGBT",
    "Tan Son Nhat Airport" : "VVTS"
}

while True:
    if user_command == 'new':
        new_airport = input('Enter new airport: ')
        new_code = input('Enter new airport code: ')
        airports[new_airport] = new_code
        user_command = print('Please type what you want to do (new/fetch/quit):')
    elif user_command == 'fetch':
        fetch_airport = input(print('Which airport would you like to fetch? - '))
        if fetch_airport in airports:
            print(f'The ICAO code of {fetch_airport} is {airports[fetch_airport]} ')
        else:
            print("The {fetch_airport} is not in the airports list")
        user_command = print('Please type what you want to do (new/fetch/quit):')
    if user_command == 'quit':
        break