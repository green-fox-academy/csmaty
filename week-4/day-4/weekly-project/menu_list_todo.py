todolist = [
        {'status': '[ ]', 'description': 'vegyel ezt' },
        {'status': '[ ]', 'description': 'vegyel azt'},
        {'status': '[ ]', 'description': 'vegyel amazt'},
        {'status': '[ ]', 'description': 'vidd ki a szemetet'}
]

menu_list = [
        ['___MENU:_____'],
        ['              '],
        ['1: LIST ALL ITEMS'],
        ['2: ADD ITEM'],
        ['3: MARK ITEM AS COMPLETED'],
        ['4: REMOVE ITEM'],
        ['000: EXIT']

    ]

def choose_menu_option():
    displaymenu(menu_list)

    menu_option_input = input('\nType the number of the chosen option:\n\n\n')
    try:
        if int(menu_option_input) == 1:
            itemlister(todolist)
            choose_menu_option()

        elif int(menu_option_input) == 2:
            itemadder(todolist)
            choose_menu_option()

        elif int(menu_option_input) == 3:
            taskcompleted(todolist)
            choose_menu_option()

        elif int(menu_option_input) == 4:
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

    newitem = {'status': '[ ]', 'description': str(input("\nWrite the next todo item: \n"))}
    todolist.append(newitem)
    return todolist

def itemremover(todolist):

    i = int(input('\nGive me the number of the item you want to remove:\n')) -1
    todolist.pop(i)
    return todolist

def taskcompleted(todolist):
    itemlister(todolist)
    i = int(input('\nGive me the number of the item you have completed:\n')) -1
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
