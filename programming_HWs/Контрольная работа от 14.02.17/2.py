import re

def text_process () :
    f = open('corpus.xml', 'r', encoding="utf-8")
    text = f.read()
    text = text.split('\n')
    f.close()
    return(text)

def dictkeys ():
    k = open('keys.txt', 'w', encoding="utf-8")
    text = text_process()
    dic = {}
    for line in text :
        if re.search('<w lemma=', line) :
            if re.search('type="(.+?)"', line).group().strip('type="') in dic :
                dic[re.search('type="(.+?)"', line).group().strip('type="')] += 1
            else :
                dic[re.search('type="(.+?)"', line).group().strip('type="')] = 1
    for word in list(dic.keys()) :
        k.write(word)
        k.write('\n')
    k.close()

dictkeys()
