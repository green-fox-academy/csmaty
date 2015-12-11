from tkinter import *
from ball import Ball

master = Tk()

canvas = Canvas(master, width = 400, height = 400)
canvas.pack()

canvas. create_rectangle(0, 0, 400, 400, fill ='#ffffff')
ball = Ball((150, 250), (2, -2), 25)
while True:
    ball.move()
    bbox = ball.get_bbox()
    canvas. create_rectangle(0, 0, 400, 400, fill ='#ffffff')
    canvas.create_oval(bbox, fill='#000000')
    # (same as previous line) canvas.create_oval(bbox[0], bbox[1], bbox[3], bbox[4], fill='#000000')
    canvas.after(1000 // 60)
    canvas.update()


mainloop()
