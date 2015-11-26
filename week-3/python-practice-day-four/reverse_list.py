def reverse_list(mylist):
    my_reversed_list = []
    i = len(mylist)-1

    while i != -1:
        my_reversed_list.append(mylist[i])
        i -= 1
    print(my_reversed_list)

reverse_list([4, 5, 98, 23, 13, 46])
