from tkinter import*

master = Tk()

w = Canvas(master, width = 400, height = 300)
w.pack()

w.create_rectangle(20, 20, 150, 80, fill= "#ff0000")
w.create_line(0, 0, 50, 20, fill= "#00ff00", width=3)

mainloop()
