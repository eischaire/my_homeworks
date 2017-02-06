import re

def text_process () :
    f = open('france.html', 'r', encoding='utf-8')
    text = f.read()
    text = text.split('\n')
    f.close()
    return(text)

def capit () :
    k = open('capital.txt', 'w')
    text = text_process()
    for i, word in enumerate(text) :
        if re.search('[Сс]толица', text[i]):
            cap = re.search('[А-Яа-я]+<', text[i+1]).group().strip('<')
            k.write(cap)
            break
    k.close()

capit()

