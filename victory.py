# 1 - Билл Гейтс 1955
# 2 - Махатма Ганди 1869
# 3 - Михаэль Шумахер 1969
# 4 - Иван Грозный 1530
# 5 - Антонио Вивальди 1678
total_questions = 5
total_right = 0
year1 = int(input('В каком году родился Билл Гейтс?'))
if year1 == 1955:
    total_right += 1
year2 = int(input('В каком году родился Махатма Ганди?'))
if year2 == 1869:
    total_right += 1
year3 = int(input('В каком году родился Михаэль Шумахер?'))
if year3 == 1969:
    total_right += 1
year4 = int(input('В каком году родился Иван Грозный?'))
if year4 == 1530:
    total_right += 1
year5 = int(input('В каком году родился Антонио Вивальди?'))
if year5 == 1678:
    total_right += 1

wrong = total_questions - total_right
right_percent = int(total_right*100/5)
wrong_percent = int(wrong*100/5)

print('Правильных ответов:', total_right)
print('Количество ошибок:', wrong)
print('Процент верных ответов: ', right_percent, '%', sep='')
print('Процент неверных ответов: ', wrong_percent, '%', sep='')






