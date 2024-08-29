talent = float(input("Enter the number of talents: "))
pound  = float(input("Enter the number of pounds: "))
lot    = float(input("Enter the number of lots: "))

total_lot = (talent * 20 + pound)* 32
gram = total_lot * 13.3

kilogram = gram // 1000
print(f'The weight in modern unit is: {kilogram:.0f} kilograms and {gram - (kilogram * 1000):.2f} gram')
