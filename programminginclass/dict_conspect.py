Словарь как структура данных
Необходим в ситуациях, когда нужно явным образом связать 2 штуки.
Элементы словаря - пары ключ-значение
Ключи - только неизменяемые типы данных (строки, числа, числа с плавающей точкой)
Не может быть двух одинаковых ключей (можно, но последующий ключ заменит предыдущий)
Значения - любые структуры данных (включая массивы, словари etc.)
Пары ключ-значение не составляют последовательности

Объявление словаря:
d = {} - пустой словарь (не стоит называть переменную dict)
d = {1: 'a', 2: 'b'} - ключи 1 и 2, значения 'a' и 'b'
В словаре нет append! Расширение словаря проще:
d[4] = 'd'
#de = d[3] - обращение по несуществующему ключу не работает (хм логично)
if 2 in d :
    de = d[3]

d[1] = 'rty'
d[1] += 'qwe'

d[3] = []
d[3].append('kek') - добавление элемента в массив, который является сейчас элементом словаря

d[5] = 0
d[5] += 1

for k in d :
    print(d[k])
    #d[2] = 3

for k in sorted(d) :
    print(k)

Нельзя менять словарь в цикле, обходящем этот словарь. Можно задать какой-нибудь массив и в цикле, обходящем массив, менять словарь

words = ['abc', 'def', 'ghi', 'abc']
word_count = {}
for word in words :
    if word not in word_count :
        word_count[word] = 1
    else :
        word_count[word] += 1

for word in sorted(word_count) :
    print(word, word_count[word])

keys_list = list(word_count.keys())
values_list = list(word_count.values())

del(word_count[word])

dic = {1: 'a', 2: 'b', 3: ('a': 1, 'b': 2}}
dic[3]['b']

b = a[:]
dic1 = dic.copy






                   
