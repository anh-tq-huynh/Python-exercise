def gasoline(volume):
    volume_liter = volume * 3.785
    return volume_liter

volume_gallon = float(input("Enter the volume of gasoline in American gallon: "))
while volume_gallon > 0:
    gasoline(volume_gallon)
    print(f'Your gasoline in liter is: {gasoline(volume_gallon)}')
    volume_gallon = float(input("Enter the volume of gasoline in American gallon: "))


