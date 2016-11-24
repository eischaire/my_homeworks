s1 = input('Ваша строка: ')
n = len(s1)
arr = []
while n != 0 :
    for nmbr in range(0,n):
        arr.append(s1[nmbr])
    s = ''.join(arr)
    arr = []
    print(s)
    n -= 1
