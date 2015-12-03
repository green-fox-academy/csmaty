alma_file = open("alma.txt")

lines = alma_file.readlines()
def line_char_counter(lines):
    linecount = 0
    charcount = 0
    for i in lines:
        linecount += 1
        for char in i:
            charcount += 1

    countlist = [linecount, charcount]
    return countlist

print(line_char_counter(lines))

alma_file.close()
