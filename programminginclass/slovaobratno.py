wrds = []
a = input('')
while a != (''):
    wrds.append(a)
    a = input('')
b = len(wrds) - 1
for i in range(b,0,-1):
    print (wrds[i])
print(wrds[0])
