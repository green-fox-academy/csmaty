from tkinter import*

master = Tk()

w = Canvas(master, width = 1000, height = 1000)
w.pack()

oval_args = [60, 60, 90, 90]
for i in range (10):
    w.create_oval(oval_args[0], oval_args[1], oval_args[2], oval_args[3])
    oval_args[2] += 15
    oval_args[3] += 15




args = [0, 0, 0, 300]
for i in range (20):
    w.create_line(args[0], args[1], args[2], args[3], fill= "#000000", width=1)
    args[0] += 0
    args[1] += 15
    args[2] += 15
    args[3] += 0

mainloop()
