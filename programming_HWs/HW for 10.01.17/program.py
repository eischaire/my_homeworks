import random
def arr_form(text) :
    file = open(text, 'r', encoding="utf-8")
    arr = file.read()
    arr = arr.split(' ')
    file.close()
    return arr

def vocals(PoS) :
    V = 0
    for letter in PoS:
        if letter in 'аоуыэяёюиеАОУЫЭЯЁЮИЕ' :
            V += 1
    return V

def nounword(n_nouns) :
    nouns = arr_form("nouns.txt")
    x = 'no'
    while x != 'yes' :
        noun = random.choice(nouns)
        Vnoun = vocals(noun)
        if Vnoun <= n_nouns :
            x = 'yes'
    return noun

def verbword(n_verbs) :
    verbs = arr_form("verbs.txt")
    x = 'no'
    while x != 'yes' :
        verb = random.choice(verbs)
        Vverb = vocals(verb)
        if Vverb <= n_verbs :
            x = 'yes'
    return verb
def accword(n_accs) :
    accusatives = arr_form("accusatives.txt")
    x = 'no'
    while x != 'yes' :
        acc = random.choice(accusatives)
        Vacc = vocals(acc)
        if Vacc <= n_accs :
            x = 'yes'
    return acc

def punct() :
    punctuation = ['.', ',', '!', '?', '...', ' - ', ':', ';']
    return random.choice(punctuation)

def punct2() :
    punctuation = ['.', '!', '?', '...']
    return random.choice(punctuation)

def str1() :
    noun = nounword(5)
    n_verbs = 5 - vocals(noun)
    verb = verbword(n_verbs)
    while vocals(verb) != n_verbs :
        verb = verbword(n_verbs)
    print(noun, ' ', verb, punct(), sep='')

def str2() :
    noun = nounword(7)
    n_verbs = 7 - vocals(noun)
    verb = verbword(n_verbs)
    while len(verb) == 0 :
        verb = verbword(n_verbs)
    n_accs = n_verbs - vocals(verb)
    acc = accword(n_accs)
    while vocals(acc) != n_accs :
        acc = accword(n_accs)
    if len(acc) != 0 :
        print(noun, ' ', verb, ' ', acc, punct(), sep='')
    else :
        print(noun, ' ', verb, punct(), sep='')
    
def str3() :
    noun = nounword(5)
    n_verbs = 5 - vocals(noun)
    verb = verbword(n_verbs)
    while vocals(verb) != n_verbs :
        verb = verbword(n_verbs)
    print(noun, ' ', verb, punct2(), sep='')

str1()
str2()
str3()
