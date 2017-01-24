import re
def text_process () :
    f = open('check.txt', 'r', encoding='utf-8')
    text = f.read()
    text = text.split()
    summ = 0
    for i, word in enumerate(text) :
        text[i] = word.strip(',./<>?\'";:!@#$%^&*()-_«»—')
    for j, word in enumerate(text) :
        text[j] = word.lower()
        if len(text[j]) < 1 :
            del(text[j])
    f.close()
    return(text)

def search ():
    text = text_process()
    for word in text :
        if re.search('.*[аоыэуяёиеюАОЫЭУЯЁИЕЮ].*[аоыэуяёиеюАОЫЭУЯЁИЕЮ].*[аоыэуяёиеюАОЫЭУЯЁИЕЮ].*', word) :
            print(word)

search()
