from tkinter import *
root = Tk()
cv = Canvas(root, bg = 'white', width = 200, height = 100) 
cv.create_oval (10,10,100,50, outline = 'blue', fill = 'red', width=2)		#椭圆
cv.create_oval (100,10,190,100, outline = 'blue', fill = 'red', width=2)		#圆形
cv.pack()
root.mainloop()













