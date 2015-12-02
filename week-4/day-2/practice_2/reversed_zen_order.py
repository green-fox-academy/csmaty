my_file = open("texts/reversed_zen_order.txt")
out_file = open("w_output/reversed_zen_order.txt", "w")

lines = my_file.readlines()
reversed_lines = lines[::-1]

for i in reversed_lines:
    print(i)
    out_file.write(i)


my_file.close()
out_file.close()
