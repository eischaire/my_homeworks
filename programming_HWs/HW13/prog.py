import os, re
def main():
    numb = [f for f in os.listdir('.') if re.search('[0-9]', f)]
    arr = []
    for f in os.listdir('.'):
        if '.' in f:
            t = f.split('.')
            f = t[0]
        if f not in arr:
            arr.append(f)
    print('%s папок и файлов, содержащих цифры' %(len(numb)))
    print(arr)

main()
