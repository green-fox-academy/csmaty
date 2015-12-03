filename = "alma.txt"

def wc(filename):
    input_file = open("alma.txt")
    lines = input_file.readlines()

    linecount = 0
    charcount = 0
    for i in lines:
        linecount += 1
        for char in i:
            charcount += 1

    countlist = [linecount, charcount]
    return countlist
    alma_file.close()

print(wc(filename))
