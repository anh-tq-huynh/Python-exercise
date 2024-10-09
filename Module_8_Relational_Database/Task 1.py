import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '121100',
    autocommit = True,
    collation = 'utf8mb3_general_mysql500_ci'
)

def retrieve_airport(icao_code):
    airport_sql = f'select name, municipality from airport where ident = "{icao_code}";'
    airport_cursor = connection.cursor()
    airport_cursor.execute(airport_sql)
    result = airport_cursor.fetchall()
    if airport_cursor.rowcount >0:
        for row in result:
            print(f'The airport with {icao_code} is {row[0]} in {row[1]}')
    return

icao_input = input('What is the ICAO code you are looking for? - ').upper()
retrieve_airport(icao_input)