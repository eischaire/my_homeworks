import os, re
def textprocessing(name):
    f = open(name, 'r', encoding='windows-1251')
    text = f.read()
    f.close()
    return(text)

def countwords():
    countwords = {}
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name.endswith('.xhtml'):
                k = 0
                text = textprocessing(name)
                text = text.split('\n')
                for word in text:
                    if word.startswith('<w>'):
                        k += 1
                countwords[name] = k
    a = open('countwords.txt', 'w', encoding='utf-8')
    for name in sorted(countwords):
        a.write(name)
        a.write('\t')
        a.write(str(countwords[name]))
        a.write('\n')
    a.close()
#Можно ли было просто регулярным выражением вытащить число из тега words в разметке? Я побоялась это делать, вдруг там неправильные числа

def authors():
    auths = {}
    dates = {}
    b = open('authors.csv', 'w', encoding='utf-8')
    b.write('Название файла')
    b.write('\t')
    b.write('Автор')
    b.write('\t')
    b.write('Дата создания')
    b.write('\n')
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name.endswith('.xhtml'):
                file = textprocessing(name)
                if re.search('meta content=".+?" name="author">', file):
                    auths[name] = re.search('".+?"', re.search('<meta content=".+?" name="author">', file).group()).group().strip('"')
                if re.search('meta content=".+?" name="created">', file):
                    dates[name] = re.search('".+?"', re.search('<meta content=".+?" name="created">', file).group()).group().strip('"')
                b.write(name)
                b.write('\t')
                b.write(auths[name])
                b.write('\t')
                b.write(dates[name])
                b.write('\n')
    b.close()

def main():
    countwords()
    authors()        

main()
