age = 1799
day = 26
age_answer = int(input('In what year was A. S. Pushkin born? '))
if age_answer == age:
    day_answer = int(input('What day was A. S. Pushkin born? '))
    if day_answer == day:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')
