from tkinter import *

root = Tk()
cv = Canvas(root, bg='white', width=300, height=120)
cv.rceate_line(10, 10, 100, 80, width=2, dash=7)
cv.pack()
root.mainloop()