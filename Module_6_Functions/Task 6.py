import math

#function to calculate the size & unit price of the pizza
def pizza(diameter, price):
    size = math.pi * (diameter/2) ** 2
    size_meter = size / 10000
    unit_price = price / size_meter
    return unit_price

#Ask the user to input 2 times the diameter and price of the pizza
pizza_diameter1 = float(input("Enter the diameter of the 1st pizza: "))
pizza_price1 = float(input("Enter the price of the 1st pizza in euro: "))

pizza_diameter2 = float(input("\nEnter the diameter of the 2nd pizza: "))
pizza_price2 = float(input("Enter the price of the 2nd pizza in euro: "))

#Print the results
print(f'\nPrice of the 1st pizza {pizza(pizza_diameter1, pizza_price1):.2f} euros per square meter')
print(f'Price of the 2nd pizza {pizza(pizza_diameter2, pizza_price2):.2f} euros per square meter\n')

if pizza(pizza_diameter1, pizza_price1) < pizza(pizza_diameter2, pizza_price2):
    print(f'The 1st pizza has better value for money')
else:
    print(f'The 2nd pizza has better value for money')

