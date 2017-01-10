def text_process (text_name) :
    f = open(text_name, 'r', encoding='utf-8')
    text = f.read()
    for sym in text :
        if sym in '[]' :
            sym = ' ['
    text = text.split()
    for i, word in enumerate(text) :
        text[i] = word.strip(',./<>?\'";:!@#$%^&*()[]-_«»—')
    for j, word in enumerate(text) :       
        text[j] = word.lower()
        if len(text[j]) < 1 :
            del(text[j])
    f.close()
    return(text)

def vocals(PoS) :
    V = 0
    for letter in PoS :
        if letter in 'аоуыэяёюие' :
            V += 1
    return V


def syllables() :
    words = []
    text = text_process('1.txt')
    n = int(input())
    for wordd in text :
        V = vocals(wordd)
        if V == n :
            words.append(wordd)
    print(' '.join(words))

def beginning() :
    words = []
    text = text_process('1.txt')
    let = input()
    for word in text :
        if word.startswith(let) :
            words.append(word)
    print(' '.join(words))

def main() :
    a = input('Если Вы хотите слова с определенным количеством слогов, введите 0. Если Вам нужны слова с одной буквы, введите 1: ')
    if a == '0' :
        syllables()
    else :
        beginning()

main()
