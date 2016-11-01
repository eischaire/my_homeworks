s = 'I\'m ok'
for letter in s :
    print(letter)
print (done)

range(10)
range(3,14)

for digit in range(10):
    d1 = digit + 5
    if d1 < 15 :
        print(d1)

print('Длина строки', len(s))
print('Первый индекс', s[0])
print('Последний индекс, если строка ненулевой длины', s[-1])

for indx, letter in enumerate(s) :
    if indx %2 == 0:
        print(indx, letter)

x = 0
while x < len(s):
    print (x, s[x])
    x+=1
    if s[x]=='o':
        break

while x<len(s):
    x+=1
    if s[x]=='o':
        continue
        print(s[x])
