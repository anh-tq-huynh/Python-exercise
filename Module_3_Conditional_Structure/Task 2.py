cabin = input('Please enter your cabin class (LUX/A/B/C): ')
if cabin == "LUX":
    print('Upper-deck cabbin with a balcony')

elif cabin == "A":
    print('Above the car deck, equipped with a window')

elif cabin == "B":
    print('Windowless cabin above the car deck')

elif cabin == "C":
    print ('Windowless cabin below the car deck')

else:
    print('Invalid cabin class entered')