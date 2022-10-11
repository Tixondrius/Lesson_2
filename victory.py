Elon_age = 1971     # Elon Mask
Jobs_age = 1955     # Steve Jobs
Reeves_age = 1964   # Keanu Reeves
Holland_age = 1996  # Tom Holland
Jackman_age = 1968  # Hugh Jackman
answers = 5
count = 0
again = 'да'


while again == 'да':
    Elon_age_answer = int(input('In what year was Elon Mask born? '))
    Jobs_age_answer = int(input('In what year was Steve Jobs born? '))
    Reeves_age_answer = int(input('In what year was Keanu Reeves born? '))
    Holland_age_answer = int(input('In what year was Tom Holland born? '))
    Jackman_age_answer = int(input('In what year was Hugh Jackman born? '))
    if Elon_age_answer == Elon_age:
        count += 1
    if Jobs_age_answer == Jobs_age:
        count += 1
    if Reeves_age_answer == Reeves_age:
        count += 1
    if Holland_age_answer == Holland_age:
        count += 1
    if Jobs_age_answer == Jobs_age:
        count += 1
    print('Правильных ответов: ', count)
    print('Ошибок: ', answers - count)
    print('Процент правильных ответов: ', (count*100/answers))
    print('Процент неправильных ответов: ', 100-(count*100/answers))
    again = str(input('Хотите сыграть снова? '))
