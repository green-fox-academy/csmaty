my_file = open("texts/reversed_zen_lines.txt")
out_file = open("w_output/reversed_zen_lines.txt", "w")

lines = my_file.readlines()

for i in lines:
    i = i[::-1]
    print(i)
    out_file.write(i)
my_file.close()
