import random
def file_process () :
    f = open('bigrams.csv', 'r', encoding='utf-8')
    text = f.readlines()
    f.close()
    return text

def dic () :
    dic = {}
    text = file_process()
    for line in text :
        line = line.strip('\n')
        line = line.split(', ')
        dic[line[0]] = line[-1]
    return dic

def main() :
    game_dic = dic()
    key = random.choice(list(game_dic.keys()))
    user = input(game_dic[key])
    n = 1
    while n <= len(key) :
        if user == key :
            print('YOU WIN')
            break
        elif n == len(key) :
            print('you lose')
            break
        else :
            n += 1
            print('try again: ')
            user = input(game_dic[key])

main()
