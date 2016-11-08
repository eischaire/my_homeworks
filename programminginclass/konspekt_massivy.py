print('massive')
s = [1,2,3]
print(s)
print('ih mozhno skladyvat\', a odin massiv umnozhat\' na chislo')
print('s[1:3] - элемент с индексом 1 включается в срез, а с индексом 3 - уже нет, страдай')
print('s[1::2] - элементы с первого с шагом 2')
print('s[1:4:2] - элементы с 1 включительно до 4 невключительно с шагом 2')
print('dobavit\' dopolnitel\'niy element v massiv:')
s.append(4)
s + [5,6]
print('moshno dobavit\' peremennuyu:')
i = 7
s.append(i)
j = 8
s + [j]
print('Dobavili element kuda ugodno, naprimer v nachalo:')
s.insert(0,0)
print('Udalim chto-nibud\'. Plohoy sposob:')
del s[-1]
print('Horoshiy sposob,, pri kotorom element pri udalenii padaet v druguyu peremennuyu:')
x = s.pop(-1)
print('Pechataem massiv:')
for i in s:
    print(i)
print('Esche pechataem, mozhem napechatat\' indeksy:')    
for i in range(len(s)):
    print(i)
    print(s[i])
print('mozhno ne s pervogo:')
for i in range (1, len(s),1):
    print(i)
    print(s[i])
print('Tol\'ko obraschayas\' k indeksam, mozhno menyat\' elementy pryamo v tsykle')
print('TABLICHKAAA!!!')
table = [[1,2],[3,4]]
for row in table:
    for column in row:
        print(column)

print('I','am','fine',sep='! ',end='?')

s = 'fhsio4hr834749tph93r2h0o'
letters = []
numbers = '0123456789'
for symbol in s:
    if symbol not in numbers:
        letters.append(symbol)
print('delaem is stroki massiv')
strk = '1 2 3 4 5'
arr = strk.split()

strk = '1,2,3,4,5'
arr = strk.split(',')

print('skleivaem obratno v stroku')

strk = ' '.join(arr)
