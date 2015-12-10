from tkinter import*

master = Tk()

w = Canvas(master, width = 400, height = 400)
w.pack()

w.create_rectangle(0, 00, 400, 300, fill= "#ffffff")
w.create_rectangle(0, 0, 20, 20, fill= "#ff0000")
w.create_rectangle(20, 20, 40, 40, fill= "#ff0000")
w.create_rectangle(40, 0, 60, 20, fill= "#ff0000")
w.create_rectangle(60, 20, 80, 40, fill= "#ff0000")




mainloop()
