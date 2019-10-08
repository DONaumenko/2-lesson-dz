# 1 - Билл Гейтс 1955
# 2 - Махатма Ганди 1869
# 3 - Михаэль Шумахер 1969
# 4 - Иван Грозный 1530
# 5 - Антонио Вивальди 1678
right1 = 0
right2 = 0
right3 = 0
right4 = 0
right5 = 0
year1 = int(input('В каком году родился Билл Гейтс?'))
if year1 == 1955:
    right1 = 1
year2 = int(input('В каком году родился Махатма Ганди?'))
if year2 == 1869:
    right2 = 1
year3 = int(input('В каком году родился Михаэль Шумахер?'))
if year3 == 1969:
    right3 = 1
year4 = int(input('В каком году родился Иван Грозный?'))
if year4 == 1530:
    right4 = 1
year5 = int(input('В каком году родился Антонио Вивальди?'))
if year5 == 1678:
    right5 = 1

total_right = right1 + right2 + right3 + right4 + right5

wrong = 5 - total_right
right_percent = int(total_right*100/5)
wrong_percent = int(wrong*100/5)

print('Правильных ответов:', total_right)
print('Количество ошибок:', wrong)
print('Процент верных ответов: ', right_percent, '%', sep='')
print('Процент неверных ответов: ', wrong_percent, '%', sep='')






