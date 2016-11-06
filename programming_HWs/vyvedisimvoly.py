s = input('слово: ')
for nmbr, smbl in enumerate(s) :
    if nmbr % 2 != 0 :
        if (smbl == 'а'or smbl == 'к'):
            continue
        print(smbl)
            
