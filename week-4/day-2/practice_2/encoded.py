my_file = open("texts/encoded_zen_lines.txt")
out_file = open("w_output/encoded_zen_lines.txt", "w")

line = my_file.readlines()



for i in line:
    rstripped_line = i.rstrip()
    words = rstripped_line.split(" ")
    decoded_word = ""
    for j in words:
        decoded_word_list = []
        for char in j:
            decoded_word += chr(ord(char) - 1)
        decoded_word += ' '

        decoded_word_list.append(decoded_word)

    print(" ".join(decoded_word_list))
    out_file.write('\n' + " ".join(decoded_word_list))

my_file.close()
out_file.close()
