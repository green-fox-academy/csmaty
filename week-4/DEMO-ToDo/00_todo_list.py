todolist = []



def initiate():
    read_txt()
    choose_menu_option()

def read_txt():
    import os

    textfile = open("listfile/todo.txt", 'r')
    if os.stat("listfile/todo.txt").st_size == 0:
        pass
    else:
        lines = textfile.readlines()
        for i in lines:
            linelength = len(i)
            statusbox = i[0:3]
            itemtext = i[4:(len(i)-1)]

            newitem = {'status': statusbox, 'description': itemtext}
            todolist.append(newitem)

    return todolist
    textfile.close()

def savetotxt():
    textfile = open("listfile/todo.txt", 'w')
    for i in todolist:
        values_combined = str(i['status']) + ' ' +  str(i['description'] + '\n')
        textfile.write(str(values_combined))
    textfile.close()
    exit()


def choose_menu_option():
    menu_list = [
            '   [MENU:]           ',
            ' ',
            '   L : LIST ALL ITEMS',
            '   A : ADD ITEM',
            '   C : MARK ITEM AS COMPLETED',
            '  RM : REMOVE ITEM',
            '  EX : SAVE & EXIT'
        ]

    itemlister(todolist)
    displaymenu(menu_list)

    menu_option_input = input('\n>>>>Type the command for the chosen option:\n\n')
    if menu_option_input.lower() == 'l':
        itemlister(todolist)


    elif menu_option_input.lower().lower() == 'a':
        itemadder(todolist)


    elif menu_option_input.lower() == 'c':
        taskcompleted(todolist)


    elif menu_option_input.lower() == 'rm':
        itemremover(todolist)


    elif menu_option_input.lower() == 'ex':
        savetotxt()
    else:
        print("\n!INCORRECT INPUT!\n")





def displaymenu(menu_list):

    print('\n')
    for i in menu_list:
        print(str(i))
    print('\n')

def itemlister(todolist):
    import os
    os.system('clear')
    n = 0
    print('\n')
    print('*****************************************')
    print('         TODO LIST:')
    print('*****************************************')
    for i in todolist:
        n += 1
        print (str(n) + '. ' + i['status'], i['description'])
    print('*****************************************')


def itemadder(todolist):

    newitem = {'status': '[ ]', 'description': str(input("\n>>>>Write the next todo item: \n"))}
    todolist.append(newitem)
    return todolist

def itemremover(todolist):

    i = int(input('\n>>>>Give me the number of the item you want to remove:\n')) -1
    todolist.pop(i)
    return todolist

def taskcompleted(todolist):

    i = int(input('\n>>>>Give me the number of the item you have completed:\n')) -1
    todolist[i]['status'] = '[X]'
    return todolist


initiate()
while True:
    choose_menu_option()
