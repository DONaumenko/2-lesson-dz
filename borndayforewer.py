year_of_birth = ''
day_of_birth = ''

while year_of_birth != 1799:
    year_of_birth = int(input('Не соблаговолите ли сказать, когда родился товарищ Пушкин?'))
    if year_of_birth == 1799:
        while day_of_birth != '6 июня':
            day_of_birth = input('А дату рождения помните?')
            if day_of_birth == '6 июня':
                print('Верно')
