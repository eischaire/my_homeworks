f = open("1.txt", 'r', encoding="utf-8")
a = f.readlines()
quant = len(a)
words = 0
for line in a:
    words += len(line)
aver = words/quant
print(aver)
