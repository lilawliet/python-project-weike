'''
	绘制矩形
'''

from tkinter import *

root = Tk()

# 创建一个Canvas
cv = Canvas(root, bg='white', width=200, height=150)
cv.create_rectangle(10, 10, 110, 110, width=2, fill='red')

cv.create_rectangle(120, 20, 180, 80, outline='green')

cv.pack()

root.mainloop()