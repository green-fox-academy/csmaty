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

    menu_option_input = input('\n>>>>Type the command for the chosen option:\n\n')
    try:
        if menu_option_input.lower() == 'l':
            itemlister(todolist)
            choose_menu_option()

        elif menu_option_input.lower().lower() == 'a':
            itemadder(todolist)
            choose_menu_option()

        elif menu_option_input.lower() == 'c':
            taskcompleted(todolist)
            choose_menu_option()

        elif menu_option_input.lower() == 'rm':
            itemremover(todolist)
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
    itemlister(todolist)
    i = int(input('\n>>>>Give me the number of the item you have completed:\n')) -1
    todolist[i]['status'] = '[X]'
    return todolist

choose_menu_option()
