import re

def text_process () :
    f = open('corpus.xml', 'r', encoding="utf-8")
    text = f.read()
    text = text.split('\n')
    f.close()
    return(text)

def adjs () :
    k = open('adjs.txt', 'w', encoding="utf-8")
    text = text_process()
    dic = {}
    for line in text :
        if re.search('type="l.f(.+?)"', line) :
            if re.search('type="l.f(.+?)"', line).group().strip('type="') in dic :
                dic[re.search('type="(.+?)"', line).group().strip('type="')] += 1
            else :
                dic[re.search('type="(.+?)"', line).group().strip('type="')] = 1
    for word in list(dic.keys()) :
        k.write(word)
        k.write('  ')
        k.write(str(dic[word]))
        k.write('\n')
    k.close()

def csvfile () :
    csv = open('corpus.csv', 'w', encoding="utf-8")
    text = text_process()
    for line in text :
        if re.search('<w lemma="(.+?)" type="(.+?)">(.+?)</w>', line):
            string = re.sub('<w lemma="(.+?)" type="(.+?)">(.+?)</w>', '\\1,\\2,\\3', line)
            csv.write(string)
            csv.write('\n')


csvfile()
