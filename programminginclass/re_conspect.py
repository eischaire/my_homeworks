Поиск в тексте.
Регулярные выражения.
| - дизъюнкция (лог. ИЛИ)
() - группа
. - любой символ
\ - экранирование следующего символа
Квантификаторы:
? - предыдущего символа/группы может и не быть
* - предыдущий символ/группа может повторяться любое число раз (включая 0)
+ - предыдущий символ/группа может повторяться любое положительное число раз
В Питоне функции для работы с ними используются в модуле re и работают ТОЛЬКО СО СТРОКАМИ (!!!!!!111)
"Жадность": в матч включается всё, что подпадает под паттерн
Ограничение жадности квантификатора: ставится ? после нужного квантификатора
[abc] - один из символов a b, или c
[a-c] - один из символов в диапазоне
Можно комбинировать: [a-cA-Cdf] - один символ из диапазонов или перечисленных символов
Если хочешь весь русский алфавит: [а-яё]

Про Питон:
import re
s = 'abcde'
if re.search([ab-f], s) :
    print('True')
