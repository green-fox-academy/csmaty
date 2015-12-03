todolist = [
        {'status': '[ ]', 'description': 'vegyel ezt' },
        {'status': '[ ]', 'description': 'vegyel azt'},
        {'status': '[ ]', 'description': 'vegyel amazt'},
        {'status': '[ ]', 'description': 'vidd ki a szemetet'}
]

menu_list = [
        '   [MENU:]     ',
        '              ',
        '   L : LIST ALL ITEMS',
        '   A : ADD ITEM',
        '   C : MARK ITEM AS COMPLETED',
        '  RM : REMOVE ITEM',
        ' 000 : EXIT'
    ]

def choose_menu_option():
    displaymenu(menu_list)

    menu_option_input = input('\n>>>>Type the number of the chosen option:\n\n')
    try:
        if menu_option_input == 'L' or 'l':
            itemlister(todolist)
            choose_menu_option()

        elif int(menu_option_input) == 'A' or 'a':
            itemadder(todolist)
            itemlister(todolist)
            choose_menu_option()

        elif int(menu_option_input) == 'C'or 'c':
            taskcompleted(todolist)
            itemlister(todolist)
            choose_menu_option()

        elif int(menu_option_input) == 'RM' or 'rm':
            itemremover(todolist)
            itemlister(todolist)
            choose_menu_option()
    except:
        print("\n!INCORRECT INPUT!\n")
        choose_menu_option()



def displaymenu(menu_list):

    print('\n')
    for i in menu_list:
        print(str(i))
    print('\n')


def itemlister(todolist):
    n = 0
    print('\n')
    print('         TODO LIST:')
    print('*****************************************')
    for i in todolist:
        n += 1
        print ('      ' + str(n) + '. ' + i['status'], i['description'])
    print('*****************************************')


def itemadder(todolist):

    newitem = {'status': '[ ]', 'description': str(input("\n>>>> Write the next todo item: \n"))}
    todolist.append(newitem)
    return todolist

def itemremover(todolist):

    i = int(input('\n>>>> Give me the number of the item you want to remove:\n')) -1
    todolist.pop(i)
    return todolist

def taskcompleted(todolist):

    i = int(input('\n>>>> Give me the number of the item you have completed:\n')) -1
    todolist[i]['status'] = '[X]'
    return todolist


#displaymenu(menu_list)
#itemlister(todolist)
#itemadder(todolist)
#itemlister(todolist)
#itemremover(todolist)
#itemlister(todolist)
#taskcompleted(todolist)
#itemlister(todolist)
choose_menu_option()
