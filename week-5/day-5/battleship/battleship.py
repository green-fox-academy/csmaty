
field = [
        [1,1,0,1,0,0,1,1,1,1],
        [0,0,0,1,0,0,0,0,0,0],
        [1,0,0,1,0,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,1,0,0,0,1],
        [0,0,0,0,0,1,0,0,0,1],
        [1,1,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,1]
        ]

def shoot_cell(field):
    linenumber = int(input('Give me the line:')) - 1
    rownumber = int(input('Give me the row:')) -1
    selected_line = field[linenumber]
    selected_cell = selected_line[rownumber]
    print(selected_cell)
    if selected_line[rownumber] == 0:
        selected_line[rownumber] = 3
    if selected_line[rownumber] == 1:
        selected_line[rownumber] = 4

    print(selected_line)
    return field

shoot_cell(field)
