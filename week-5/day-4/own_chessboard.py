from tkinter import*

master = Tk()

w = Canvas(master, width = 400, height = 400)
w.pack()


w.create_rectangle(0, 0, 400, 300, fill= "#ffffff")
args = [0, 0, 20, 20]
for j in range (4):
    w.create_rectangle(args[0], args[1], args[2], args[3], fill= "#ff0000")
    for i in range (3):
        args[0] += 40
        args[2] += 40
        w.create_rectangle(args[0], args[1], args[2], args[3], fill= "#ff0000")
    args[0] += -100
    args[2] += -100
    args[1] += 20
    args[3] += 20
    w.create_rectangle(args[0], args[1], args[2], args[3], fill= "#ff0000")
    for i in range (3):
        w.create_rectangle(args[0], args[1], args[2], args[3], fill= "#ff0000")
        args[0] += 40
        args[2] += 40
        w.create_rectangle(args[0], args[1], args[2], args[3], fill= "#ff0000")
    args[0] += -140
    args[2] += -140
    args[1] += 20
    args[3] += 20







mainloop()
