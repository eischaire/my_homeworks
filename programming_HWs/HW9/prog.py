import re
def text_process () :
    f = open('text.txt', 'r', encoding='utf-8')
    text = f.read()
    text = text.split()
    for i, word in enumerate(text) :
        text[i] = word.strip(',./<>?\'";:!@#$%^&*()[]-_«»—')
    for j, word in enumerate(text) :       
        text[j] = word.lower()
        if len(text[j]) < 1 :
            del(text[j])
    f.close()
    return(text)

def search ():
    arr = []
    text = text_process()
    for word in text :
        if re.search('^откр(о(е(шь|те?|м)|ют?)|ы(?!ва)(л[аи]?|т(?!(и|ост))(ь|ы([йех]|ми?)?|ая?|ую|о([ей]|му?|го)?)?|в(ш(ая|ую|е([ей]|го|му?)|и([ех]|ми?)))?))(с[яь])?', word) :
            if word not in arr :
                arr.append (word)
    return arr

def main ():
    arr = search()
    for word in arr :
        print (word)

main()
