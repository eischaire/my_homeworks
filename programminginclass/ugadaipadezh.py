word = input('введите слово: ')
if word.endswith('а') or word.endswith('я'):
    print('Nom Sing')
elif word.endswith('ы') or word.endswith('и'):
    print('Gen Sing | Nom Pl')
elif word.endswith('е'):
    print('Dat/Abl Sing')
elif word.endswith('у'):
    print('Acc Sing')
elif word.endswith('ой') or word.endswith('ей'):
    print('Instr Sing')
elif word.endswith('ам') or word.endswith('ям') :
    print('Dat Pl')
elif word.endswith('ами') or word.endswith('ями') :
    print('Instr Pl')
elif word.endswith('ах') or word.endswith('ях') :
    print('Abl Pl')
else:
    print('Совсем не 1-е склонение')
