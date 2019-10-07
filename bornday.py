year_of_birth = int(input('Не соблаговолите ли сказать, когда родился товарищ Пушкин?'))
if year_of_birth == 1799:
    day_of_birth = input('Может быть, вспомните и день его рождения?')
    if day_of_birth == '6 июня':
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')

