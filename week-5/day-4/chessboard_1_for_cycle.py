from tkinter import*

master = Tk()

w = Canvas(master, width = 400, height = 400)
w.pack()

w.create_rectangle(0, 00, 400, 300, fill= "#ffffff")

    for n in range(16):
    i = n % 4
    j = n // 4
    ox = 40 * i
    oy = 40 * j
    w.create_rectangle(0 + ox, 0 + oy, 20 + ox, 20 + oy, fill="#ff0000")
    w.create_rectangle(20 + ox, 20 + oy, 40 + ox, 40 + oy, fill="#ff0000")

mainloop()
