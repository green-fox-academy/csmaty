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


def displaymenu(menu_list):

    print('\n\n')
    for i in menu_list:
        print(str(i))
    print('\n\n')



def itemlister(todolist):
    n = 0
    for i in todolist:
        n += 1
        print (str(n) + '. ' + i['status'], i['description'])


def itemadder(todolist):

    newitem = {'status': '[ ]', 'description': str(input("\nWrite the next todo item: \n"))}
    todolist.append(newitem)
    return todolist

def itemremover(todolist):

    i = int(input('\nGive me the number of the item you want to remove:\n')) -1
    todolist.pop(i)
    return todolist

def taskcompleted(todolist):
    i = int(input('\nGive me the number of the item completed:\n')) -1
    todolist[i]['status'] = '[X]'
    return todolist


displaymenu(menu_list)
itemlister(todolist)
itemadder(todolist)
itemlister(todolist)
itemremover(todolist)
itemlister(todolist)
taskcompleted(todolist)
itemlister(todolist)
