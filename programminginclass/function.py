def text_process (text_name) :
    f = open(text_name, 'r', encoding='utf-8')
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
text = text_process('1.txt')
print(text)
print(len(text))
