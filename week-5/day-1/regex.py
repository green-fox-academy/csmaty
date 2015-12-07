import re

def filereader():
    with open("proba.txt", "r") as inp:
        text = inp.read()
        v = re.sub(r'u', '[U]', text)
        print(v)

filereader()
