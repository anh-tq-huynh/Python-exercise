import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '121100',
    autocommit = True,
    collation = 'utf8mb3_general_mysql500_ci')

def coordinate(icao_code):
    cor_sql = f'select latitude_deg, longitude_deg from airport where ident = "{icao_code}";'
    cor_cursor = connection.cursor()
    cor_cursor.execute(cor_sql)
    result_cor = cor_cursor.fetchall()
    if cor_cursor.rowcount >0:
        latitude = result_cor[0][0]
        longitude = result_cor[0][1]
    else:
        latitude = None
        longitude = None
    return latitude, longitude

def airport_name(icao_code):
    airport_sql =f'select name from airport where ident = "{icao_code}";'
    airport_cursor = connection.cursor()
    airport_cursor.execute(airport_sql)
    result_airport = airport_cursor.fetchall()
    if airport_cursor.rowcount > 0:
        airport_name = result_airport[0][0]
    else:
        airport_name = None
    return airport_name

icao_input1 = input('Please enter ICAO of airport number 1: ').upper()
icao_input2 = input('Please enter ICAO of airport number 2: ').upper()
airport1 = coordinate(icao_input1)
airport2 = coordinate(icao_input2)
airport_name1 = airport_name(icao_input1)
airport_name2 = airport_name(icao_input2)

if airport_name1 == None or airport_name2 == None:
    print('Invalid ICAO code, please try again')
else:
    print(f'The distance between {(airport_name(icao_input1))} and {airport_name(icao_input2)} is: {distance.distance(airport1, airport2).km:.3f}km')

