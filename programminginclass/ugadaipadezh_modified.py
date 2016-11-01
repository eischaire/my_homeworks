word = input('введите слово: ')
while word!='':
    if word.endswith('а') or word.endswith('я'):
        print('Nom Sing')
        word = input ('новое слово ')
    elif word.endswith('ы') or word.endswith('и'):
        print('Gen Sing | Nom Pl')
        word = input ('новое слово ')
    elif word.endswith('е'):
        print('Dat/Abl Sing')
        word = input ('новое слово ')
    elif word.endswith('у'):
        print('Acc Sing')
        word = input ('новое слово ')
    elif word.endswith('ой') or word.endswith('ей'):
        print('Instr Sing')
        word = input ('новое слово ')
    elif word.endswith('ам') or word.endswith('ям') :
        print('Dat Pl')
        word = input ('новое слово ')
    elif word.endswith('ами') or word.endswith('ями') :
        print('Instr Pl')
        word = input ('новое слово ')
    elif word.endswith('ах') or word.endswith('ях') :
        print('Abl Pl')
        word = input ('новое слово ')
    else:
        print('Совсем не 1-е склонение')
        word = input ('новое слово ')
if word=='':
    print('byyyye byyyyye bye my darling')
