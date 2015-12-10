from tkinter import*

master = Tk()

w = Canvas(master, width = 400, height = 400)
w.pack()

w.create_rectangle(0, 00, 400, 300, fill= "#ffffff")

for j in range(4):
    for i in range(4):
        ox= 40 * j
        oy = 40 * i
        w.create_rectangle(0 + ox, 0 + oy, 20 + ox, 20 + oy, fill='#ff0000')
        w.create_rectangle(20 + ox, 20 + oy, 40 + ox, 40 + oy, fill='#ff0000')

mainloop()
