sex = input('Please enter your biological gender (male/female): ')
hem = float(input('Please enter your hemoglobin value(g/l): '))

if sex == 'male':
    if hem < 134:
        print('Your hemoglobin value is low')
    elif 134 < hem < 167:
        print('Your hemoglobin value is normal')
    else:
        print('Your hemoglobin value is high')

elif sex =='female':
    if hem < 117:
        print ('Your hemoglobin value is low')
    elif 117 < hem < 155:
        print ('Your hemoglobin value is normal')
    else:
        print ('Your hemoglobin value is high')

else:
    print ('Invalid gender entered')