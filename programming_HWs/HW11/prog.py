import re

def text_process () :
    f = open('komar.html', 'r', encoding="utf-8")
    text = f.read()
    text = text.split('\n')
    f.close()
    return(text)

def komar () :
    text = text_process()
    k = open('slon.html', 'w', encoding="utf-8")
    for i, word in enumerate(text) :
        text[i] = re.sub('Комар(а(х|ми?)?|у|о(в|м)|е|ы)?([!\? <.,;:\)])', 'Слон\\1\\4', text[i])
        text[i] = re.sub('комар(а(х|ми?)?|у|о(в|м)|е|ы)?([!\? <.,;:\)])', 'слон\\1\\4', text[i])
        k.write(text[i])
        k.write('\n')
    k.close()

komar()
