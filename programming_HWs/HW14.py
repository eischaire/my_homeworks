import os
def main():
    md = 0
    for root, dirs, files in os.walk('.'):
        t = 0
        for sym in root:
            if sym == os.sep:
                t += 1
            if t > md :
                md = t
    print(md)

main()
