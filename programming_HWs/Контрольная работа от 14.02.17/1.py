def text_process () :
    f = open('corpus.xml', 'r', encoding="utf-8")
    text = f.read()
    text = text.split('\n')
    f.close()
    return(text)

def str_count ():
    k = open('count_strings.txt', 'w', encoding="utf-8")
    text = text_process()
    k.write(str(len(text)))
    k.close()

str_count()
