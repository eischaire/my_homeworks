def text_process (text_name) :
    f = open(text_name, 'r', encoding='utf-8')
    text = f.read()
    for sym in text :
        if sym in '[]' :
            sym = ' ['
    text = text.split()
    for i, word in enumerate(text) :
        text[i] = word.strip(',./<>?\'";:!@#$%^&*()[]-_«»—')
    for j, word in enumerate(text) :       
        text[j] = word.lower()
        if len(text[j]) < 1 :
            del(text[j])
    f.close()
    return(text)

def end_ing (text_name) :
    text = text_process(text_name)
    num = 0
    for wordform in text :
        if wordform.endswith('ing') :
           num += 1
    print('Количество слов на \'-ing\' в тексте:', num)

def user_ing (text_name) :
    text = text_process(text_name)
    word0 = input('Пожалуйста, укажите слово на \'-ing\': ')
    num = 0
    for wordform in text :
        if wordform == word0 :
            num += 1
    print('Слово встречается в тексте', num, 'раз(а)')

def main () :
    text_name = input('Пожалуйста, укажите название файла в формате \'name.txt\': ')
    end_ing(text_name)
    user_ing(text_name)

main()
    
