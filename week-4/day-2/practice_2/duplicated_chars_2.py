my_file = open("texts/duplicated_chars.txt")
out_file = open("w_output/duplicated_chars.txt", "w")

lines = my_file.readlines()
filtered_word = []

for i in lines:
    wordlist = i.split()
    for word in wordlist:
        rstripped_word = word.rstrip()
        filtered_word.append(rstripped_word[::2] + ' ')
    filtered_word.append('\n')

    print("".join(filtered_word))
    out_file.write("".join(filtered_word))

my_file.close()
out_file.close()
