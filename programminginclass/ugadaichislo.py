a = 5
b = input('наколдуйте мне число: ')
b = int (b)
if a == b :
    print ('КАК ВЫ ЭТО СДЕЛАЛИ?!')
elif a > b :
    print ('Нет, но Вы будете близки, если напишете число побольше')
    b = input ('Попробуйте ещё раз: ')
    b = int(b)
else :
    print ('Нет, но Вы будете близки, если напишете число поменьше')
    b = input ('Попробуйте ещё раз: ')
    b = int(b)
if a == b :
    print ('Да! Вы настоящий экстрасенс!')
elif a > b :
    print ('Минимализм сегодня сыграл не в Вашу пользу :с')
else :
    print ('Слишком много, до свидания :с')
