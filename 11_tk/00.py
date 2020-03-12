'''
	画虚线
'''

from tkinter import *

root = Tk()
cv = Canvas(root, bg='white', width=300, height=120)
cv.create_line(10, 10, 100, 80, width=2, dash=7)
cv.pack()
root.mainloop()