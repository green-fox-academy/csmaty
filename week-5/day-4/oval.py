from tkinter import*

master = Tk()

w = Canvas(master, width = 900, height = 900)
w.pack()


oval_args = [60, 60, 80, 80]
for i in range (30):
    w.create_oval(oval_args[0], oval_args[1], oval_args[2], oval_args[3])
    oval_args[2] += 10
    oval_args[3] += 10


oval_args = [120, 120, 80, 80]
for i in range (30):
    w.create_oval(oval_args[0], oval_args[1], oval_args[2], oval_args[3])
    oval_args[2] += 10
    oval_args[3] += 10

oval_args = [300, 300, 80, 80]
for i in range (30):
    w.create_oval(oval_args[0], oval_args[1], oval_args[2], oval_args[3])
    oval_args[2] += 10
    oval_args[3] += 10



mainloop()
