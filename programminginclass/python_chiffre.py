alf='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !,.:1234567890'
s = input('your text: ')
while s != '' :
    s2 = []
    for smbl in s:
        if smbl == alf[-1]:
            s2.append(alf[0])
        for indx in range(len(alf)-1):
                if smbl == alf[indx] :
                    s2.append(alf[indx+1])
        s=''.join(s2)
    print(s)
    s = input('your text: ')
