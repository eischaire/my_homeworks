def text_process () :
    f = open('text.txt', 'r', encoding='utf-8')
    text = f.read().lower().split('.!?')
    for i, sent in enumerate(text) :
        text[i] = sent.strip(',./<>?\'";:!@#$%^&*()[]-_«»—„0123456789')     
        
    f.close()
    return(text)

def abracadabra():
    text = text_process()
    for sent in text:
        dic = {word.strip(',./<>?\'";:!@#$%^&*()[]-_«»—„'): len(word.strip(',./<>?\'";:!@#$%^&*()[]-_«»—„0123456789')) for word in sent.split() if len(word.strip(',./<>?\'";:!@#$%^&*()[]-_«»—„0123456789')) > 7}
    return(dic)

def main():
    dic = abracadabra()
    for word in dic:
        template = ('{:-<35}')
        print('{}{}'.format(template.format(str(word)), dic[word]))

    
main()
