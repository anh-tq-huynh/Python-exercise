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
def airport_type(area_code):
    type_sql = f'select name, type from airport where iso_country = "{area_code}" order by type;'
    airport_type_cursor = connection.cursor()
    airport_type_cursor.execute(type_sql)
    result = airport_type_cursor.fetchall()
    print('Airport name, Type of airport')
    closed = 0
    large = 0
    small = 0
    medium = 0
    heliport = 0
    if airport_type_cursor.rowcount > 0:
        for row in result:
            print(f'{row[0]},{row[1]}')
            if row[1] == "closed":
                closed += 1
            elif row[1] == "large_airport":
                large += 1
            elif row[1] == "small_airport":
                small += 1
            elif row[1] == "heliport":
                heliport += 1
            elif row[1] == "medium_airport":
                medium +=1
    return large, small, medium, heliport, closed

def country(country_code):
    country_sql = f'select country.name from country where iso_country = "{country_code}";'
    country_cursor = connection.cursor()
    country_cursor.execute(country_sql)
    result = country_cursor.fetchall()
    country = result[0][0]
    return country

area = input('Type in the area code: ').upper()
airport_type(area)
large, small, medium, heliport, closed = airport_type(area)
print(f'{country(area)} has {large} large airports, {medium} medium airports, {small} small airports, {heliport} heliports, and {closed} closed airports.')

