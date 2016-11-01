a = 5
b = input('наколдуйте мне число: ')
while b!=a :
    if b=='' :
        print('well ok bye')
        break
    b=int(b)
    if b<a :
        b = input ('Нет, моё число больше. Попробуйте ещё раз: ')
    elif b>a :
        b = input ('Нет, моё число меньше. Попробуйте ещё раз: ')
if b==a :
    print('Вы угадали')
