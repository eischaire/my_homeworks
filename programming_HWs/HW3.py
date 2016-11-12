arr = []
s = input('слово: ')
s2 = []
while s != '' :
    arr.append(s)
    s = input('следующее слово: ')
for i in range(len(arr)):
    s1 = arr[i]
    for j in range(len(s1)-1,0,-1):
        if j == 2 :
            continue
        s2.append(s1[j])
    s2.append(s1[0])
    otvet = ''.join(s2)
    print(otvet)
    s2 = []
